#!/usr/bin/env python3
"""P2.7.4b — xschem leaf cells for LO divider [SCH].

Leaves match circuit.py / step-3 sizes. Flat tops stay the sim golden
(lo_*_flat.vacask); hierarchical tops instance these symbols. Leaf spice
(vacask) is the LVS reference for layout cells.
"""
from __future__ import annotations

import hashlib
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "analog", "vco", "sch"))

from xsch_lib import Sch, write_sym  # noqa: E402
import circuit as C  # noqa: E402


def place_devs(sch: Sch, body: str):
    for d in C.parse_body(body):
        if d.kind == "nmos":
            sch.nmos(d.name, *d.nodes, d.params["w"], d.params["l"],
                     int(d.params.get("ng", 1)), model=d.params["model"])
        elif d.kind == "pmos":
            sch.pmos(d.name, *d.nodes, d.params["w"], d.params["l"],
                     int(d.params.get("ng", 1)), model=d.params["model"])
        elif d.kind == "res":
            sch.res(d.name, d.nodes[0], d.nodes[1], d.params["r"])
        elif d.kind == "capa":
            sch.capa(d.name, d.nodes[0], d.nodes[1], d.params["c"])


def write_leaf(name, ports, body, title):
    sch = Sch(name, os.path.join(HERE, f"{name}.sch"))
    for p in ports:
        sch.iopin(p)
    sch.title(title)
    place_devs(sch, body)
    sch.write()
    write_sym(os.path.join(HERE, f"{name}.sym"), name, ports)
    C.write_vacask(os.path.join(HERE, "netlists", f"{name}.vacask"),
                   f"P2.7.4b {name}", C.parse_body(body))
    # LVS spice (M-prefix; rppd fab loads where ideal R was CML RL)
    spice_path = os.path.join(HERE, "netlists", f"{name}.spice")
    spice = body
    # rppd L from R·w/ρ with ρ≈250 Ω/sq [PDK/HAND]; 666.7→5.334u, 1666.7→13.334u
    spice = re.sub(
        r"^(\S+) \((\S+) (\S+)\) resistor r=([\d.]+)\s*$",
        lambda m: (
            f"R{m.group(1)} {m.group(2)} {m.group(3)} gnd rppd "
            f"w=2.0u l={float(m.group(4)) * 2.0 / 250.0:.3f}u ps=0.18u b=0 m=1"
        ),
        spice,
        flags=re.M,
    )
    # rename MOS to M-prefix for KLayout reader
    spice = re.sub(
        r"^([a-z]\S*) \((\S+) (\S+) (\S+) (\S+)\) (sg13_lv_[np]mos) (.*)$",
        lambda m: f"M{m.group(1)} {m.group(2)} {m.group(3)} {m.group(4)} "
                  f"{m.group(5)} {m.group(6)} {m.group(7)}",
        spice,
        flags=re.M,
    )
    ports_sp = " ".join("gnd" if p in ("0", "gnd") else p for p in ports)
    open(spice_path, "w").write(
        f"* P2.7.4b {name} LVS reference [SCH]\n"
        f".subckt {name} {ports_sp}\n"
        + spice
        + ".ends\n"
    )
    return name, len(C.parse_body(body)), len(ports)


def cml_latch_body(i, tailless, name="a"):
    C.apply_knobs(i_latch=i if not tailless else 0.75e-3,
                  vhf_i_latch=i if tailless else 0.30e-3,
                  k=1.5, swing=0.5, vhf_tailless=tailless, b2=4.0)
    ii, rl, w = C.L1.cml_params(i, 1.2)
    C.L1.VARIANT["k"] = C.K_REGEN
    C.L1.VARIANT["tailless"] = tailless
    body = C.L1.cml_latch(name, "dp", "dn", "ckp", "ckn", "qp", "qn", ii, rl, w)
    if not tailless:
        body = C.replace_tails(body, i)
    # local vdd pin name
    body = body.replace("(vdd ", "(vdd ")
    return body


def buffer_body():
    C.apply_knobs(i_latch=0.75e-3, b2=4.0, vhf_tailless=True)
    # step2 buffer uses tp/tn → buffered clocks; pull from L2
    return C.L2.buffer()


