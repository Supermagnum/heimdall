#!/usr/bin/env python3
"""P2.7.4b step 3b1 — cml_diff_pair + matched rppd loads [SCH].

Instantiates proven cml_diff_pair GDS and adds two rppd (666.7 Ω) from
d1/d2 to vdd. Prove DRC/LVS before adding tail / regen.
"""
from __future__ import annotations

import gzip
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path[:0] = [
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402, F401

DBU = 0.001
R_W, R_L = "2.0u", "5.334u"


def um(x):
    return int(round(x / DBU))


def main():
    ly = pya.Layout()
    ly.dbu = DBU
    ly.technology_name = "sg13g2"
    lib = pya.Library.library_by_name("SG13_dev", "sg13g2")
    lib_ly = lib.layout()

    # load proven pair as library cell
    pair_ly = pya.Layout()
    pair_ly.read(os.path.join(OUT, "cml_diff_pair.gds"))
    pair_top = pair_ly.top_cell()
    pair_cid = ly.add_cell(pair_top.name)
    ly.cell(pair_cid).copy_tree(pair_top)

    top = ly.create_cell("cml_pair_loads")
    t = pya.Trans(pya.Trans.R0, 0, 0)
    top.insert(pya.CellInstArray(pair_cid, t))
    pbb = ly.cell(pair_cid).bbox().to_dtype(ly.dbu)

    rh = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("rppd").id(),
        {"R": "666.7", "w": R_W, "l": R_L, "b": 0,
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

    # Find pin texts — KLayout may stringify as "('d1',r0 …)"
    import re as _re
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

    y_r = pbb.top + 4.0
    bb_rl = place(rh, xd1 - rloc.width() / 2 - rloc.left, y_r - rloc.bottom)
    bb_rr = place(rh, xd2 - rloc.width() / 2 - rloc.left, y_r - rloc.bottom)

    # connect d pins up to resistor bottoms; tops to vdd
    for (xd, yd), bb in (((xd1, yd1), bb_rl), ((xd2, yd2), bb_rr)):
        cx = 0.5 * (bb.left + bb.right)
        box(xd - 0.14, yd, xd + 0.14, bb.bottom + 0.3)
        box(min(xd, cx) - 0.14, bb.bottom + 0.2,
            max(xd, cx) + 0.14, bb.bottom + 0.5)
        box(cx - 0.14, bb.bottom + 0.2, cx + 0.14, bb.bottom + 0.5)
        box(cx - 0.14, bb.top - 0.3, cx + 0.14, bb.top + 2.0)

    y_vdd = max(bb_rl.top, bb_rr.top) + 2.0
    box(min(bb_rl.left, bb_rr.left), y_vdd,
        max(bb_rl.right, bb_rr.right), y_vdd + 0.28)
    pin(0.5 * (bb_rl.left + bb_rr.right), y_vdd + 0.5, "vdd")

    # re-export pair ports
    for name, (x, y) in pins.items():
        if name != "d1" and name != "d2":
            pin(x, y, name)
        else:
            # d1/d2 still available as mid-net labels for LVS (internal to loads)
            pass
    pin(xd1, yd1 - 2.0, "d1")  # keep for debug; spice uses internal
    pin(xd2, yd2 - 2.0, "d2")

    gds = os.path.join(OUT, "cml_pair_loads.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)
    # LVS: pair + loads; expose d1/d2 as loaded outputs (qp/qn style)
    open(os.path.join(OUT, "cml_pair_loads.spice"), "w").write(
        "* P2.7.4b cml_pair_loads = diff pair + rppd [SCH]\n"
        ".subckt cml_pair_loads d1 d2 g1 g2 s gnd vdd\n"
        "Xpair d1 d2 g1 g2 s gnd cml_diff_pair\n"
        f"Rrlp vdd d1 gnd rppd w={R_W} l={R_L} ps=0.18u b=0 m=1\n"
        f"Rrln vdd d2 gnd rppd w={R_W} l={R_L} ps=0.18u b=0 m=1\n"
        ".ends\n"
        "* inline pair for flat LVS (no hierarchy in spice reader)\n"
        ".subckt cml_diff_pair d1 d2 g1 g2 s gnd\n"
        "Mm1 d1 g1 s gnd sg13_lv_nmos w=7.5u l=0.13u\n"
        "Mm2 d2 g2 s gnd sg13_lv_nmos w=7.5u l=0.13u\n"
        "Mdum gnd gnd gnd gnd sg13_lv_nmos w=3.0u l=0.13u\n"
        ".ends\n"
    )
    # Flat spice preferred for IHP LVS
    open(os.path.join(OUT, "cml_pair_loads.spice"), "w").write(
        "* P2.7.4b cml_pair_loads flat [SCH]\n"
        ".subckt cml_pair_loads d1 d2 g1 g2 s gnd vdd\n"
        "Mm1 d1 g1 s gnd sg13_lv_nmos w=7.5u l=0.13u\n"
        "Mm2 d2 g2 s gnd sg13_lv_nmos w=7.5u l=0.13u\n"
        "Mdum gnd gnd gnd gnd sg13_lv_nmos w=3.0u l=0.13u\n"
        f"Rrlp vdd d1 gnd rppd w={R_W} l={R_L} ps=0.18u b=0 m=1\n"
        f"Rrln vdd d2 gnd rppd w={R_W} l={R_L} ps=0.18u b=0 m=1\n"
        ".ends\n"
    )
    print("WROTE", gds, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
