#!/usr/bin/env python3
"""Flatten xschem-exported vco_top.spice for LVS (no hand device edits).

Reads sch/netlists/vco_top.spice (xschem hierarchical expand), builds one
flat .subckt vco_top. Leaf mappings for LVS tools live in lvs_setup.tcl /
notes — this script only flattens hierarchy and renames models that the PDK
LVS deck expects (documented, not arbitrary).
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
SCH_SPICE = os.path.join(REPO, "analog", "vco", "sch", "netlists", "vco_top.spice")
OUT = os.path.join(HERE, "out")

# PDK LVS extract name ↔ schematic model [PDK / decisions 2026-11-18]
MODEL_MAP = {
    "sg13_hv_svaricap_fx": "sg13_hv_svaricap",
}

# Inductor: pin-only black box (layout LVS GDS has no spiral) [TOOL]
BLACKBOX = {"l2n0"}


def parse_spice(path: str):
    """Return (top_ports, {name: (ports, body_lines)})."""
    text = open(path).read()
    # xschem comments the top .subckt with ** — recover ports from that line
    top_ports = None
    m = re.search(
        r"^\*+\.subckt\s+vco_top\s+(.+)$", text, re.M | re.I
    )
    if m:
        ports = m.group(1).split()
        # continuation *+ lines (xschem: "*+ code2 code3 ...")
        pos = m.end()
        while True:
            while pos < len(text) and text[pos] in "\r\n":
                pos += 1
            nxt = re.match(r"\*+\+\s*(.+)$", text[pos:], re.M)
            if not nxt:
                break
            ports += nxt.group(1).split()
            pos += nxt.end()
        top_ports = ports

    cells = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i]
        m = re.match(r"^\.subckt\s+(\S+)\s*(.*)$", ln.strip(), re.I)
        if not m:
            i += 1
            continue
        name, port_str = m.group(1), m.group(2)
        ports = port_str.split()
        body = []
        i += 1
        while i < len(lines):
            s = lines[i].strip()
            if s.lower().startswith(".ends"):
                i += 1
                break
            if s.startswith("*") or s.startswith("*.") or not s:
                i += 1
                continue
            # join '+' continuations
            while i + 1 < len(lines) and lines[i + 1].lstrip().startswith("+"):
                ln2 = lines[i + 1].lstrip()[1:].strip()
                s = s + " " + ln2
                i += 1
            body.append(s)
            i += 1
        cells[name] = (ports, body)
    return top_ports, cells


def rename_models(line: str) -> str:
    for a, b in MODEL_MAP.items():
        line = re.sub(rf"\b{re.escape(a)}\b", b, line)
    return line


def spice_letter_for_model(model: str) -> str:
    """SPICE instance letter from model — MOS must be M, not X [TOOL].

    xschem exports Xm1 … sg13_lv_nmos; netgen then treats X as a subcircuit
    call (\"undefined subcircuit sg13_lv_nmos\") and D/S permute on the PDK
    MOSFET class does not apply the same way. Leaf LVS spice uses M. [PDK]
    """
    m = model.split("/")[-1].lower()
    if "nmos" in m or "pmos" in m:
        return "M"
    if "svaricap" in m:
        return "X"  # multi-terminal; netgen path keeps X [PDK]
    if m.startswith("cap_") or "cmim" in m or "rfcmim" in m:
        return "C"
    if m in ("rhigh", "rsil", "rppd") or m.startswith("r"):
        return "R"
    return "X"


def spice_inst_name(prefix: str, name: str, model: str | None = None) -> str:
    """Type letter first so netgen/KLayout parse the instance [TOOL].

    Xm1 + prefix bank_ + model nmos → Mbank_m1 (not Xbank_m1 / bank_Xm1).
    """
    letter = spice_letter_for_model(model) if model else None
    if letter is None:
        if name and name[0] in "XxMmCcRrLlDdQqVvIi":
            letter = name[0].upper() if name[0] in "MmCcRrLl" else name[0]
        else:
            letter = "X"
    body = name[1:] if name and name[0] in "XxMmCcRrLlDdQqVvIi" else name
    return f"{letter}{prefix}{body}"


def flatten_inst(prefix: str, cell: str, pinmap: dict, cells: dict,
                 out: list, depth=0):
    if cell not in cells:
        raise SystemExit(f"missing subckt {cell}")
    ports, body = cells[cell]
    if cell in BLACKBOX:
        # Pin-only LVS: omit instance (leaf core spice has no l2n0 either;
        # layout extract has no inductor device). Ports stay as top pins [TOOL].
        return
    for ln in body:
        ln = rename_models(ln)
        # subckt instance: Xname n1 n2 ... subckt
        m = re.match(r"^[Xx](\S+)\s+(.+)\s+(\S+)\s*$", ln)
        if m and m.group(3) in cells:
            iname, argstr, sub = m.group(1), m.group(2), m.group(3)
            args = argstr.split()
            sub_ports, _ = cells[sub]
            if len(args) != len(sub_ports):
                raise SystemExit(
                    f"pin count {iname}: {len(args)} vs {len(sub_ports)} "
                    f"of {sub}"
                )

            def map_net(n):
                if n in ("0", "gnd", "GND"):
                    return pinmap.get("gnd", n) if n != "0" else "0"
                if n in pinmap:
                    return pinmap[n]
                # local net
                key = f"{prefix}{iname}_{n}"
                return key

            child_map = {sp: map_net(a) for sp, a in zip(sub_ports, args)}
            flatten_inst(f"{prefix}{iname}_", sub, child_map, cells, out,
                         depth + 1)
            continue

        # primitive: rewrite nets
        toks = ln.split()
        if not toks:
            continue
        name = toks[0]
        # find model token
        model_i = None
        for j, t in enumerate(toks[1:], 1):
            if t.startswith("sg13_") or t.startswith("cap_") or t in (
                    "rhigh", "resistor", "capacitor", "inductor"):
                model_i = j
                break
        if model_i is None:
            # two-terminal R/L/C style: name n1 n2 value
            if len(toks) >= 3 and name[0] in "RrLlCcVvIi":
                n1, n2 = toks[1], toks[2]
                rest = " ".join(toks[3:])

                def mn(n):
                    if n in ("0",):
                        return "0"
                    return pinmap.get(n, f"{prefix}{n}")

                out.append(
                    f"{spice_inst_name(prefix, name)} {mn(n1)} {mn(n2)} "
                    f"{rest}".rstrip()
                )
            continue

        nodes = toks[1:model_i]
        model = toks[model_i]
        rest = " ".join(toks[model_i:])

        def mn(n):
            # Extract ties svaricap body to gnd; xschem uses sub! [GDS/TOOL]
            if n in ("0",):
                return n
            if n == "sub!":
                return "gnd"
            if n in pinmap:
                return pinmap[n]
            return f"{prefix}{n}"

        # xschem sg13_svaricap netlists G2,NW,G1,body; KLayout extract is
        # G1,W,G2,B — swap G1/G2 for LVS [PDK/TOOL / run_equiv note].
        mlow = model.split("/")[-1].lower()
        if "svaricap" in mlow and len(nodes) >= 4:
            g2, nw, g1, body = nodes[0], nodes[1], nodes[2], nodes[3]
            nodes = [g1, nw, g2, body] + list(nodes[4:])

        mapped = " ".join(mn(n) for n in nodes)
        out.append(
            f"{spice_inst_name(prefix, name, model)} {mapped} {rest}"
        )


def main():
    os.makedirs(OUT, exist_ok=True)
    if not os.path.exists(SCH_SPICE):
        raise SystemExit(f"missing {SCH_SPICE} — export vco_top.sch first")
    top_ports, cells = parse_spice(SCH_SPICE)
    if not top_ports:
        raise SystemExit("could not parse vco_top ports from spice")
    # Build pinmap for top: each port maps to itself
    # Instantiate top children from the commented top body in the file
    text = open(SCH_SPICE).read()
    # Extract X lines between **.subckt vco_top and **.ends
    m = re.search(
        r"\*+\.subckt\s+vco_top\b.*?$(.*?)^\*+\.ends",
        text, re.M | re.S | re.I,
    )
    if not m:
        raise SystemExit("could not find top instance body")
    inst_lines = []
    for ln in m.group(1).splitlines():
        s = ln.strip()
        if not s or s.startswith("*"):
            continue
        while True:
            # no '+' in that block typically after join — handle anyway
            break
        inst_lines.append(s)
    # join continuations
    joined = []
    for ln in inst_lines:
        if ln.startswith("+") and joined:
            joined[-1] = joined[-1] + " " + ln[1:].strip()
        else:
            joined.append(ln)

    out_devs = []
    for ln in joined:
        m = re.match(r"^[Xx](\S+)\s+(.+)\s+(\S+)\s*$", ln)
        if not m:
            continue
        iname, argstr, sub = m.group(1), m.group(2), m.group(3)
        args = argstr.split()
        if sub not in cells:
            raise SystemExit(f"unknown child {sub}")
        sub_ports, _ = cells[sub]
        if len(args) != len(sub_ports):
            raise SystemExit(
                f"top {iname}: {len(args)} args vs {len(sub_ports)} ports"
            )
        pinmap = {sp: a for sp, a in zip(sub_ports, args)}
        # gnd alias
        flatten_inst(f"{iname}_", sub, pinmap, cells, out_devs)

    ports = " ".join(top_ports)
    lines = [
        f"* Flattened from xschem vco_top.sch export [SCH/TOOL]\n",
        f"* Source: {SCH_SPICE}\n",
        f"* MODEL_MAP: {MODEL_MAP}\n",
        f"* BLACKBOX: {sorted(BLACKBOX)} (pin-only inductor LVS GDS)\n",
        f".subckt vco_top {ports}\n",
    ]
    for d in out_devs:
        lines.append(d + "\n")
    lines.append(".ends\n")
    lines.append(
        "* BLACKBOX omitted as instances (pin-only LVS GDS): "
        f"{sorted(BLACKBOX)}\n"
    )
    lines.append(".end\n")

    path = os.path.join(OUT, "vco_top_sch_flat.spice")
    open(path, "w").writelines(lines)
    print(f"wrote {path} ({len(out_devs)} devices, "
          f"{len(top_ports)} ports)", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
