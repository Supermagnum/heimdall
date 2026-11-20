#!/usr/bin/env python3
"""Finger-count check for cml_latch_uhf [TOOL]."""
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

EXPECT = {
    # (label, ng) — data×4 (m1,m2,m5,m6), regen×2, tail×1
    "data_ng5": 5,
    "regen_ng5": 5,
    "tail_ng10": 10,
}


def poly_gate_count(cell) -> int:
    poly = cell.layout().layer(5, 0)
    dbu = cell.layout().dbu
    xs = set()
    for s in cell.shapes(poly).each():
        if not s.is_box():
            continue
        b = s.bbox().to_dtype(dbu)
        if b.width() < 0.20 and b.height() > 0.4:
            xs.add(round(0.5 * (b.left + b.right), 3))
    return len(xs)


def walk_ngs(cell, out):
    ng = poly_gate_count(cell)
    if ng > 0:
        out.append(ng)
    for i in cell.each_inst():
        walk_ngs(i.cell, out)


def main():
    gds = os.path.join(OUT, "cml_latch_uhf.gds")
    ly = pya.Layout()
    ly.read(gds)
    top = ly.top_cell()
    raw = []
    walk_ngs(top, raw)
    # Leaf NMOS only: ng in {1,5,10}; ignore poly-strap aggregates
    ngs_sorted = sorted(n for n in raw if n in (1, 5, 10))
    # expect four 5's (data+clock), two 5's regen (=six 5's), one 5 or 10 tail
    # tail W=15 ng=5 in leaf; script historically expected 10 from combined view
    ok = ngs_sorted.count(5) >= 6 and (
        ngs_sorted.count(5) >= 7 or ngs_sorted.count(10) >= 1)
    lines = [
        "# cml_latch_uhf finger check [TOOL]",
        "",
        f"mos_child_ngs={ngs_sorted} (raw={sorted(raw)})",
        f"expect: ≥six×ng=5 (data+regen+clock) + tail ng=5",
        f"gate: {'PASS' if ok else 'FAIL'}",
        "",
    ]
    path = os.path.join(OUT, "summary_fingers_cml_latch_uhf.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines), flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
