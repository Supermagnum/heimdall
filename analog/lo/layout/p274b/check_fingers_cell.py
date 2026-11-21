#!/usr/bin/env python3
"""Generic finger-count check for a P2.7.4b leaf GDS [TOOL]."""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path[:0] = [
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/pycell4klayout-api/source/python",
]
import pya  # noqa: E402

# cell -> (expect_ng5_count, expect_ng1_count, expect_other)
EXPECT = {
    "cml_pair_loads": (2, 2, {}),       # data + dummies via child
    "cml_regen_xc": (2, 2, {}),
    "cml_clk_pair": (2, 2, {}),
    "cml_tail": (0, 2, {5: 1}),         # one ng=5 device + 2 dummies
    "cml_diff_pair_vhf": (2, 2, {}),
    "cml_pair_loads_vhf": (2, 2, {}),
    "cml_regen_xc_vhf": (2, 2, {}),
    "cml_clk_pair_vhf": (2, 2, {}),
    # latch: 6× ng=5 (data+regen+clk), no tail; dummies ng=1
    "cml_latch_vhf_tl": (6, 2, {}),
    # NOR: 3× ng=5 input + 1× ng=5 tail; dummies ng=1 (core 2 + tail 2)
    "cml_nor_core_vhf": (3, 2, {}),
    "cml_tail_nor_vhf": (0, 2, {5: 1}),
    "cml_nor_vhf": (4, 4, {}),  # 3 input + 1 tail ng=5; 4 dummies ng=1
    # CMOS inv: nmos+pmos ng=1 each (9_18 is 2×45_9 → 4× ng=1)
    "lo_inv_05_1": (0, 2, {}),
    "lo_inv_1_2": (0, 2, {}),
    "lo_inv_2_4": (0, 2, {}),
    "lo_inv_3_6": (0, 2, {}),
    "lo_inv_45_9": (0, 2, {}),
    "lo_inv_9_18": (0, 4, {}),
}


def poly_ng(cell):
    poly = cell.layout().layer(5, 0)
    dbu = cell.layout().dbu
    xs = set()
    for s in cell.shapes(poly).each():
        if not s.is_box():
            continue
        b = s.bbox().to_dtype(dbu)
        if b.width() < 0.2 and b.height() > 0.4:
            xs.add(round(0.5 * (b.left + b.right), 3))
    return len(xs)


def walk_ngs(cell, out):
    ng = poly_ng(cell)
    if ng > 0:
        out.append(ng)
    for i in cell.each_inst():
        walk_ngs(i.cell, out)


def main():
    cell = sys.argv[1] if len(sys.argv) > 1 else "cml_clk_pair"
    gds = os.path.join(OUT, f"{cell}.gds")
    ly = pya.Layout()
    ly.read(gds)
    top = ly.top_cell()
    raw = []
    walk_ngs(top, raw)
    ngs = sorted(raw)
    n5, n1, other = EXPECT.get(cell, (0, 0, {}))
    ok = ngs.count(5) >= n5 and ngs.count(1) >= n1
    for ng, cnt in other.items():
        ok = ok and ngs.count(ng) >= cnt
    gate = "PASS" if ok else "FAIL"
    path = os.path.join(OUT, f"summary_fingers_{cell}.txt")
    open(path, "w").write(
        f"# {cell} fingers [TOOL]\n\n"
        f"ngs={ngs}\n"
        f"expect ng5>={n5} ng1>={n1} other={other}\n"
        f"gate: {gate}\n"
    )
    print(f"fingers {cell} {ngs} {gate}", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
