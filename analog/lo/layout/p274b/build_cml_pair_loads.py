#!/usr/bin/env python3
"""P2.7.4b — cml_diff_pair + matched rppd loads [SCH].

Face pins follow 2026-11-20 latch plan: s=S, d1/d2=E, gnd=W, g1/g2/vdd=N.
"""
from __future__ import annotations

import gzip
import os
import re as _re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path[:0] = [
    HERE,
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402, F401
import pin_face as PF  # noqa: E402

DBU = 0.001
R_W, R_L = "2.0u", "5.334u"
R_OHM = "666.7"
CELL = "cml_pair_loads"
PAIR_GDS = "cml_diff_pair.gds"
PAIR_W = "7.5u"
DUM_W = "3.0u"


def um(x):
    return int(round(x / DBU))


def main():
    ly = pya.Layout()
    ly.dbu = DBU
    ly.technology_name = "sg13g2"
    lib = pya.Library.library_by_name("SG13_dev", "sg13g2")
    lib_ly = lib.layout()

    pair_ly = pya.Layout()
    pair_ly.read(os.path.join(OUT, PAIR_GDS))
    pair_top = pair_ly.top_cell()
    pair_cid = ly.add_cell(pair_top.name)
    ly.cell(pair_cid).copy_tree(pair_top)

    top = ly.create_cell(CELL)
    t = pya.Trans(pya.Trans.R0, 0, 0)
    top.insert(pya.CellInstArray(pair_cid, t))
    pbb = ly.cell(pair_cid).bbox().to_dtype(ly.dbu)

    rh = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("rppd").id(),
        {"R": R_OHM, "w": R_W, "l": R_L, "b": 0,
         "Calculate": "R", "guardRingType": "none"})
    rloc = ly.cell(rh).bbox().to_dtype(ly.dbu)
    m1 = ly.layer(8, 0)
    m1pin = ly.layer(8, 2)
    m1txt = ly.layer(8, 25)

    def box(x0, y0, x1, y1):
        top.shapes(m1).insert(pya.DBox(
            min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def pin(x, y, name):
        box(x - 0.25, y - 0.25, x + 0.25, y + 0.25)
        top.shapes(m1pin).insert(pya.DBox(x - 0.2, y - 0.2, x + 0.2, y + 0.2))
        top.shapes(m1txt).insert(pya.DText(name, pya.DTrans(x, y)))

    def place(cid, x, y):
        tr = pya.Trans(pya.Trans.R0, um(x), um(y))
        top.insert(pya.CellInstArray(cid, tr))
        return ly.cell(cid).bbox().transformed(tr).to_dtype(ly.dbu)

    pins = {}
    for s in ly.cell(pair_cid).shapes(m1txt).each():
        if not s.is_text():
            continue
        raw = s.text
        if isinstance(raw, tuple):
            name = raw[0]
        else:
            m = _re.match(r"\('([^']+)'", str(raw))
            name = m.group(1) if m else str(raw)
        pins[name] = (s.text_dtrans.disp.x, s.text_dtrans.disp.y)
    print("pair pins", pins, flush=True)
    xd1, yd1 = pins["d1"]
    xd2, yd2 = pins["d2"]
    xs, ys = pins["s"]
    xg, yg = pins["gnd"]

    # Resistors north of pair body; X near device centers (not east pins)
    y_r = pbb.top + 4.0
    x_rl = 0.5 * (pbb.left + 0.0)   # left half
    x_rr = 0.5 * (0.0 + pbb.right)  # right half
    bb_rl = place(rh, x_rl - rloc.width() / 2 - rloc.left, y_r - rloc.bottom)
    bb_rr = place(rh, x_rr - rloc.width() / 2 - rloc.left, y_r - rloc.bottom)

    # East drains → north on separate X/Y. d2 north escape uses M2 so M1 at
    # yd1 stays free for d1 H to the common E-face X [LVS].
    lib = pya.Library.library_by_name("SG13_dev", "sg13g2")
    lib_ly = lib.layout()
    vs12 = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("via_stack").id(),
        {"b_layer": "Metal1", "t_layer": "Metal2",
         "vn_columns": 1, "vn_rows": 1})
    m2 = ly.layer(10, 0)

    def via(x, y):
        top.insert(pya.CellInstArray(
            vs12, pya.Trans(pya.Trans.R0, um(x - 0.05), um(y))))

    def box2(x0, y0, x1, y1):
        top.shapes(m2).insert(pya.DBox(
            min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    x_lane1, x_lane2 = xd1 + 2.0, xd2 + 4.0
    x_face = x_lane2 + 2.5
    y_west1, y_west2 = pbb.top + 1.0, pbb.top + 2.8

    # d1: M1 lane vertical (yd1 is this net — OK)
    cx1 = 0.5 * (bb_rl.left + bb_rl.right)
    box(xd1 - 0.14, yd1 - 0.14, xd1 + 0.14, yd1 + 0.14)
    box(min(xd1, x_lane1) - 0.14, yd1 - 0.14,
        max(xd1, x_lane1) + 0.14, yd1 + 0.14)
    box(x_lane1 - 0.14, yd1, x_lane1 + 0.14, y_west1)
    box(min(x_lane1, cx1) - 0.14, y_west1 - 0.14,
        max(x_lane1, cx1) + 0.14, y_west1 + 0.14)
    box(cx1 - 0.14, min(y_west1, bb_rl.bottom + 0.3),
        cx1 + 0.14, max(y_west1, bb_rl.bottom + 0.5))
    box(cx1 - 0.14, bb_rl.bottom + 0.2, cx1 + 0.14, bb_rl.bottom + 0.5)
    box(cx1 - 0.14, bb_rl.top - 0.3, cx1 + 0.14, bb_rl.top + 2.0)

    # d2: H at yd2 to lane; M2 vertical (gap in M1 at yd1 for d1 face stub)
    cx2 = 0.5 * (bb_rr.left + bb_rr.right)
    box(xd2 - 0.14, yd2 - 0.14, xd2 + 0.14, yd2 + 0.14)
    box(min(xd2, x_lane2) - 0.14, yd2 - 0.14,
        max(xd2, x_lane2) + 0.14, yd2 + 0.14)
    via(x_lane2, yd2)
    box2(x_lane2 - 0.20, yd2 - 0.15, x_lane2 + 0.20, y_west2 + 0.40)
    via(x_lane2, y_west2)
    box(min(x_lane2, cx2) - 0.14, y_west2 - 0.14,
        max(x_lane2, cx2) + 0.14, y_west2 + 0.14)
    box(cx2 - 0.14, min(y_west2, bb_rr.bottom + 0.3),
        cx2 + 0.14, max(y_west2, bb_rr.bottom + 0.5))
    box(cx2 - 0.14, bb_rr.bottom + 0.2, cx2 + 0.14, bb_rr.bottom + 0.5)
    box(cx2 - 0.14, bb_rr.top - 0.3, cx2 + 0.14, bb_rr.top + 2.0)

    # H-only M1 to common E face (no V at x_face)
    box(min(x_lane1, x_face) - 0.14, yd1 - 0.14,
        max(x_lane1, x_face) + 0.14, yd1 + 0.14)
    box(min(x_lane2, x_face) - 0.14, yd2 - 0.14,
        max(x_lane2, x_face) + 0.14, yd2 + 0.14)

    y_vdd = max(bb_rl.top, bb_rr.top) + 2.0
    box(min(bb_rl.left, bb_rr.left), y_vdd,
        max(bb_rl.right, bb_rr.right), y_vdd + 0.28)
    x_vdd = 0.5 * (bb_rl.left + bb_rr.right)
    xg1, yg1 = pins["g1"]
    xg2, yg2 = pins["g2"]
    # vdd pin on N face; g1/g2 stay at child Y (top ports; N move later if needed)
    y_n = y_vdd + 0.5

    PF.strip_pin_texts(ly.cell(pair_cid), m1txt)
    pin(x_face, yd1, "d1")
    pin(x_face, yd2, "d2")
    pin(xs, ys, "s")
    pin(xg, yg, "gnd")
    pin(xg1, yg1, "g1")
    pin(xg2, yg2, "g2")
    pin(x_vdd, y_n, "vdd")
    face_pins = PF.parse_pins(top, m1txt)
    bb = top.bbox().to_dtype(ly.dbu)
    print(f"bbox {bb} face pins {face_pins}", flush=True)
    assert abs((face_pins["d1"][0] + PF.HALF) - bb.right) < 0.05
    assert abs((face_pins["d2"][0] + PF.HALF) - bb.right) < 0.05

    gds = os.path.join(OUT, f"{CELL}.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)
    open(os.path.join(OUT, f"{CELL}.spice"), "w").write(
        f"* P2.7.4b {CELL} flat [SCH]\n"
        f".subckt {CELL} d1 d2 g1 g2 s gnd vdd\n"
        f"Mm1 d1 g1 s gnd sg13_lv_nmos w={PAIR_W} l=0.13u\n"
        f"Mm2 d2 g2 s gnd sg13_lv_nmos w={PAIR_W} l=0.13u\n"
        f"Mdum gnd gnd gnd gnd sg13_lv_nmos w={DUM_W} l=0.13u\n"
        f"Rrlp vdd d1 gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        f"Rrln vdd d2 gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        ".ends\n"
    )
    print("WROTE", gds, "s=", (xs, ys), "gnd=", (xg, yg), flush=True)
    return 0


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--cell", default="cml_pair_loads")
    ap.add_argument("--pair-gds", default="cml_diff_pair.gds")
    ap.add_argument("--pair-w", default="7.5")
    ap.add_argument("--dum-w", default="3.0")
    ap.add_argument("--r", default="666.7")
    ap.add_argument("--rw", default="2.0")
    ap.add_argument("--rl", default="5.334")
    args = ap.parse_args()
    CELL = args.cell
    PAIR_GDS = args.pair_gds
    PAIR_W = f"{float(args.pair_w):g}u"
    DUM_W = f"{float(args.dum_w):g}u"
    R_OHM = str(args.r)
    R_W = f"{float(args.rw):g}u"
    R_L = f"{float(args.rl):g}u"
    raise SystemExit(main())
