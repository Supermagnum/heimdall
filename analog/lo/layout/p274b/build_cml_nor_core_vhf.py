#!/usr/bin/env python3
"""P2.7.4b — cml_nor_core_vhf: 3× NMOS shared source (latch S/D rules) [SCH].

mgr → d_orp / g_vref; mga → d_orn / g_q1p; mgb → d_orn / g_q2p; all sources → s.
Method: same as cml_clk_pair — M1 column stubs only; join on M2; outer lanes;
source pin in an inter-device gap (never under a finger at drain-bus Y).
Face pins: s=S; d_orp/d_orn=N (distinct X, like clk_pair); g_*=E; gnd=W.
"""
from __future__ import annotations

import gzip
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)
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
CELL = "cml_nor_core_vhf"
W_IN, NG, W_DUM = "3.0u", 5, "0.6u"


def um(x):
    return int(round(float(x) / DBU))


class Core:
    def __init__(self):
        self.ly = pya.Layout()
        self.ly.dbu = DBU
        self.ly.technology_name = "sg13g2"
        self.lib = pya.Library.library_by_name("SG13_dev", "sg13g2")
        self.lib_ly = self.lib.layout()
        self.m1 = self.ly.layer(8, 0)
        self.m1pin = self.ly.layer(8, 2)
        self.m1txt = self.ly.layer(8, 25)
        self.m2 = self.ly.layer(10, 0)
        self.cont = self.ly.layer(6, 0)
        self.poly = self.ly.layer(5, 0)
        self.activ = self.ly.layer(1, 0)
        self.log = []

    def say(self, s=""):
        print(s, flush=True)
        self.log.append(s)

    def pcell(self, name, params):
        decl = self.lib_ly.pcell_declaration(name)
        return self.ly.add_pcell_variant(self.lib, decl.id(), params)

    def place(self, parent, cid, x, y, mirror=False):
        t = pya.Trans(pya.Trans.M90 if mirror else pya.Trans.R0, um(x), um(y))
        parent.insert(pya.CellInstArray(cid, t))
        return self.ly.cell(cid).bbox().transformed(t).to_dtype(self.ly.dbu), t

    def box(self, cell, layer, x0, y0, x1, y1):
        cell.shapes(layer).insert(
            pya.DBox(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def m1_sd_cols(self, cid, trans):
        uniq = {}
        for s in self.ly.cell(cid).shapes(self.m1).each():
            if not s.is_box():
                continue
            b = s.bbox().transformed(trans).to_dtype(self.ly.dbu)
            if b.width() > 0.25 or b.height() < 0.4:
                continue
            cx = round((b.left + b.right) / 2, 3)
            uniq[cx] = b
        return [uniq[k] for k in sorted(uniq)]

    def poly_gates(self, cid, trans):
        boxes = []
        for s in self.ly.cell(cid).shapes(self.poly).each():
            if not s.is_box():
                continue
            b = s.bbox().transformed(trans).to_dtype(self.ly.dbu)
            if b.width() < 0.20 and b.height() > 0.5:
                boxes.append(b)
        boxes.sort(key=lambda b: b.left)
        out, seen = [], set()
        for b in boxes:
            cx = round(0.5 * (b.left + b.right), 3)
            if cx not in seen:
                seen.add(cx)
                out.append(b)
        return out

    def activ_top(self, cid, trans):
        top = None
        for s in self.ly.cell(cid).shapes(self.activ).each():
            if s.is_box():
                b = s.bbox().transformed(trans).to_dtype(self.ly.dbu)
                top = b.top if top is None else max(top, b.top)
        return top if top is not None else 0.0

    def gate_poly_strap(self, cell, gates, activ_top):
        self.box(cell, self.poly, gates[0].left, activ_top + 0.08,
                 gates[-1].right, activ_top + 0.55)

    def gate_m1_exit(self, cell, gates, activ_top, x_bus, y_bus):
        y_pad0 = max(activ_top + 0.50, max(g.top for g in gates) + 0.30)
        y_pad1 = y_pad0 + 0.50
        gx0 = min(g.left for g in gates)
        gx1 = max(g.right for g in gates)
        for g in gates:
            gx = 0.5 * (g.left + g.right)
            half = 0.5 * (g.right - g.left)
            self.box(cell, self.poly, gx - half, g.top - 0.05,
                     gx + half, y_pad0 + 0.05)
        self.box(cell, self.poly, gx0 - 0.05, y_pad0, gx1 + 0.05, y_pad1)
        for g in gates:
            gx = 0.5 * (g.left + g.right)
            self.box(cell, self.cont, gx - 0.08, y_pad0 + 0.16,
                     gx + 0.08, y_pad0 + 0.32)
            self.box(cell, self.m1, gx - 0.08, y_pad0 + 0.16,
                     gx + 0.08, y_pad1 + 0.16)
        self.box(cell, self.m1, gx0 - 0.08, y_pad0 + 0.16,
                 gx1 + 0.08, y_pad1 + 0.16)
        g_exit = min(gates, key=lambda g: abs(0.5 * (g.left + g.right) - x_bus))
        gx = 0.5 * (g_exit.left + g_exit.right)
        y_rise = y_pad1 + 0.40
        self.box(cell, self.m1, gx - 0.10, y_pad1, gx + 0.10, y_rise + 0.28)
        self.box(cell, self.m1, min(x_bus, gx) - 0.14, y_rise,
                 max(x_bus, gx) + 0.14, y_rise + 0.28)
        self.box(cell, self.m1, x_bus - 0.14, min(y_rise, y_bus),
                 x_bus + 0.14, max(y_rise + 0.28, y_bus))
        return y_pad1

    def build(self):
        top = self.ly.create_cell(CELL)
        nmos = self.pcell("nmos", {
            "w": W_IN, "l": "0.13u", "ng": NG, "m": 1,
            "guardRingType": "none",
        })
        dum = self.pcell("nmos", {
            "w": W_DUM, "l": "0.13u", "ng": 1, "m": 1,
            "guardRingType": "none",
        })
        vs12 = self.pcell("via_stack", {
            "b_layer": "Metal1", "t_layer": "Metal2",
            "vn_columns": 1, "vn_rows": 1,
        })
        ptap = self.pcell("ptap1", {"w": "0.78u", "l": "0.78u"})

        loc = self.ly.cell(nmos).bbox().to_dtype(self.ly.dbu)
        dloc = self.ly.cell(dum).bbox().to_dtype(self.ly.dbu)
        # Wide gaps: V1.b + keep source pin clear of drain columns [DRC/LVS]
        gap = 18.0
        x_r = -gap - loc.right
        x_a = 0.0
        x_b = gap + loc.right
        bb_r, t_r = self.place(top, nmos, x_r, 0.0)
        bb_a, t_a = self.place(top, nmos, x_a, 0.0)
        bb_b, t_b = self.place(top, nmos, x_b, 0.0, mirror=True)
        self.say(f"mgr {bb_r}; mga {bb_a}; mgb {bb_b} [SCH]")

        x_dumL = bb_r.left - 6.0 - dloc.right
        x_dumR = bb_b.right + 6.0 - dloc.left
        bb_dL, t_dL = self.place(top, dum, x_dumL, 0.0)
        bb_dR, t_dR = self.place(top, dum, x_dumR, 0.0)

        def sd(tr):
            cols = self.m1_sd_cols(nmos, tr)
            assert len(cols) == NG + 1, len(cols)
            return ([cols[i] for i in range(0, len(cols), 2)],
                    [cols[i] for i in range(1, len(cols), 2)])

        drn_r, src_r = sd(t_r)
        drn_a, src_a = sd(t_a)
        drn_b, src_b = sd(t_b)
        g_r = self.poly_gates(nmos, t_r)
        g_a = self.poly_gates(nmos, t_a)
        g_b = self.poly_gates(nmos, t_b)
        at_r = self.activ_top(nmos, t_r)
        at_a = self.activ_top(nmos, t_a)
        at_b = self.activ_top(nmos, t_b)
        self.say(f"S/D order even=D odd=S nD={len(drn_r)} [LVS]")

        y_s = min(bb_r.bottom, bb_a.bottom, bb_b.bottom) - 3.0
        y_dr = y_s - 4.0
        y_gnd = y_dr - 5.0
        y_port = y_gnd - 4.0

        # Gnd rails outboard; drain lanes further out (never share X with gnd)
        # — same separation as cml_clk_pair [LVS]
        x_gL = bb_dL.left - 4.0
        x_gR = bb_dR.right + 4.0
        x_w_lane = x_gL - 3.0
        x_e_lane = x_gR + 3.0
        x_e_orn = x_gR + 6.0
        x_e_orp = x_gR + 9.0
        # Source pin in gap between mgr and mga (no drain finger under it)
        x_s_pin = 0.5 * (bb_r.right + bb_a.left)

        # --- Sources → M2 bus; pin drop only in gap ---
        for c in src_r + src_a + src_b:
            self.box(top, self.m1, c.left, y_s, c.right, c.bottom)
            self.place(top, vs12, 0.5 * (c.left + c.right) - 0.05, y_s)
        self.box(top, self.m2,
                 min(src_r[0].left, src_a[0].left) - 0.3, y_s - 0.15,
                 max(src_b[-1].right, src_a[-1].right) + 0.3, y_s + 0.55)
        # Spur M2 into gap, then via + M1 down (never under a device at y_dr)
        self.box(top, self.m2, x_s_pin - 0.20, y_s - 0.15,
                 x_s_pin + 0.20, y_s + 0.55)
        self.place(top, vs12, x_s_pin - 0.05, y_s)
        y_s_face = y_port - 1.0
        self.box(top, self.m1, x_s_pin - 0.25, y_s_face - 0.5,
                 x_s_pin + 0.25, y_s + 0.40)

        # --- orp drains (mgr): south bus → west lane → east face ---
        for c in drn_r:
            self.box(top, self.m1, c.left, y_dr, c.right, c.bottom)
            self.place(top, vs12, 0.5 * (c.left + c.right) - 0.05, y_dr)
        self.box(top, self.m2, x_w_lane - 0.20, y_dr - 0.15,
                 max(c.right for c in drn_r) + 0.2, y_dr + 0.55)
        self.place(top, vs12, x_w_lane - 0.05, y_dr)
        y_orp = y_dr + 2.0
        self.box(top, self.m2, x_w_lane - 0.20, y_dr - 0.15,
                 x_w_lane + 0.20, y_orp + 0.40)
        self.box(top, self.m2, x_w_lane - 0.20, y_orp - 0.15,
                 x_e_orp + 0.20, y_orp + 0.40)
        self.place(top, vs12, x_e_orp - 0.05, y_orp)
        self.box(top, self.m1, x_e_orp - 0.25, y_orp - 0.5,
                 x_e_orp + 0.25, y_orp + 0.40)

        # --- orn drains (mga+mgb): south bus → east lane (separate Y) ---
        for c in drn_a + drn_b:
            self.box(top, self.m1, c.left, y_dr, c.right, c.bottom)
            self.place(top, vs12, 0.5 * (c.left + c.right) - 0.05, y_dr)
        self.box(top, self.m2, min(c.left for c in drn_a) - 0.2, y_dr - 0.15,
                 max(c.right for c in drn_b) + 0.2, y_dr + 0.55)
        # Do NOT span west into mgr — keep orp/orn M2 disjoint at y_dr
        self.place(top, vs12, x_e_lane - 0.05, y_dr)
        self.box(top, self.m2, max(c.right for c in drn_b) - 0.2, y_dr - 0.15,
                 x_e_lane + 0.20, y_dr + 0.55)
        y_orn = y_dr - 2.0
        self.box(top, self.m2, x_e_lane - 0.20, y_orn - 0.15,
                 x_e_lane + 0.20, y_dr + 0.55)
        self.box(top, self.m2, x_e_lane - 0.20, y_orn - 0.15,
                 x_e_orn + 0.20, y_orn + 0.40)
        self.place(top, vs12, x_e_orn - 0.05, y_orn)
        self.box(top, self.m1, x_e_orn - 0.25, y_orn - 0.5,
                 x_e_orn + 0.25, y_orn + 0.40)

        # --- Gates north; Cont off Activ; corridor exits ---
        y_g = max(at_r, at_a, at_b) + 4.0
        # Gate bus X in device–dummy / inter-device corridors (not through drain V)
        x_gr = 0.5 * (bb_r.left + bb_dL.right)
        x_ga = 0.5 * (bb_a.left + bb_r.right)
        x_gb = 0.5 * (bb_b.right + bb_dR.left)
        self.gate_poly_strap(top, g_r, at_r)
        self.gate_poly_strap(top, g_a, at_a)
        self.gate_poly_strap(top, g_b, at_b)
        self.gate_m1_exit(top, g_r, at_r, x_gr, y_g)
        self.gate_m1_exit(top, g_a, at_a, x_ga, y_g)
        self.gate_m1_exit(top, g_b, at_b, x_gb, y_g)

        # --- Dummies + gnd (x_gL / x_gR already set above) ---
        for bb_d, t_d, xg in ((bb_dL, t_dL, x_gL), (bb_dR, t_dR, x_gR)):
            dcols = self.m1_sd_cols(dum, t_d)
            dg = self.poly_gates(dum, t_d)
            at_d = self.activ_top(dum, t_d)
            for c in dcols:
                self.box(top, self.m1, c.left, y_gnd + 1.0, c.right, c.bottom)
            if dcols:
                self.box(top, self.m1,
                         min(min(c.left for c in dcols), xg), y_gnd + 1.0,
                         max(max(c.right for c in dcols), xg), y_gnd + 1.35)
            if dg:
                self.gate_poly_strap(top, dg, at_d)
                self.gate_m1_exit(top, dg, at_d, xg, at_d + 2.0)
                self.box(top, self.m1, xg - 0.14, y_gnd + 1.0,
                         xg + 0.14, at_d + 2.4)
            self.box(top, self.m1, xg - 0.20, y_gnd, xg + 0.20, y_gnd + 1.40)
        for x, y in ((x_gL - 0.4, bb_dL.bottom - 1.5),
                     (x_gR - 0.4, bb_dR.bottom - 1.5),
                     (x_gL - 0.4, y_gnd), (x_gR - 0.4, y_gnd)):
            self.place(top, ptap, x, y)
            self.box(top, self.m1, x, y, x + 0.78, y + 0.78)
        self.place(top, vs12, x_gL - 0.05, y_gnd)
        self.place(top, vs12, x_gR - 0.05, y_gnd)
        self.box(top, self.m2, x_gL - 0.20, y_gnd - 0.15,
                 x_gR + 0.20, y_gnd + 0.55)
        y_gpin = 0.5 * (bb_a.bottom + bb_a.top)
        self.box(top, self.m1, x_gL - 0.20, min(y_gnd, y_gpin),
                 x_gL + 0.20, max(y_gnd + 0.50, y_gpin))
        self.box(top, self.m1, x_gL - 2.0, y_gpin - 0.25,
                 x_gL + 0.20, y_gpin + 0.25)

        bb = top.bbox().to_dtype(self.ly.dbu)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "d_orp", "E", x_e_orp, y_orp, bb)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "d_orn", "E", x_e_orn, y_orn, bb)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "s", "S", x_s_pin, y_s_face, bb)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "g_vref", "N", x_gr, y_g, bb)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "g_q1p", "N", x_ga, y_g, bb)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "g_q2p", "N", x_gb, y_g, bb)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "gnd", "W",
            x_gL - 1.5, y_gpin, bb)

        fp = PF.parse_pins(top, self.m1txt)
        bb = top.bbox().to_dtype(self.ly.dbu)
        area = (bb.right - bb.left) * (bb.top - bb.bottom) * 1e-6
        self.say(f"bbox {bb}; area {area:.5f} mm² [GDS]")
        self.say(f"face pins {fp}")
        PF.assert_pins_on_faces(top, fp, {
            "d_orp": "E", "d_orn": "E", "s": "S",
            "g_vref": "N", "g_q1p": "N", "g_q2p": "N", "gnd": "W",
        }, tol=0.10)

        gds = os.path.join(OUT, f"{CELL}.gds")
        self.ly.write(gds)
        with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
            shutil.copyfileobj(f, z)
        open(os.path.join(OUT, f"{CELL}.spice"), "w").write(
            f"* P2.7.4b {CELL} [SCH]\n"
            f".subckt {CELL} d_orp d_orn g_vref g_q1p g_q2p s gnd\n"
            f"Mmgr d_orp g_vref s gnd sg13_lv_nmos w={W_IN} l=0.13u\n"
            f"Mmga d_orn g_q1p s gnd sg13_lv_nmos w={W_IN} l=0.13u\n"
            f"Mmgb d_orn g_q2p s gnd sg13_lv_nmos w={W_IN} l=0.13u\n"
            f"Mdum gnd gnd gnd gnd sg13_lv_nmos w=1.2u l=0.13u\n"
            ".ends\n"
        )
        open(os.path.join(OUT, f"summary_build_{CELL}.txt"), "w").write(
            "\n".join(self.log) + f"\narea_mm2={area:.5f}\n")
        self.say(f"wrote {gds}")
        return 0


if __name__ == "__main__":
    raise SystemExit(Core().build())
