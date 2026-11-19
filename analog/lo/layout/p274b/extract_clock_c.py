#!/usr/bin/env python3
"""Estimate clock/output wiring C from metal+poly area [HAND/GDS].

Uses PDK-ish areal densities (IHP SG13G2 order-of-magnitude) to report the
share of the 15 fF/side clock-net floor budget used by this leaf cell.
Not a full Magic/KLayout PEX — tagged accordingly.
"""
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

# Areal C dens fF/µm² [HAND] — approx vs substrate; good enough for budget share
C_M1 = 0.04
C_M2 = 0.03
C_POLY = 0.09  # gate-ish; poly area outside Activ counted as wire


def area_um2(ly, cell, layer):
    a = 0.0
    dbu = ly.dbu
    for s in cell.shapes(layer).each():
        if s.is_box():
            b = s.bbox().to_dtype(dbu)
            a += b.width() * b.height()
    return a


def main():
    gds = os.path.join(OUT, "cml_latch_uhf.gds")
    ly = pya.Layout()
    ly.read(gds)
    top = ly.top_cell()
    m1 = ly.layer(8, 0)
    m2 = ly.layer(10, 0)
    poly = ly.layer(5, 0)
    a_m1 = area_um2(ly, top, m1)
    a_m2 = area_um2(ly, top, m2)
    a_poly = area_um2(ly, top, poly)
    # Crude: half of top-level M1/M2 attributed to each clock side (ckp/ckn
    # routing is the leaf's share of the matched clock); poly gates of clock
    # devices ≈ 2/7 of all nmos poly (2 of 7 devices are clock).
    c_ck_side = 0.5 * (a_m1 * C_M1 + a_m2 * C_M2) + (2.0 / 7.0) * a_poly * C_POLY
    c_out_side = 0.5 * (a_m1 * C_M1)  # qp/qn local
    budget = 15.0
    lines = [
        "# cml_latch_uhf clock/output C estimate [HAND/GDS]",
        "",
        f"Top M1 area {a_m1:.1f} µm²; M2 {a_m2:.1f}; poly {a_poly:.1f}.",
        f"C dens M1={C_M1} M2={C_M2} poly={C_POLY} fF/µm² [HAND].",
        "",
        f"| Net | C (fF/side) | of 15 fF budget |",
        f"|---|---:|---:|",
        f"| ckp or ckn (leaf share) | {c_ck_side:.2f} | "
        f"{100*c_ck_side/budget:.1f} % |",
        f"| qp or qn (local) | {c_out_side:.2f} | — |",
        "",
        f"Gate vs ≤15 fF/side: leaf uses **{c_ck_side:.2f} fF/side** "
        f"({'PASS share' if c_ck_side <= budget else 'OVER'}).",
        "Full-assembly clock C is the sum of leaf + route; re-check at assemble.",
        "",
    ]
    path = os.path.join(OUT, "summary_c_ck_cml_latch_uhf.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
