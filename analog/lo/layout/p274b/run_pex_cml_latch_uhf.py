#!/usr/bin/env python3
"""P2.7.4b — Magic RC extract of cml_latch_uhf; wiring C per net [PEX-RC].

Same method as VCO bank / vco_top: Magick .ext node C + coupling caps;
**wiring add** = sum of coupling to other nets (substrate/node area C
excluded). Device C lives in PDK MOSFET / rppd models — not counted here.

Ports of interest: ckp, ckn (clock), qp, qn (outputs), ta (tail).
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PEX = os.path.join(OUT, "pex_cml_latch_uhf")
GDS_SRC = os.path.join(OUT, "cml_latch_uhf.gds")
CELL = "cml_latch_uhf"
PDK_MAGICRC = "/foss/pdks/ihp-sg13g2/libs.tech/magic/ihp-sg13g2.magicrc"

# Port preference for union-find roots (survive merge/equiv)
_PORT_PREF = (
    "ckp", "ckn", "qp", "qn", "ta", "dp", "dn", "nb_lo", "vdd", "gnd",
    "s1a", "s2a", "sub!", "0",
)
# Top-level ports; ta is internal (not a cell pin) — resolved from .ext
INTEREST = ("ckp", "ckn", "qp", "qn", "ta")

os.makedirs(PEX, exist_ok=True)


def run_magic() -> str:
    if not os.path.exists(GDS_SRC):
        raise SystemExit(f"missing {GDS_SRC}")
    gds = os.path.join(PEX, f"{CELL}.gds")
    shutil.copy2(GDS_SRC, gds)
    spice = os.path.join(PEX, f"{CELL}.pex.spice")
    tcl = os.path.join(PEX, "pex_latch.tcl")
    open(tcl, "w").write(f"""
