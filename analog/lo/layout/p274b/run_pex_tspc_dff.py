#!/usr/bin/env python3
"""P2.7.4b — Magic RC wiring C for tspc_dff (sub+coup; gnd substrate-ref) [PEX-RC]."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PEX = os.path.join(OUT, "pex_tspc_dff")
CELL = "tspc_dff"
GDS_SRC = os.path.join(OUT, f"{CELL}.gds")
PDK_MAGICRC = "/foss/pdks/ihp-sg13g2/libs.tech/magic/ihp-sg13g2.magicrc"
sys.path.insert(0, HERE)
import wiring_c_method as W  # noqa: E402

# Ports + key internals; ck vs 15 fF/side clock budget [SCH]
INTEREST = ("d", "ck", "q", "vdg", "gnd")
CK_BUDGET_FF = 15.0


def run_magic() -> str:
    os.makedirs(PEX, exist_ok=True)
    gds = os.path.join(PEX, f"{CELL}.gds")
    shutil.copy2(GDS_SRC, gds)
    spice = os.path.join(PEX, f"{CELL}.pex.spice")
    tcl = os.path.join(PEX, "pex.tcl")
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
    with open(log, "w") as fh:
        r = subprocess.run(
            ["magic", "-dnull", "-noconsole", "-rcfile", PDK_MAGICRC, tcl],
            cwd=PEX, stdout=fh, stderr=subprocess.STDOUT)
    ext = os.path.join(PEX, f"{CELL}.ext")
    print(f"magic exit={r.returncode} ext={os.path.exists(ext)}", flush=True)
    if r.returncode != 0 or not os.path.exists(ext):
        raise SystemExit("Magic PEX failed")
    return ext


def main():
    if not os.path.exists(GDS_SRC):
        raise SystemExit(f"missing {GDS_SRC}")
    ext = run_magic()
    rows = W.wiring_per_net(ext, INTEREST)
    lines = [
        "# tspc_dff wiring C — substrate + coupling [PEX-RC]\n\n",
        W.METHOD_BLURB,
        "\n",
        "| net | substrate | coupling | wiring C | unit | tag | note |\n",
        "|---|---:|---:|---:|---|---|---|\n",
    ]
    for p in INTEREST:
        r = rows[p]
        note = r.get("note") or ("bound" if r.get("bound") else "unbound")
        lines.append(
            f"| {p} | {r['sub_ff']:.3f} | {r['coup_ff']:.3f} | "
            f"**{r['wire_ff']:.3f}** | fF | [PEX-RC] | {note} |\n"
        )
    ck = rows["ck"]["wire_ff"]
    ck_ok = ck <= CK_BUDGET_FF + 1e-9
    lines.append(
        f"\n- ck wiring C **{ck:.3f} fF** vs budget **{CK_BUDGET_FF:.1f} fF/side** "
        f"[SCH]: {'PASS' if ck_ok else 'FAIL — re-run phase-error check'}.\n"
    )
    path = os.path.join(OUT, "summary_pex_wiring_tspc_dff.txt")
    open(path, "w").write("".join(lines))
    print("".join(lines), flush=True)
    print("WROTE", path, flush=True)
    if not rows["gnd"].get("bound") and rows["gnd"]["wire_ff"] == 0:
        return 1
    return 0 if ck_ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
