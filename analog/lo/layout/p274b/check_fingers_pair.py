#!/usr/bin/env python3
"""Finger check + PNG for cml_diff_pair."""
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


def main():
    gds = os.path.join(OUT, "cml_diff_pair.gds")
    ly = pya.Layout()
    ly.read(gds)
    top = ly.top_cell()
    ngs = sorted(
        poly_ng(ly.cell(i.cell_index))
        for i in top.each_inst()
        if poly_ng(ly.cell(i.cell_index)) > 0
    )
    ok = ngs.count(5) == 2 and ngs.count(1) == 2
    gate = "PASS" if ok else "FAIL"
    open(os.path.join(OUT, "summary_fingers_cml_diff_pair.txt"), "w").write(
        f"# cml_diff_pair fingers [TOOL]\n\n"
        f"ngs={ngs}\nexpect two×ng=5 + two×ng=1 dummies\n"
        f"gate: {gate}\n"
    )
    print(f"fingers {ngs} {gate}", flush=True)

    # C estimate [HAND/GDS]
    m1 = ly.layer(8, 0)
    m2 = ly.layer(10, 0)
    poly = ly.layer(5, 0)
    a_m1 = a_m2 = a_p = 0.0
    dbu = ly.dbu
    for layer, acc in ((m1, "m1"), (m2, "m2"), (poly, "p")):
        a = 0.0
        for s in top.shapes(layer).each():
            if s.is_box():
                b = s.bbox().to_dtype(dbu)
                a += b.width() * b.height()
        if acc == "m1":
            a_m1 = a
        elif acc == "m2":
            a_m2 = a
        else:
            a_p = a
    c_ck = 0.5 * (a_m1 * 0.04 + a_m2 * 0.03) + 0.5 * a_p * 0.09
    open(os.path.join(OUT, "summary_c_ck_cml_diff_pair.txt"), "w").write(
        f"# cml_diff_pair C [HAND/GDS]\n\n"
        f"M1 {a_m1:.1f} M2 {a_m2:.1f} poly {a_p:.1f} µm²\n"
        f"C gate-ish /side ≈ {c_ck:.2f} fF of 15 fF "
        f"({100*c_ck/15:.1f}%)\n"
    )
    print(f"C≈{c_ck:.2f} fF/side", flush=True)

    # PNG render
    lv = pya.LayoutView()
    lv.load_layout(gds, 0)
    lv.max_hier()
    lv.zoom_fit()
    png = os.path.join(OUT, "cml_diff_pair.png")
    lv.save_image(png, 1200, 800)
    print("PNG", os.path.exists(png), flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