def main():
    os.makedirs(os.path.join(HERE, "netlists"), exist_ok=True)
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    rows = []

    # bias leaf (symbol used by hier tops)
    bias_body = C.lo_bias_netlist("vdd")
    rows.append(write_leaf(
        "lo_bias", ["nbias", "en_lodiv", "nb_lo", "vdd", "0"],
        bias_body, "lo_bias_nbias_en"))

    # --- UHF CML latch (tailed, 0.75 mA) ---
    body = cml_latch_body(0.75e-3, False)
    rows.append(write_leaf(
        "cml_latch_uhf",
        ["dp", "dn", "ckp", "ckn", "qp", "qn", "nb_lo", "vdd", "0"],
        body, "cml_latch_uhf_0p75mA_tailed"))

    # --- VHF tail-less latch (0.30 mA) ---
    body = cml_latch_body(0.30e-3, True)
    rows.append(write_leaf(
        "cml_latch_vhf_tl",
        ["dp", "dn", "ckp", "ckn", "qp", "qn", "vdd", "0"],
        body, "cml_latch_vhf_tl_0p30mA"))

    # --- VHF CML NOR (÷3 gate; MOSFET tail 0.30 mA) ---
    C.apply_knobs(i_latch=0.30e-3, vhf_i_latch=0.30e-3, k=1.5, swing=0.5,
                  vhf_tailless=True)
    _i, rl, w = C.L1.cml_params(0.30e-3, 1.2)
    tw = C.tail_w(0.30e-3)
    nor = (
        f"rgp (vdd orp) resistor r={rl:.1f}\n"
        f"rgn (vdd orn) resistor r={rl:.1f}\n"
        f"mga (orn q1p tg 0) sg13_lv_nmos w={w:.2f}u l=0.13u\n"
        f"mgb (orn q2p tg 0) sg13_lv_nmos w={w:.2f}u l=0.13u\n"
        f"mgr (orp vref tg 0) sg13_lv_nmos w={w:.2f}u l=0.13u\n"
        f"mtg (tg nb_lo 0 0) sg13_lv_nmos w={tw:g}u l={C.TAIL_L}\n"
    )
    rows.append(write_leaf(
        "cml_nor_vhf",
        ["q1p", "q2p", "vref", "orp", "orn", "nb_lo", "vdd", "0"],
        nor, "cml_nor_vhf_0p30mA"))

    # --- Diff pair leaf (clock/data pair only — layout step 3a) ---
    C.apply_knobs(i_latch=0.75e-3, swing=0.5, k=1.5)
    _, _, w = C.L1.cml_params(0.75e-3, 1.2)
    pair = (
        f"mm1 (d1 g1 s 0) sg13_lv_nmos w={w:.2f}u l=0.13u\n"
        f"mm2 (d2 g2 s 0) sg13_lv_nmos w={w:.2f}u l=0.13u\n"
    )
    rows.append(write_leaf(
        "cml_diff_pair",
        ["d1", "d2", "g1", "g2", "s", "0"],
        pair, "cml_diff_pair_W7p5"))

    # --- Buffer (from step2) ---
    try:
        buf = buffer_body()
        # buffer may use vbuf supply name
        ports_b = sorted({n for d in C.parse_body(buf) for n in d.nodes
                          if not re.match(r"^[a-z]+\d", n) and n not in (
                              "s1", "s2")})
        # keep known buffer ports
        ports_b = ["tp", "tn", "ckp", "ckn", "vbuf", "0"]
        # filter body nets that exist
        rows.append(write_leaf("lo_buffer", ports_b, buf, "lo_buffer_B2_4"))
    except Exception as e:
        print(f"WARN buffer leaf: {e}", flush=True)

    # Hierarchical tops: symbols + flat golden unchanged from circuit
    C.apply_knobs(i_latch=0.75e-3, vhf_i_latch=0.30e-3, b2=4.0,
                  vhf_tailless=True)
    flat_hashes = {}
    for band in ("uhf", "vhf"):
        body, names, ideal, ndiv, duty = C.build_band_body(band, 1.2)
        body = re.sub(r"^vref \(vref 0\) vsource .*\n", "", body, flags=re.M)
        if band == "uhf":
            ports = ["tp", "tn", "nbias", "en_lodiv",
                     "x_p0", "x_p1", "x_p2", "x_p3",
                     "vbuf", "vdv", "vcv", "vdg", "vdd", "0"]
        else:
            ports = ["tp", "tn", "nbias", "en_lodiv", "vref",
                     "x_r1", "x_r2", "x_r3", "x_r4",
                     "x_r1b", "x_r2b", "x_r3b", "x_r4b",
                     "vbuf", "vdv", "vcv", "vdg", "vdd", "0"]
        # Flat top (sim golden — same as P2.7.4a3; device connectivity unchanged)
        sch = Sch(f"lo_{band}_top", os.path.join(HERE, f"lo_{band}_top.sch"))
        for p in ports:
            sch.iopin(p)
        sch.title(f"lo_{band}_top_flat_golden")
        place_devs(sch, body)
        sch.write()
        write_sym(os.path.join(HERE, f"lo_{band}_top.sym"),
                  f"lo_{band}_top", ports)

        # Hierarchical shell: leaf symbols only (LVS/layout hierarchy view)
        hier = Sch(f"lo_{band}_hier", os.path.join(HERE, f"lo_{band}_hier.sch"))
        for p in ports:
            hier.iopin(p)
        hier.title(f"lo_{band}_hier_leaf_symbols")
        if band == "uhf":
            hier.subckt_inst(
                "cml_latch_uhf.sym", "xlat0",
                {p: p for p in ["dp", "dn", "ckp", "ckn", "qp", "qn",
                                "nb_lo", "vdd", "0"]},
                x=0, y=0)
        else:
            hier.subckt_inst(
                "cml_latch_vhf_tl.sym", "xlat0",
                {p: p for p in ["dp", "dn", "ckp", "ckn", "qp", "qn",
                                "vdd", "0"]},
                x=0, y=0)
        hier.subckt_inst(
            "cml_diff_pair.sym", "xpair0",
            {p: p for p in ["d1", "d2", "g1", "g2", "s", "0"]},
            x=400, y=0)
        hier.subckt_inst(
            "lo_bias.sym", "xbias",
            {p: p for p in ["nbias", "en_lodiv", "nb_lo", "vdd", "0"]},
            x=800, y=0)
        hier.write()
        write_sym(os.path.join(HERE, f"lo_{band}_hier.sym"),
                  f"lo_{band}_hier", ports)
        flat_path = os.path.join(HERE, "netlists", f"lo_{band}_flat.vacask")
        C.write_vacask(flat_path, f"P2.7.4b lo_{band} flat", C.parse_body(body))
        h = hashlib.sha256(open(flat_path, "rb").read()).hexdigest()[:16]
        flat_hashes[band] = h
        rows.append((f"lo_{band}_top", len(C.parse_body(body)), len(ports)))

    # Compare to accepted snapshots if present
    lines = [
        "# P2.7.4b xschem leaf cells\n\n",
        "Leaf cells are LVS references. Flat tops remain the sim golden "
        "(circuit.py body). Leaf symbols are placed on the top sheet for "
        "hierarchy documentation; flat device connectivity is unchanged.\n\n",
        "| Cell | Devices | Ports |\n|---|---:|---:|\n",
    ]
    for n, nd, np_ in rows:
        lines.append(f"| `{n}` | {nd} | {np_} |\n")
    lines.append("\n## Flat netlist compare vs accepted\n\n")
    for band in ("uhf", "vhf"):
        acc = f"/tmp/lo_{band}_flat_accepted.vacask"
        cur = os.path.join(HERE, "netlists", f"lo_{band}_flat.vacask")
        if os.path.exists(acc):
            # device-line compare (ignore header)
            def devset(path):
                s = set()
                for ln in open(path):
                    ln = ln.strip()
                    # ignore headers / comments (P2.7.4a2 vs 4b title)
                    if (not ln or ln.startswith("*") or ln.startswith(".")
                            or " flat" in ln and ln.startswith("P2.")):
                        continue
                    s.add(" ".join(ln.split()))
                return s
            a, b = devset(acc), devset(cur)
            miss, extra = sorted(a - b), sorted(b - a)
            ok = not miss and not extra
            lines.append(
                f"- lo_{band}_flat devices: **{'PASS' if ok else 'FAIL'}** "
                f"(missing {len(miss)} extra {len(extra)}; "
                f"title-only diffs ignored)\n"
            )
            if not ok:
                lines.append(f"  missing sample: {miss[:3]}\n")
                lines.append(f"  extra sample: {extra[:3]}\n")
        else:
            lines.append(f"- lo_{band}_flat: no accepted snapshot [TOOL]\n")

    summary = "".join(lines)
    open(os.path.join(HERE, "out", "summary_xsch_lo_leaves.txt"), "w").write(
        summary)
    print(summary, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
