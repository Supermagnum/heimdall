#!/usr/bin/env python3
"""Dump M1 text pins in a GDS hierarchy (debug)."""
from __future__ import annotations

import os
import re
import sys

sys.path[:0] = ["/foss/pdks/ihp-sg13g2/libs.tech/klayout/python"]
import pya  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
gds = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "out", "cml_latch_uhf.gds")


def name_of(s):
    raw = s.text
    if isinstance(raw, tuple):
        return raw[0]
    m = re.match(r"\('([^']+)'", str(raw))
    return m.group(1) if m else str(raw)


def walk(cell, trans, depth=0):
    m1txt = cell.layout().layer(8, 25)
    for s in cell.shapes(m1txt).each():
        if not s.is_text():
            continue
        p = s.text_dtrans.disp
        wp = trans.trans(pya.DPoint(p.x, p.y))
        print(f"{'  ' * depth}{cell.name}: {name_of(s)} @ ({wp.x:.3f},{wp.y:.3f})")
    for i in cell.each_inst():
        walk(i.cell, trans * i.dtrans, depth + 1)


ly = pya.Layout()
ly.read(gds)
walk(ly.top_cell(), pya.DCplxTrans())
