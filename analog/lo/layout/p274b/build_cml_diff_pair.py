#!/usr/bin/env python3
"""P2.7.4b step 3a — CML differential pair cell (clock/data latch pair).

Copied method from vco_xc_pair [spec/p27-layout-notes.md]:
- PCell guardRingType=none; hand ptap
- Never M1 across opposite S/D; join same-net cols via M2
- Gate Cont on poly pads above Activ; poly strap at Activ top
- End dummies G=S=D=gnd local only
- even M1 cols = drain; odd = source [LVS]

Open gates (not XC): ports d1 d2 g1 g2 s gnd.
UHF sizes: W=7.5 µm ng=5 [SCH].
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
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402, F401

DBU = 0.001
W_PAIR = "7.5u"
NG = 5
W_DUM = "1.5u"  # = W/ng


def um(x: float) -> int:
    return int(round(float(x) / DBU))


class Pair:
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
        if mirror:
            t = pya.Trans(pya.Trans.M90, um(x), um(y))
        else:
            t = pya.Trans(pya.Trans.R0, um(x), um(y))
        parent.insert(pya.CellInstArray(cid, t))
        return self.ly.cell(cid).bbox().transformed(t).to_dtype(self.ly.dbu), t

    def box(self, cell, layer, x0, y0, x1, y1):
        cell.shapes(layer).insert(
            pya.DBox(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def pin_m1(self, cell, x, y, name):
        self.box(cell, self.m1, x - 0.25, y - 0.25, x + 0.25, y + 0.25)
        self.box(cell, self.m1pin, x - 0.2, y - 0.2, x + 0.2, y + 0.2)
        cell.shapes(self.m1txt).insert(pya.DText(name, pya.DTrans(x, y)))

    def m1_sd_cols(self, cid, trans):
        cell = self.ly.cell(cid)
        uniq = {}
        for s in cell.shapes(self.m1).each():
            if not s.is_box():
                continue
            b = s.bbox().transformed(trans).to_dtype(self.ly.dbu)
            if b.width() > 0.25 or b.height() < 1.0:
                continue
            cx = round((b.left + b.right) / 2, 3)
            uniq[cx] = b
        return [uniq[k] for k in sorted(uniq)]

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

    def gate_poly_strap(self, cell, gates, activ_top):
        g0, g1 = gates[0], gates[-1]
        self.box(cell, self.poly, g0.left, activ_top + 0.08,
                 g1.right, activ_top + 0.55)

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
        top = self.ly.create_cell("cml_diff_pair")
        nmos = self.pcell("nmos", {
            "w": W_PAIR, "l": "0.13u", "ng": NG, "m": 1,
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
        gap = 8.0
        y0 = 0.0
        x_m1 = -gap / 2 - loc.right
        x_m2 = gap / 2 + loc.right
        bb1, t1 = self.place(top, nmos, x_m1, y0, mirror=False)
        bb2, t2 = self.place(top, nmos, x_m2, y0, mirror=True)
        self.say(f"M1 {bb1}; M2 {bb2} [SCH W={W_PAIR} ng={NG}]")

        x_d1 = bb1.left - 6.0
        x_d2 = bb2.right + 6.0
        x_dumL = x_d1 - 5.0 - dloc.right
        x_dumR = x_d2 + 5.0 - dloc.left
        bb_dL, t_dL = self.place(top, dum, x_dumL, y0)
        bb_dR, t_dR = self.place(top, dum, x_dumR, y0)

        cols1 = self.m1_sd_cols(nmos, t1)
        cols2 = self.m1_sd_cols(nmos, t2)
        g1 = self.poly_gates(nmos, t1)
        g2 = self.poly_gates(nmos, t2)
        at1 = self.activ_top(nmos, t1)
        at2 = self.activ_top(nmos, t2)
        n_col = len(cols1)
        assert n_col == NG + 1, (n_col, NG)
        assert len(g1) == NG and len(g2) == NG, (len(g1), len(g2))
        drn1 = [cols1[i] for i in range(0, n_col, 2)]
        src1 = [cols1[i] for i in range(1, n_col, 2)]
        drn2 = [cols2[i] for i in range(0, n_col, 2)]
        src2 = [cols2[i] for i in range(1, n_col, 2)]
        self.say(f"S/D order: even=D odd=S; nS={len(src1)} nD={len(drn1)} [LVS]")

        y_s = min(bb1.bottom, bb2.bottom) - 3.0
        y_dr = y_s - 4.0
        y_gnd = y_dr - 5.0
        y_port = y_gnd - 4.0

        # Gate exits between device and drain spur (not through dummy)
        x_g1 = 0.5 * (bb1.left + x_d1)
        x_g2 = 0.5 * (bb2.right + x_d2)

        # Face pins per 2026-11-20 plan: s=S X≈0; d1/d2=E; gnd=W; g1/g2=N.
        x_gL = min(bb_dL.left, x_d1) - 4.0
        x_gR = max(bb_dR.right, x_d2) + 4.0
        x_east = x_gR + 3.0

        # Sources → s on SOUTH face at X≈0: M1 drop + via; M2 bus
        for c in src1 + src2:
            self.box(top, self.m1, c.left, y_s, c.right, c.bottom)
            self.place(top, vs12, 0.5 * (c.left + c.right) - 0.05, y_s)
        x_s_pin = 0.0
        self.box(top, self.m2,
                 min(src1[0].left - 0.3, x_s_pin - 0.3), y_s - 0.15,
                 max(src2[-1].right + 0.3, x_s_pin + 0.3), y_s + 0.55)
        y_s_pin = y_port - 1.0
        self.place(top, vs12, x_s_pin - 0.05, y_s)
        self.box(top, self.m1, x_s_pin - 0.25, y_s_pin - 0.5,
                 x_s_pin + 0.25, y_s + 0.40)
        self.pin_m1(top, x_s_pin, y_s_pin, "s")

        # Drains → east face (off south join face); M2 outboard then east
        for c in drn1:
            self.box(top, self.m1, c.left, y_dr, c.right, c.bottom)
            self.place(top, vs12, 0.5 * (c.left + c.right) - 0.05, y_dr)
        self.box(top, self.m2, x_d1 - 0.20, y_dr - 0.15,
                 max(c.right for c in drn1) + 0.2, y_dr + 0.55)
        self.place(top, vs12, x_d1 - 0.05, y_dr)
        self.box(top, self.m1, x_d1 - 0.20, y_dr, x_d1 + 0.20, y_dr + 0.40)

        for c in drn2:
            self.box(top, self.m1, c.left, y_dr, c.right, c.bottom)
            self.place(top, vs12, 0.5 * (c.left + c.right) - 0.05, y_dr)
        self.box(top, self.m2, min(c.left for c in drn2) - 0.2, y_dr - 0.15,
                 x_d2 + 0.20, y_dr + 0.55)
        self.place(top, vs12, x_d2 - 0.05, y_dr)
        self.box(top, self.m1, x_d2 - 0.20, y_dr, x_d2 + 0.20, y_dr + 0.40)

        # East-face drain pins at distinct Y (d1 above d2)
        y_d1e = y_dr + 3.0
        y_d2e = y_dr - 1.0
        self.place(top, vs12, x_d1 - 0.05, y_d1e)
        self.box(top, self.m2, x_d1 - 0.20, y_dr - 0.15,
                 x_d1 + 0.20, y_d1e + 0.40)
        self.box(top, self.m2, x_d1 - 0.20, y_d1e - 0.15,
                 x_east + 0.20, y_d1e + 0.40)
        self.place(top, vs12, x_east - 0.05, y_d1e)
        self.box(top, self.m1, x_east - 0.25, y_d1e - 0.5,
                 x_east + 0.25, y_d1e + 0.40)
        self.pin_m1(top, x_east, y_d1e, "d1")

        self.place(top, vs12, x_d2 - 0.05, y_d2e)
        self.box(top, self.m2, x_d2 - 0.20, min(y_dr, y_d2e) - 0.15,
                 x_d2 + 0.20, max(y_dr, y_d2e) + 0.40)
        self.box(top, self.m2, x_d2 - 0.20, y_d2e - 0.15,
                 x_east + 0.20, y_d2e + 0.40)
        self.place(top, vs12, x_east - 0.05, y_d2e)
        self.box(top, self.m1, x_east - 0.25, y_d2e - 0.5,
                 x_east + 0.25, y_d2e + 0.40)
        self.pin_m1(top, x_east, y_d2e, "d2")

        # Gates — contacted off active; open ports g1/g2 (not XC)
        self.gate_poly_strap(top, g1, at1)
        self.gate_poly_strap(top, g2, at2)
        y_g_exit = max(at1, at2) + 4.0
        self.gate_m1_exit(top, g1, at1, x_g1, y_g_exit)
        self.gate_m1_exit(top, g2, at2, x_g2, y_g_exit)
        y_g_pin = y_g_exit + 2.0
        self.box(top, self.m1, x_g1 - 0.14, y_g_exit, x_g1 + 0.14, y_g_pin)
        self.box(top, self.m1, x_g2 - 0.14, y_g_exit, x_g2 + 0.14, y_g_pin)
        self.pin_m1(top, x_g1, y_g_pin, "g1")
        self.pin_m1(top, x_g2, y_g_pin, "g2")

        # Dummies + gnd outboard; gnd pin on WEST face
        for bb_d, t_d, x_gnd_d in ((bb_dL, t_dL, x_gL), (bb_dR, t_dR, x_gR)):
            dcols = self.m1_sd_cols(dum, t_d)
            dg = self.poly_gates(dum, t_d)
            at_d = self.activ_top(dum, t_d)
            y_dg = at_d + 2.0
            for c in dcols:
                self.box(top, self.m1, c.left, y_gnd + 1.0, c.right, c.bottom)
            if dcols:
                self.box(top, self.m1,
                         min(min(c.left for c in dcols), x_gnd_d), y_gnd + 1.0,
                         max(max(c.right for c in dcols), x_gnd_d), y_gnd + 1.35)
            if dg:
                self.gate_poly_strap(top, dg, at_d)
                self.gate_m1_exit(top, dg, at_d, x_gnd_d, y_dg)
                self.box(top, self.m1, x_gnd_d - 0.14, y_gnd + 1.0,
                         x_gnd_d + 0.14, y_dg + 0.40)
            self.box(top, self.m1, x_gnd_d - 0.20, y_gnd, x_gnd_d + 0.20,
                     y_gnd + 1.40)

        for x, y in ((x_gL - 0.4, bb_dL.bottom - 1.5),
                     (x_gR - 0.4, bb_dR.bottom - 1.5),
                     (x_gL - 0.4, y_gnd), (x_gR - 0.4, y_gnd)):
            self.place(top, ptap, x, y)
            self.box(top, self.m1, x, y, x + 0.78, y + 0.78)
        # Tie L/R gnd rails
        self.place(top, vs12, x_gL - 0.05, y_gnd)
        self.place(top, vs12, x_gR - 0.05, y_gnd)
        self.box(top, self.m2, x_gL - 0.20, y_gnd - 0.15,
                 x_gR + 0.20, y_gnd + 0.55)
        y_gpin = 0.5 * (min(bb1.bottom, bb2.bottom) + max(bb1.top, bb2.top))
        self.box(top, self.m1, x_gL - 0.20, min(y_gnd, y_gpin),
                 x_gL + 0.20, max(y_gnd + 0.50, y_gpin))
        self.box(top, self.m1, x_gL - 2.0, y_gpin - 0.25,
                 x_gL + 0.20, y_gpin + 0.25)
        self.pin_m1(top, x_gL - 1.5, y_gpin, "gnd")

        bb = top.bbox().to_dtype(self.ly.dbu)
        area = (bb.right - bb.left) * (bb.top - bb.bottom) * 1e-6
        self.say(f"pair bbox {bb}; area {area:.5f} mm² [GDS]")

        gds = os.path.join(OUT, "cml_diff_pair.gds")
        self.ly.write(gds)
        with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
            shutil.copyfileobj(f, z)
        spice = os.path.join(OUT, "cml_diff_pair.spice")
        # Dummies combine → W=3.0 [LVS]; ng omitted
        open(spice, "w").write(
            "* P2.7.4b cml_diff_pair — open-gate NMOS pair + end dummies\n"
            ".subckt cml_diff_pair d1 d2 g1 g2 s gnd\n"
            f"Mm1 d1 g1 s gnd sg13_lv_nmos w={W_PAIR} l=0.13u\n"
            f"Mm2 d2 g2 s gnd sg13_lv_nmos w={W_PAIR} l=0.13u\n"
            f"Mdum gnd gnd gnd gnd sg13_lv_nmos w=3.0u l=0.13u\n"
            ".ends\n"
        )
        open(os.path.join(OUT, "summary_build_cml_diff_pair.txt"), "w").write(
            "\n".join(self.log) + "\n")
        self.say(f"wrote {gds}")
        return 0


if __name__ == "__main__":
    sys.exit(Pair().build())
