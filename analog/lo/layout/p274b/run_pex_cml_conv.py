#!/usr/bin/env python3
"""P2.7.4b — Magic RC wiring C for cml_conv (sub+coup; gnd substrate-ref) [PEX-RC]."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PEX = os.path.join(OUT, "pex_cml_conv")
CELL = "cml_conv"
GDS_SRC = os.path.join(OUT, f"{CELL}.gds")
PDK_MAGICRC = "/foss/pdks/ihp-sg13g2/libs.tech/magic/ihp-sg13g2.magicrc"
sys.path.insert(0, HERE)
import wiring_c_method as W  # noqa: E402

INTEREST = ("dp", "dn", "y", "vcv", "gnd")
CMIM_PLATE_FF = 50.0  # per cmim PCell request [DS]


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
        "# cml_conv wiring C — substrate + coupling [PEX-RC]\n\n",
        W.METHOD_BLURB,
        "- Cell has 3× series cmim; plate C stated separately (not in wiring C) "
        "[PEX-RC].\n\n",
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
    lines.append(
        f"\n- cmim plate C (PCell request): **{CMIM_PLATE_FF:.1f} fF** each ×3 "
        f"(p/n/b); not added into wiring C [DS].\n"
    )
    path = os.path.join(OUT, "summary_pex_wiring_cml_conv.txt")
    open(path, "w").write("".join(lines))
    print("".join(lines), flush=True)
    print("WROTE", path, flush=True)
    if not rows["gnd"].get("bound") and rows["gnd"]["wire_ff"] == 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
