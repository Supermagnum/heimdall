#!/usr/bin/env python3
"""P2.7.4b — build + prove cml_nor_vhf bottom-up [TOOL].

Order: checklist → core → tail → assemble (rppd in parent) → prove →
fingers → wiring C → render.
"""
from __future__ import annotations

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)


def run(cmd, log=None):
    print("+", " ".join(cmd), flush=True)
    if log:
        with open(log, "w") as fh:
            r = subprocess.run(cmd, cwd=HERE, stdout=fh, stderr=subprocess.STDOUT)
    else:
        r = subprocess.run(cmd, cwd=HERE)
    print(f"  exit {r.returncode}", flush=True)
    if r.returncode != 0:
        raise SystemExit(r.returncode)
    return r.returncode


def prove(cell):
    run([sys.executable, "-u", "run_drc_lvs.py", cell],
        os.path.join(OUT, f"run_drc_lvs_{cell}.log"))
    run([sys.executable, "-u", "check_fingers_cell.py", cell],
        os.path.join(OUT, f"run_fingers_{cell}.log"))


def main():
    steps = [
        ([sys.executable, "-u", "build_cml_nor_core_vhf.py"],
         "cml_nor_core_vhf"),
        ([sys.executable, "-u", "build_cml_tail.py",
          "--w", "6.0", "--cell", "cml_tail_nor_vhf"],
         "cml_tail_nor_vhf"),
    ]
    for cmd, cell in steps:
        run(cmd, os.path.join(OUT, f"run_build_{cell}.log"))
        prove(cell)

    run([sys.executable, "-u", "build_cml_nor_vhf.py"],
        os.path.join(OUT, "run_build_cml_nor_vhf.log"))
    prove("cml_nor_vhf")

    pex = os.path.join(HERE, "run_pex_cml_nor_vhf.py")
    if os.path.isfile(pex):
        run([sys.executable, "-u", pex],
            os.path.join(OUT, "run_pex_cml_nor_vhf.log"))

    render = os.path.join(OUT, "_render_nor_vhf.py")
    open(render, "w").write(
        "import pya, os\n"
        f"OUT = {OUT!r}\n"
        "ly = pya.Layout(); ly.read(os.path.join(OUT, 'cml_nor_vhf.gds'))\n"
        "lv = pya.LayoutView(); lv.show_layout(ly, False); lv.max_hier()\n"
        "png = os.path.join(OUT, 'cml_nor_vhf.png')\n"
        "lv.save_image(png, 1200, 900); print('PNG', os.path.exists(png))\n"
    )
    run([sys.executable, "-u", render],
        os.path.join(OUT, "run_render_cml_nor_vhf.log"))
    print("NOR VHF pipeline done", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
