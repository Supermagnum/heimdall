#!/usr/bin/env python3
"""P2.7.4b — two rppd loads for cml_nor_vhf (face pins) [SCH].

Pins: orp/orn=S (to core drains), vdd=N, gnd=W (substrate ring only).
R = 1666.7 Ω, w=2 µm, l=13.334 µm [SCH].
"""
from __future__ import annotations

import gzip
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
sys.path[:0] = [
    HERE,
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/"
    "pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402, F401
import pin_face as PF  # noqa: E402

DBU = 0.001
CELL = "cml_nor_loads_vhf"
R_W, R_L, R_OHM = "2.0u", "13.334u", "1666.7"


def um(x):
    return int(round(float(x) / DBU))


def main():
    ly = pya.Layout()
    ly.dbu = DBU
    ly.technology_name = "sg13g2"
    lib = pya.Library.library_by_name("SG13_dev", "sg13g2")
    lib_ly = lib.layout()
    m1 = ly.layer(8, 0)
    m1pin = ly.layer(8, 2)
    m1txt = ly.layer(8, 25)

    rh = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("rppd").id(),
        {"R": R_OHM, "w": R_W, "l": R_L, "b": 0,
         "Calculate": "R", "guardRingType": "none"})
    rloc = ly.cell(rh).bbox().to_dtype(ly.dbu)
    top = ly.create_cell(CELL)

    def box(x0, y0, x1, y1):
        top.shapes(m1).insert(pya.DBox(
            min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def place(cid, x, y):
        tr = pya.Trans(pya.Trans.R0, um(x), um(y))
        top.insert(pya.CellInstArray(cid, tr))
        return ly.cell(cid).bbox().transformed(tr).to_dtype(ly.dbu)

    # Place two resistors side by side; gap for separate or* stubs
    gap = 8.0
    x_rp = -gap / 2 - rloc.right
    x_rn = gap / 2 + rloc.right
    bb_p = place(rh, x_rp, 0.0)
    bb_n = place(rh, x_rn, 0.0)
    print(f"Rrp {bb_p}; Rrn {bb_n} [SCH R={R_OHM}]", flush=True)

    # rppd: typically port A (top / +Y) and B (bottom / -Y) on M1
    # Connect top → vdd bus; bottom → orp / orn
    y_vdd = max(bb_p.top, bb_n.top) + 3.0
    y_or = min(bb_p.bottom, bb_n.bottom) - 3.0
    x_mid_p = 0.5 * (bb_p.left + bb_p.right)
    x_mid_n = 0.5 * (bb_n.left + bb_n.right)

    # Drop from resistor body mid-X; assume PCell ports near bbox edges
    box(x_mid_p - 0.20, bb_p.top - 0.05, x_mid_p + 0.20, y_vdd + 0.25)
    box(x_mid_n - 0.20, bb_n.top - 0.05, x_mid_n + 0.20, y_vdd + 0.25)
    box(min(x_mid_p, x_mid_n) - 0.20, y_vdd - 0.20,
        max(x_mid_p, x_mid_n) + 0.20, y_vdd + 0.25)

    box(x_mid_p - 0.20, y_or - 0.25, x_mid_p + 0.20, bb_p.bottom + 0.05)
    box(x_mid_n - 0.20, y_or - 0.25, x_mid_n + 0.20, bb_n.bottom + 0.05)

    # Local gnd (substrate) rail west — no device bulk on rppd without ring
    x_g = min(bb_p.left, bb_n.left) - 4.0
    y_g = 0.5 * (bb_p.bottom + bb_p.top)
    box(x_g - 0.20, y_g - 0.20, bb_p.left, y_g + 0.20)

    bb = top.bbox().to_dtype(ly.dbu)
    # x_from must stay inside/on the face — never past bb, or the stub grows
    # the bbox and the pin is no longer flush [pin_face].
    PF.connect_and_pin_on_face(
        top, m1, m1pin, m1txt, "vdd", "N", 0.5 * (x_mid_p + x_mid_n), y_vdd, bb)
    PF.connect_and_pin_on_face(
        top, m1, m1pin, m1txt, "orp", "S", x_mid_p, y_or, bb)
    PF.connect_and_pin_on_face(
        top, m1, m1pin, m1txt, "orn", "S", x_mid_n, y_or, bb)
    PF.connect_and_pin_on_face(
        top, m1, m1pin, m1txt, "gnd", "W", x_g, y_g, bb)
    fp = PF.parse_pins(top, m1txt)
    bb = top.bbox().to_dtype(ly.dbu)
    area = (bb.right - bb.left) * (bb.top - bb.bottom) * 1e-6
    print(f"bbox {bb}; area {area:.5f} mm² [GDS]", flush=True)
    print(f"face pins {fp}", flush=True)
    PF.assert_pins_on_faces(
        top, fp, {"vdd": "N", "orp": "S", "orn": "S", "gnd": "W"}, tol=0.10)

    gds = os.path.join(OUT, f"{CELL}.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)
    open(os.path.join(OUT, f"{CELL}.spice"), "w").write(
        f"* P2.7.4b {CELL} [SCH]\n"
        f".subckt {CELL} orp orn vdd gnd\n"
        f"Rrp vdd orp gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        f"Rrn vdd orn gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        ".ends\n"
    )
    open(os.path.join(OUT, f"summary_build_{CELL}.txt"), "w").write(
        f"area_mm2={area:.5f}\npins={fp}\n")
    print(f"wrote {gds}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
