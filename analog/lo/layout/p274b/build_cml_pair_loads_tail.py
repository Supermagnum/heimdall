#!/usr/bin/env python3
"""P2.7.4b step 3b2 — join proven cml_pair_loads + cml_tail [SCH].

Escape routing: M2 leaves each pin outboard, then runs in clear space
beside both cells. Never draw M2/M1 through either child bbox.
"""
from __future__ import annotations

import gzip
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path[:0] = [
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/"
    "pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402, F401

DBU = 0.001
R_W, R_L = "2.0u", "5.334u"


def um(x):
    return int(round(float(x) / DBU))


def parse_pins(ly, cid, m1txt):
    pins = {}
    for s in ly.cell(cid).shapes(m1txt).each():
        if not s.is_text():
            continue
        raw = s.text
        if isinstance(raw, tuple):
            name = raw[0]
        else:
            m = re.match(r"\('([^']+)'", str(raw))
            name = m.group(1) if m else str(raw)
        pins[name] = (s.text_dtrans.disp.x, s.text_dtrans.disp.y)
    return pins


def load_cell(ly, gds_name, cell_name):
    src = pya.Layout()
    src.read(os.path.join(OUT, gds_name))
    src_top = None
    for c in src.each_cell():
        if c.name == cell_name:
            src_top = c
            break
    if src_top is None:
        src_top = src.top_cell()
    cid = ly.add_cell(cell_name + "_lib")
    ly.cell(cid).copy_tree(src_top)
    ly.cell(cid).name = cell_name
    return cid


def main():
    ly = pya.Layout()
    ly.dbu = DBU
    ly.technology_name = "sg13g2"
    lib = pya.Library.library_by_name("SG13_dev", "sg13g2")
    lib_ly = lib.layout()

    m1 = ly.layer(8, 0)
    m1pin = ly.layer(8, 2)
    m1txt = ly.layer(8, 25)
    m2 = ly.layer(10, 0)

    pl_cid = load_cell(ly, "cml_pair_loads.gds", "cml_pair_loads")
    tl_cid = load_cell(ly, "cml_tail.gds", "cml_tail")

    top = ly.create_cell("cml_pair_loads_tail")
    top.insert(pya.CellInstArray(pl_cid, pya.Trans(pya.Trans.R0, 0, 0)))
    pbb = ly.cell(pl_cid).bbox().to_dtype(ly.dbu)
    pp = parse_pins(ly, pl_cid, m1txt)
    print("pair_loads", pp, "pbb", pbb, flush=True)

    tloc = ly.cell(tl_cid).bbox().to_dtype(ly.dbu)
    gap = 12.0
    y_t = pbb.bottom - gap - tloc.top
    # centre tail under pair
    x_t = 0.5 * (pbb.left + pbb.right) - 0.5 * (tloc.left + tloc.right)
    top.insert(pya.CellInstArray(
        tl_cid, pya.Trans(pya.Trans.R0, um(x_t), um(y_t))))
    tbb = ly.cell(tl_cid).bbox().transformed(
        pya.Trans(pya.Trans.R0, um(x_t), um(y_t))).to_dtype(ly.dbu)
    tp0 = parse_pins(ly, tl_cid, m1txt)
    tp = {n: (x + x_t, y + y_t) for n, (x, y) in tp0.items()}
    print("tail", tp, "tbb", tbb, flush=True)

    vs12 = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("via_stack").id(),
        {"b_layer": "Metal1", "t_layer": "Metal2",
         "vn_columns": 1, "vn_rows": 1})

    def box(layer, x0, y0, x1, y1):
        top.shapes(layer).insert(pya.DBox(
            min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def pin(x, y, name):
        box(m1, x - 0.25, y - 0.25, x + 0.25, y + 0.25)
        top.shapes(m1pin).insert(pya.DBox(x - 0.2, y - 0.2, x + 0.2, y + 0.2))
        top.shapes(m1txt).insert(pya.DText(name, pya.DTrans(x, y)))

    def via(x, y):
        top.insert(pya.CellInstArray(
            vs12, pya.Trans(pya.Trans.R0, um(x), um(y))))

    xs, ys = pp["s"]
    xd, yd = tp["drain"]
    # s sits above the d1/d2 vertical M1 straps — never run M1 east at ys.
    # Drop s south on M2 into the inter-cell gap, then east outside.
    x_esc = max(pbb.right, tbb.right) + 5.0
    y_gap = 0.5 * (pbb.bottom + tbb.top)  # mid-gap, clear of both

    via(xs, ys)
    # M2 south from s into gap only (stop before leaving pair? — use via
    # at south face of pair, M2 only below pbb.bottom)
    y_face_p = pbb.bottom - 0.5
    via(xs, y_face_p)
    # short M2 from s pin to south face — RISK: may hit pair M2.
    # Prefer: M1 south from s to face (s is source bus; d straps are east),
    # then via at face.
    box(m1, xs - 0.20, y_face_p - 0.20, xs + 0.20, ys + 0.20)
    # M2 in gap: south face → mid gap → east to esc → south to tail face
    y_face_t = tbb.top + 0.5
    box(m2, xs - 0.20, y_gap - 0.15, xs + 0.20, y_face_p + 0.20)
    box(m2, xs - 0.20, y_gap - 0.15, x_esc + 0.20, y_gap + 0.40)
    box(m2, x_esc - 0.20, min(y_gap, y_face_t) - 0.15,
        x_esc + 0.20, max(y_gap, y_face_t) + 0.40)
    via(x_esc, y_face_t)
    # into tail: M1 from north face down to drain (drain is south of tail top)
    # path along east outside then in to drain — M1 only outside tail or
    # short spur at drain Y from east.
    x_edge_t = tbb.right + 1.0
    box(m1, x_esc - 0.20, y_face_t - 0.20, x_esc + 0.20, yd + 0.20)
    box(m1, xd - 0.20, yd - 0.20, x_esc + 0.20, yd + 0.20)
    via(xd, yd)

    # gnd: south from pair gnd into gap on west, then to tail gnd.
    # pair gnd is south; avoid d1/d2 which are also south — go west first.
    xg_p, yg_p = pp["gnd"]
    xg_t, yg_t = tp["gnd"]
    x_west = min(pbb.left, tbb.left) - 5.0
    # pair gnd → west outside (gnd is centre; d1 is west — go further west
    # past d1 pin x before turning)
    x_clear = min(pp["d1"][0], pbb.left) - 3.0
    x_west = min(x_west, x_clear - 2.0)
    box(m1, x_west - 0.20, yg_p - 0.20, xg_p + 0.20, yg_p + 0.20)
    via(x_west, yg_p)
    box(m1, x_west - 0.20, yg_t - 0.20, xg_t + 0.20, yg_t + 0.20)
    via(x_west, yg_t)
    box(m2, x_west - 0.20, min(yg_p, yg_t) - 0.15,
        x_west + 0.20, max(yg_p, yg_t) + 0.40)

    for name, (x, y) in pp.items():
        if name == "s":
            continue
        pin(x, y, name)
    pin(tp["nb_lo"][0], tp["nb_lo"][1], "nb_lo")
    pin(xs, ys, "s")

    gds = os.path.join(OUT, "cml_pair_loads_tail.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)

    # Dummies: pair 3.0 + tail 6.0 → combine to 9.0 for LVS
    open(os.path.join(OUT, "cml_pair_loads_tail.spice"), "w").write(
        "* P2.7.4b cml_pair_loads_tail = pair_loads + cml_tail [SCH]\n"
        ".subckt cml_pair_loads_tail d1 d2 g1 g2 s gnd vdd nb_lo\n"
        "Mm1 d1 g1 s gnd sg13_lv_nmos w=7.5u l=0.13u\n"
        "Mm2 d2 g2 s gnd sg13_lv_nmos w=7.5u l=0.13u\n"
        f"Rrlp vdd d1 gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        f"Rrln vdd d2 gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        "Mmt s nb_lo gnd gnd sg13_lv_nmos w=15.0u l=0.13u\n"
        "Mdum gnd gnd gnd gnd sg13_lv_nmos w=9.0u l=0.13u\n"
        ".ends\n"
    )
    print("WROTE", gds, "escape", x_esc, x_west, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
