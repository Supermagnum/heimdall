#!/usr/bin/env python3
"""P2.7.4b step 3b2a — standalone MOSFET tail cell [SCH].

Ports: drain (=latch s), nb_lo, gnd.
W=15 µm ng=5. Same method as cml_diff_pair (no M1 across S/D).
Prove alone before joining to cml_pair_loads.
"""
from __future__ import annotations

import gzip
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path[:0] = [
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/"
    "pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402, F401

DBU = 0.001
W_TAIL, NG = "15.0u", 5
W_DUM = "3.0u"


def um(x: float) -> int:
    return int(round(float(x) / DBU))


class Tail:
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
        t = (pya.Trans(pya.Trans.M90, um(x), um(y)) if mirror
             else pya.Trans(pya.Trans.R0, um(x), um(y)))
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
        top = self.ly.create_cell("cml_tail")
        nmos = self.pcell("nmos", {
            "w": W_TAIL, "l": "0.13u", "ng": NG, "m": 1,
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
        y0 = 0.0
        bb, t = self.place(top, nmos, -0.5 * (loc.left + loc.right), y0)
        self.say(f"tail {bb} W={W_TAIL} ng={NG}")

        gap = 5.0
        bb_dL, t_dL = self.place(top, dum, bb.left - gap - dloc.right, y0)
        bb_dR, t_dR = self.place(top, dum, bb.right + gap - dloc.left, y0)

        cols = self.m1_sd_cols(nmos, t)
        gates = self.poly_gates(nmos, t)
        at = self.activ_top(nmos, t)
        n_col = len(cols)
        assert n_col == NG + 1 and len(gates) == NG, (n_col, len(gates))
        drains = [cols[i] for i in range(0, n_col, 2)]
        sources = [cols[i] for i in range(1, n_col, 2)]
        self.say(f"even=D odd=S; nD={len(drains)} nS={len(sources)} [LVS]")

        # Internal S/D still exit SOUTH (never into gate Cont zone).
        # Face pins per 2026-11-20 plan: drain=N, gnd=W, nb_lo=E.
        y_s = bb.bottom - 3.0
        y_dr = y_s - 4.0
        y_gnd = y_dr - 5.0
        x_gL = min(bb_dL.left, bb.left) - 4.0
        x_gR = max(bb_dR.right, bb.right) + 4.0
        x_nb_e = x_gR + 3.0          # nb_lo east face (M1)
        x_d_e = x_gR + 6.0           # drain east escape (M2, outside nb_lo)
        x_drain = 0.0                # north-face drain pin X
        # Keep drain north strap well above nb_lo M2 (same-Y shorted drain|nb_lo)
        y_nb = at + 6.0
        y_north = max(at, bb.top, bb_dL.top, bb_dR.top, y_nb) + 5.0

        # Sources → gnd via M2 at y_s, then west face
        for c in sources:
            self.box(top, self.m1, c.left, y_s, c.right, c.bottom)
            self.place(top, vs12, 0.5 * (c.left + c.right) - 0.05, y_s)
        self.box(top, self.m2, sources[0].left - 0.3, y_s - 0.15,
                 sources[-1].right + 0.3, y_s + 0.55)
        self.box(top, self.m2, x_gL - 0.20, y_s - 0.15,
                 sources[-1].right + 0.3, y_s + 0.55)
        self.place(top, vs12, x_gL - 0.05, y_s)
        self.box(top, self.m1, x_gL - 0.20, y_gnd, x_gL + 0.20, y_s + 0.40)

        # Drains → south bus → east lane → north face (M2 outside body)
        for c in drains:
            self.box(top, self.m1, c.left, y_dr, c.right, c.bottom)
            self.place(top, vs12, 0.5 * (c.left + c.right) - 0.05, y_dr)
        self.box(top, self.m2, drains[0].left - 0.3, y_dr - 0.15,
                 x_d_e + 0.20, y_dr + 0.55)
        self.place(top, vs12, x_d_e - 0.05, y_dr)
        # vertical M2 on outer east lane up to north
        self.box(top, self.m2, x_d_e - 0.20, y_dr - 0.15,
                 x_d_e + 0.20, y_north + 0.40)
        self.place(top, vs12, x_d_e - 0.05, y_north)
        self.box(top, self.m2, min(x_drain, x_d_e) - 0.20, y_north - 0.15,
                 max(x_drain, x_d_e) + 0.20, y_north + 0.40)
        self.place(top, vs12, x_drain - 0.05, y_north)
        self.box(top, self.m1, x_drain - 0.25, y_north - 0.5,
                 x_drain + 0.25, y_north + 0.40)
        self.pin_m1(top, x_drain, y_north - 0.3, "drain")

        # Gate → nb_lo on EAST face (exit in device–left-dummy gap first)
        self.gate_poly_strap(top, gates, at)
        x_gexit = 0.5 * (bb.left + bb_dL.right)
        y_g = at + 4.0
        self.gate_m1_exit(top, gates, at, x_gexit, y_g)
        # M1 then M2 to east face; Y clear of drain north strap
        self.box(top, self.m1, x_gexit - 0.14, y_g, x_gexit + 0.14, y_nb + 0.20)
        self.place(top, vs12, x_gexit - 0.05, y_nb)
        self.box(top, self.m2, x_gexit - 0.20, y_nb - 0.15,
                 x_nb_e + 0.20, y_nb + 0.40)
        self.place(top, vs12, x_nb_e - 0.05, y_nb)
        self.box(top, self.m1, x_nb_e - 0.25, y_nb - 0.5,
                 x_nb_e + 0.25, y_nb + 0.40)
        self.pin_m1(top, x_nb_e, y_nb, "nb_lo")

        # Dummies → gnd (west)
        for bb_d, t_d, x_gd in ((bb_dL, t_dL, x_gL), (bb_dR, t_dR, x_gR)):
            dcols = self.m1_sd_cols(dum, t_d)
            dg = self.poly_gates(dum, t_d)
            at_d = self.activ_top(dum, t_d)
            y_dg = at_d + 2.0
            for c in dcols:
                self.box(top, self.m1, c.left, y_gnd + 1.0, c.right, c.bottom)
            if dcols:
                self.box(top, self.m1,
                         min(min(c.left for c in dcols), x_gd), y_gnd + 1.0,
                         max(max(c.right for c in dcols), x_gd), y_gnd + 1.35)
            if dg:
                self.gate_poly_strap(top, dg, at_d)
                self.gate_m1_exit(top, dg, at_d, x_gd, y_dg)
                self.box(top, self.m1, x_gd - 0.14, y_gnd + 1.0,
                         x_gd + 0.14, y_dg + 0.40)
            self.box(top, self.m1, x_gd - 0.20, y_gnd, x_gd + 0.20, y_gnd + 1.40)

        for x, y in ((x_gL - 0.4, bb_dL.bottom - 1.5),
                     (x_gR - 0.4, bb_dR.bottom - 1.5),
                     (x_gL - 0.4, y_gnd), (x_gR - 0.4, y_gnd)):
            self.place(top, ptap, x, y)
            self.box(top, self.m1, x, y, x + 0.78, y + 0.78)

        # Tie east gnd rail to west via M2 below body (no child-through)
        self.box(top, self.m1, x_gR - 0.20, y_gnd, x_gR + 0.20, y_s + 0.40)
        self.place(top, vs12, x_gL - 0.05, y_gnd)
        self.place(top, vs12, x_gR - 0.05, y_gnd)
        self.box(top, self.m2, x_gL - 0.20, y_gnd - 0.15,
                 x_gR + 0.20, y_gnd + 0.55)

        # gnd pin on WEST face
        y_gpin = 0.5 * (bb.bottom + bb.top)
        self.box(top, self.m1, x_gL - 0.20, min(y_gnd, y_gpin),
                 x_gL + 0.20, max(y_gnd + 0.50, y_gpin))
        self.box(top, self.m1, x_gL - 2.0, y_gpin - 0.25,
                 x_gL + 0.20, y_gpin + 0.25)
        self.pin_m1(top, x_gL - 1.5, y_gpin, "gnd")

        abb = top.bbox().to_dtype(self.ly.dbu)
        area = (abb.right - abb.left) * (abb.top - abb.bottom) * 1e-6
        self.say(f"bbox {abb}; area {area:.5f} mm² [GDS]")

        gds = os.path.join(OUT, "cml_tail.gds")
        self.ly.write(gds)
        with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
            shutil.copyfileobj(f, z)
        open(os.path.join(OUT, "cml_tail.spice"), "w").write(
            "* P2.7.4b cml_tail MOSFET [SCH]\n"
            ".subckt cml_tail drain nb_lo gnd\n"
            f"Mmt drain nb_lo gnd gnd sg13_lv_nmos w={W_TAIL} l=0.13u\n"
            "Mdum gnd gnd gnd gnd sg13_lv_nmos w=6.0u l=0.13u\n"
            ".ends\n"
        )
        open(os.path.join(OUT, "summary_build_cml_tail.txt"), "w").write(
            "\n".join(self.log) + "\n")
        self.say(f"WROTE {gds}")
        return 0


if __name__ == "__main__":
    raise SystemExit(Tail().build())
