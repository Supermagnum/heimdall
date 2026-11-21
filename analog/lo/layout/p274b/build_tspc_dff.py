#!/usr/bin/env python3
"""P2.7.4b — tspc_dff (lo_tspc size-2 + Q keepers) flat leaf [SCH].

Routing (lo_inv method, no stacked M3 on device X):
- PCell guardRingType=none; hand ptap/ntap + NWell
- even M1 col = drain, odd = source
- M1 stubs off Activ to side vias → M2; never M1 across gate
- One device row; M2 H tracks in a bay south of Activ (pitch 2 µm)
- Each net uses a dedicated M2 spine X east of the row (no shared-X risers)
- Face pins: d=W, q=E, ck=S, vdg=N, gnd=S [pin plan]
- 100 Meg a/b omitted (sim-only); keepers laid out [HAND]
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
CELL = "tspc_dff"
MW = 0.40
HW = 0.5 * MW
VIA_PITCH = 0.42
TRACK_PITCH = 2.0
SPINE_PITCH = 2.0

# (name, type, w_um, D, G, S, B)
DEVICES = [
    ("xp1", "pmos", 2.0, "nx1", "d", "vdg", "vdg"),
    ("xp2", "pmos", 2.0, "na", "ck", "nx1", "vdg"),
    ("xn1", "nmos", 1.0, "na", "d", "gnd", "gnd"),
    ("xp3", "pmos", 2.0, "nb", "ck", "vdg", "vdg"),
    ("xn2", "nmos", 1.0, "nb", "na", "nx2", "gnd"),
    ("xn3", "nmos", 1.0, "nx2", "ck", "gnd", "gnd"),
    ("xp4", "pmos", 2.0, "q", "nb", "vdg", "vdg"),
    ("xn4", "nmos", 1.0, "q", "ck", "nx3", "gnd"),
    ("xn5", "nmos", 1.0, "nx3", "nb", "gnd", "gnd"),
    ("xkq1p", "pmos", 0.3, "nkq", "q", "vdg", "vdg"),
    ("xkq1n", "nmos", 0.15, "nkq", "q", "gnd", "gnd"),
    ("xkq2p", "pmos", 0.3, "q", "nkq", "vdg", "vdg"),
    ("xkq2n", "nmos", 0.15, "q", "nkq", "gnd", "gnd"),
]

NET_ORDER = [
    "gnd", "ck", "d", "na", "nx1", "nx2", "nb", "nx3", "nkq", "q", "vdg",
]


def um(x):
    return int(round(float(x) / DBU))


class Tspc:
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
        self.m3 = self.ly.layer(30, 0)
        self.cont = self.ly.layer(6, 0)
        self.poly = self.ly.layer(5, 0)
        self.activ = self.ly.layer(1, 0)
        self.nw = self.ly.layer(31, 0)
        self._via_xy = []
        self._via23_xy = []
        self.log = []

    def say(self, s=""):
        print(s, flush=True)
        self.log.append(s)

    def pcell(self, name, params):
        return self.ly.add_pcell_variant(
            self.lib, self.lib_ly.pcell_declaration(name).id(), params)

    def place(self, parent, cid, x, y):
        t = pya.Trans(pya.Trans.R0, um(x), um(y))
        parent.insert(pya.CellInstArray(cid, t))
        return self.ly.cell(cid).bbox().transformed(t).to_dtype(self.ly.dbu), t

    def box(self, cell, layer, x0, y0, x1, y1):
        cell.shapes(layer).insert(
            pya.DBox(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)))

    def via12(self, cell, vs12, x, y):
        x = round(float(x), 2)
        y = round(float(y), 2)
        for _ in range(16):
            clash = False
            for (px, py) in self._via_xy:
                if abs(px - x) < 1e-6 and abs(py - y) < 1e-6:
                    clash = False
                    break
                if max(abs(px - x), abs(py - y)) < VIA_PITCH - 1e-9:
                    x = round(px + VIA_PITCH, 2)
                    clash = True
                    break
            if not clash:
                break
        if not any(abs(px - x) < 1e-6 and abs(py - y) < 1e-6
                   for (px, py) in self._via_xy):
            self._via_xy.append((x, y))
        self.box(cell, self.m1, x - 0.30, y - 0.30, x + 0.30, y + 0.30)
        self.box(cell, self.m2, x - 0.30, y - 0.30, x + 0.30, y + 0.30)
        self.place(cell, vs12, x, y)
        return x, y

    def m1_sd_cols(self, cid, trans):
        cell = self.ly.cell(cid)
        uniq = {}
        for s in cell.shapes(self.m1).each():
            if not s.is_box():
                continue
            b = s.bbox().transformed(trans).to_dtype(self.ly.dbu)
            if b.width() > 0.25 or b.height() < 0.12:
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
        top = None
        for s in self.ly.cell(cid).shapes(self.activ).each():
            if s.is_box():
                b = s.bbox().transformed(trans).to_dtype(self.ly.dbu)
                top = b.top if top is None else max(top, b.top)
        return top if top is not None else 0.0

    def gate_contact(self, cell, gates, activ_top):
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
        return y_pad1, 0.5 * (gx0 + gx1)

    def m2_h(self, cell, x0, y, x1):
        xa, xb = min(x0, x1), max(x0, x1)
        self.box(cell, self.m2, xa - HW, y - HW, xb + HW, y + HW)

    def m3_v(self, cell, x, y0, y1):
        ya, yb = min(y0, y1), max(y0, y1)
        self.box(cell, self.m3, x - HW, ya - HW, x + HW, yb + HW)

    def via23(self, cell, vs23, x, y):
        """M2–M3 via; pitch-bump on Via2 [V2.b]."""
        x = round(float(x), 2)
        y = round(float(y), 2)
        for _ in range(16):
            clash = False
            for (px, py) in self._via23_xy:
                if abs(px - x) < 1e-6 and abs(py - y) < 1e-6:
                    clash = False
                    break
                if max(abs(px - x), abs(py - y)) < VIA_PITCH - 1e-9:
                    x = round(px + VIA_PITCH, 2)
                    clash = True
                    break
            if not clash:
                break
        if not any(abs(px - x) < 1e-6 and abs(py - y) < 1e-6
                   for (px, py) in self._via23_xy):
            self._via23_xy.append((x, y))
        self.box(cell, self.m2, x - HW, y - HW, x + HW, y + HW)
        self.box(cell, self.m3, x - HW, y - HW, x + HW, y + HW)
        self.place(cell, vs23, x, y)
        return x, y

    def place_mos(self, top, vs12, kind, w, x0, y0, tag, y_dr, y_s):
        """Place MOS; stub D west / S east to vias at y_dr / y_s; gate north."""
        mos = self.pcell(kind, {
            "w": f"{w:g}u", "l": "0.13u", "ng": 1, "m": 1,
            "guardRingType": "none",
        })
        loc = self.ly.cell(mos).bbox().to_dtype(self.ly.dbu)
        ox = x0 - loc.left
        oy = y0 - loc.bottom
        bb, tr = self.place(top, mos, ox, oy)
        cols = self.m1_sd_cols(mos, tr)
        gates = self.poly_gates(mos, tr)
        assert len(cols) == 2, (tag, len(cols))
        assert len(gates) == 1, (tag, len(gates))
        drain, source = cols[0], cols[1]
        at = self.activ_top(mos, tr)
        y_pad, gx = self.gate_contact(top, gates, at)

        # Drain: M1 south of Activ to y_dr, via WEST of col [lo_inv / M1.b]
        dx = drain.left - 0.55
        self.box(top, self.m1, drain.left, y_dr, drain.right, drain.bottom)
        self.box(top, self.m1, dx - 0.30, y_dr, drain.right, y_dr + 0.40)
        dx, dy = self.via12(top, vs12, dx, y_dr + 0.20)

        # Source: via EAST of col at y_s (separate Y from drain) [LVS]
        sx = source.right + 0.55
        self.box(top, self.m1, source.left, y_s, source.right,
                 max(source.bottom, y_s + 0.40))
        self.box(top, self.m1, source.left, y_s, sx + 0.30, y_s + 0.40)
        sx, sy = self.via12(top, vs12, sx, y_s + 0.20)

        # Gate via on pad
        gy = y_pad + 0.14
        gx, gy = self.via12(top, vs12, gx, gy)

        return {
            "tag": tag, "kind": kind, "bb": bb,
            "d": (dx, dy), "s": (sx, sy), "g": (gx, gy),
        }

    def wire_to_spine(self, top, vs23, pts, spine_x, track_y, to_spine=True):
        """M3 vertical drop per terminal X → M2 track H (optional spine).

        M3 for verticals so drops do not short foreign M2 tracks they cross.
        Set to_spine=False to keep the track only over terminals (shorter C).
        """
        if not pts:
            return
        xs = [spine_x] if to_spine else []
        for (x, y) in pts:
            x1, y1 = self.via23(top, vs23, x, y)
            x2, y2 = self.via23(top, vs23, x1, track_y)
            self.m3_v(top, x1, y1, y2)
            if abs(x2 - x1) > 1e-6:
                self.m2_h(top, x1, track_y, x2)
            xs.extend([x1, x2])
        if len(xs) >= 2:
            self.m2_h(top, min(xs), track_y, max(xs))
        elif len(xs) == 1:
            self.m2_h(top, xs[0], track_y, xs[0])

    def wire_h_then_spine(self, top, vs23, pts, spine_x, track_y):
        """M2 H to spine X at pad Y, then single M3 drop on spine only.

        Use for taps whose X would collide with device D/G/S M3 columns.
        """
        if not pts:
            return
        for (x, y) in pts:
            self.m2_h(top, x, y, spine_x)
            self.via23(top, vs23, x, y)
        self.via23(top, vs23, spine_x, pts[0][1])
        y_top = pts[0][1]
        for (x, y) in pts[1:]:
            y_top = max(y_top, y)
            self.via23(top, vs23, spine_x, y)
            self.m2_h(top, spine_x, y_top, y)  # noop if same; keeps spine M2
        # one drop on spine from highest pad Y to track
        ys = [p[1] for p in pts]
        self.via23(top, vs23, spine_x, track_y)
        self.m3_v(top, spine_x, max(ys), track_y)
        self.m2_h(top, spine_x, track_y, spine_x)

    def build(self):
        top = self.ly.create_cell(CELL)
        vs12 = self.pcell("via_stack", {
            "b_layer": "Metal1", "t_layer": "Metal2",
            "vn_columns": 1, "vn_rows": 1})
        vs23 = self.pcell("via_stack", {
            "b_layer": "Metal2", "t_layer": "Metal3",
            "vn_columns": 1, "vn_rows": 1})
        ptap = self.pcell("ptap1", {"w": "0.78u", "l": "0.78u"})
        ntap = self.pcell("ntap1", {"w": "0.78u", "l": "0.78u"})

        pitch_x = 10.0
        placed = {}
        p_bbs, n_bbs = [], []
        # Drain via Y and source via Y below Activ (shared bay) [lo_inv]
        y_dr = -2.5
        y_s = -5.0
        for i, (name, kind, w, *_rest) in enumerate(DEVICES):
            x0 = i * pitch_x
            info = self.place_mos(top, vs12, kind, w, x0, 0.0, name, y_dr, y_s)
            placed[name] = info
            (p_bbs if kind == "pmos" else n_bbs).append(info["bb"])
            self.say(f"  {name} {kind} W={w} bb={info['bb']}")

        nets = {n: [] for n in NET_ORDER}
        for name, kind, w, nd, ng, ns, nb in DEVICES:
            info = placed[name]
            nets[nd].append(info["d"])
            nets[ng].append(info["g"])
            nets[ns].append(info["s"])

        # M2 track bay south of source vias; spines east of last device
        y_bay0 = y_s - 3.0
        track = {n: y_bay0 - TRACK_PITCH * i for i, n in enumerate(NET_ORDER)}
        x_right = max(b.right for b in p_bbs + n_bbs)
        spine0 = x_right + 4.0
        spine = {n: spine0 + SPINE_PITCH * i for i, n in enumerate(NET_ORDER)}

        # ck/d: no east spine spur (face pins leave from terminal span) [PEX-RC]
        no_spine = {"ck", "d"}
        for n in NET_ORDER:
            self.wire_to_spine(
                top, vs23, nets[n], spine[n], track[n],
                to_spine=(n not in no_spine))
            self.say(f"  net {n}: {len(nets[n])} terms "
                     f"spine_x={spine[n]:.1f} y={track[n]:.1f}")

        # Per-PMOS NWell (no mega-well over NMOS) [LVS].
        # ntap NORTH of each PMOS (not east — east M3 would merge with S/D
        # drops and short vdg to signal nets) [LVS].
        ntap_pts = []
        for bb in p_bbs:
            ntx = 0.5 * (bb.left + bb.right) - 0.39
            # Clear above gate Cont/via so M2 H to spine misses gate pads
            nty = bb.top + 3.0
            # NWell must cover ntap Activ (nty..nty+0.78) [LVS bulk]
            self.box(top, self.nw,
                     bb.left - 0.8, bb.bottom - 0.8,
                     bb.right + 0.8, nty + 1.2)
            self.place(top, ntap, ntx, nty)
            self.box(top, self.m1, ntx, nty, ntx + 0.78, nty + 0.78)
            vx, vy = self.via12(top, vs12, ntx + 0.39, nty + 0.39)
            ntap_pts.append((vx, vy))
        if ntap_pts:
            self.wire_h_then_spine(
                top, vs23, ntap_pts, spine["vdg"], track["vdg"])
        if n_bbs:
            ptx = min(b.left for b in n_bbs) - 3.5
            self.place(top, ptap, ptx, track["gnd"] - 0.39)
            self.box(top, self.m1, ptx, track["gnd"] - 0.39,
                     ptx + 0.78, track["gnd"] + 0.39)
            vx, vy = self.via12(top, vs12, ptx + 0.39, track["gnd"])
            self.m2_h(top, vx, track["gnd"], spine["gnd"])

        # Face pins: M2 to face via12 → M1 pin [pin plan]
        # d → W
        xd = min(b.left for b in p_bbs + n_bbs) - 3.0
        self.m2_h(top, xd, track["d"], spine["d"])
        self.via12(top, vs12, xd, track["d"])
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "d", "W",
            xd, track["d"], bb=top.bbox().to_dtype(self.ly.dbu))
        # q → E
        xq = spine["vdg"] + 3.0
        self.m2_h(top, spine["q"], track["q"], xq)
        self.via12(top, vs12, xq, track["q"])
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "q", "E",
            xq, track["q"], bb=top.bbox().to_dtype(self.ly.dbu))
        # ck → S from median ck terminal (no east spine spur) [PEX-RC]
        yc = track[NET_ORDER[-1]] - 3.0
        xck = sorted(x for x, _ in nets["ck"])[len(nets["ck"]) // 2]
        xck, _ = self.via23(top, vs23, xck, track["ck"])
        xck2, _ = self.via23(top, vs23, xck, yc)
        self.m3_v(top, xck, track["ck"], yc)
        if abs(xck2 - xck) > 1e-6:
            self.m2_h(top, xck, yc, xck2)
        self.via12(top, vs12, xck2, yc)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "ck", "S",
            xck2, yc, bb=top.bbox().to_dtype(self.ly.dbu))
        # gnd → S from spine (supply; C not clock-budgeted)
        xg, _ = self.via23(top, vs23, spine["gnd"], track["gnd"])
        xg2, _ = self.via23(top, vs23, xg, yc)
        self.m3_v(top, xg, track["gnd"], yc)
        if abs(xg2 - xg) > 1e-6:
            self.m2_h(top, xg, yc, xg2)
        self.via12(top, vs12, xg2, yc)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "gnd", "S",
            xg2, yc, bb=top.bbox().to_dtype(self.ly.dbu))
        # vdg → N: reuse spine via from ntap routing; only extend M3 if needed
        yv = max(p[1] for p in ntap_pts) + 2.0 if ntap_pts else (
            max(b.top for b in p_bbs + n_bbs) + 3.0)
        xv, _ = self.via23(top, vs23, spine["vdg"], track["vdg"])
        xv2, yv2 = self.via23(top, vs23, xv, yv)
        self.m3_v(top, xv, track["vdg"], yv2)
        if abs(xv2 - xv) > 1e-6:
            self.m2_h(top, xv, yv2, xv2)
        self.via12(top, vs12, xv2, yv2)
        PF.connect_and_pin_on_face(
            top, self.m1, self.m1pin, self.m1txt, "vdg", "N",
            xv2, yv2, bb=top.bbox().to_dtype(self.ly.dbu))

        bb = top.bbox().to_dtype(self.ly.dbu)
        area = (bb.right - bb.left) * (bb.top - bb.bottom) / 1e6
        gds = os.path.join(OUT, f"{CELL}.gds")
        self.ly.write(gds)
        with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
            shutil.copyfileobj(f, z)
        # M-device LVS spice (not X-subckt) [TOOL / lo_inv]
        lines = [
            "* tspc_dff LVS from lo_tspc [SCH]; rka/rkb omitted [HAND]\n",
            f".subckt {CELL} d ck q vdg gnd\n",
        ]
        for name, kind, w, nd, ng, ns, nb in DEVICES:
            model = "sg13_lv_pmos" if kind == "pmos" else "sg13_lv_nmos"
            lines.append(
                f"M{name} {nd} {ng} {ns} {nb} {model} w={w:g}u l=0.13u\n")
        lines.append(".ends\n")
        open(os.path.join(OUT, f"{CELL}.spice"), "w").writelines(lines)
        self.say(f"{CELL} bbox {bb}; area {area:.5f} mm2 [GDS]")
        open(os.path.join(OUT, f"summary_build_{CELL}.txt"), "w").write(
            "\n".join(self.log) + "\n")
        return area


def main():
    print(f"=== build {CELL} ===", flush=True)
    Tspc().build()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
