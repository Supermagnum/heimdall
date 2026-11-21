#!/usr/bin/env python3
"""P2.7.4b — CMOS inverter leaf for cml_conv / lo_buffer [SCH].

Method from ota_vds + latch notes (spec/p27-layout-notes.md):
- PCell guardRingType=none; hand ptap (gnd) + ntap + NWell fill (vcv)
- even M1 cols = drain, odd = source
- Never M1 across Activ at a Y that hits another terminal
- Gate Cont on poly pads above Activ; shared a-gate N+P
- Face pins: a=W, y=E, vcv=N, gnd=S

Usage:
  python3 build_lo_inv.py --wn 2 --wp 4 --ng 1 --cell lo_inv_2_4
"""
from __future__ import annotations

import argparse
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


def um(x: float) -> int:
    return int(round(float(x) / DBU))


class Inv:
    def __init__(self, wn: float, wp: float, ng: int, cell: str):
        self.wn = wn
        self.wp = wp
        self.ng = ng
        self.cell = cell
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
        self.nw = self.ly.layer(31, 0)
        self.log = []

    def say(self, s=""):
        print(s, flush=True)
        self.log.append(s)

    def pcell(self, name, params):
        decl = self.lib_ly.pcell_declaration(name)
        return self.ly.add_pcell_variant(self.lib, decl.id(), params)

    def place(self, parent, cid, x, y):
        t = pya.Trans(pya.Trans.R0, um(x), um(y))
        parent.insert(pya.CellInstArray(cid, t))
        return self.ly.cell(cid).bbox().transformed(t).to_dtype(self.ly.dbu), t

    def box(self, cell, layer, x0, y0, x1, y1):
        cell.shapes(layer).insert(
            pya.DBox(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def m1_sd_cols(self, cid, trans):
        cell = self.ly.cell(cid)
        uniq = {}
        for s in cell.shapes(self.m1).each():
            if not s.is_box():
                continue
            b = s.bbox().transformed(trans).to_dtype(self.ly.dbu)
            if b.width() > 0.25 or b.height() < 0.3:
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
            if b.width() < 0.20 and b.height() > 0.4:
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

    def gate_contact(self, cell, gates, activ_top):
        """Cont on poly pads above Activ; return (y_pad1, gx0, gx1)."""
        y_pad0 = max(activ_top + 0.50, max(g.top for g in gates) + 0.30)
        y_pad1 = y_pad0 + 0.50
        gx0 = min(g.left for g in gates)
        gx1 = max(g.right for g in gates)
        for g in gates:
            gx = 0.5 * (g.left + g.right)
            half = 0.5 * (g.right - g.left)
            self.box(cell, self.poly, gx - half, g.top - 0.05,
                     gx + half, y_pad0 + 0.05)
            self.box(cell, self.cont, gx - 0.08, y_pad0 + 0.16,
                     gx + 0.08, y_pad0 + 0.32)
            self.box(cell, self.m1, gx - 0.08, y_pad0 + 0.16,
                     gx + 0.08, y_pad1 + 0.16)
        self.box(cell, self.poly, gx0 - 0.05, y_pad0, gx1 + 0.05, y_pad1)
        self.box(cell, self.m1, gx0 - 0.08, y_pad0 + 0.16,
                 gx1 + 0.08, y_pad1 + 0.16)
        return y_pad1, gx0, gx1

    def via12(self, cell, vs12, x, y):
        """M1–M2 via with 0.6 µm landings (avoids V1.b / M1.b) [OTA]."""
        self.box(cell, self.m1, x - 0.30, y - 0.30, x + 0.30, y + 0.30)
        self.box(cell, self.m2, x - 0.30, y - 0.30, x + 0.30, y + 0.30)
        self.place(cell, vs12, x, y)

    def build(self):
        top = self.ly.create_cell(self.cell)
        wn_s = f"{self.wn:g}u"
        wp_s = f"{self.wp:g}u"
        nmos = self.pcell("nmos", {
            "w": wn_s, "l": "0.13u", "ng": self.ng, "m": 1,
            "guardRingType": "none",
        })
        pmos = self.pcell("pmos", {
            "w": wp_s, "l": "0.13u", "ng": self.ng, "m": 1,
            "guardRingType": "none",
        })
        vs12 = self.pcell("via_stack", {
            "b_layer": "Metal1", "t_layer": "Metal2",
            "vn_columns": 1, "vn_rows": 1,
        })
        ptap = self.pcell("ptap1", {"w": "0.78u", "l": "0.78u"})
        ntap = self.pcell("ntap1", {"w": "0.78u", "l": "0.78u"})

        nloc = self.ly.cell(nmos).bbox().to_dtype(self.ly.dbu)
        ploc = self.ly.cell(pmos).bbox().to_dtype(self.ly.dbu)

        # Center both devices on X=0
        xn = -0.5 * (nloc.left + nloc.right)
        xp = -0.5 * (ploc.left + ploc.right)
        bb_n, tn = self.place(top, nmos, xn, 0.0)
        y_p = bb_n.top + 10.0  # extra gap so gate/drain buses clear
        bb_p, tp = self.place(top, pmos, xp, y_p - ploc.bottom)
        self.say(f"nmos {bb_n}; pmos {bb_p} [SCH W={wn_s}/{wp_s} ng={self.ng}]")

        cols_n = self.m1_sd_cols(nmos, tn)
        cols_p = self.m1_sd_cols(pmos, tp)
        gn = self.poly_gates(nmos, tn)
        gp = self.poly_gates(pmos, tp)
        at_n = self.activ_top(nmos, tn)
        at_p = self.activ_top(pmos, tp)
        n_col = len(cols_n)
        assert n_col == self.ng + 1, (n_col, self.ng)
        assert len(cols_p) == self.ng + 1, (len(cols_p), self.ng)
        assert len(gn) == self.ng and len(gp) == self.ng
        drn_n = [cols_n[i] for i in range(0, n_col, 2)]
        src_n = [cols_n[i] for i in range(1, n_col, 2)]
        drn_p = [cols_p[i] for i in range(0, len(cols_p), 2)]
        src_p = [cols_p[i] for i in range(1, len(cols_p), 2)]
        self.say(f"S/D order: even=D odd=S; nS={len(src_n)} nD={len(drn_n)} "
                 f"pS={len(src_p)} pD={len(drn_p)} [LVS]")

        # Bus Y: source via just below Activ; drain via further south; gnd lowest
        y_s_via = bb_n.bottom - 0.5
        y_dr_n = y_s_via - 2.5
        y_gnd = y_dr_n - 3.0
        y_out = bb_n.top + 4.0
        y_vcv = bb_p.top + 4.0

        # NMOS sources: short M1 stub + via EAST of each col → M2 → gnd
        # (M1 must not continue through drain-via Y) [LVS]
        x_s_n_via = bb_n.right + 2.0
        for c in src_n:
            vx = c.right + 0.55
            self.box(top, self.m1, c.left, y_s_via, c.right, c.bottom)
            self.box(top, self.m1, c.left, y_s_via, vx + 0.30, y_s_via + 0.40)
            self.via12(top, vs12, vx, y_s_via + 0.20)
        self.box(top, self.m2,
                 min(c.right for c in src_n) + 0.25, y_s_via,
                 x_s_n_via + 0.30, y_s_via + 0.40)
        self.via12(top, vs12, x_s_n_via, y_s_via + 0.20)
        self.box(top, self.m2, x_s_n_via - 0.30, y_gnd,
                 x_s_n_via + 0.30, y_s_via + 0.40)
        self.via12(top, vs12, x_s_n_via, y_gnd + 0.25)
        self.box(top, self.m1, x_s_n_via - 0.30, y_gnd,
                 x_s_n_via + 0.30, y_gnd + 0.50)

        # ptap west; M1 + M2 to gnd rail [LVS bulk=gnd]
        ptx = bb_n.left - 3.5
        pty = y_gnd
        self.place(top, ptap, ptx, pty)
        self.box(top, self.m1, ptx, pty, ptx + 0.78, pty + 0.78)
        self.box(top, self.m1, ptx, y_gnd, x_s_n_via + 0.30, y_gnd + 0.50)

        # NMOS drains: stub to y_dr_n; via WEST of each col (away from S);
        # join on M2 [LVS / M1.b]
        x_dr_via = bb_n.left - 2.0
        for c in drn_n:
            vx = c.left - 0.55
            self.box(top, self.m1, c.left, y_dr_n, c.right, c.bottom)
            self.box(top, self.m1, vx - 0.30, y_dr_n, c.right, y_dr_n + 0.40)
            self.via12(top, vs12, vx, y_dr_n + 0.20)
        self.box(top, self.m2,
                 x_dr_via - 0.30, y_dr_n,
                 max(c.left for c in drn_n) - 0.25, y_dr_n + 0.40)
        self.via12(top, vs12, x_dr_via, y_dr_n + 0.20)
        self.box(top, self.m2, x_dr_via - 0.30, y_dr_n,
                 x_dr_via + 0.30, y_out + 0.40)
        x_out_lo = x_dr_via - 0.30
        x_out_hi = x_dr_via + 0.30
        self.box(top, self.m2, x_out_lo, y_out, x_out_hi, y_out + 0.40)

        # PMOS drains: stub to y_out; via west of each col; M2 join
        x_dr_p = bb_p.left - 2.0
        for c in drn_p:
            vx = c.left - 0.55
            self.box(top, self.m1, c.left, y_out, c.right, c.bottom)
            self.box(top, self.m1, vx - 0.30, y_out, c.right, y_out + 0.40)
            self.via12(top, vs12, vx, y_out + 0.20)
        self.box(top, self.m2,
                 x_dr_p - 0.30, y_out,
                 max(c.left for c in drn_p) - 0.25, y_out + 0.40)
        self.via12(top, vs12, x_dr_p, y_out + 0.20)
        self.box(top, self.m2,
                 min(x_out_lo, x_dr_p - 0.30), y_out,
                 max(x_out_hi, x_dr_p + 0.30), y_out + 0.40)
        x_out_lo = min(x_out_lo, x_dr_p - 0.30)
        x_out_hi = max(x_out_hi, x_dr_p + 0.30)

        # PMOS sources: via EAST of each col (no M1 through D cols); M2→vcv
        y_s_p = 0.5 * (bb_p.bottom + bb_p.top)
        x_s_via = bb_p.right + 2.0
        for c in src_p:
            vx = c.right + 0.55
            self.box(top, self.m1, c.left, y_s_p - 0.20,
                     vx + 0.30, y_s_p + 0.20)
            self.via12(top, vs12, vx, y_s_p)
        self.box(top, self.m2,
                 min(c.right for c in src_p) + 0.25, y_s_p - 0.30,
                 x_s_via + 0.30, y_s_p + 0.30)
        self.via12(top, vs12, x_s_via, y_s_p)
        self.box(top, self.m2, x_s_via - 0.30, y_s_p - 0.30,
                 x_s_via + 0.30, y_vcv + 0.40)

        # Gates: Cont off active; west corridor; N↔P on M2
        y_pad_n, gx0n, gx1n = self.gate_contact(top, gn, at_n)
        y_pad_p, gx0p, gx1p = self.gate_contact(top, gp, at_p)
        x_a = min(bb_n.left, bb_p.left, ptx) - 2.0
        self.box(top, self.m1, x_a - 0.20, y_pad_n,
                 gx1n + 0.08, y_pad_n + 0.28)
        self.box(top, self.m1, x_a - 0.20, y_pad_p,
                 gx1p + 0.08, y_pad_p + 0.28)
        self.via12(top, vs12, x_a, y_pad_n + 0.14)
        self.via12(top, vs12, x_a, y_pad_p + 0.14)
        self.box(top, self.m2, x_a - 0.30, y_pad_n,
                 x_a + 0.30, y_pad_p + 0.40)

        # NWell fill + ntap → vcv on same M2 riser as PMOS source (one net)
        # ntap must sit inside NWell [LVS bulk]
        ntx = x_s_via + 0.8
        nty = y_s_p - 0.39
        self.box(top, self.nw, bb_p.left - 2.5, bb_p.bottom - 1.0,
                 ntx + 1.2, bb_p.top + 1.5)
        self.place(top, ntap, ntx, nty)
        self.box(top, self.m1, ntx, nty, ntx + 0.78, nty + 0.78)
        self.via12(top, vs12, ntx + 0.39, nty + 0.39)
        self.box(top, self.m2, x_s_via - 0.30, y_s_p - 0.30,
                 ntx + 0.68, y_s_p + 0.30)
        self.box(top, self.m2, ntx + 0.09, nty + 0.09,
                 ntx + 0.69, y_vcv + 0.40)

        # Out bus M2 across to east face; vcv/gnd vias at mid-X
        x_east = max(bb_n.right, bb_p.right, x_s_via + 0.30, ntx + 0.78) + 2.5
        self.box(top, self.m2, x_out_lo, y_out, x_east - 0.5, y_out + 0.40)
        self.via12(top, vs12, x_east - 1.0, y_out + 0.20)

        x_mid = 0.0
        # vcv: M2 from PMOS source via to mid, then via to M1 pin
        self.box(top, self.m2, min(x_mid, x_s_via) - 0.30, y_vcv,
                 max(x_mid, x_s_via) + 0.30, y_vcv + 0.40)
        self.via12(top, vs12, x_mid, y_vcv + 0.20)
        self.via12(top, vs12, x_mid, y_gnd + 0.25)
        self.box(top, self.m1, min(ptx, x_mid - 0.30, x_s_n_via - 0.30),
                 y_gnd, max(x_s_n_via + 0.30, x_mid + 0.30), y_gnd + 0.50)

        bb = top.bbox().to_dtype(self.ly.dbu)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "a", "W",
            x_a, y_pad_n + 0.14, bb=bb)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "y", "E",
            x_east - 1.0, y_out + 0.20, bb=bb)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "vcv", "N",
            x_mid, y_vcv + 0.20, bb=bb)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "gnd", "S",
            x_mid, y_gnd + 0.25, bb=bb)

        bb = top.bbox().to_dtype(self.ly.dbu)
        area = (bb.right - bb.left) * (bb.top - bb.bottom) * 1e-6
        self.say(f"inv bbox {bb}; area {area:.5f} mm² [GDS]")

        gds = os.path.join(OUT, f"{self.cell}.gds")
        self.ly.write(gds)
        with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
            shutil.copyfileobj(f, z)
        spice = os.path.join(OUT, f"{self.cell}.spice")
        open(spice, "w").write(
            f"* P2.7.4b {self.cell} CMOS inv [SCH]\n"
            f".subckt {self.cell} a y vcv gnd\n"
            f"Mxp y a vcv vcv sg13_lv_pmos w={wp_s} l=0.13u\n"
            f"Mxn y a gnd gnd sg13_lv_nmos w={wn_s} l=0.13u\n"
            ".ends\n"
        )
        open(os.path.join(OUT, f"summary_build_{self.cell}.txt"), "w").write(
            "\n".join(self.log) + "\n")
        self.say(f"wrote {gds}")
        return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wn", type=float, default=2.0)
    ap.add_argument("--wp", type=float, default=4.0)
    ap.add_argument("--ng", type=int, default=1)
    ap.add_argument("--cell", default="lo_inv_2_4")
    args = ap.parse_args()
    return Inv(args.wn, args.wp, args.ng, args.cell).build()


if __name__ == "__main__":
    raise SystemExit(main())
