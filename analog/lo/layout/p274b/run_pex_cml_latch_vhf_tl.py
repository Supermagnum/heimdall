#!/usr/bin/env python3
"""P2.7.4b — Magic RC wiring C for cml_latch_vhf_tl [PEX-RC].

Same bank-method as cml_latch_uhf / VCO. Ports: ckp, ckn, qp, qn.
No internal tail MOSFET — clk sources are gnd (tailless).
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
PEX = os.path.join(OUT, "pex_cml_latch_vhf_tl")
GDS_SRC = os.path.join(OUT, "cml_latch_vhf_tl.gds")
CELL = "cml_latch_vhf_tl"
PDK_MAGICRC = "/foss/pdks/ihp-sg13g2/libs.tech/magic/ihp-sg13g2.magicrc"

_PORT_PREF = (
    "ckp", "ckn", "qp", "qn", "dp", "dn", "vdd", "gnd", "sub!", "0",
)
INTEREST = ("ckp", "ckn", "qp", "qn")
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
            caps.append((toks[1].strip('"'), toks[2].strip('"'),
                         float(toks[3])))
    return find, node_c, caps


def to_ff(af: float) -> float:
    return af / 1000.0


def wiring_table(ext_path: str) -> dict:
    find, node_c, caps = parse_ext(ext_path)
    alias = {p: find(p) for p in INTEREST}
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
            "sub_ff": round(to_ff(sub[p]), 4),
            "all_ff": round(to_ff(sub[p] + wire), 4),
            "wire_ff": round(to_ff(wire), 4),
            "top_partners": [
                (k, round(to_ff(v), 4))
                for k, v in sorted(coup[p].items(), key=lambda x: -abs(x[1]))[:8]
            ],
        }
    return rows


def assembly_hand() -> dict:
    c_m2, c_m3, w, k = 0.03, 0.025, 0.4, 1.5
    len_l2l, len_b2l = 15.0, 40.0
    c_l2l = k * len_l2l * w * c_m2
    c_b2l = k * len_b2l * w * c_m3
    return {
        "c_l2l_ff": round(c_l2l, 2),
        "c_b2l_ff": round(c_b2l, 2),
        "c_asm_ff": round(c_l2l + c_b2l, 2),
    }


def write_report(rows: dict, asm: dict) -> str:
    budget = 15.0
    ck_side = max(rows["ckp"]["wire_ff"], rows["ckn"]["wire_ff"])
    q_side = max(rows["qp"]["wire_ff"], rows["qn"]["wire_ff"])
    total_ck = ck_side + asm["c_asm_ff"]
    gate = "PASS" if total_ck <= budget else "FAIL"
    lines = [
        "# cml_latch_vhf_tl wiring C — Magic RC [PEX-RC]\n\n",
        "## Method\n",
        "- Same bank-method wiring add as `cml_latch_uhf` / VCO "
        "(coupling only; device C excluded) [PEX-RC].\n",
        "- Tailless: no separate `ta` net (clk sources ≡ gnd) [SCH].\n",
        "- Series R: `extresist` not run [TOOL].\n\n",
        "## Wiring C per net\n\n",
        "| net | substrate node C | all + substrate | **wiring add** | unit | tag |\n",
        "|---|---:|---:|---:|---|---|\n",
    ]
    for p in INTEREST:
        r = rows[p]
        lines.append(
            f"| {p} | {r['sub_ff']:.2f} | {r['all_ff']:.2f} | "
            f"**{r['wire_ff']:.2f}** | fF | [PEX-RC] |\n"
        )
    lines.extend([
        "\n## Clock budget vs ≤ 15 fF / side\n\n",
        f"| quantity | value | unit | tag |\n",
        f"|---|---:|---|---|\n",
        f"| clock wiring max(ckp, ckn) | {ck_side:.2f} | fF | [PEX-RC] |\n",
        f"| assembly total add | {asm['c_asm_ff']:.2f} | fF | [HAND] |\n",
        f"| **clock + assembly** | **{total_ck:.2f}** | fF | [PEX-RC]+[HAND] |\n",
        f"| budget | {budget:.1f} | fF/side | [SCH] |\n",
        f"| gate | **{gate}** | | |\n\n",
        f"| qp/qn max wiring | {q_side:.2f} | fF | [PEX-RC] |\n",
    ])
    path = os.path.join(OUT, "summary_pex_wiring_cml_latch_vhf_tl.txt")
    open(path, "w").write("".join(lines))
    open(os.path.join(PEX, "wiring_c.json"), "w").write(
        json.dumps({"rows": rows, "asm": asm, "gate": gate}, indent=2))
    return path, gate


def main():
    ext = run_magic()
    rows = wiring_table(ext)
    asm = assembly_hand()
    path, gate = write_report(rows, asm)
    print(open(path).read())
    print(f"Wrote {path} gate={gate}", flush=True)
    return 0 if gate == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
