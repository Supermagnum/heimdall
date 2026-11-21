#!/usr/bin/env python3
"""P2.7.4b — assemble cml_conv with VCO island layer rules [SCH].

Parent routing (spec/p27-layout-notes.md — cml_conv parent plan):
  M1  — face stubs / via landings only (≤ M1_STUB_MAX); no parent straps
  M2  — signal horizontal only
  M3  — signal vertical only
  M4  — supply rails (vcv north, gnd south) — supplies on their own layer
  M5/TM1 — series cmim; TM1 w≥1.70 / space≥1.64 [DS]

Stages (--stage): power | ac_p | ac_n | xc | taper | full
LVS after each; stop at first gnd|vcv (or other) merge.
"""
from __future__ import annotations

import argparse
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
from assembly_guard import ParentChildGuard, M1_STUB_MAX  # noqa: E402

DBU = 0.001
CELL = "cml_conv"
# PCell request; extract reports 5.71 / 17.58 — spice uses extract [LVS]
CMIM_SIDE = 5.774
CMIM_LVS = 5.71
RHIGH_L_LVS = 17.58
GAP = 8.0  # room for supply riser + signal M3 in inter-column gaps
TM1_W = 2.00
TM1_SPACE = 1.70
MW = 0.40          # M2/M3/M4 wire half→ full width
HW = 0.5 * MW
M1_PAD = 0.50      # via landing on M1 (≤ M1_STUB_MAX)


def um(x):
    return int(round(float(x) / DBU))


STAGES = ("power", "ac_p", "ac_n", "xc", "taper", "full")


def stage_ge(have, need):
    return STAGES.index(have) >= STAGES.index(need)


def load_cell(ly, gds_name, cell_name, as_name=None):
    path = os.path.join(OUT, gds_name)
    if not os.path.isfile(path) and os.path.isfile(path + ".gz"):
        with gzip.open(path + ".gz", "rb") as z, open(path, "wb") as f:
            shutil.copyfileobj(z, f)
    src = pya.Layout()
    src.read(path)
    src_top = None
    for c in src.each_cell():
        if c.name == cell_name:
            src_top = c
            break
    if src_top is None:
        src_top = src.top_cell()
    name = as_name or cell_name
    cid = ly.add_cell(name)
    ly.cell(cid).copy_tree(src_top)
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


