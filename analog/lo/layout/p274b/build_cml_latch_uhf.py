#!/usr/bin/env python3
"""P2.7.4b — UHF CML latch (0.75 mA, tailed) from PDK pcells [SCH].

Symmetric L/R: data pair, regen pair, clock pair, shared MOSFET tail,
matched rppd loads. Ports: vdd gnd dp dn ckp ckn qp qn nb_lo.
"""
from __future__ import annotations

import gzip
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

import sys
sys.path[:0] = [
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402

DBU = 0.001
# [SCH] circuit.py I_LATCH=0.75 mA, SWING=0.5 → RL=666.7, w=7.5, k=1.5
W_DATA = "7.5u"
W_REGEN = "11.25u"
W_TAIL = "15.0u"
NG_DATA = 5
NG_REGEN = 5
NG_TAIL = 10
# rppd ≈ 250 Ω/sq [PDK]: L = 666.7 * 2 / 250 = 5.334 µm
R_W, R_L = "2.0u", "5.334u"


def um(x):
    return int(round(x / DBU))


class B:
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
        self.poly = self.ly.layer(5, 0)
        self.activ = self.ly.layer(1, 0)
        self.cont = self.ly.layer(6, 0)
        self.log = []

    def say(self, s=""):
        print(s, flush=True)
        self.log.append(s)

    def pcell(self, name, params):
        return self.ly.add_pcell_variant(
            self.lib, self.lib_ly.pcell_declaration(name).id(), params)

    def place(self, parent, cid, x, y, mirror=False):
        if mirror:
            t = pya.Trans(pya.Trans.M90, um(x), um(y))
        else:
            t = pya.Trans(pya.Trans.R0, um(x), um(y))
        parent.insert(pya.CellInstArray(cid, t))
        return self.ly.cell(cid).bbox().transformed(t).to_dtype(self.ly.dbu), t

    def box(self, cell, layer, x0, y0, x1, y1):
        cell.shapes(layer).insert(pya.DBox(
            min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def pin(self, cell, x, y, name):
        self.box(cell, self.m1, x - 0.25, y - 0.25, x + 0.25, y + 0.25)
        cell.shapes(self.m1pin).insert(
            pya.DBox(x - 0.2, y - 0.2, x + 0.2, y + 0.2))
        cell.shapes(self.m1txt).insert(pya.DText(name, pya.DTrans(x, y)))

    def m1_sd_cols(self, cid, trans):
        cell = self.ly.cell(cid)
        boxes = []
        for s in cell.shapes(self.m1).each():
            if not s.is_box():
                continue
            b = s.bbox().transformed(trans).to_dtype(self.ly.dbu)
            if b.width() < 0.20 and b.height() > 0.8:
                boxes.append(b)
        boxes.sort(key=lambda b: b.left)
        return boxes

    def poly_gates(self, cid, trans):
        cell = self.ly.cell(cid)
        boxes = []
        for s in cell.shapes(self.poly).each():
            if not s.is_box():
                continue
            b = s.bbox().transformed(trans).to_dtype(self.ly.dbu)
            if b.width() < 0.20 and b.height() > 0.5:
                boxes.append(b)
        boxes.sort(key=lambda b: b.left)
        # unique X centres
        out, seen = [], set()
        for b in boxes:
            cx = round(0.5 * (b.left + b.right), 3)
            if cx not in seen:
                seen.add(cx)
                out.append(b)
        return out

    def activ_top(self, cid, trans):
        cell = self.ly.cell(cid)
        top = None
        for s in cell.shapes(self.activ).each():
            if s.is_box():
                b = s.bbox().transformed(trans).to_dtype(self.ly.dbu)
                top = b.top if top is None else max(top, b.top)
        return top if top is not None else 0.0

    def gate_exit(self, cell, gates, activ_top, x_bus, y_bus):
        y_pad0 = max(activ_top + 0.50, max(g.top for g in gates) + 0.30)
        y_pad1 = y_pad0 + 0.50
        gx0 = min(g.left for g in gates)
        gx1 = max(g.right for g in gates)
        for g in gates:
            gx = 0.5 * (g.left + g.right)
            half = 0.5 * (g.right - g.left)
            self.box(cell, self.poly, gx - half, g.top - 0.05, gx + half, y_pad0 + 0.05)
        self.box(cell, self.poly, gx0 - 0.05, y_pad0, gx1 + 0.05, y_pad1)
        for g in gates:
            gx = 0.5 * (g.left + g.right)
            self.box(cell, self.cont, gx - 0.08, y_pad0 + 0.16, gx + 0.08, y_pad0 + 0.32)
            self.box(cell, self.m1, gx - 0.08, y_pad0 + 0.16, gx + 0.08, y_pad1 + 0.16)
        self.box(cell, self.m1, gx0 - 0.08, y_pad0 + 0.16, gx1 + 0.08, y_pad1 + 0.16)
        g_exit = min(gates, key=lambda g: abs(0.5 * (g.left + g.right) - x_bus))
        gx = 0.5 * (g_exit.left + g_exit.right)
        y_rise = y_pad1 + 0.40
        self.box(cell, self.m1, gx - 0.10, y_pad1, gx + 0.10, y_rise + 0.28)
        self.box(cell, self.m1, min(x_bus, gx) - 0.14, y_rise,
                 max(x_bus, gx) + 0.14, y_rise + 0.28)
        self.box(cell, self.m1, x_bus - 0.14, min(y_rise, y_bus),
                 x_bus + 0.14, max(y_rise + 0.28, y_bus))
        return y_pad1

    def join_cols_m1_below(self, cell, cols, y_bus):
        """Drop each SD column to a bus *below* Activ — never fill the finger
        height (that shorts D–S inside the device) [LVS lesson from vco_xc_pair]."""
        for c in cols:
            self.box(cell, self.m1, c.left, min(y_bus, c.bottom),
                     c.right, c.bottom)
        if cols:
            self.box(cell, self.m1, cols[0].left, y_bus,
                     cols[-1].right, y_bus + 0.28)

    def join_cols_m1_above(self, cell, cols, y_bus):
        """Rise each SD column to a bus *above* Activ."""
        for c in cols:
            self.box(cell, self.m1, c.left, c.top,
                     c.right, max(y_bus + 0.28, c.top))
        if cols:
            self.box(cell, self.m1, cols[0].left, y_bus,
                     cols[-1].right, y_bus + 0.28)

    def build(self):
        top = self.ly.create_cell("cml_latch_uhf")
        n_data = self.pcell("nmos", {
            "w": W_DATA, "l": "0.13u", "ng": NG_DATA, "m": 1,
            "guardRingType": "none",
        })
        n_regen = self.pcell("nmos", {
            "w": W_REGEN, "l": "0.13u", "ng": NG_REGEN, "m": 1,
            "guardRingType": "none",
        })
        n_tail = self.pcell("nmos", {
            "w": W_TAIL, "l": "0.13u", "ng": NG_TAIL, "m": 1,
            "guardRingType": "none",
        })
        rload = self.pcell("rppd", {
            "R": "666.7", "w": R_W, "l": R_L, "b": 0,
            "Calculate": "R", "guardRingType": "none",
        })
        vs12 = self.pcell("via_stack", {
            "b_layer": "Metal1", "t_layer": "Metal2",
            "vn_columns": 1, "vn_rows": 1,
        })
        ptap = self.pcell("ptap1", {"w": "0.78u", "l": "0.78u"})

        dloc = self.ly.cell(n_data).bbox().to_dtype(self.ly.dbu)
        rloc = self.ly.cell(n_regen).bbox().to_dtype(self.ly.dbu)
        tloc = self.ly.cell(n_tail).bbox().to_dtype(self.ly.dbu)
        lloc = self.ly.cell(rload).bbox().to_dtype(self.ly.dbu)

        gap = 5.0
        x_m1 = -gap / 2 - dloc.right
        x_m2 = gap / 2 + dloc.right

        # Bottom→top stack: tail → clock → data → regen → loads
        # so clock drains (=s1/s2) sit under data sources [LVS routing].
        y_t = 0.0
        bb_t, tt = self.place(top, n_tail, -tloc.width() / 2 - tloc.left,
                              y_t - tloc.bottom)
        self.say(f"tail mt {bb_t} W={W_TAIL} ng={NG_TAIL}")

        y_ck = bb_t.top + 6.0
        bb5, t5 = self.place(top, n_data, x_m1, y_ck - dloc.bottom, mirror=False)
        bb6, t6 = self.place(top, n_data, x_m2, y_ck - dloc.bottom, mirror=True)
        self.say(f"clock m5/m6 {bb5} {bb6}")

        y_d = max(bb5.top, bb6.top) + 6.0
        bb1, t1 = self.place(top, n_data, x_m1, y_d - dloc.bottom, mirror=False)
        bb2, t2 = self.place(top, n_data, x_m2, y_d - dloc.bottom, mirror=True)
        self.say(f"data m1/m2 {bb1} {bb2} W={W_DATA} ng={NG_DATA}")

        y_rgn = max(bb1.top, bb2.top) + 6.0
        bb3, t3 = self.place(top, n_regen, x_m1, y_rgn - rloc.bottom,
                             mirror=False)
        bb4, t4 = self.place(top, n_regen, x_m2, y_rgn - rloc.bottom,
                             mirror=True)
        self.say(f"regen m3/m4 {bb3} {bb4} W={W_REGEN} ng={NG_REGEN}")

        y_r = max(bb3.top, bb4.top) + 4.0
        bb_rl, trl = self.place(top, rload, bb1.left - lloc.left, y_r)
        bb_rr, trr = self.place(top, rload, bb2.left - lloc.left, y_r)
        self.say(f"loads rppd {bb_rl} {bb_rr} R=666.7 [SCH]")

        def sd(cid, tr):
            cols = self.m1_sd_cols(cid, tr)
            assert len(cols) >= 2, len(cols)
            drn = [cols[i] for i in range(0, len(cols), 2)]
            src = [cols[i] for i in range(1, len(cols), 2)]
            return drn, src, cols

        d1, s1a, _ = sd(n_data, t1)
        d2, s2a, _ = sd(n_data, t2)
        d3, s3, _ = sd(n_regen, t3)
        d4, s4, _ = sd(n_regen, t4)
        d5, s5, _ = sd(n_data, t5)  # clock drains = s1 / sources = ta
        d6, s6, _ = sd(n_data, t6)
        dt, st, _ = sd(n_tail, tt)

        # Mid-gap buses (clear of Activ)
        y_ta = 0.5 * (bb_t.top + bb5.bottom)
        y_s1 = 0.5 * (bb5.top + bb1.bottom)   # clock drain ↔ data source
        y_s2 = y_s1 + 1.5                     # separate M1 for s2 (ckn side)
        # Keep s1/s2 buses on opposite X halves to avoid M1.b merge
        y_qn = max(bb1.top, bb3.top) + 1.5
        y_qp = y_qn + 2.0
        y_vdd = max(bb_rl.top, bb_rr.top) + 2.0
        y_gnd = bb_t.bottom - 3.0
        y_nb = y_gnd - 3.0

        # --- ta: clock sources + tail drain ---
        self.join_cols_m1_below(top, s5 + s6, y_ta)
        self.join_cols_m1_above(top, dt, y_ta)
        self.box(top, self.m1,
                 min(min(c.left for c in s5 + s6), min(c.left for c in dt)),
                 y_ta,
                 max(max(c.right for c in s5 + s6), max(c.right for c in dt)),
                 y_ta + 0.28)
        self.join_cols_m1_below(top, st, y_gnd)
        self.place(top, ptap, bb_t.left - 2.0, y_gnd - 0.4)
        self.place(top, ptap, bb_t.right + 1.2, y_gnd - 0.4)

        # --- s1: clock-L drain + data-L/R sources (m1/m2 share s1) ---
        self.join_cols_m1_above(top, d5, y_s1)
        self.join_cols_m1_below(top, s1a + s2a, y_s1)
        self.box(top, self.m1,
                 min(c.left for c in d5 + s1a + s2a), y_s1,
                 max(c.right for c in d5 + s1a + s2a), y_s1 + 0.28)

        # --- s2: clock-R drain + regen sources ---
        self.join_cols_m1_above(top, d6, y_s2)
        self.join_cols_m1_below(top, s3 + s4, y_s2)
        # vertical M2 stem on right outboard for s2 (avoid crossing s1 M1)
        x_s2 = bb6.right + 2.5
        for c in d6:
            self.place(top, vs12, 0.5 * (c.left + c.right), y_s2)
        for c in s3 + s4:
            self.place(top, vs12, 0.5 * (c.left + c.right),
                       min(bb3.bottom, bb4.bottom) - 0.5)
        self.box(top, self.m2, x_s2 - 0.2,
                 min(y_s2, min(bb3.bottom, bb4.bottom) - 0.5),
                 x_s2 + 0.2,
                 max(y_s2 + 0.4, max(bb3.bottom, bb4.bottom)))
        self.box(top, self.m2,
                 min(c.left for c in d6), y_s2,
                 x_s2 + 0.2, y_s2 + 0.4)
        self.box(top, self.m2,
                 min(c.left for c in s3 + s4),
                 min(bb3.bottom, bb4.bottom) - 0.7,
                 x_s2 + 0.2,
                 min(bb3.bottom, bb4.bottom) - 0.3)

        # --- qp / qn drains ---
        self.join_cols_m1_above(top, d1 + d3, y_qn)
        self.join_cols_m1_above(top, d2 + d4, y_qp)

        def r_terms(bb):
            cx = 0.5 * (bb.left + bb.right)
            return (cx, bb.bottom + 0.3), (cx, bb.top - 0.3)

        (rl_b, rl_by), (rl_t, rl_ty) = r_terms(bb_rl)
        (rr_b, rr_by), (rr_t, rr_ty) = r_terms(bb_rr)
        self.box(top, self.m1, rl_b - 0.14, min(y_qn, rl_by),
                 rl_b + 0.14, max(y_qn + 0.28, rl_by))
        self.box(top, self.m1, min(rl_b, d1[0].left) - 0.14, y_qn,
                 max(rl_b, d1[-1].right) + 0.14, y_qn + 0.28)
        self.box(top, self.m1, rr_b - 0.14, min(y_qp, rr_by),
                 rr_b + 0.14, max(y_qp + 0.28, rr_by))
        self.box(top, self.m1, min(rr_b, d2[0].left) - 0.14, y_qp,
                 max(rr_b, d2[-1].right) + 0.14, y_qp + 0.28)
        self.box(top, self.m1, rl_t - 0.14, rl_ty, rl_t + 0.14, y_vdd + 0.28)
        self.box(top, self.m1, rr_t - 0.14, rr_ty, rr_t + 0.14, y_vdd + 0.28)
        self.box(top, self.m1, min(rl_t, rr_t) - 0.14, y_vdd,
                 max(rl_t, rr_t) + 0.14, y_vdd + 0.28)

        # Gates — exit outboard; regen cross-couple to qp/qn
        g1 = self.poly_gates(n_data, t1)
        g2 = self.poly_gates(n_data, t2)
        g3 = self.poly_gates(n_regen, t3)
        g4 = self.poly_gates(n_regen, t4)
        g5 = self.poly_gates(n_data, t5)
        g6 = self.poly_gates(n_data, t6)
        gt = self.poly_gates(n_tail, tt)
        x_dp = bb1.left - 4.0
        x_dn = bb2.right + 4.0
        x_ckp = bb5.left - 4.0
        x_ckn = bb6.right + 4.0
        x_nb = 0.5 * (bb_t.left + bb_t.right)
        y_dp = 0.5 * (bb1.bottom + bb1.top)
        y_ckp = 0.5 * (bb5.bottom + bb5.top)

        self.gate_exit(top, g1, self.activ_top(n_data, t1), x_dp, y_dp)
        self.gate_exit(top, g2, self.activ_top(n_data, t2), x_dn, y_dp)
        self.gate_exit(top, g3, self.activ_top(n_regen, t3),
                       bb3.left - 3.0, y_qp)
        self.box(top, self.m1, bb3.left - 3.14, y_qp,
                 max(d2[-1].right, bb3.left) + 0.14, y_qp + 0.28)
        self.gate_exit(top, g4, self.activ_top(n_regen, t4),
                       bb4.right + 3.0, y_qn)
        self.box(top, self.m1, min(d1[0].left, bb4.right) - 0.14, y_qn,
                 bb4.right + 3.14, y_qn + 0.28)
        self.gate_exit(top, g5, self.activ_top(n_data, t5), x_ckp, y_ckp)
        self.gate_exit(top, g6, self.activ_top(n_data, t6), x_ckn, y_ckp)
        self.gate_exit(top, gt, self.activ_top(n_tail, tt), x_nb, y_nb)

        self.pin(top, 0.5 * (rl_t + rr_t), y_vdd + 0.5, "vdd")
        self.pin(top, x_nb, y_gnd - 0.5, "gnd")
        self.pin(top, x_dp, y_dp, "dp")
        self.pin(top, x_dn, y_dp, "dn")
        self.pin(top, x_ckp, y_ckp, "ckp")
        self.pin(top, x_ckn, y_ckp, "ckn")
        self.pin(top, bb1.left - 2.0, y_qn, "qn")
        self.pin(top, bb2.right + 2.0, y_qp, "qp")
        self.pin(top, x_nb, y_nb, "nb_lo")

        bb = top.bbox().to_dtype(self.ly.dbu)
        area = bb.width() * bb.height() * 1e-6
        self.say(f"bbox {bb}; area {area:.5f} mm² [GDS]")

        gds = os.path.join(OUT, "cml_latch_uhf.gds")
        self.ly.write(gds)
        with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
            shutil.copyfileobj(f, z)
        self.say(f"WROTE {gds} / .gz")

        spice = os.path.join(OUT, "cml_latch_uhf.spice")
        open(spice, "w").write(
            "* P2.7.4b cml_latch_uhf [SCH] I=0.75 mA tailed; rppd loads\n"
            ".subckt cml_latch_uhf vdd gnd dp dn ckp ckn qp qn nb_lo\n"
            f"Rrlp vdd qp gnd rppd w={R_W} l={R_L} ps=0.18u b=0 m=1\n"
            f"Rrln vdd qn gnd rppd w={R_W} l={R_L} ps=0.18u b=0 m=1\n"
            f"Mm1 qn dp s1 gnd sg13_lv_nmos w={W_DATA} l=0.13u\n"
            f"Mm2 qp dn s1 gnd sg13_lv_nmos w={W_DATA} l=0.13u\n"
            f"Mm3 qn qp s2 gnd sg13_lv_nmos w={W_REGEN} l=0.13u\n"
            f"Mm4 qp qn s2 gnd sg13_lv_nmos w={W_REGEN} l=0.13u\n"
            f"Mm5 s1 ckp ta gnd sg13_lv_nmos w={W_DATA} l=0.13u\n"
            f"Mm6 s2 ckn ta gnd sg13_lv_nmos w={W_DATA} l=0.13u\n"
            f"Mmt ta nb_lo gnd gnd sg13_lv_nmos w={W_TAIL} l=0.13u\n"
            ".ends\n"
        )
        self.say(f"WROTE {spice}")
        open(os.path.join(OUT, "summary_build_cml_latch_uhf.txt"), "w").write(
            "\n".join(self.log) + "\n")
        return 0


if __name__ == "__main__":
    raise SystemExit(B().build())
