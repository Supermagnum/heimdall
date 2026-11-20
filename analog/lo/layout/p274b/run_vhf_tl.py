#!/usr/bin/env python3
"""P2.7.4b — build + prove cml_latch_vhf_tl bottom-up [TOOL].

Order: pin plan → sized leaves (prove each) → assemble → prove → fingers
→ wiring C → render.
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
    # fingers: extend EXPECT on the fly
    run([sys.executable, "-u", "check_fingers_cell.py", cell],
        os.path.join(OUT, f"run_fingers_{cell}.log"))


def main():
    # --- pin plan recorded by latch builder; leaves first ---
    steps = [
        ([sys.executable, "-u", "build_cml_diff_pair.py",
          "--w", "3.0", "--cell", "cml_diff_pair_vhf"],
         "cml_diff_pair_vhf"),
        ([sys.executable, "-u", "build_cml_pair_loads.py",
          "--cell", "cml_pair_loads_vhf",
          "--pair-gds", "cml_diff_pair_vhf.gds",
          "--pair-w", "3.0", "--dum-w", "1.2",
          "--r", "1666.7", "--rl", "13.335"],
         "cml_pair_loads_vhf"),
        ([sys.executable, "-u", "build_cml_regen_xc.py",
          "--w", "4.5", "--cell", "cml_regen_xc_vhf"],
         "cml_regen_xc_vhf"),
        ([sys.executable, "-u", "build_cml_clk_pair.py",
          "--w", "3.0", "--cell", "cml_clk_pair_vhf"],
         "cml_clk_pair_vhf"),
    ]
    for cmd, cell in steps:
        run(cmd, os.path.join(OUT, f"run_build_{cell}.log"))
        prove(cell)

    run([sys.executable, "-u", "build_cml_latch_vhf_tl.py"],
        os.path.join(OUT, "run_build_cml_latch_vhf_tl.log"))
    prove("cml_latch_vhf_tl")

    run([sys.executable, "-u", "run_pex_cml_latch_vhf_tl.py"],
        os.path.join(OUT, "run_pex_cml_latch_vhf_tl.log"))

    # Render PNG (same path as check_fingers_pair)
    render = os.path.join(OUT, "_render_vhf_tl.py")
    open(render, "w").write(
        "import pya, os\n"
        f"OUT = {OUT!r}\n"
        "ly = pya.Layout(); ly.read(os.path.join(OUT, 'cml_latch_vhf_tl.gds'))\n"
        "lv = pya.LayoutView(); lv.show_layout(ly, False); lv.max_hier()\n"
        "png = os.path.join(OUT, 'cml_latch_vhf_tl.png')\n"
        "lv.save_image(png, 1200, 900); print('PNG', os.path.exists(png))\n"
    )
    run([sys.executable, "-u", render],
        os.path.join(OUT, "run_render_cml_latch_vhf_tl.log"))
    print("VHF TL pipeline done", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
