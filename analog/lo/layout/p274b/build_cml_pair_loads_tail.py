#!/usr/bin/env python3
"""P2.7.4b step 3b2 — cml_pair_loads + MOSFET tail on s [SCH].

Instantiates proven cml_pair_loads GDS; adds NMOS W=15 µm ng=5 from s→gnd,
gate=nb_lo (UHF latch tail). Prove DRC/LVS before regen XC.
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
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402, F401

DBU = 0.001
R_W, R_L = "2.0u", "5.334u"
W_TAIL, NG_TAIL = "15.0u", 5
W_DUM = "3.0u"  # 15/5


def um(x):
    return int(round(x / DBU))


def main():
    ly = pya.Layout()
    ly.dbu = DBU
    ly.technology_name = "sg13g2"
    lib = pya.Library.library_by_name("SG13_dev", "sg13g2")
    lib_ly = lib.layout()

    src = pya.Layout()
    src.read(os.path.join(OUT, "cml_pair_loads.gds"))
    src_top = src.top_cell()
    cid = ly.add_cell(src_top.name)
    ly.cell(cid).copy_tree(src_top)

    top = ly.create_cell("cml_pair_loads_tail")
    top.insert(pya.CellInstArray(cid, pya.Trans(pya.Trans.R0, 0, 0)))
    pbb = ly.cell(cid).bbox().to_dtype(ly.dbu)

    m1 = ly.layer(8, 0)
    m1pin = ly.layer(8, 2)
    m1txt = ly.layer(8, 25)
    poly = ly.layer(5, 0)
    cont = ly.layer(6, 0)
    activ = ly.layer(1, 0)

    def box(x0, y0, x1, y1, layer=m1):
        top.shapes(layer).insert(pya.DBox(
            min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def pin(x, y, name):
        box(x - 0.25, y - 0.25, x + 0.25, y + 0.25)
        top.shapes(m1pin).insert(pya.DBox(x - 0.2, y - 0.2, x + 0.2, y + 0.2))
        top.shapes(m1txt).insert(pya.DText(name, pya.DTrans(x, y)))

    # parse parent pins
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
    print("parent pins", pins, flush=True)
    xs, ys = pins["s"]
    xg, yg = pins.get("gnd", (0.0, pbb.bottom - 2.0))

    # Tail MOSFET below source pin (VCO method: guardRingType=none)
    nmos = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("nmos").id(),
        {"w": W_TAIL, "l": "0.13u", "ng": NG_TAIL, "m": 1,
         "guardRingType": "none"})
    dum = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("nmos").id(),
        {"w": W_DUM, "l": "0.13u", "ng": 1, "m": 1,
         "guardRingType": "none"})
    ptap = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("ptap1").id(),
        {"w": "0.78u", "l": "0.78u"})

    loc = ly.cell(nmos).bbox().to_dtype(ly.dbu)
    dloc = ly.cell(dum).bbox().to_dtype(ly.dbu)
    y_tail = pbb.bottom - 6.0 - loc.top
    x_tail = xs - 0.5 * (loc.left + loc.right)
    t = pya.Trans(pya.Trans.R0, um(x_tail), um(y_tail))
    top.insert(pya.CellInstArray(nmos, t))
    tbb = ly.cell(nmos).bbox().transformed(t).to_dtype(ly.dbu)

    # End dummies left/right, G=S=D=gnd local
    gap = 2.0
    for sign, dum_cid in ((-1, dum), (1, dum)):
        xd = (tbb.left - gap - dloc.right) if sign < 0 else (
            tbb.right + gap - dloc.left)
        td = pya.Trans(pya.Trans.R0, um(xd), um(y_tail))
        top.insert(pya.CellInstArray(dum_cid, td))
        dbb = ly.cell(dum_cid).bbox().transformed(td).to_dtype(ly.dbu)
        # short all SDG of dummy to local gnd via M1
        box(dbb.left, dbb.bottom, dbb.right, dbb.top)

    # M1 S/D columns of tail: even=D odd=S (same as pair)
    def m1_sd_cols(cid, trans):
        cell = ly.cell(cid)
        uniq = {}
        for s in cell.shapes(m1).each():
            if not s.is_box():
                continue
            b = s.bbox().transformed(trans).to_dtype(ly.dbu)
            if b.width() > 0.25 or b.height() < 1.0:
                continue
            cx = round((b.left + b.right) / 2, 3)
            uniq[cx] = b
        return [uniq[k] for k in sorted(uniq)]

    cols = m1_sd_cols(nmos, t)
    drains = [c for i, c in enumerate(cols) if i % 2 == 0]
    sources = [c for i, c in enumerate(cols) if i % 2 == 1]
    print(f"tail cols={len(cols)} D={len(drains)} S={len(sources)}", flush=True)

    # Drain (=s of pair) join via M2 spur method: M1 stubs + M2
    m2 = ly.layer(10, 0)
    via = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("via_stack").id(),
        {"b_layer": "Metal1", "t_layer": "Metal2",
         "vn_columns": 1, "vn_rows": 1})

    def place_via(x, y):
        top.insert(pya.CellInstArray(
            via, pya.Trans(pya.Trans.R0, um(x), um(y))))

    # Join drains to s pin (above) without M1 across opposite S/D
    y_bus_d = tbb.top + 1.2
    for c in drains:
        cx = 0.5 * (c.left + c.right)
        box(cx - 0.14, c.top - 0.1, cx + 0.14, y_bus_d + 0.2)
        place_via(cx, y_bus_d)
    if drains:
        box(drains[0].left, y_bus_d, drains[-1].right, y_bus_d + 0.28,
            layer=m2)
        # M2 up toward s, then via down to M1 at s
        place_via(xs, y_bus_d)
        box(min(xs, 0.5 * (drains[0].left + drains[-1].right)) - 0.14,
            y_bus_d, max(xs, 0.5 * (drains[0].left + drains[-1].right)) + 0.14,
            y_bus_d + 0.28, layer=m2)
        box(xs - 0.14, y_bus_d, xs + 0.14, ys, layer=m2)
        place_via(xs, ys)
        box(xs - 0.14, ys - 0.2, xs + 0.14, ys + 0.2)

    # Sources to gnd
    y_bus_s = tbb.bottom - 1.2
    for c in sources:
        cx = 0.5 * (c.left + c.right)
        box(cx - 0.14, y_bus_s - 0.2, cx + 0.14, c.bottom + 0.1)
        place_via(cx, y_bus_s)
    if sources:
        box(sources[0].left, y_bus_s - 0.28, sources[-1].right, y_bus_s,
            layer=m2)
        # gnd rail
        box(min(tbb.left, xg) - 1.0, y_bus_s - 0.28,
            max(tbb.right, xg) + 1.0, y_bus_s, layer=m2)
        place_via(xg if "gnd" in pins else 0.5 * (tbb.left + tbb.right),
                  y_bus_s)

    # Gate exit off active (poly pad above Activ)
    gates = []
    for s in ly.cell(nmos).shapes(poly).each():
        if not s.is_box():
            continue
        b = s.bbox().transformed(t).to_dtype(ly.dbu)
        if b.width() < 0.20 and b.height() > 0.5:
            gates.append(b)
    gates.sort(key=lambda b: b.left)
    # unique by cx
    uniq_g, seen = [], set()
    for g in gates:
        cx = round(0.5 * (g.left + g.right), 3)
        if cx not in seen:
            seen.add(cx)
            uniq_g.append(g)
    gates = uniq_g
    activ_top = tbb.top
    for s in ly.cell(nmos).shapes(activ).each():
        if s.is_box():
            b = s.bbox().transformed(t).to_dtype(ly.dbu)
            activ_top = max(activ_top, b.top)
    if gates:
        y_pad0 = max(activ_top + 0.50, max(g.top for g in gates) + 0.30)
        y_pad1 = y_pad0 + 0.50
        gx0 = min(g.left for g in gates)
        gx1 = max(g.right for g in gates)
        for g in gates:
            gx = 0.5 * (g.left + g.right)
            half = 0.5 * (g.right - g.left)
            box(gx - half, g.top - 0.05, gx + half, y_pad0 + 0.05, layer=poly)
        box(gx0 - 0.05, y_pad0, gx1 + 0.05, y_pad1, layer=poly)
        for g in gates:
            gx = 0.5 * (g.left + g.right)
            box(gx - 0.08, y_pad0 + 0.16, gx + 0.08, y_pad0 + 0.32, layer=cont)
            box(gx - 0.08, y_pad0 + 0.16, gx + 0.08, y_pad1 + 0.16)
        box(gx0 - 0.08, y_pad0 + 0.16, gx1 + 0.08, y_pad1 + 0.16)
        x_nb = tbb.right + 3.0
        y_nb = y_pad1 + 0.5
        box(gx1 - 0.14, y_pad1, gx1 + 0.14, y_nb + 0.28)
        box(min(gx1, x_nb) - 0.14, y_nb, max(gx1, x_nb) + 0.14, y_nb + 0.28)
        pin(x_nb, y_nb + 0.5, "nb_lo")

    # ptap near source
    top.insert(pya.CellInstArray(
        ptap, pya.Trans(pya.Trans.R0, um(tbb.left - 2.0), um(y_bus_s))))

    # re-export ports
    for name, (x, y) in pins.items():
        if name == "s":
            continue  # s is now internal (drain of tail)
        pin(x, y, name)
    pin(xs, ys - 0.5, "s")  # keep s for debug / LVS as drain node

    gds = os.path.join(OUT, "cml_pair_loads_tail.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)

    open(os.path.join(OUT, "cml_pair_loads_tail.spice"), "w").write(
        "* P2.7.4b cml_pair_loads_tail flat [SCH]\n"
        ".subckt cml_pair_loads_tail d1 d2 g1 g2 s gnd vdd nb_lo\n"
        "Mm1 d1 g1 s gnd sg13_lv_nmos w=7.5u l=0.13u\n"
        "Mm2 d2 g2 s gnd sg13_lv_nmos w=7.5u l=0.13u\n"
        "Mdum gnd gnd gnd gnd sg13_lv_nmos w=3.0u l=0.13u\n"
        f"Rrlp vdd d1 gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        f"Rrln vdd d2 gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        "Mmt s nb_lo gnd gnd sg13_lv_nmos w=15.0u l=0.13u\n"
        "Mdumt gnd gnd gnd gnd sg13_lv_nmos w=3.0u l=0.13u\n"
        ".ends\n"
    )
    print("WROTE", gds, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