def ensure_gds(names):
    for gn in names:
        gds = os.path.join(OUT, f"{gn}.gds")
        if not os.path.isfile(gds) and os.path.isfile(gds + ".gz"):
            with gzip.open(gds + ".gz", "rb") as z, open(gds, "wb") as f:
                shutil.copyfileobj(z, f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="full", choices=STAGES)
    args = ap.parse_args()
    stage = args.stage
    print(f"=== cml_conv build stage={stage} ===", flush=True)

    ly = pya.Layout()
    ly.dbu = DBU
    ly.technology_name = "sg13g2"
    lib = pya.Library.library_by_name("SG13_dev", "sg13g2")
    lib_ly = lib.layout()

    m1 = ly.layer(8, 0)
    m1pin = ly.layer(8, 2)
    m1txt = ly.layer(8, 25)
    m2 = ly.layer(10, 0)
    m3 = ly.layer(30, 0)
    m4 = ly.layer(50, 0)
    m5 = ly.layer(67, 0)
    tm1 = ly.layer(126, 0)

    def pcell(name, params):
        return ly.add_pcell_variant(
            lib, lib_ly.pcell_declaration(name).id(), params)

    vs12 = pcell("via_stack", {
        "b_layer": "Metal1", "t_layer": "Metal2",
        "vn_columns": 1, "vn_rows": 1})
    vs23 = pcell("via_stack", {
        "b_layer": "Metal2", "t_layer": "Metal3",
        "vn_columns": 1, "vn_rows": 1})
    vs34 = pcell("via_stack", {
        "b_layer": "Metal3", "t_layer": "Metal4",
        "vn_columns": 1, "vn_rows": 1})
    vs15 = pcell("via_stack", {
        "b_layer": "Metal1", "t_layer": "Metal5",
        "vn_columns": 2, "vn_rows": 2})
    vs1t = pcell("via_stack", {
        "b_layer": "Metal1", "t_layer": "TopMetal1",
        "vn_columns": 2, "vn_rows": 2})
    mim = pcell("cmim", {
        "w": f"{CMIM_SIDE:.3f}u", "l": f"{CMIM_SIDE:.3f}u",
        "C": "50f", "Calculate": "w&l", "guardRingType": "none"})
    rhi = pcell("rhigh", {
        "R": "50e3", "w": "0.5u", "b": "0",
        "Calculate": "l", "guardRingType": "none"})

    ensure_gds(["lo_inv_2_4", "lo_inv_05_1", "lo_inv_3_6", "lo_inv_9_18"])

    invs = {}
    for key, gds, cname in (
            ("p", "lo_inv_2_4.gds", "lo_inv_2_4"),
            ("n", "lo_inv_2_4.gds", "lo_inv_2_4"),
            ("b", "lo_inv_2_4.gds", "lo_inv_2_4"),
            ("xc_a", "lo_inv_05_1.gds", "lo_inv_05_1"),
            ("xc_b", "lo_inv_05_1.gds", "lo_inv_05_1"),
            ("t3", "lo_inv_3_6.gds", "lo_inv_3_6"),
            ("t9", "lo_inv_9_18.gds", "lo_inv_9_18"),
    ):
        cid = load_cell(ly, gds, cname, as_name=f"{cname}_{key}")
        pins = parse_pins(ly, cid, m1txt)
        PF.strip_pin_texts(ly.cell(cid), m1txt)
        bb = ly.cell(cid).bbox().to_dtype(ly.dbu)
        invs[key] = {"cid": cid, "pins": pins, "bb": bb}

    top = ly.create_cell(CELL)
    guard = ParentChildGuard()

    def box(layer, x0, y0, x1, y1, tag, layer_name=""):
        b = pya.DBox(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))
        guard.add_parent_box(tag, b, allow_face=True, layer=layer_name)
        top.shapes(layer).insert(b)

    def place_inst(cid, x, y, tag, is_child=False):
        tr = pya.Trans(pya.Trans.R0, um(x), um(y))
        top.insert(pya.CellInstArray(cid, tr))
        bb = ly.cell(cid).bbox().transformed(tr).to_dtype(ly.dbu)
        if is_child:
            guard.add_child(tag, bb)
        else:
            guard.add_parent_inst(tag, bb, allow_face=False)
        return bb, tr

    def map_pins(pins0, x, y):
        return {n: (x + px, y + py) for n, (px, py) in pins0.items()}

    def via(cid, x, y, tag, allow_face=True):
        # Face vias may kiss the pin pad; allow_face=True [HAND]
        tr = pya.Trans(pya.Trans.R0, um(x), um(y))
        top.insert(pya.CellInstArray(cid, tr))
        bb = ly.cell(cid).bbox().transformed(tr).to_dtype(ly.dbu)
        guard.add_parent_inst(tag, bb, allow_face=allow_face)

    def m1_pad(x, y, tag):
        h = 0.5 * M1_PAD
        box(m1, x - h, y - h, x + h, y + h, tag, "M1")

    def lift_to_m2(x, y, tag):
        """Short M1 pad + via12 at (x,y) — pin or device contact up to M2."""
        m1_pad(x, y, f"{tag}_m1")
        via(vs12, x, y, f"{tag}_v12", allow_face=True)
        box(m2, x - HW, y - HW, x + HW, y + HW, f"{tag}_m2p", "M2")

    def drop_m2_to_m1(x, y, tag):
        lift_to_m2(x, y, tag)  # same stack

    def m2_h(x0, y, x1, tag):
        box(m2, x0, y - HW, x1, y + HW, tag, "M2")

    def m3_v(x, y0, y1, tag):
        box(m3, x - HW, y0, x + HW, y1, tag, "M3")

    def m4_h(x0, y, x1, tag):
        box(m4, x0, y - HW, x1, y + HW, tag, "M4")

    def m2_to_m3(x, y, tag):
        via(vs23, x, y, f"{tag}_v23")
        box(m3, x - HW, y - HW, x + HW, y + HW, f"{tag}_m3p", "M3")

    def signal_ew(pin_a, bb_a, pin_b, bb_b, tag):
        """Gap stub E–W on M2; M1 pads + via12 at each face (outside/at face)."""
        ya, yb = pin_a[1], pin_b[1]
        x_lo, x_hi = bb_a.right, bb_b.left
        assert x_hi >= x_lo + 0.5, (tag, x_lo, x_hi)
        # Lift at faces (pin coords are on face)
        lift_to_m2(pin_a[0], ya, f"{tag}_a")
        lift_to_m2(pin_b[0], yb, f"{tag}_b")
        if abs(ya - yb) < 0.05:
            m2_h(pin_a[0], ya, pin_b[0], f"{tag}_h")
        else:
            x_mid = 0.5 * (x_lo + x_hi)
            m2_h(pin_a[0], ya, x_mid, f"{tag}_h1")
            m2_to_m3(x_mid, ya, f"{tag}_up")
            m3_v(x_mid, ya, yb, f"{tag}_v")
            m2_to_m3(x_mid, yb, f"{tag}_dn")
            m2_h(x_mid, yb, pin_b[0], f"{tag}_h2")
        print(f"  {tag} M2 gap-EW L={x_hi - x_lo:.3f}", flush=True)

    def biggest(boxes):
        return max(boxes, key=lambda b: (b.right - b.left) * (b.top - b.bottom))

    def lyr_boxes(cid, trans, layer):
        out = []
        for s in ly.cell(cid).shapes(layer).each():
            if s.is_box():
                out.append(s.bbox().transformed(trans).to_dtype(ly.dbu))
        return out

    # ---- Place children (always all invs for stable floorplan) ----
    # West strip x≤8 reserved for supply M3 spines; cmim/rhigh in 10…28; invs at ≥30
    y_p, y_n, y_b = 22.0, -28.0, 0.0
    x_inv = 40.0

    inv_p_bb, _ = place_inst(
        invs["p"]["cid"], x_inv - invs["p"]["bb"].left, y_p, "inv_p", True)
    ip = map_pins(invs["p"]["pins"], x_inv - invs["p"]["bb"].left, y_p)
    inv_n_bb, _ = place_inst(
        invs["n"]["cid"], x_inv - invs["n"]["bb"].left, y_n, "inv_n", True)
    inn = map_pins(invs["n"]["pins"], x_inv - invs["n"]["bb"].left, y_n)

    x_xc = max(inv_p_bb.right, inv_n_bb.right) + GAP
    oy_a = ip["y"][1] - invs["xc_a"]["pins"]["a"][1]
    oy_b = inn["y"][1] - invs["xc_b"]["pins"]["a"][1]
    xca_bb, _ = place_inst(
        invs["xc_a"]["cid"], x_xc - invs["xc_a"]["bb"].left, oy_a, "xc_a", True)
    xca = map_pins(invs["xc_a"]["pins"], x_xc - invs["xc_a"]["bb"].left, oy_a)
    xcb_bb, _ = place_inst(
        invs["xc_b"]["cid"], x_xc - invs["xc_b"]["bb"].left, oy_b, "xc_b", True)
    xcb = map_pins(invs["xc_b"]["pins"], x_xc - invs["xc_b"]["bb"].left, oy_b)

    x_inv_b = max(xca_bb.right, xcb_bb.right) + GAP + 20.0
    inv_b_bb, _ = place_inst(
        invs["b"]["cid"], x_inv_b - invs["b"]["bb"].left, y_b, "inv_b", True)
    ib = map_pins(invs["b"]["pins"], x_inv_b - invs["b"]["bb"].left, y_b)

    x_t3 = inv_b_bb.right + GAP
    oy_t3 = ib["y"][1] - invs["t3"]["pins"]["a"][1]
    t3_bb, _ = place_inst(
        invs["t3"]["cid"], x_t3 - invs["t3"]["bb"].left, oy_t3, "inv_t3", True)
    t3 = map_pins(invs["t3"]["pins"], x_t3 - invs["t3"]["bb"].left, oy_t3)

    x_t9 = t3_bb.right + GAP
    oy_t9 = t3["y"][1] - invs["t9"]["pins"]["a"][1]
    t9_bb, _ = place_inst(
        invs["t9"]["cid"], x_t9 - invs["t9"]["bb"].left, oy_t9, "inv_t9", True)
    t9 = map_pins(invs["t9"]["pins"], x_t9 - invs["t9"]["bb"].left, oy_t9)

    child_bbs = [inv_p_bb, inv_n_bb, xca_bb, xcb_bb, inv_b_bb, t3_bb, t9_bb]
    vcv_pts = [ip["vcv"], inn["vcv"], ib["vcv"], xca["vcv"], xcb["vcv"],
               t3["vcv"], t9["vcv"]]
    gnd_pts = [ip["gnd"], inn["gnd"], ib["gnd"], xca["gnd"], xcb["gnd"],
               t3["gnd"], t9["gnd"]]
    bbs_for = [inv_p_bb, inv_n_bb, inv_b_bb, xca_bb, xcb_bb, t3_bb, t9_bb]

    # ---- (a) POWER: M4 rails + via14 at face pins [VCO rule] ----
    # Supply M2 tracks must sit outside AC pocket corridors (±1.5 from child faces)
    y_over = max(b.top for b in child_bbs) + 4.0
    y_under = min(b.bottom for b in child_bbs) - 4.0
    y_vcv = max(b.top for b in child_bbs) + 7.0
    y_gnd = min(b.bottom for b in child_bbs) - 7.0
    xs_all = [p[0] for p in vcv_pts + gnd_pts]
    x_lo_r = min(xs_all) - 2.0
    x_hi_r = max(xs_all) + 2.0

    print("power: M4 H rails + M3 columns outside children", flush=True)
    from collections import defaultdict
    from assembly_guard import penetration_depth

    assert y_vcv >= y_over + 2.0 and y_gnd <= y_under - 2.0, (
        y_vcv, y_over, y_gnd, y_under)
    # Supply spines in reserved west strip (x≤8); local risers just west of each inv
    by_left = defaultdict(list)
    for i, bb in enumerate(bbs_for):
        by_left[round(bb.left, 1)].append(i)
    x_side_of = {}
    for _left, idxs in by_left.items():
        for k, i in enumerate(idxs):
            # Stay east of spine strip (spines at ≤8); west of this child
            x_side_of[id(bbs_for[i])] = max(
                10.0, bbs_for[i].left - 1.0 - 2.0 * k)
    x_vcv_col = 4.0
    x_gnd_col = 2.0
    x_lo_r = min(x_lo_r, 0.0)
    m4_h(x_lo_r, y_vcv, x_hi_r, "vcv_m4")
    m4_h(x_lo_r, y_gnd, x_hi_r, "gnd_m4")

    def supply_drop(x, bb, y_rail, face, x_col, tag):
        """Face → M2 to local riser → M3 up/down to y_over/y_under → M2 to spine → M4.

        Tall M3 lives only at x_side (per child). AC signal M3 must not share that X.
        """
        if face == "N":
            y_via = bb.top + 0.35
            y_track = y_over
            box(m1, x - HW, bb.top, x + HW, y_via + 0.25, f"{tag}_m1", "M1")
        else:
            y_via = bb.bottom - 0.35
            y_track = y_under
            box(m1, x - HW, y_via - 0.25, x + HW, bb.bottom, f"{tag}_m1", "M1")
        m1_pad(x, y_via, f"{tag}_pad")
        via(vs12, x, y_via, f"{tag}_v12")
        box(m2, x - HW, y_via - HW, x + HW, y_via + HW, f"{tag}_m2", "M2")
        x_side = x_side_of[id(bb)]
        m2_h(min(x, x_side), y_via, max(x, x_side), f"{tag}_m2side")
        via(vs23, x_side, y_via, f"{tag}_v23a")
        m3_v(x_side, y_via, y_track, f"{tag}_m3loc")
        via(vs23, x_side, y_track, f"{tag}_v23b")
        box(m2, x_side - HW, y_track - HW, x_side + HW, y_track + HW,
            f"{tag}_m2t", "M2")
        m2_h(min(x_side, x_col), y_track, max(x_side, x_col), f"{tag}_m2h")
        via(vs23, x_col, y_track, f"{tag}_v23c")
        m3_v(x_col, y_track, y_rail, f"{tag}_m3")
        via(vs34, x_col, y_rail, f"{tag}_v34")
        box(m4, x_col - HW, y_rail - HW, x_col + HW, y_rail + HW,
            f"{tag}_m4p", "M4")

    for (x, y), bb in zip(vcv_pts, bbs_for):
        supply_drop(x, bb, y_vcv, "N", x_vcv_col, "vcv")
    for (x, y), bb in zip(gnd_pts, bbs_for):
        supply_drop(x, bb, y_gnd, "S", x_gnd_col, "gnd")

    def place_series_cmim(x, y, tag):
        bb, tr = place_inst(mim, x, y, tag, is_child=False)
        m5p = biggest(lyr_boxes(mim, tr, m5))
        tmp = biggest(lyr_boxes(mim, tr, tm1))
        tw = TM1_W
        # M5 → M1 pad south → lift to M2
        mx = 0.5 * (m5p.left + m5p.right)
        y_via = m5p.bottom - 1.8
        via(vs15, mx - 0.35, y_via - 0.15, f"{tag}_vs15")
        box(m5, mx - 0.50, y_via, mx + 0.50, m5p.bottom + 0.3, f"{tag}_m5", "M5")
        m1_pad(mx, y_via, f"{tag}_m1m")
        lift_to_m2(mx, y_via, f"{tag}_m5up")
        m5_xy = (mx, y_via)
        # TM1 legal stub east → via → M1 → M2
        tx = 0.5 * (tmp.left + tmp.right)
        y_bus = tmp.top + TM1_SPACE
        y_via_t = y_bus + tw + 1.2
        x_jog = tmp.right + TM1_SPACE + 0.5 * tw
        box(tm1, tx - 0.5 * tw, tmp.top - 0.5, tx + 0.5 * tw, y_bus + tw,
            f"{tag}_tm1v", "TM1")
        box(tm1, min(tx, x_jog) - 0.5 * tw, y_bus,
            max(tx, x_jog) + 0.5 * tw, y_bus + tw, f"{tag}_tm1h", "TM1")
        box(tm1, x_jog - 0.5 * tw, y_bus, x_jog + 0.5 * tw, y_via_t,
            f"{tag}_tm1vj", "TM1")
        box(tm1, x_jog - 0.5 * tw, y_via_t - 0.5 * tw,
            x_jog + 0.5 * tw, y_via_t + 0.5 * tw, f"{tag}_tm1p", "TM1")
        via(vs1t, x_jog - 0.35, y_via_t - 0.3, f"{tag}_vs1t")
        m1_pad(x_jog, y_via_t, f"{tag}_m1t")
        lift_to_m2(x_jog, y_via_t, f"{tag}_tmup")
        return bb, m5_xy, (x_jog, y_via_t)

    def place_rhigh(x, y, tag):
        bb, tr = place_inst(rhi, x, y, tag, is_child=False)
        m1s = [s.bbox().transformed(tr).to_dtype(ly.dbu)
               for s in ly.cell(rhi).shapes(m1).each() if s.is_box()]
        bot = min(m1s, key=lambda b: b.bottom)
        top_t = max(m1s, key=lambda b: b.top)
        rbot = (0.5 * (bot.left + bot.right), 0.5 * (bot.bottom + bot.top))
        rtop = (0.5 * (top_t.left + top_t.right),
                0.5 * (top_t.bottom + top_t.top))
        lift_to_m2(rbot[0], rbot[1], f"{tag}_bot")
        lift_to_m2(rtop[0], rtop[1], f"{tag}_top")
        return bb, rbot, rtop

    def wire_ac_pocket(inv_bb, inv_pins, y_cm, tag, rtop_side="S"):
        """cmim|rhigh west of inv; signal on M2/M3 only."""
        rh_x = inv_bb.left - GAP - 0.7
        rh_bb, rbot, rtop = place_rhigh(rh_x, y_cm - 2.0, f"rh_{tag}")
        cm_x = rh_bb.left - GAP - 7.0
        cm_bb, m5_xy, tm_xy = place_series_cmim(cm_x, y_cm, f"cmim_{tag}")
        # TM1 mid (M2) → rbot (M2): jog if Y differs (rhigh bot ≠ TM1 via Y)
        xa, ya = inv_pins["a"]
        x_sup = x_side_of[id(inv_bb)]
        x_j = rh_bb.left - 1.5
        if abs(x_j - x_sup) < 1.5:
            x_j = min(x_sup, rh_bb.left) - 1.5
        assert abs(x_j - x_sup) >= 1.5, (tag, x_j, x_sup)
        if abs(tm_xy[1] - rbot[1]) < 0.05:
            m2_h(min(tm_xy[0], rbot[0]), tm_xy[1],
                 max(tm_xy[0], rbot[0]), f"{tag}_tm_r")
        else:
            m2_h(min(tm_xy[0], x_j), tm_xy[1], max(tm_xy[0], x_j),
                 f"{tag}_tm_rh")
            m2_to_m3(x_j, tm_xy[1], f"{tag}_tm_r_up")
            m3_v(x_j, tm_xy[1], rbot[1], f"{tag}_tm_r_v")
            m2_to_m3(x_j, rbot[1], f"{tag}_tm_r_dn")
            m2_h(min(x_j, rbot[0]), rbot[1], max(x_j, rbot[0]),
                 f"{tag}_tm_r_bot")
        # same node → inv.a (M2/M3); M3 X must miss supply risers
        if abs(rbot[1] - ya) < 0.05:
            m2_h(min(rbot[0], xa), ya, max(rbot[0], xa), f"{tag}_tm_a")
        else:
            m2_h(min(rbot[0], x_j), rbot[1], max(rbot[0], x_j),
                 f"{tag}_tm_a0")
            m2_to_m3(x_j, rbot[1], f"{tag}_tm_up")
            m3_v(x_j, rbot[1], ya, f"{tag}_tm_v")
            m2_to_m3(x_j, ya, f"{tag}_tm_dn")
            m2_h(x_j, ya, xa, f"{tag}_tm_a1")
        lift_to_m2(xa, ya, f"{tag}_a")
        # rtop → inv.y on corridor side (M2/M3); keep clear of supply y_over/y_under
        xy, yy = inv_pins["y"]
        y_out = (inv_bb.top + 1.5) if rtop_side == "N" else (inv_bb.bottom - 1.5)
        assert abs(y_out - y_over) >= 1.5 and abs(y_out - y_under) >= 1.5, (
            f"{tag} AC corridor y_out={y_out} collides supply "
            f"y_over={y_over} y_under={y_under}")
        x_east = inv_bb.right + 1.5
        m2_to_m3(rtop[0], rtop[1], f"{tag}_rt_up")
        m3_v(rtop[0], rtop[1], y_out, f"{tag}_rt_v")
        m2_to_m3(rtop[0], y_out, f"{tag}_rt_dn")
        m2_h(rtop[0], y_out, x_east, f"{tag}_rt_h")
        m2_to_m3(x_east, y_out, f"{tag}_rt_up2")
        m3_v(x_east, y_out, yy, f"{tag}_rt_v2")
        m2_to_m3(x_east, yy, f"{tag}_rt_dn2")
        m2_h(x_east, yy, xy, f"{tag}_rt_y")
        lift_to_m2(xy, yy, f"{tag}_y")
        return cm_bb, m5_xy, tm_xy, rh_bb

    m5_p = m5_n = m5_b = None
    tm_p = tm_n = tm_b = None

    if stage_ge(stage, "ac_p"):
        print("AC-p pocket", flush=True)
        cm_p, m5_p, tm_p, rh_p = wire_ac_pocket(
            inv_p_bb, ip, y_p + 2.0, "p", rtop_side="S")

    if stage_ge(stage, "ac_n"):
        print("AC-n pocket", flush=True)
        cm_n, m5_n, tm_n, rh_n = wire_ac_pocket(
            inv_n_bb, inn, y_n + 2.0, "n", rtop_side="S")

    if stage_ge(stage, "xc"):
        print("XC gap stubs + cross (M2/M3)", flush=True)
        signal_ew(ip["y"], inv_p_bb, xca["a"], xca_bb, "x_o2p_to_xca")
        signal_ew(inn["y"], inv_n_bb, xcb["a"], xcb_bb, "x_o2n_to_xcb")
        # Cross on separate M2 Y / M3 X corridors
        y_lo = max(inv_n_bb.top, xcb_bb.top) + 1.5
        y_hi = min(inv_p_bb.bottom, xca_bb.bottom) - 1.5
        assert y_hi >= y_lo + 1.0, (y_lo, y_hi)
        x_e_a = max(xca_bb.right, xcb_bb.right) + 2.0
        x_e_b = x_e_a + 2.0
        # Stay east of inv, west of xc supply risers (x_side ≈ xc.left-1/-3)
        x_c_a = inv_n_bb.right + 1.5
        x_c_b = inv_p_bb.right + 3.0
        _sup = {x_side_of[id(b)] for b in (
            inv_p_bb, inv_n_bb, xca_bb, xcb_bb, inv_b_bb)}
        for _xc in (x_c_a, x_c_b, x_e_a, x_e_b):
            assert all(abs(_xc - s) >= 1.5 for s in _sup), (_xc, _sup)

        def cross_m2m3(pin_xc, bb_xc, pin_inv, bb_inv, y_g, x_e, x_c, tag):
            lift_to_m2(pin_xc[0], pin_xc[1], f"{tag}_xc")
            lift_to_m2(pin_inv[0], pin_inv[1], f"{tag}_inv")
            m2_h(pin_xc[0], pin_xc[1], x_e, f"{tag}_out")
            m2_to_m3(x_e, pin_xc[1], f"{tag}_eup")
            m3_v(x_e, pin_xc[1], y_g, f"{tag}_ev")
            m2_to_m3(x_e, y_g, f"{tag}_edn")
            m2_h(x_c, y_g, x_e, f"{tag}_inh")
            m2_to_m3(x_c, y_g, f"{tag}_cup")
            m3_v(x_c, y_g, pin_inv[1], f"{tag}_cv")
            m2_to_m3(x_c, pin_inv[1], f"{tag}_cdn")
            m2_h(bb_inv.right, pin_inv[1], x_c, f"{tag}_to")
            # also connect from xc E face
            m2_h(bb_xc.right, pin_xc[1], x_e, f"{tag}_out2")
            print(f"  {tag} cross y={y_g:.3f} x_e={x_e:.3f}", flush=True)

        cross_m2m3(xca["y"], xca_bb, inn["y"], inv_n_bb, y_lo, x_e_a, x_c_a,
                   "xca_y_to_o2n")
        cross_m2m3(xcb["y"], xcb_bb, ip["y"], inv_p_bb, y_hi, x_e_b, x_c_b,
                   "xcb_y_to_o2p")

    if stage_ge(stage, "taper"):
        print("AC-b + taper", flush=True)
        cm_b, m5_b, tm_b, rh_b = wire_ac_pocket(
            inv_b_bb, ib, y_b + 2.0, "b", rtop_side="S")
        # feed x_o2p → cmim_b.M5 on M2 above children, below vcv M4
        y_feed = max(inv_p_bb.top, xca_bb.top, inv_b_bb.top) + 1.5
        assert y_vcv >= y_feed + 2.0, (y_vcv, y_feed)
        lift_to_m2(ip["y"][0], ip["y"][1], "feed_y")
        x_f = inv_p_bb.right + 1.2
        m2_h(ip["y"][0], ip["y"][1], x_f, "feed_h0")
        m2_to_m3(x_f, ip["y"][1], "feed_up0")
        m3_v(x_f, ip["y"][1], y_feed, "feed_v")
        m2_to_m3(x_f, y_feed, "feed_dn0")
        m2_h(x_f, y_feed, m5_b[0], "feed_h")
        m2_to_m3(m5_b[0], y_feed, "feed_up1")
        m3_v(m5_b[0], y_feed, m5_b[1], "feed_dn")
        m2_to_m3(m5_b[0], m5_b[1], "feed_dn1")
        # M5 node already lifted in place_series_cmim
        signal_ew(ib["y"], inv_b_bb, t3["a"], t3_bb, "cy_to_t3")
        signal_ew(t3["y"], t3_bb, t9["a"], t9_bb, "cz_to_t9")

    # ---- Top pins (rim; supplies already on M4) ----
    bb = top.bbox().to_dtype(ly.dbu)

    def pin_m1(name, x, y):
        PF.place_pin(top, m1, m1pin, m1txt, x, y, name)

    # vcv / gnd on M4 rim via short via14 already; add pin text on M1 at rim
    # after dropping via14 from rim M4… use M1 pin over via at rail ends
    # Top supply pins: via stack from M4 rail down to M1 pin text
    xp = 0.5 * (x_lo_r + x_hi_r)
    via(vs34, xp, y_vcv, "vcv_pin_v34")
    via(vs23, xp, y_vcv, "vcv_pin_v23")
    via(vs12, xp, y_vcv, "vcv_pin_v12")
    m1_pad(xp, y_vcv, "vcv_pin_m1")
    pin_m1("vcv", xp, y_vcv)
    via(vs34, xp, y_gnd, "gnd_pin_v34")
    via(vs23, xp, y_gnd, "gnd_pin_v23")
    via(vs12, xp, y_gnd, "gnd_pin_v12")
    m1_pad(xp, y_gnd, "gnd_pin_m1")
    pin_m1("gnd", xp, y_gnd)

    if stage_ge(stage, "ac_p") and m5_p:
        lift_to_m2(m5_p[0], m5_p[1], "dp_lift")
        # west rim on M2
        m2_h(bb.left + 0.5, m5_p[1], m5_p[0], "dp_m2")
        drop_m2_to_m1(bb.left + 0.5, m5_p[1], "dp_drop")
        pin_m1("dp", bb.left + 0.5, m5_p[1])
    if stage_ge(stage, "ac_n") and m5_n:
        lift_to_m2(m5_n[0], m5_n[1], "dn_lift")
        m2_h(bb.left + 0.5, m5_n[1], m5_n[0], "dn_m2")
        drop_m2_to_m1(bb.left + 0.5, m5_n[1], "dn_drop")
        pin_m1("dn", bb.left + 0.5, m5_n[1])
    if stage_ge(stage, "taper"):
        # east of t9 (top bbox.right still coincides with child face)
        x_y_pin = t9_bb.right + 2.0
        lift_to_m2(t9["y"][0], t9["y"][1], "y_lift")
        m2_h(t9["y"][0], t9["y"][1], x_y_pin, "y_m2")
        drop_m2_to_m1(x_y_pin, t9["y"][1], "y_drop")
        pin_m1("y", x_y_pin, t9["y"][1])

    # For early stages, export leaf a/y as pins so LVS has ports
    if not stage_ge(stage, "taper"):
        for name, (x, y) in (
                ("a_p", ip["a"]), ("y_p", ip["y"]),
                ("a_n", inn["a"]), ("y_n", inn["y"]),
                ("a_b", ib["a"]), ("y_b", ib["y"]),
                ("a_xca", xca["a"]), ("y_xca", xca["y"]),
                ("a_xcb", xcb["a"]), ("y_xcb", xcb["y"]),
                ("a_t3", t3["a"]), ("y_t3", t3["y"]),
                ("a_t9", t9["a"]), ("y_t9", t9["y"])):
            pin_m1(name, x, y)

    guard.check_top_shapes(
        top, [(m1, "M1"), (m2, "M2"), (m3, "M3"), (m4, "M4"),
              (m5, "M5"), (tm1, "TM1")], tag_prefix="scan")

    bb = top.bbox().to_dtype(ly.dbu)
    area = (bb.right - bb.left) * (bb.top - bb.bottom) * 1e-6
    print(f"cml_conv stage={stage} bbox {bb}; area {area:.5f} mm² [GDS]",
          flush=True)
    print(f"GUARD PASS: {guard.summary()}", flush=True)

    gds = os.path.join(OUT, f"{CELL}.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)

    spice = _spice_for_stage(stage)
    open(os.path.join(OUT, f"{CELL}.spice"), "w").write(spice)
    open(os.path.join(OUT, f"summary_build_{CELL}.txt"), "w").write(
        f"stage={stage}\narea_mm2={area:.5f}\n"
        f"tm1_w={TM1_W}\nm1_stub_max={M1_STUB_MAX}\n"
        f"guard={guard.summary()}\n")
    print(f"wrote {gds}", flush=True)
    return 0


def _spice_for_stage(stage):
    """Stage-matched flat spice for LVS [SCH]."""
    cm = CMIM_LVS
    rh = RHIGH_L_LVS
    invs_pwr = """
Mxp_p y_p a_p vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_p y_p a_p gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxp_n y_n a_n vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_n y_n a_n gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxp_b y_b a_b vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_b y_b a_b gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxp_xca y_xca a_xca vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxn_xca y_xca a_xca gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Mxp_xcb y_xcb a_xcb vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxn_xcb y_xcb a_xcb gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Mxp_t3 y_t3 a_t3 vcv vcv sg13_lv_pmos w=6.0u l=0.13u
Mxn_t3 y_t3 a_t3 gnd gnd sg13_lv_nmos w=3.0u l=0.13u
Mxp_t9 y_t9 a_t9 vcv vcv sg13_lv_pmos w=9.0u l=0.13u m=2
Mxn_t9 y_t9 a_t9 gnd gnd sg13_lv_nmos w=4.5u l=0.13u m=2
"""
    if stage == "power":
        ports = ("vcv gnd a_p y_p a_n y_n a_b y_b "
                 "a_xca y_xca a_xcb y_xcb a_t3 y_t3 a_t9 y_t9")
        return f"* stage power\n.subckt {CELL} {ports}\n{invs_pwr}.ends\n"

    if stage == "ac_p":
        ports = ("dp vcv gnd y_p a_n y_n a_b y_b "
                 "a_xca y_xca a_xcb y_xcb a_t3 y_t3 a_t9 y_t9")
        # a_p = x_cip, y_p = x_o2p with rhigh + cmim
        return f"""* stage ac_p
.subckt {CELL} {ports}
Cccap a_p dp cap_cmim w={cm:.3f}u l={cm:.3f}u m=1
Rrcap a_p y_p gnd rhigh w=0.5u l={rh:.2f}u b=0 m=1
Mxp_p y_p a_p vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_p y_p a_p gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxp_n y_n a_n vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_n y_n a_n gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxp_b y_b a_b vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_b y_b a_b gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxp_xca y_xca a_xca vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxn_xca y_xca a_xca gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Mxp_xcb y_xcb a_xcb vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxn_xcb y_xcb a_xcb gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Mxp_t3 y_t3 a_t3 vcv vcv sg13_lv_pmos w=6.0u l=0.13u
Mxn_t3 y_t3 a_t3 gnd gnd sg13_lv_nmos w=3.0u l=0.13u
Mxp_t9 y_t9 a_t9 vcv vcv sg13_lv_pmos w=9.0u l=0.13u m=2
Mxn_t9 y_t9 a_t9 gnd gnd sg13_lv_nmos w=4.5u l=0.13u m=2
.ends
"""

    if stage == "ac_n":
        ports = ("dp dn vcv gnd y_p y_n a_b y_b "
                 "a_xca y_xca a_xcb y_xcb a_t3 y_t3 a_t9 y_t9")
        return f"""* stage ac_n
.subckt {CELL} {ports}
Cccap a_p dp cap_cmim w={cm:.3f}u l={cm:.3f}u m=1
Rrcap a_p y_p gnd rhigh w=0.5u l={rh:.2f}u b=0 m=1
Mxp_p y_p a_p vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_p y_p a_p gnd gnd sg13_lv_nmos w=2u l=0.13u
Cccan a_n dn cap_cmim w={cm:.3f}u l={cm:.3f}u m=1
Rrcan a_n y_n gnd rhigh w=0.5u l={rh:.2f}u b=0 m=1
Mxp_n y_n a_n vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_n y_n a_n gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxp_b y_b a_b vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_b y_b a_b gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxp_xca y_xca a_xca vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxn_xca y_xca a_xca gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Mxp_xcb y_xcb a_xcb vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxn_xcb y_xcb a_xcb gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Mxp_t3 y_t3 a_t3 vcv vcv sg13_lv_pmos w=6.0u l=0.13u
Mxn_t3 y_t3 a_t3 gnd gnd sg13_lv_nmos w=3.0u l=0.13u
Mxp_t9 y_t9 a_t9 vcv vcv sg13_lv_pmos w=9.0u l=0.13u m=2
Mxn_t9 y_t9 a_t9 gnd gnd sg13_lv_nmos w=4.5u l=0.13u m=2
.ends
"""

    if stage == "xc":
        # y_p = x_o2p = a_xca = y_xcb; y_n = x_o2n = a_xcb = y_xca
        ports = ("dp dn vcv gnd y_p y_n a_b y_b a_t3 y_t3 a_t9 y_t9")
        return f"""* stage xc
.subckt {CELL} {ports}
Cccap a_p dp cap_cmim w={cm:.3f}u l={cm:.3f}u m=1
Rrcap a_p y_p gnd rhigh w=0.5u l={rh:.2f}u b=0 m=1
Mxp_p y_p a_p vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_p y_p a_p gnd gnd sg13_lv_nmos w=2u l=0.13u
Cccan a_n dn cap_cmim w={cm:.3f}u l={cm:.3f}u m=1
Rrcan a_n y_n gnd rhigh w=0.5u l={rh:.2f}u b=0 m=1
Mxp_n y_n a_n vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_n y_n a_n gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxp_xca y_n y_p vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxn_xca y_n y_p gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Mxp_xcb y_p y_n vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxn_xcb y_p y_n gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Mxp_b y_b a_b vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxn_b y_b a_b gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxp_t3 y_t3 a_t3 vcv vcv sg13_lv_pmos w=6.0u l=0.13u
Mxn_t3 y_t3 a_t3 gnd gnd sg13_lv_nmos w=3.0u l=0.13u
Mxp_t9 y_t9 a_t9 vcv vcv sg13_lv_pmos w=9.0u l=0.13u m=2
Mxn_t9 y_t9 a_t9 gnd gnd sg13_lv_nmos w=4.5u l=0.13u m=2
.ends
"""

    # taper / full — complete lo_converter
    return f"""* P2.7.4b {CELL} = lo_converter [SCH] stage={stage}
.subckt {CELL} dp dn y vcv gnd
Cccap x_cip dp cap_cmim w={cm:.3f}u l={cm:.3f}u m=1
Rrcap x_cip x_o2p gnd rhigh w=0.5u l={rh:.2f}u b=0 m=1
Mxcapp x_o2p x_cip vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxcapn x_o2p x_cip gnd gnd sg13_lv_nmos w=2u l=0.13u
Cccan x_cin dn cap_cmim w={cm:.3f}u l={cm:.3f}u m=1
Rrcan x_cin x_o2n gnd rhigh w=0.5u l={rh:.2f}u b=0 m=1
Mxcanp x_o2n x_cin vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxcann x_o2n x_cin gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxcxap x_o2n x_o2p vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxcxan x_o2n x_o2p gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Mxcxbp x_o2p x_o2n vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxcxbn x_o2p x_o2n gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Cccb x_cbi x_o2p cap_cmim w={cm:.3f}u l={cm:.3f}u m=1
Rrcb x_cbi x_cy gnd rhigh w=0.5u l={rh:.2f}u b=0 m=1
Mxcbp x_cy x_cbi vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxcbn x_cy x_cbi gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxcv3p x_cz x_cy vcv vcv sg13_lv_pmos w=6.0u l=0.13u
Mxcv3n x_cz x_cy gnd gnd sg13_lv_nmos w=3.0u l=0.13u
Mxcv4p y x_cz vcv vcv sg13_lv_pmos w=9.0u l=0.13u m=2
Mxcv4n y x_cz gnd gnd sg13_lv_nmos w=4.5u l=0.13u m=2
.ends
"""


if __name__ == "__main__":
    raise SystemExit(main())
