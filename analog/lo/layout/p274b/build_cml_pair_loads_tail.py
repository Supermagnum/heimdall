#!/usr/bin/env python3
"""P2.7.4b — join cml_pair_loads + cml_tail by 2026-11-20 pin plan [SCH].

pair_loads.s (S, X≈0) ↔ cml_tail.drain (N, X≈0): straight M1 stub in gap.
gnd on west faces: west M1 rail in gaps only. No metal through child cells.
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
GAP = 3.0  # ≥2 µm per plan


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

    m1 = ly.layer(8, 0)
    m1pin = ly.layer(8, 2)
    m1txt = ly.layer(8, 25)

    pl_cid = load_cell(ly, "cml_pair_loads.gds", "cml_pair_loads")
    tl_cid = load_cell(ly, "cml_tail.gds", "cml_tail")

    # Rename tail.drain pin text → s so extract port is s (not drain|s)
    # [netgen pin match]. Geometry unchanged.
    for sh in list(ly.cell(tl_cid).shapes(m1txt).each()):
        if not sh.is_text():
            continue
        raw = sh.text
        if isinstance(raw, tuple):
            name = raw[0]
        else:
            m = re.match(r"\('([^']+)'", str(raw))
            name = m.group(1) if m else str(raw)
        if name == "drain":
            sh.text = pya.DText("s", sh.text_dtrans)

    top = ly.create_cell("cml_pair_loads_tail")
    top.insert(pya.CellInstArray(pl_cid, pya.Trans(pya.Trans.R0, 0, 0)))
    pbb = ly.cell(pl_cid).bbox().to_dtype(ly.dbu)
    pp = parse_pins(ly, pl_cid, m1txt)
    print("pair_loads", pp, "pbb", pbb, flush=True)

    tloc = ly.cell(tl_cid).bbox().to_dtype(ly.dbu)
    # X-align former-drain (now s) under pair s pin
    xs, ys = pp["s"]
    tp0 = parse_pins(ly, tl_cid, m1txt)
    xd0, yd0 = tp0["s"]
    x_t = xs - xd0
    y_t = pbb.bottom - GAP - tloc.top
    top.insert(pya.CellInstArray(
        tl_cid, pya.Trans(pya.Trans.R0, um(x_t), um(y_t))))
    tbb = ly.cell(tl_cid).bbox().transformed(
        pya.Trans(pya.Trans.R0, um(x_t), um(y_t))).to_dtype(ly.dbu)
    tp = {n: (x + x_t, y + y_t) for n, (x, y) in tp0.items()}
    # keep key name drain for stub coords (= renamed s pin on tail)
    tp["drain"] = tp["s"]
    print("tail", tp, "tbb", tbb, flush=True)

    def box(layer, x0, y0, x1, y1):
        top.shapes(layer).insert(pya.DBox(
            min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def pin(x, y, name):
        box(m1, x - 0.25, y - 0.25, x + 0.25, y + 0.25)
        top.shapes(m1pin).insert(pya.DBox(x - 0.2, y - 0.2, x + 0.2, y + 0.2))
        top.shapes(m1txt).insert(pya.DText(name, pya.DTrans(x, y)))

    xd, yd = tp["drain"]
    # Straight M1 stub in gap only (pins already on facing faces)
    assert abs(xs - xd) < 0.05, (xs, xd)
    box(m1, xs - 0.20, yd, xs + 0.20, ys)
    print(f"s↔drain stub Y {yd:.2f}→{ys:.2f} gap={pbb.bottom - tbb.top:.2f}",
          flush=True)

    # gnd west rail in gap / outside both bboxes
    xg_p, yg_p = pp["gnd"]
    xg_t, yg_t = tp["gnd"]
    x_west = min(pbb.left, tbb.left, xg_p, xg_t) - 2.0
    box(m1, x_west - 0.20, yg_p - 0.20, xg_p + 0.20, yg_p + 0.20)
    box(m1, x_west - 0.20, yg_t - 0.20, xg_t + 0.20, yg_t + 0.20)
    box(m1, x_west - 0.20, min(yg_p, yg_t),
        x_west + 0.20, max(yg_p, yg_t))

    for name, (x, y) in pp.items():
        if name == "s":
            continue
        pin(x, y, name)
    pin(tp["nb_lo"][0], tp["nb_lo"][1], "nb_lo")
    pin(xs, ys, "s")  # keep label; net is drain|s

    gds = os.path.join(OUT, "cml_pair_loads_tail.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)

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
    print("WROTE", gds, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
