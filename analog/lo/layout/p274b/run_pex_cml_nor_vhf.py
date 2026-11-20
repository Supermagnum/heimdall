#!/usr/bin/env python3
"""P2.7.4b — Magic RC wiring C for cml_nor_vhf (sub+coup) [PEX-RC]."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PEX = os.path.join(OUT, "pex_cml_nor_vhf")
CELL = "cml_nor_vhf"
GDS_SRC = os.path.join(OUT, f"{CELL}.gds")
PDK_MAGICRC = "/foss/pdks/ihp-sg13g2/libs.tech/magic/ihp-sg13g2.magicrc"
sys.path.insert(0, HERE)
import wiring_c_method as W  # noqa: E402

INTEREST = ("orp", "orn", "q1p", "q2p", "vref", "nb_lo", "tg")
os.makedirs(PEX, exist_ok=True)


def run_magic() -> str:
    gds = os.path.join(PEX, f"{CELL}.gds")
    shutil.copy2(GDS_SRC, gds)
    spice = os.path.join(PEX, f"{CELL}.pex.spice")
    tcl = os.path.join(PEX, "pex_nor.tcl")
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
    # tg may be unnamed internal — try resolve
    find, node_c, _ = W.parse_ext(
        ext, INTEREST + ("vdd", "gnd", "sub!", "0", "tg"))
    alias = {}
    if "tg" not in {find(n) for n in node_c} and "tg" not in node_c:
        # leave empty; wiring_per_net will skip missing
        pass
    rows = W.wiring_per_net(ext, INTEREST, alias=alias or None)
    lines = [
        "# cml_nor_vhf wiring C — substrate + coupling [PEX-RC]\n\n",
        W.METHOD_BLURB if hasattr(W, "METHOD_BLURB") else "",
        "| net | substrate | coupling | **wiring C** | unit | tag |\n",
        "|---|---:|---:|---:|---|---|\n",
    ]
    for p in INTEREST:
        if p not in rows:
            lines.append(f"| {p} | — | — | **n/a** | fF | [PEX-RC] |\n")
            continue
        r = rows[p]
        lines.append(
            f"| {p} | {r['sub_ff']:.2f} | {r['coup_ff']:.2f} | "
            f"**{r['wire_ff']:.2f}** | fF | [PEX-RC] |\n"
        )
    path = os.path.join(OUT, "summary_pex_wiring_cml_nor_vhf.txt")
    open(path, "w").write("".join(lines))
    open(os.path.join(PEX, "wiring_c.json"), "w").write(
        json.dumps({"rows": rows, "method": "sub+coup"}, indent=2, default=float))
    print(open(path).read(), flush=True)
    print("Wrote", path, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