crashbackups stop
drc off
gds read {gds}
load {CELL}
select top cell
flatten {CELL}_flat
load {CELL}_flat
cellname delete {CELL}
cellname rename {CELL}_flat {CELL}
select top cell
extract path {PEX}
extract do unique
extract all
ext2spice lvs
ext2spice cthresh 0.01
ext2spice -p {PEX} -o {spice}
quit -noprompt
""")
    log = os.path.join(PEX, "magic_pex.log")
    cmd = ["magic", "-dnull", "-noconsole", "-rcfile", PDK_MAGICRC, tcl]
    print("+", " ".join(cmd), flush=True)
    with open(log, "w") as fh:
        r = subprocess.run(cmd, cwd=PEX, stdout=fh, stderr=subprocess.STDOUT)
    print(f"magic exit={r.returncode} log={log}", flush=True)
    ext = os.path.join(PEX, f"{CELL}.ext")
    if r.returncode != 0 or not os.path.exists(ext):
        raise SystemExit(f"Magic PEX failed (ext={os.path.exists(ext)})")
    return ext


def parse_ext(path: str):
    parent: dict[str, str] = {}

    def find(a: str) -> str:
        parent.setdefault(a, a)
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def rank(n: str) -> int:
        if n in _PORT_PREF:
            return _PORT_PREF.index(n)
        return 100 + len(n)

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        if rank(rb) < rank(ra):
            ra, rb = rb, ra
        parent[rb] = ra

    node_c: dict[str, float] = {}
    caps: list[tuple[str, str, float]] = []
    for ln in open(path):
        toks = ln.split()
        if not toks:
            continue
        if toks[0] == "node" and len(toks) >= 4:
            name = toks[1].strip('"')
            try:
                c = float(toks[3])
            except ValueError:
                continue
            node_c[name] = node_c.get(name, 0.0) + c
        elif toks[0] in ("merge", "equiv") and len(toks) >= 3:
            union(toks[1].strip('"'), toks[2].strip('"'))
        elif toks[0] == "cap" and len(toks) >= 4:
            a = toks[1].strip('"')
            b = toks[2].strip('"')
            caps.append((a, b, float(toks[3])))
    return find, node_c, caps


def to_ff(af: float) -> float:
    return af / 1000.0


def resolve_tail(ext_path: str, find, node_c) -> str:
    """Map internal tail drain: prefer label 'ta', else Magic auto-name.

    Flatten drops the internal 'ta' pin; Magic names the common clk-pair
    source / tail-drain node (device: sg13_lv_nmos D=ta G=nb_lo). From the
    accepted latch GDS that node is `a_n5476_0#` [PEX-RC].
    """
    roots = {find(n) for n in node_c}
    if "ta" in roots:
        return "ta"
    # Known extract name from this GDS; verify it couples to nb_lo / ckp/ckn
    cand = "a_n5476_0#"
    if cand in node_c or cand in roots:
        return find(cand) if cand in node_c else cand
    # Fallback: largest unnamed node that is not a known port
    known = set(INTEREST) | {"dp", "dn", "nb_lo", "vdd", "gnd", "sub!", "0"}
    best, best_c = None, -1.0
    for n, c in node_c.items():
        r = find(n)
        if r in known or r.startswith("a_") is False and "#" not in r:
            if r in known:
                continue
        if r.startswith("a_") and c > best_c:
            best, best_c = r, c
    if best is None:
        raise SystemExit("cannot resolve tail node in .ext")
    return best


def wiring_table(ext_path: str) -> dict:
    find, node_c, caps = parse_ext(ext_path)
    ta_root = resolve_tail(ext_path, find, node_c)
    # Logical name -> .ext root after merge/equiv
    alias = {p: find(p) for p in ("ckp", "ckn", "qp", "qn")}
    alias["ta"] = find(ta_root)

    sub: dict[str, float] = defaultdict(float)
    for n, c in node_c.items():
        r = find(n)
        for p, root in alias.items():
            if r == root:
                sub[p] += c

    coup: dict[str, dict[str, float]] = {p: defaultdict(float) for p in INTEREST}
    for a, b, c in caps:
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        for p, root in alias.items():
            if ra == root:
                coup[p][rb] += c
            elif rb == root:
                coup[p][ra] += c

    rows = {}
    for p in INTEREST:
        wire = sum(coup[p].values())
        rows[p] = {
            "ext_name": ta_root if p == "ta" else p,
            "sub_ff": round(to_ff(sub[p]), 4),
            "all_ff": round(to_ff(sub[p] + wire), 4),
            "wire_ff": round(to_ff(wire), 4),
            "top_partners": [
                (k, round(to_ff(v), 4))
                for k, v in sorted(coup[p].items(), key=lambda x: -abs(x[1]))[:12]
            ],
        }
    return rows


def assembly_hand() -> dict:
    """Estimate latch-to-latch and buffer-to-latch clock wiring add [HAND].

    Floorplan: matched M2 E–W equal length (±1 µm); M3 N–S feeds; shields.
    Per-side share of one differential clock pair at one latch face.
    Densities order-of-magnitude vs SG13G2 [HAND] (same order as prior
    extract_clock_c).
    """
    c_m2 = 0.03  # fF/µm² [HAND]
    c_m3 = 0.025  # fF/µm² [HAND]
    w = 0.4  # µm typical signal width [HAND]
    # Latch-to-latch: short abutment corridor ~15 µm M2 per side [HAND]
    len_l2l = 15.0
    # Buffer-to-latch: longer M3 feed ~40 µm per side into LO island [HAND]
    len_b2l = 40.0
    # Couplings / shields roughly +50 % on area term [HAND]
    k_coup = 1.5
    c_l2l = k_coup * len_l2l * w * c_m2
    c_b2l = k_coup * len_b2l * w * c_m3
    return {
        "c_l2l_ff": round(c_l2l, 2),
        "c_b2l_ff": round(c_b2l, 2),
        "c_asm_ff": round(c_l2l + c_b2l, 2),
        "note": (
            f"M2 {len_l2l} µm × {w} µm × {c_m2} ×{k_coup} + "
            f"M3 {len_b2l} µm × {w} µm × {c_m3} ×{k_coup} [HAND]"
        ),
    }


def write_report(rows: dict, asm: dict) -> str:
    budget = 15.0
    ck_side = max(rows["ckp"]["wire_ff"], rows["ckn"]["wire_ff"])
    q_side = max(rows["qp"]["wire_ff"], rows["qn"]["wire_ff"])
    ta = rows["ta"]["wire_ff"]
    total_ck = ck_side + asm["c_asm_ff"]
    gate = "PASS" if total_ck <= budget else "FAIL"
    lines = [
        "# cml_latch_uhf wiring C — Magic RC [PEX-RC]\n\n",
        "## Method\n",
        "- Tool: Magic + `ihp-sg13g2.magicrc`; flatten cell; `extract all`; "
        "keep `.ext` [TOOL].\n",
        "- Units: Magic `.ext` aF / 1000 = fF.\n",
        "- **Wiring add** = sum of coupling caps to other nets "
        "(= all partners + substrate − substrate/node C). Same bank-method "
        "as VCO (`summary_pex_bank`) [PEX-RC].\n",
        "- Substrate/node C includes diffusion/gate area Magic attributes to "
        "the net; device C is in PDK MOSFET / rppd models and is **excluded** "
        "from wiring add [PEX-RC / PDK].\n",
        "- Series R: `extresist` not run [TOOL].\n",
        f"- GDS: `out/cml_latch_uhf.gds` cell `{CELL}`.\n\n",
        "## Wiring C per net (device C excluded)\n\n",
        "| net | .ext name | substrate node C | all + substrate | **wiring add** | unit | tag |\n",
        "|---|---|---:|---:|---:|---|---|\n",
    ]
    for p in INTEREST:
        r = rows[p]
        en = r.get("ext_name", p)
        note = p if en == p else f"{p} (internal)"
        lines.append(
            f"| {note} | `{en}` | {r['sub_ff']:.2f} | {r['all_ff']:.2f} | "
            f"**{r['wire_ff']:.2f}** | fF | [PEX-RC] |\n"
        )
    if rows["ta"]["ext_name"] != "ta":
        lines.append(
            "\nTail is not a top-level pin; mapped to Magic node "
            f"`{rows['ta']['ext_name']}` (clk-pair common source / "
            "tail MOSFET drain) [PEX-RC].\n"
        )
    lines.append("\n### Top coupling partners\n\n")
    for p in INTEREST:
        lines.append(f"**{p}:**\n")
        for k, v in rows[p]["top_partners"]:
            lines.append(f"- `{k}`: {v:.3f} fF\n")
        lines.append("\n")

    lines.extend([
        "## Clock budget vs ≤ 15 fF / side\n\n",
        f"| quantity | value | unit | tag |\n",
        f"|---|---:|---|---|\n",
        f"| clock wiring max(ckp, ckn) | {ck_side:.2f} | fF | [PEX-RC] |\n",
        f"| assembly latch↔latch (est.) | {asm['c_l2l_ff']:.2f} | fF | [HAND] |\n",
        f"| assembly buffer→latch (est.) | {asm['c_b2l_ff']:.2f} | fF | [HAND] |\n",
        f"| assembly total add | {asm['c_asm_ff']:.2f} | fF | [HAND] |\n",
        f"| **clock + assembly** | **{total_ck:.2f}** | fF | [PEX-RC]+[HAND] |\n",
        f"| budget | {budget:.1f} | fF/side | [SCH] |\n",
        f"| gate | **{gate}** | | |\n\n",
        f"Assembly estimate: {asm['note']}.\n\n",
        f"| other nets | wiring add | unit | tag |\n",
        f"|---|---:|---|---|\n",
        f"| qp/qn max | {q_side:.2f} | fF | [PEX-RC] |\n",
        f"| ta (tail) | {ta:.2f} | fF | [PEX-RC] |\n\n",
    ])
    if gate == "PASS":
        lines.append(
            "Clock + assembly ≤ 15 fF/side → continue to `cml_latch_vhf_tl`.\n"
        )
    else:
        lines.append(
            "Clock + assembly **over** 15 fF/side → tighten latch before "
            "more divider cells.\n"
        )
    path = os.path.join(OUT, "summary_pex_wiring_cml_latch_uhf.txt")
    open(path, "w").write("".join(lines))
    open(os.path.join(PEX, "wiring_c.json"), "w").write(
        json.dumps({"rows": rows, "asm": asm, "ck_side": ck_side,
                    "total_ck": total_ck, "gate": gate}, indent=2)
    )
    return path, gate, total_ck, ck_side


def main():
    ext = run_magic()
    rows = wiring_table(ext)
    asm = assembly_hand()
    path, gate, total, ck = write_report(rows, asm)
    print(open(path).read())
    print(f"Wrote {path} gate={gate} ck={ck:.2f} total={total:.2f}", flush=True)
    return 0 if gate == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
