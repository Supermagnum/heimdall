#!/usr/bin/env python3
"""Pin-on-bbox-face helpers for P2.7.4b divider cells [HAND].

Join pins sit on the cell bounding-box face from the pin plan; metal reaches
the face and nothing of that pin pad protrudes past the face. Parents join
with gap stubs only (no reach-in).
"""
from __future__ import annotations

import re

HALF = 0.25  # pin M1 half-width


def pin_name(shape):
    raw = shape.text
    if isinstance(raw, tuple):
        return raw[0]
    m = re.match(r"\('([^']+)'", str(raw))
    return m.group(1) if m else str(raw)


def strip_pin_texts(cell, m1txt_layer):
    for sh in list(cell.shapes(m1txt_layer).each()):
        if sh.is_text():
            sh.delete()
    for i in cell.each_inst():
        strip_pin_texts(i.cell, m1txt_layer)


def parse_pins(cell, m1txt_layer):
    out = {}
    for s in cell.shapes(m1txt_layer).each():
        if s.is_text():
            out[pin_name(s)] = (s.text_dtrans.disp.x, s.text_dtrans.disp.y)
    return out


def _box(x0, y0, x1, y1):
    import pya
    return pya.DBox(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))


def place_pin(cell, m1, m1pin, m1txt, x, y, name):
    import pya
    cell.shapes(m1).insert(_box(x - HALF, y - HALF, x + HALF, y + HALF))
    cell.shapes(m1pin).insert(_box(x - 0.2, y - 0.2, x + 0.2, y + 0.2))
    cell.shapes(m1txt).insert(pya.DText(name, pya.DTrans(x, y)))


def cell_dbbox(cell):
    return cell.bbox().to_dtype(cell.layout().dbu)


def connect_and_pin_on_face(cell, m1, m1pin, m1txt, name, face, x_from, y_from,
                            bb=None, w=0.40):
    """M1 from (x_from,y_from) to face of bb; pin flush (outer edge = face).

    Pin center is inset by HALF so the pad does not protrude past the face.
    Returns (x_pin, y_pin).
    """
    if bb is None:
        bb = cell_dbbox(cell)
    hw = 0.5 * w
    if face == "E":
        x_pin = bb.right - HALF
        y_pin = y_from
        cell.shapes(m1).insert(_box(x_from, y_from - hw, x_pin, y_from + hw))
    elif face == "W":
        x_pin = bb.left + HALF
        y_pin = y_from
        cell.shapes(m1).insert(_box(x_pin, y_from - hw, x_from, y_from + hw))
    elif face == "N":
        x_pin = x_from
        y_pin = bb.top - HALF
        cell.shapes(m1).insert(_box(x_from - hw, y_from, x_from + hw, y_pin))
    elif face == "S":
        x_pin = x_from
        y_pin = bb.bottom + HALF
        cell.shapes(m1).insert(_box(x_from - hw, y_pin, x_from + hw, y_from))
    else:
        raise ValueError(face)
    place_pin(cell, m1, m1pin, m1txt, x_pin, y_pin, name)
    return x_pin, y_pin


def pin_flush_on_face(cell, m1, m1pin, m1txt, name, face, x_hint, y_hint,
                      bb=None):
    """Place pin flush on face without assuming prior metal (metal + pin)."""
    return connect_and_pin_on_face(
        cell, m1, m1pin, m1txt, name, face, x_hint, y_hint, bb=bb)


def assert_pins_on_faces(cell, pins, faces, tol=0.05):
    """faces: {name: 'E'|'W'|'N'|'S'}. pins: {name: (x,y)}."""
    bb = cell_dbbox(cell)
    for name, face in faces.items():
        x, y = pins[name]
        if face == "E":
            assert abs((x + HALF) - bb.right) <= tol, (name, "E", x, bb.right)
        elif face == "W":
            assert abs((x - HALF) - bb.left) <= tol, (name, "W", x, bb.left)
        elif face == "N":
            assert abs((y + HALF) - bb.top) <= tol, (name, "N", y, bb.top)
        elif face == "S":
            assert abs((y - HALF) - bb.bottom) <= tol, (name, "S", y, bb.bottom)
