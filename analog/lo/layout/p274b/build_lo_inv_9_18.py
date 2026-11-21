#!/usr/bin/env python3
"""P2.7.4b — lo_inv_9_18 as 2× parallel lo_inv_45_9 [SCH W=9/18].

ng=3 single-device mega-shorted; parallel half-size leaves stay ng=1 proven.
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
    HERE,
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/"
    "pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402, F401
import pin_face as PF  # noqa: E402

DBU = 0.001
CELL = "lo_inv_9_18"
CHILD = "lo_inv_45_9"
GAP = 3.0


def um(x):
    return int(round(float(x) / DBU))


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


def main():
    ly = pya.Layout()
    ly.dbu = DBU
    ly.technology_name = "sg13g2"
    lib = pya.Library.library_by_name("SG13_dev", "sg13g2")
    lib_ly = lib.layout()
    m1 = ly.layer(8, 0)
    m1pin = ly.layer(8, 2)
    m1txt = ly.layer(8, 25)
    vs12 = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("via_stack").id(),
        {"b_layer": "Metal1", "t_layer": "Metal2",
         "vn_columns": 1, "vn_rows": 1})

    cid = load_cell(ly, f"{CHILD}.gds", CHILD)
    pins0 = parse_pins(ly, cid, m1txt)
    bb0 = ly.cell(cid).bbox().to_dtype(ly.dbu)
    PF.strip_pin_texts(ly.cell(cid), m1txt)

    # second copy under a distinct cell name (shared GDS)
    src = pya.Layout()
    src.read(os.path.join(OUT, f"{CHILD}.gds"))
    src_top = src.top_cell()
    for c in src.each_cell():
        if c.name == CHILD:
            src_top = c
            break
    cid2 = ly.add_cell(CHILD + "_b")
    ly.cell(cid2).copy_tree(src_top)
    PF.strip_pin_texts(ly.cell(cid2), m1txt)

    top = ly.create_cell(CELL)
    x0 = -bb0.right - GAP / 2
    x1 = -bb0.left + GAP / 2
    top.insert(pya.CellInstArray(cid, pya.Trans(pya.Trans.R0, um(x0), 0)))
    top.insert(pya.CellInstArray(cid2, pya.Trans(pya.Trans.R0, um(x1), 0)))

    def map_pins(x):
        return {n: (x + px, py) for n, (px, py) in pins0.items()}

    pL, pR = map_pins(x0), map_pins(x1)

    def stub(n1, n2, name):
        (x_a, y_a), (x_b, y_b) = n1, n2
        # H then V if needed; gap stub only
        ym = 0.5 * (y_a + y_b)
        top.shapes(m1).insert(pya.DBox(
            min(x_a, x_b) - 0.20, ym - 0.20, max(x_a, x_b) + 0.20, ym + 0.20))
        top.shapes(m1).insert(pya.DBox(
            x_a - 0.20, min(y_a, ym) - 0.20, x_a + 0.20, max(y_a, ym) + 0.20))
        top.shapes(m1).insert(pya.DBox(
            x_b - 0.20, min(y_b, ym) - 0.20, x_b + 0.20, max(y_b, ym) + 0.20))

    for net in ("a", "y", "vcv", "gnd"):
        stub(pL[net], pR[net], net)

    bb = top.bbox().to_dtype(ly.dbu)
    # re-export face pins from left child hints
    faces = {"a": "W", "y": "E", "vcv": "N", "gnd": "S"}
    for net, face in faces.items():
        x, y = pL[net]
        if face == "E":
            x, y = pR[net]
        PF.connect_and_pin_on_face(
            top, m1, m1pin, m1txt, net, face, x, y, bb=bb)

    bb = top.bbox().to_dtype(ly.dbu)
    area = (bb.right - bb.left) * (bb.top - bb.bottom) * 1e-6
    print(f"{CELL} bbox {bb}; area {area:.5f} mm² [GDS]", flush=True)

    gds = os.path.join(OUT, f"{CELL}.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)
    # Like sch: two parallel 4.5/9 (combine_devices → 9/18) [SCH]
    open(os.path.join(OUT, f"{CELL}.spice"), "w").write(
        f"* P2.7.4b {CELL} = 2× {CHILD} parallel [SCH]\n"
        f".subckt {CELL} a y vcv gnd\n"
        f"Mxp y a vcv vcv sg13_lv_pmos w=9u l=0.13u m=2\n"
        f"Mxn y a gnd gnd sg13_lv_nmos w=4.5u l=0.13u m=2\n"
        ".ends\n"
    )
    open(os.path.join(OUT, f"summary_build_{CELL}.txt"), "w").write(
        f"2× {CHILD} gap={GAP}; area={area:.5f} mm² [GDS]\n")
    print(f"wrote {gds}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
