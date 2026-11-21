#!/usr/bin/env python3
"""P2.7.4b — assemble cml_conv (lo_converter) by pin plan [SCH].

Pin plan: out/summary_pin_plan_cml_conv.txt
Rules: gap stubs only; no parent metal through child bboxes (assembly_guard);
series cmim TM1 stubs at legal width/spacing (TM1.a ≥1.70 / TM1.b ≥1.64 [DS]);
lo_inv_9_18 = 2×45_9 (m=2 in spice).
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
from assembly_guard import ParentChildGuard  # noqa: E402

DBU = 0.001
CELL = "cml_conv"
CMIM_SIDE = 5.774  # µm = √(50/1.5) [PDK caspec]
GAP = 4.0
TM1_W = 2.00  # ≥ TM1.a 1.70 [DS]; bank_unit / hold pattern
TM1_SPACE = 1.70  # ≥ TM1.b 1.64 [DS]
M1_W = 0.40
HW = 0.5 * M1_W


def um(x):
    return int(round(float(x) / DBU))


def load_cell(ly, gds_name, cell_name, as_name=None):
    src = pya.Layout()
    path = os.path.join(OUT, gds_name)
    if not os.path.isfile(path):
        path = path + ".gz" if not path.endswith(".gz") else path
        # prefer ungzipped sibling written by leaf builders
        alt = os.path.join(OUT, gds_name)
        if os.path.isfile(alt):
            path = alt
        elif os.path.isfile(alt + ".gz"):
            import tempfile
            with gzip.open(alt + ".gz", "rb") as z, open(
                    os.path.join(OUT, gds_name), "wb") as f:
                shutil.copyfileobj(z, f)
            path = os.path.join(OUT, gds_name)
    src.read(path if os.path.isfile(path) else os.path.join(OUT, gds_name))
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


def main():
    ly = pya.Layout()
    ly.dbu = DBU
    ly.technology_name = "sg13g2"
    lib = pya.Library.library_by_name("SG13_dev", "sg13g2")
    lib_ly = lib.layout()
    m1 = ly.layer(8, 0)
    m1pin = ly.layer(8, 2)
    m1txt = ly.layer(8, 25)
    m5 = ly.layer(67, 0)
    tm1 = ly.layer(126, 0)

    vs15 = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("via_stack").id(),
        {"b_layer": "Metal1", "t_layer": "Metal5",
         "vn_columns": 2, "vn_rows": 2})
    vs1t = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("via_stack").id(),
        {"b_layer": "Metal1", "t_layer": "TopMetal1",
         "vn_columns": 2, "vn_rows": 2})
    mim = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("cmim").id(),
        {"w": f"{CMIM_SIDE:.3f}u", "l": f"{CMIM_SIDE:.3f}u",
         "C": "50f", "Calculate": "w&l", "guardRingType": "none"})
    rhi = ly.add_pcell_variant(
        lib, lib_ly.pcell_declaration("rhigh").id(),
        {"R": "50e3", "w": "0.5u", "b": "0",
         "Calculate": "l", "guardRingType": "none"})

    # Ensure ungzipped leaf GDS present
    for gn in ("lo_inv_2_4", "lo_inv_05_1", "lo_inv_3_6", "lo_inv_9_18"):
        gds = os.path.join(OUT, f"{gn}.gds")
        gz = gds + ".gz"
        if not os.path.isfile(gds) and os.path.isfile(gz):
            with gzip.open(gz, "rb") as z, open(gds, "wb") as f:
                shutil.copyfileobj(z, f)

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

    def box(layer, x0, y0, x1, y1, tag="m"):
        b = pya.DBox(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))
        guard.add_parent_box(tag, b, allow_face=True)
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

    def biggest(boxes):
        return max(boxes, key=lambda b: (b.right - b.left) * (b.top - b.bottom))

    def lyr_boxes(cid, trans, layer):
        out = []
        for s in ly.cell(cid).shapes(layer).each():
            if s.is_box():
                out.append(s.bbox().transformed(trans).to_dtype(ly.dbu))
        return out

    def place_series_cmim(x, y, tag):
        """Series cmim; return bb, m5_m1_xy, tm1_m1_xy. TM1 legal [DS]."""
        bb, tr = place_inst(mim, x, y, tag, is_child=False)
        m5p = biggest(lyr_boxes(mim, tr, m5))
        tmp = biggest(lyr_boxes(mim, tr, tm1))
        tw = TM1_W
        # M5 (MINUS) south of plate → M1 (cbf/hold: via outside plate)
        mx = 0.5 * (m5p.left + m5p.right)
        y_via = m5p.bottom - 1.8
        place_inst(vs15, mx - 0.35, y_via - 0.15, f"{tag}_vs15")
        box(m5, mx - 0.50, y_via, mx + 0.50, m5p.bottom + 0.3, f"{tag}_m5")
        box(m1, mx - 0.50, y_via - 0.50, mx + 0.50, y_via + 0.50, f"{tag}_m1m")
        m5_xy = (mx, y_via)

        # TM1 (PLUS) north of plate → jog east → via down (bank_unit pattern)
        tx = 0.5 * (tmp.left + tmp.right)
        y_bus = tmp.top + TM1_SPACE  # clear plate (TM1.b)
        y_via_t = y_bus + tw + 1.2
        x_jog = tmp.right + TM1_SPACE + 0.5 * tw
        # vertical from plate top (overlap plate edge) to bus
        box(tm1, tx - 0.5 * tw, tmp.top - 0.5, tx + 0.5 * tw, y_bus + tw,
            f"{tag}_tm1v")
        # horizontal to jog (clear of plate: x starts at plate mid, ends east)
        box(tm1, min(tx, x_jog) - 0.5 * tw, y_bus,
            max(tx, x_jog) + 0.5 * tw, y_bus + tw, f"{tag}_tm1h")
        # via landing pad on TM1
        box(tm1, x_jog - 0.5 * tw, y_via_t - 0.5 * tw,
            x_jog + 0.5 * tw, y_via_t + 0.5 * tw, f"{tag}_tm1p")
        box(tm1, x_jog - 0.5 * tw, y_bus, x_jog + 0.5 * tw, y_via_t,
            f"{tag}_tm1vj")
        place_inst(vs1t, x_jog - 0.35, y_via_t - 0.3, f"{tag}_vs1t")
        box(m1, x_jog - 0.50, y_via_t - 0.50, x_jog + 0.50, y_via_t + 0.50,
            f"{tag}_m1t")
        tm_xy = (x_jog, y_via_t)
        return bb, m5_xy, tm_xy

    def place_rhigh(x, y, tag):
        bb, tr = place_inst(rhi, x, y, tag, is_child=False)
        m1s = []
        for s in ly.cell(rhi).shapes(m1).each():
            if s.is_box():
                m1s.append(s.bbox().transformed(tr).to_dtype(ly.dbu))
        bot = min(m1s, key=lambda b: b.bottom)
        top_t = max(m1s, key=lambda b: b.top)
        return bb, (0.5 * (bot.left + bot.right), 0.5 * (bot.bottom + bot.top)), \
            (0.5 * (top_t.left + top_t.right), 0.5 * (top_t.bottom + top_t.top))

    def gap_stub_ew(pin_w, bb_w, pin_e, bb_e, tag):
        """M1 only in the gap between bb_w.right and bb_e.left [latch]."""
        x0, y0 = pin_w
        x1, y1 = pin_e
        x_lo = bb_w.right
        x_hi = bb_e.left
        assert x_hi >= x_lo + 0.5, (tag, x_lo, x_hi)
        if abs(y0 - y1) < 0.05:
            box(m1, x_lo, y0 - HW, x_hi, y0 + HW, tag)
        else:
            x_mid = 0.5 * (x_lo + x_hi)
            box(m1, x_lo, y0 - HW, x_mid + HW, y0 + HW, f"{tag}_hw")
            box(m1, x_mid - HW, min(y0, y1), x_mid + HW, max(y0, y1),
                f"{tag}_v")
            box(m1, x_mid - HW, y1 - HW, x_hi, y1 + HW, f"{tag}_he")
        print(f"  {tag} gap-EW L={x_hi - x_lo:.3f} dY={abs(y0 - y1):.3f}",
              flush=True)

    def cross_via_xc_gap(pin_xc, bb_xc, pin_inv, bb_inv, bb_xc_other, tag,
                         y_gap, x_east, x_col):
        """Join xc.E → opposite-row inv.E via dedicated corridor (no shared metal)."""
        ya = pin_xc[1]
        yb = pin_inv[1]
        assert bb_xc.left >= bb_inv.right + 0.5, (tag, bb_inv, bb_xc)
        box(m1, bb_xc.right, ya - HW, x_east, ya + HW, f"{tag}_out")
        box(m1, x_east - HW, min(ya, y_gap), x_east + HW, max(ya, y_gap),
            f"{tag}_eastv")
        box(m1, x_col, y_gap - HW, x_east, y_gap + HW, f"{tag}_in_h")
        box(m1, x_col - HW, min(y_gap, yb), x_col + HW, max(y_gap, yb),
            f"{tag}_col")
        box(m1, bb_inv.right, yb - HW, x_col, yb + HW, f"{tag}_to_inv")
        print(f"  {tag} cross y_gap={y_gap:.3f} x_col={x_col:.3f} "
              f"x_east={x_east:.3f}", flush=True)

    def stub_outside_to(pt, x1, y1, tag):
        """Manhattan M1 from pt to (x1,y1); caller must keep path outside children."""
        x0, y0 = pt
        if abs(y0 - y1) < 0.05:
            box(m1, x0, y0 - HW, x1, y0 + HW, tag)
        elif abs(x0 - x1) < 0.05:
            box(m1, x0 - HW, y0, x0 + HW, y1, tag)
        else:
            box(m1, x0, y0 - HW, x1, y0 + HW, f"{tag}_h")
            box(m1, x1 - HW, y0, x1 + HW, y1, f"{tag}_v")

    # ---- Place AC-p / AC-n inverters first (children) ----
    # Origins chosen so N/S gap ≥ GAP and E faces share an X for XC.
    y_p = 22.0
    y_n = -28.0
    x_inv = 30.0  # room for cmim+rhigh west

    inv_p_bb, _ = place_inst(
        invs["p"]["cid"], x_inv - invs["p"]["bb"].left, y_p, "inv_p",
        is_child=True)
    ip = map_pins(invs["p"]["pins"], x_inv - invs["p"]["bb"].left, y_p)

    inv_n_bb, _ = place_inst(
        invs["n"]["cid"], x_inv - invs["n"]["bb"].left, y_n, "inv_n",
        is_child=True)
    inn = map_pins(invs["n"]["pins"], x_inv - invs["n"]["bb"].left, y_n)

    assert inv_p_bb.bottom >= inv_n_bb.top + GAP - 0.01, (
        inv_p_bb.bottom, inv_n_bb.top)

    # cmim + rhigh west of each inv (parent devices in pocket; no child overlap)
    def place_ac_pocket(inv_bb, inv_pins, y_cm, tag, rtop_side="N"):
        """cmim | rhigh west of inv; wire mid→a and rtop→y outside child."""
        # rhigh immediately west of inv (narrow); cmim west of rhigh
        rh_x = inv_bb.left - GAP - 0.7  # rhigh local width ~0.9
        rh_bb, rbot, rtop = place_rhigh(rh_x, y_cm - 2.0, f"rh_{tag}")
        if rh_bb.right > inv_bb.left - 0.4:
            raise RuntimeError(
                f"rhigh_{tag} invades inv: {rh_bb} vs {inv_bb}")
        cm_x = rh_bb.left - GAP - 7.0
        cm_bb, m5_xy, tm_xy = place_series_cmim(cm_x, y_cm, f"cmim_{tag}")
        if cm_bb.right > rh_bb.left - 0.4:
            raise RuntimeError(
                f"cmim_{tag} invades rhigh: {cm_bb} vs {rh_bb}")

        # TM1 mid → rbot (parent pocket) and → inv.a W face
        stub_outside_to(tm_xy, rbot[0], rbot[1], f"{tag}_tm_r")
        xa, ya = inv_pins["a"]
        stub_outside_to(tm_xy, inv_bb.left - 0.1, ya, f"{tag}_tm_a0")
        box(m1, inv_bb.left - 0.1 - HW, ya - HW, inv_bb.left, ya + HW,
            f"{tag}_tm_a1")

        # rtop → inv.y: wrap on the side away from vcv (N) / keep ≥1 µm off faces
        # so signal metal cannot touch supply face stubs [LVS].
        xy, yy = inv_pins["y"]
        if rtop_side == "N":
            y_out = inv_bb.top + 1.5
        else:
            y_out = inv_bb.bottom - 1.5
        x_east = inv_bb.right + 1.5
        stub_outside_to(rtop, rtop[0], y_out, f"{tag}_rt_v")
        stub_outside_to((rtop[0], y_out), x_east, y_out, f"{tag}_rt_h")
        stub_outside_to((x_east, y_out), x_east, yy, f"{tag}_rt_v2")
        box(m1, inv_bb.right, yy - HW, x_east + HW, yy + HW, f"{tag}_rt_y")
        return cm_bb, m5_xy, tm_xy, rh_bb

    print("placing AC pockets", flush=True)
    # Wrap rtop on the N–S corridor side (never along vcv/gnd faces)
    cm_p, m5_p, tm_p, rh_p = place_ac_pocket(
        inv_p_bb, ip, y_p + 2.0, "p", rtop_side="S")
    cm_n, m5_n, tm_n, rh_n = place_ac_pocket(
        inv_n_bb, inn, y_n + 2.0, "n", rtop_side="N")

    # ---- XC east of inv_p / inv_n ----
    x_xc = max(inv_p_bb.right, inv_n_bb.right) + GAP
    # Align xc_a.a Y with inv_p.y
    # local a_y of 05_1 = 1.64; want origin_y such that a_y + oy = ip["y"][1]
    oy_a = ip["y"][1] - invs["xc_a"]["pins"]["a"][1]
    xca_bb, _ = place_inst(
        invs["xc_a"]["cid"], x_xc - invs["xc_a"]["bb"].left, oy_a,
        "xc_a", is_child=True)
    xca = map_pins(invs["xc_a"]["pins"], x_xc - invs["xc_a"]["bb"].left, oy_a)

    oy_b = inn["y"][1] - invs["xc_b"]["pins"]["a"][1]
    xcb_bb, _ = place_inst(
        invs["xc_b"]["cid"], x_xc - invs["xc_b"]["bb"].left, oy_b,
        "xc_b", is_child=True)
    xcb = map_pins(invs["xc_b"]["pins"], x_xc - invs["xc_b"]["bb"].left, oy_b)

    assert xca_bb.bottom >= xcb_bb.top + 0.5 or xcb_bb.bottom >= xca_bb.top + 0.5 \
        or abs(xca_bb.bottom - xcb_bb.top) >= 0.5, ("xc overlap", xca_bb, xcb_bb)

    print("XC gap stubs", flush=True)
    gap_stub_ew(ip["y"], inv_p_bb, xca["a"], xca_bb, "x_o2p_to_xca")
    gap_stub_ew(inn["y"], inv_n_bb, xcb["a"], xcb_bb, "x_o2n_to_xcb")

    # Cross nets on SEPARATE corridors (shared metal → x_o2p|x_o2n short)
    y_lo_xc = max(inv_n_bb.top, xcb_bb.top)
    y_hi_xc = min(inv_p_bb.bottom, xca_bb.bottom)
    y_cross_a = y_lo_xc + 1.5          # x_o2n path (xc_a.y → inv_n)
    y_cross_b = y_hi_xc - 1.5          # x_o2p path (xc_b.y → inv_p)
    assert y_cross_b >= y_cross_a + 1.0, (y_cross_a, y_cross_b)
    x_east_a = max(xca_bb.right, xcb_bb.right) + 2.0
    x_east_b = x_east_a + 2.0
    x_col_a = inv_n_bb.right + 1.0
    x_col_b = inv_p_bb.right + 2.5
    cross_via_xc_gap(xca["y"], xca_bb, inn["y"], inv_n_bb, xcb_bb,
                     "xca_y_to_o2n", y_cross_a, x_east_a, x_col_a)
    cross_via_xc_gap(xcb["y"], xcb_bb, ip["y"], inv_p_bb, xca_bb,
                     "xcb_y_to_o2p", y_cross_b, x_east_b, x_col_b)

    # ---- AC-b + taper east of XC ----
    x_ac2 = max(xca_bb.right, xcb_bb.right) + GAP
    y_b = 0.0
    # Place inv_b first at x after cmim pocket
    x_inv_b = x_ac2 + 20.0
    inv_b_bb, _ = place_inst(
        invs["b"]["cid"], x_inv_b - invs["b"]["bb"].left, y_b, "inv_b",
        is_child=True)
    ib = map_pins(invs["b"]["pins"], x_inv_b - invs["b"]["bb"].left, y_b)

    cm_b, m5_b, tm_b, rh_b = place_ac_pocket(
        inv_b_bb, ib, y_b + 2.0, "b", rtop_side="S")  # N kept for x_o2p feed

    # Feed cmim_b.M5 from x_o2p along a track well below the vcv rail [LVS]
    y_top = max(inv_p_bb.top, xca_bb.top, inv_b_bb.top)
    y_feed = y_top + 1.5  # vcv rail will be at y_top+5; keep ≥3 µm gap
    x_feed = inv_p_bb.right + 1.2  # east of inv_p, west of xc gap stubs
    # out from inv_p.y to x_feed (already have gap stub to xc_a on same net)
    stub_outside_to(ip["y"], x_feed, ip["y"][1], "feed_from_y")
    stub_outside_to((x_feed, ip["y"][1]), x_feed, y_feed, "feed_up")
    stub_outside_to((x_feed, y_feed), m5_b[0], y_feed, "feed_h")
    stub_outside_to((m5_b[0], y_feed), m5_b[0], m5_b[1], "feed_dn")

    # Taper
    x_t3 = inv_b_bb.right + GAP
    # Align t3.a Y with inv_b.y
    oy_t3 = ib["y"][1] - invs["t3"]["pins"]["a"][1]
    t3_bb, _ = place_inst(
        invs["t3"]["cid"], x_t3 - invs["t3"]["bb"].left, oy_t3, "inv_t3",
        is_child=True)
    t3 = map_pins(invs["t3"]["pins"], x_t3 - invs["t3"]["bb"].left, oy_t3)
    gap_stub_ew(ib["y"], inv_b_bb, t3["a"], t3_bb, "cy_to_t3")

    x_t9 = t3_bb.right + GAP
    oy_t9 = t3["y"][1] - invs["t9"]["pins"]["a"][1]
    t9_bb, _ = place_inst(
        invs["t9"]["cid"], x_t9 - invs["t9"]["bb"].left, oy_t9, "inv_t9",
        is_child=True)
    t9 = map_pins(invs["t9"]["pins"], x_t9 - invs["t9"]["bb"].left, oy_t9)
    gap_stub_ew(t3["y"], t3_bb, t9["a"], t9_bb, "cz_to_t9")

    # ---- Power: face→rail; jog to W/E spine if column blocked [latch] ----
    child_bbs = [inv_p_bb, inv_n_bb, xca_bb, xcb_bb, inv_b_bb, t3_bb, t9_bb]
    y_vcv = max(b.top for b in child_bbs) + 5.0  # clear of signal feed track
    y_gnd = min(b.bottom for b in child_bbs) - 5.0
    # Separate spines for vcv vs gnd — a shared full-height spine shorts them
    x_vcv_w = min(b.left for b in child_bbs) - 3.0
    x_vcv_e = max(b.right for b in child_bbs) + 3.0
    x_gnd_w = x_vcv_w - 2.0
    x_gnd_e = x_vcv_e + 2.0
    vcv_pts = [ip["vcv"], inn["vcv"], ib["vcv"], xca["vcv"], xcb["vcv"],
               t3["vcv"], t9["vcv"]]
    gnd_pts = [ip["gnd"], inn["gnd"], ib["gnd"], xca["gnd"], xcb["gnd"],
               t3["gnd"], t9["gnd"]]
    bbs_for = [inv_p_bb, inv_n_bb, inv_b_bb, xca_bb, xcb_bb, t3_bb, t9_bb]

    def seg_hits_other(x0, y0, x1, y1, skip_bb):
        from assembly_guard import penetration_depth
        seg = pya.DBox(min(x0, x1) - HW, min(y0, y1) - HW,
                       max(x0, x1) + HW, max(y0, y1) + HW)
        for obb in child_bbs:
            if obb == skip_bb:
                continue
            if penetration_depth(seg, obb) > 0.55:
                return True
        return False

    y_escape = 0.5 * (min(inv_p_bb.bottom, xca_bb.bottom)
                      + max(inv_n_bb.top, xcb_bb.top))

    def route_to_rail(x, bb, y_ex, y_rail, spines, tag):
        """From (x,y_ex) to y_rail on this net's spines only."""
        if not seg_hits_other(x, y_ex, x, y_rail, bb):
            box(m1, x - HW, min(y_ex, y_rail), x + HW, max(y_ex, y_rail),
                f"{tag}_dir")
            return
        for x_sp in spines:
            if (not seg_hits_other(x, y_ex, x_sp, y_ex, bb)
                    and not seg_hits_other(x_sp, y_ex, x_sp, y_rail, bb)):
                box(m1, min(x, x_sp), y_ex - HW, max(x, x_sp), y_ex + HW,
                    f"{tag}_jog")
                box(m1, x_sp - HW, min(y_ex, y_rail), x_sp + HW,
                    max(y_ex, y_rail), f"{tag}_sp")
                return
        if not seg_hits_other(x, y_ex, x, y_escape, bb):
            for x_sp in spines:
                if (not seg_hits_other(x, y_escape, x_sp, y_escape, bb)
                        and not seg_hits_other(
                            x_sp, y_escape, x_sp, y_rail, bb)):
                    box(m1, x - HW, min(y_ex, y_escape), x + HW,
                        max(y_ex, y_escape), f"{tag}_esc_v")
                    box(m1, min(x, x_sp), y_escape - HW,
                        max(x, x_sp), y_escape + HW, f"{tag}_esc_h")
                    box(m1, x_sp - HW, min(y_escape, y_rail), x_sp + HW,
                        max(y_escape, y_rail), f"{tag}_esc_sp")
                    return
        raise RuntimeError(f"{tag} blocked at ({x:.3f},{y_ex:.3f})")

    for (x, y), bb in zip(vcv_pts, bbs_for):
        y_ex = bb.top + 0.35
        box(m1, x - HW, bb.top, x + HW, y_ex, "vcv_face")
        route_to_rail(x, bb, y_ex, y_vcv, (x_vcv_w, x_vcv_e), "vcv")
    for (x, y), bb in zip(gnd_pts, bbs_for):
        y_ex = bb.bottom - 0.35
        box(m1, x - HW, y_ex, x + HW, bb.bottom, "gnd_face")
        route_to_rail(x, bb, y_ex, y_gnd, (x_gnd_w, x_gnd_e), "gnd")
    xs = [p[0] for p in vcv_pts] + [x_vcv_w, x_vcv_e]
    box(m1, min(xs) - 1.0, y_vcv - HW, max(xs) + 1.0, y_vcv + HW, "vcv_rail")
    xs_g = [p[0] for p in gnd_pts] + [x_gnd_w, x_gnd_e]
    box(m1, min(xs_g) - 1.0, y_gnd - HW, max(xs_g) + 1.0, y_gnd + HW, "gnd_rail")

    # Face pins: route on the outer rim only (never straight through children)
    bb = top.bbox().to_dtype(ly.dbu)

    def pin_on_rim(name, face, x_from, y_from):
        """Stub to nearest rim, then along rim to pin; pin flush on face."""
        if face == "W":
            x_rim, y_rim = bb.left + 0.5, y_from
            # go west from source to rim X first (source is already west pocket)
            stub_outside_to((x_from, y_from), x_rim, y_from, f"pin_{name}")
            PF.place_pin(top, m1, m1pin, m1txt, x_rim, y_rim, name)
        elif face == "E":
            x_rim, y_rim = bb.right - 0.5, y_from
            stub_outside_to((x_from, y_from), x_rim, y_from, f"pin_{name}")
            PF.place_pin(top, m1, m1pin, m1txt, x_rim, y_rim, name)
        elif face == "N":
            x_rim, y_rim = x_from, bb.top - 0.5
            stub_outside_to((x_from, y_from), x_from, y_rim, f"pin_{name}")
            PF.place_pin(top, m1, m1pin, m1txt, x_rim, y_rim, name)
        elif face == "S":
            x_rim, y_rim = x_from, bb.bottom + 0.5
            stub_outside_to((x_from, y_from), x_from, y_rim, f"pin_{name}")
            PF.place_pin(top, m1, m1pin, m1txt, x_rim, y_rim, name)
        else:
            raise ValueError(face)

    pin_on_rim("dp", "W", m5_p[0], m5_p[1])
    pin_on_rim("dn", "W", m5_n[0], m5_n[1])
    pin_on_rim("y", "E", t9["y"][0], t9["y"][1])
    pin_on_rim("vcv", "N", 0.5 * (min(xs) + max(xs)), y_vcv)
    pin_on_rim("gnd", "S", 0.5 * (min(xs_g) + max(xs_g)), y_gnd)

    guard.check_top_shapes(
        top, [(m1, "M1"), (m5, "M5"), (tm1, "TM1")], tag_prefix="scan")

    bb = top.bbox().to_dtype(ly.dbu)
    area = (bb.right - bb.left) * (bb.top - bb.bottom) * 1e-6
    print(f"cml_conv bbox {bb}; area {area:.5f} mm² [GDS]", flush=True)
    print(f"GUARD PASS: {guard.summary()}", flush=True)

    gds = os.path.join(OUT, f"{CELL}.gds")
    ly.write(gds)
    with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
        shutil.copyfileobj(f, z)

    # Flat LVS spice matching lo_converter (m=2 final stage) [SCH]
    open(os.path.join(OUT, f"{CELL}.spice"), "w").write(
        f"""* P2.7.4b {CELL} = lo_converter [SCH]
.subckt {CELL} dp dn y vcv gnd
Cccap dp x_cip cap_cmim w={CMIM_SIDE:.3f}u l={CMIM_SIDE:.3f}u m=1
Rrcap x_cip x_o2p gnd rhigh w=0.5u l=18.382u b=0 m=1
Mxcapp x_o2p x_cip vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxcapn x_o2p x_cip gnd gnd sg13_lv_nmos w=2u l=0.13u
Cccan dn x_cin cap_cmim w={CMIM_SIDE:.3f}u l={CMIM_SIDE:.3f}u m=1
Rrcan x_cin x_o2n gnd rhigh w=0.5u l=18.382u b=0 m=1
Mxcanp x_o2n x_cin vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxcann x_o2n x_cin gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxcxap x_o2n x_o2p vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxcxan x_o2n x_o2p gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Mxcxbp x_o2p x_o2n vcv vcv sg13_lv_pmos w=1u l=0.13u
Mxcxbn x_o2p x_o2n gnd gnd sg13_lv_nmos w=0.5u l=0.13u
Cccb x_o2p x_cbi cap_cmim w={CMIM_SIDE:.3f}u l={CMIM_SIDE:.3f}u m=1
Rrcb x_cbi x_cy gnd rhigh w=0.5u l=18.382u b=0 m=1
Mxcbp x_cy x_cbi vcv vcv sg13_lv_pmos w=4u l=0.13u
Mxcbn x_cy x_cbi gnd gnd sg13_lv_nmos w=2u l=0.13u
Mxcv3p x_cz x_cy vcv vcv sg13_lv_pmos w=6.0u l=0.13u
Mxcv3n x_cz x_cy gnd gnd sg13_lv_nmos w=3.0u l=0.13u
Mxcv4p y x_cz vcv vcv sg13_lv_pmos w=9.0u l=0.13u m=2
Mxcv4n y x_cz gnd gnd sg13_lv_nmos w=4.5u l=0.13u m=2
.ends
""")
    open(os.path.join(OUT, f"summary_build_{CELL}.txt"), "w").write(
        f"area_mm2={area:.5f}\ncmim_side={CMIM_SIDE}\n"
        f"tm1_w={TM1_W}\ntm1_space={TM1_SPACE}\n"
        f"guard={guard.summary()}\n"
        f"pin_plan=summary_pin_plan_cml_conv.txt\n")
    print(f"wrote {gds}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
