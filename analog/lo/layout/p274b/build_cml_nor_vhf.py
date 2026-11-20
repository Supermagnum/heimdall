#!/usr/bin/env python3
"""P2.7.4b — assemble cml_nor_vhf from proven core + tail + rppd loads [SCH].

Sub-cells: cml_nor_core_vhf, cml_tail_nor_vhf. Two rppd placed in parent
(same method as cml_pair_loads). Gap stubs only; no metal through children.
Pins: orp/orn/vdd/q*/vref=N (orp/orn at distinct X — never share an E-face
H that crosses the other net’s lane); nb_lo=E; gnd=W.
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
GAP_NS = 3.0
CELL = "cml_nor_vhf"
R_W, R_L, R_OHM = "2.0u", "13.334u", "1666.7"


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


def map_pins(pins0, x, y):
    return {n: (x + px, y + py) for n, (px, py) in pins0.items()}


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
    vs12 = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("via_stack").id(),
        {"b_layer": "Metal1", "t_layer": "Metal2",
         "vn_columns": 1, "vn_rows": 1})

    cr_cid = load_cell(ly, "cml_nor_core_vhf.gds", "cml_nor_core_vhf")
    tl_cid = load_cell(ly, "cml_tail_nor_vhf.gds", "cml_tail_nor_vhf")
    rh = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("rppd").id(),
        {"R": R_OHM, "w": R_W, "l": R_L, "b": 0,
         "Calculate": "R", "guardRingType": "none"})
    rloc = ly.cell(rh).bbox().to_dtype(ly.dbu)

    def strip_all_pin_texts(cid):
        cell = ly.cell(cid)
        for sh in list(cell.shapes(m1txt).each()):
            if sh.is_text():
                sh.delete()
        for i in cell.each_inst():
            strip_all_pin_texts(i.cell_index)

    cr0 = parse_pins(ly, cr_cid, m1txt)
    tl0 = parse_pins(ly, tl_cid, m1txt)
    print("core", cr0, flush=True)
    print("tail", tl0, flush=True)
    for cid in (cr_cid, tl_cid):
        strip_all_pin_texts(cid)

    cbb0 = ly.cell(cr_cid).bbox().to_dtype(ly.dbu)
    tbb0 = ly.cell(tl_cid).bbox().to_dtype(ly.dbu)

    top = ly.create_cell(CELL)

    def box(x0, y0, x1, y1):
        top.shapes(m1).insert(pya.DBox(
            min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def box2(x0, y0, x1, y1):
        top.shapes(m2).insert(pya.DBox(
            min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def via(x, y):
        top.insert(pya.CellInstArray(
            vs12, pya.Trans(pya.Trans.R0, um(x - 0.05), um(y))))

    def place_cid(cid, x, y):
        tr = pya.Trans(pya.Trans.R0, um(x), um(y))
        top.insert(pya.CellInstArray(cid, tr))
        return ly.cell(cid).bbox().transformed(tr).to_dtype(ly.dbu), tr

    # Core at origin
    x_cr, y_cr = 0.0, 0.0
    cbb, _ = place_cid(cr_cid, x_cr, y_cr)
    cr = map_pins(cr0, x_cr, y_cr)

    # Tail south of core
    gap_tl = GAP_NS + max(0.0, cr["s"][1] - cbb.bottom) + max(
        0.0, tbb0.top - tl0["drain"][1])
    x_tl = cr["s"][0] - tl0["drain"][0]
    y_tl = cbb.bottom - gap_tl - tbb0.top
    tbb, _ = place_cid(tl_cid, x_tl, y_tl)
    tl = map_pins(tl0, x_tl, y_tl)
    assert cbb.bottom >= tbb.top - 0.01, (cbb.bottom, tbb.top)

    # Resistors north of core — mid-X aligned to drain pin X (short stubs)
    # rppd M1 contacts: local y≈−0.43…−0.13 (bot), 13.46…13.76 (top) [PDK]
    y_r = cbb.top + 5.0 - rloc.bottom
    x_rp = cr["d_orp"][0] - 0.5 * (rloc.left + rloc.right)
    x_rn = cr["d_orn"][0] - 0.5 * (rloc.left + rloc.right)
    # If drains share X (both E-face), offset resistors EW so H stubs never meet
    if abs(x_rp - x_rn) < 1.0:
        x_rp -= 8.0
        x_rn += 8.0
    bb_rp, _ = place_cid(rh, x_rp, y_r)
    bb_rn, _ = place_cid(rh, x_rn, y_r)
    print(f"Rrp {bb_rp}; Rrn {bb_rn} [SCH]", flush=True)
    print(f"gaps core-tail={cbb.bottom - tbb.top:.3f} "
          f"res-core={bb_rp.bottom - cbb.top:.3f} [GDS]", flush=True)

    # --- Connect rppd: bottom → or*; top → vdd ---
    # Core E-face drains share X — never run a tall M1 V on that X (shorts
    # orp/orn). Use separate east lanes + pin-Y-only stubs [LVS].
    cx_p = 0.5 * (bb_rp.left + bb_rp.right)
    cx_n = 0.5 * (bb_rn.left + bb_rn.right)
    y_vdd = max(bb_rp.top, bb_rn.top) + 2.0
    x_lane_p = cbb.right + 2.5
    x_lane_n = cbb.right + 5.5
    y_gap_p = cbb.top + 1.5
    y_gap_n = cbb.top + 3.0

    for bb_r, cx, (xd, yd), y_gap, x_lane, label in (
            (bb_rp, cx_p, cr["d_orp"], y_gap_p, x_lane_p, "orp"),
            (bb_rn, cx_n, cr["d_orn"], y_gap_n, x_lane_n, "orn")):
        # Overlap rppd bottom M1 contact (≈ bb.bottom+0.18…+0.48)
        box(cx - 0.40, bb_r.bottom + 0.05, cx + 0.40, bb_r.bottom + 0.50)
        box(cx - 0.14, y_gap - 0.14, cx + 0.14, bb_r.bottom + 0.50)
        # H in gap to private lane
        box(min(cx, x_lane) - 0.14, y_gap - 0.14,
            max(cx, x_lane) + 0.14, y_gap + 0.14)
        # V on private lane only
        box(x_lane - 0.14, min(yd, y_gap) - 0.14,
            x_lane + 0.14, max(yd, y_gap) + 0.14)
        # Short H at pin Y into core drain pin (no tall V on xd)
        box(min(x_lane, xd) - 0.14, yd - 0.14,
            max(x_lane, xd) + 0.14, yd + 0.14)
        print(f"{label} lane={x_lane:.3f} pinY={yd:.3f}", flush=True)

    # Top of resistor → vdd bus (overlap top contact ≈ bb.top−0.48…−0.18)
    box(cx_p - 0.40, bb_rp.top - 0.50, cx_p + 0.40, bb_rp.top - 0.05)
    box(cx_n - 0.40, bb_rn.top - 0.50, cx_n + 0.40, bb_rn.top - 0.05)
    box(cx_p - 0.14, bb_rp.top - 0.40, cx_p + 0.14, y_vdd + 0.28)
    box(cx_n - 0.14, bb_rn.top - 0.40, cx_n + 0.14, y_vdd + 0.28)
    box(min(cx_p, cx_n) - 0.14, y_vdd,
        max(cx_p, cx_n) + 0.14, y_vdd + 0.28)

    # tg stub: core.s ↔ tail.drain (gap only)
    y_hi = cbb.bottom
    y_lo = tbb.top
    xs, ys = cr["s"]
    xd, yd = tl["drain"]
    x = 0.5 * (xs + xd)
    box(x - 0.20, y_lo, x + 0.20, y_hi)
    if abs(xs - x) > 0.05:
        box(min(xs, x), y_hi - 0.40, max(xs, x), y_hi)
    if abs(xd - x) > 0.05:
        box(min(xd, x), y_lo, max(xd, x), y_lo + 0.40)
    box(xs - 0.20, y_hi - 0.40, xs + 0.20, y_hi)
    box(xd - 0.20, y_lo, xd + 0.20, y_lo + 0.40)

    # gnd west rail
    x_west = min(cbb.left, tbb.left, bb_rp.left, bb_rn.left) - 3.0
    for bb, (xg, yg) in ((cbb, cr["gnd"]), (tbb, tl["gnd"])):
        box(x_west - 0.20, yg - 0.20, bb.left, yg + 0.20)
    ys_g = [cr["gnd"][1], tl["gnd"][1]]
    box(x_west - 0.20, min(ys_g), x_west + 0.20, max(ys_g))

    # orp/orn → east landing on M2 (crosses other net’s M1 lane safely)
    x_e_land = max(x_lane_n, tbb.right, bb_rn.right) + 4.0
    for x_lane, yd in (
            (x_lane_p, cr["d_orp"][1]),
            (x_lane_n, cr["d_orn"][1])):
        via(x_lane, yd)
        box2(x_lane - 0.20, yd - 0.15, x_e_land + 0.20, yd + 0.40)
        via(x_e_land, yd)
        box(x_e_land - 0.25, yd - 0.5, x_e_land + 0.25, yd + 0.40)

    # nb_lo stub east to same landing X band
    box(tl["nb_lo"][0] - 0.20, tl["nb_lo"][1] - 0.20,
        x_e_land + 0.25, tl["nb_lo"][1] + 0.20)

    # Final bbox, then all face pins (no further geometry that grows bb)
    bb = top.bbox().to_dtype(ly.dbu)
    y_gnd_pin = 0.5 * (min(ys_g) + max(ys_g))
    for name, (x, y), face in (
            ("q1p", cr["g_q1p"], "N"),
            ("q2p", cr["g_q2p"], "N"),
            ("vref", cr["g_vref"], "N"),
            ("vdd", (0.5 * (cx_p + cx_n), y_vdd), "N"),
            ("orp", (x_e_land, cr["d_orp"][1]), "E"),
            ("orn", (x_e_land, cr["d_orn"][1]), "E"),
            ("nb_lo", (x_e_land, tl["nb_lo"][1]), "E"),
            ("gnd", (x_west + 0.5, y_gnd_pin), "W"),
    ):
        PF.connect_and_pin_on_face(top, m1, m1pin, m1txt, name, face, x, y, bb)

    fp = PF.parse_pins(top, m1txt)
    bb = top.bbox().to_dtype(ly.dbu)
    area = (bb.right - bb.left) * (bb.top - bb.bottom) * 1e-6
    print(f"bbox {bb}; area {area:.5f} mm² [GDS]", flush=True)
    print(f"face pins {fp}", flush=True)
    PF.assert_pins_on_faces(top, fp, {
        "q1p": "N", "q2p": "N", "vref": "N", "vdd": "N",
        "orp": "E", "orn": "E", "nb_lo": "E", "gnd": "W",
    }, tol=0.15)

    gds = os.path.join(OUT, f"{CELL}.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)
    open(os.path.join(OUT, f"{CELL}.spice"), "w").write(
        f"* P2.7.4b {CELL} flat LVS [SCH]\n"
        f".subckt {CELL} q1p q2p vref orp orn nb_lo vdd gnd\n"
        f"Mmga orn q1p tg gnd sg13_lv_nmos w=3.00u l=0.13u\n"
        f"Mmgb orn q2p tg gnd sg13_lv_nmos w=3.00u l=0.13u\n"
        f"Mmgr orp vref tg gnd sg13_lv_nmos w=3.00u l=0.13u\n"
        f"Mmtg tg nb_lo gnd gnd sg13_lv_nmos w=6u l=0.13u\n"
        f"Rrp vdd orp gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        f"Rrn vdd orn gnd rppd w={R_W} l={R_L} ps=0u b=0 m=1\n"
        f"Mdum gnd gnd gnd gnd sg13_lv_nmos w=3.6u l=0.13u\n"
        ".ends\n"
    )
    open(os.path.join(OUT, f"summary_build_{CELL}.txt"), "w").write(
        f"area_mm2={area:.5f}\npins={fp}\n"
        f"gaps core-tail={cbb.bottom - tbb.top:.3f}\n"
    )
    print(f"wrote {gds}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
