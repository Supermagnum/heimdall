#!/usr/bin/env python3
"""P2.7.2c — assemble vco_top from accepted block GDS + inter-block routing.

Follows spec/p27-layout-notes.md P2.7.2c routing plan (2026-11-17).
Net groups (--nets): place | power | ct | tail | tn_tp | vt | controls | all
DRC + both LVS after each group (full unique LVS = sign-off).
"""
from __future__ import annotations

import gzip
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
ROOT = os.path.abspath(os.path.join(HERE, ".."))
os.makedirs(OUT, exist_ok=True)

sys.path[:0] = [
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python",
    "/foss/pdks/ihp-sg13g2/libs.tech/klayout/python/pycell4klayout-api/source/python",
]
import pya  # noqa: E402
import sg13g2_pycell_lib  # noqa: E402

DBU = 0.001
# Fab GDS keeps the EM spiral (l2n0_em). LVS uses pin-only core (spiral stripped).
GDS_FAB = {
    "vco_core_tank": os.path.join(ROOT, "p272b", "out", "vco_core_tank.gds"),
    "vco_bank": os.path.join(ROOT, "p272b_bank", "out", "vco_bank.gds"),
    "tail_block": os.path.join(ROOT, "p272b_tail", "out", "tail_block.gds"),
    "vco_var": os.path.join(ROOT, "p272b_var", "out", "vco_var.gds"),
    "ampcal_det": os.path.join(ROOT, "p272b_det", "out", "ampcal_det.gds"),
}
GDS_LVS_CORE = os.path.join(ROOT, "p272b", "out", "vco_core_tank_lvs.gds")
GDS = dict(GDS_FAB)  # default load paths; core swapped to LVS when present
SPICE_LEAF = {
    "vco_core_tank": os.path.join(ROOT, "p272b", "out", "vco_core_tank.spice"),
    "vco_bank": os.path.join(ROOT, "p272b_bank", "out", "vco_bank.spice"),
    "tail_block": os.path.join(ROOT, "p272b_tail", "out", "tail_block.spice"),
    "vco_var": os.path.join(ROOT, "p272b_var", "out", "vco_var.spice"),
    "ampcal_det": os.path.join(ROOT, "p272b_det", "out", "ampcal_det.spice"),
}
# Top ports exported (sch vco_top; en/vthn included) [SCH]
TOP_PORTS = [
    "tp", "tn", "ct", "vt", "vdd", "gnd", "vbp", "vbp_tail", "cmp", "tail",
    "hold", "rep", "en", "vthn",
    "g0", "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10", "g11",
    "code0", "code1", "code2", "code3", "code4",
]
KEEP_PINS = {
    "vco_core_tank": {"tp", "tn", "tail", "ct", "gnd"},
    "vco_bank": {"tp", "tn", "vbp", "gnd"} | {f"g{i}" for i in range(12)},
    "tail_block": {
        "tail", "vdd", "gnd", "vbp_tail", "code0", "code1", "code2", "code3",
        "code4",
    },
    "vco_var": {"tp", "tn", "W", "vbp", "gnd"},
    "ampcal_det": {
        "tp", "tn", "ct", "vdd", "gnd", "cmp", "hold", "rep", "en", "vthn",
    },
}


def um(x):
    return int(round(x / DBU))


class Asm:
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
        self.tm1 = self.ly.layer(126, 0)
        self.tm1pin = self.ly.layer(126, 2)
        self.tm1txt = self.ly.layer(126, 25)
        self.tm2 = self.ly.layer(134, 0)
        self.tm2pin = self.ly.layer(134, 2)
        self.tm2txt = self.ly.layer(134, 25)
        self.log = []
        self.place_info = {}  # name -> {ox, oy, pins_island, bb}

    def say(self, s=""):
        print(s, flush=True)
        self.log.append(s)

    def pcell(self, name, params):
        return self.ly.add_pcell_variant(
            self.lib, self.lib_ly.pcell_declaration(name).id(), params)

    def place_ll(self, parent, cid, x, y):
        """Place so child bbox lower-left is at (x,y) µm."""
        bb0 = self.ly.cell(cid).bbox().to_dtype(self.ly.dbu)
        tr = pya.DTrans(pya.DVector(x - bb0.left, y - bb0.bottom))
        parent.insert(pya.DCellInstArray(cid, tr))
        return bb0.transformed(tr), tr

    def load_child(self, name):
        # Core + tank: prefer pin-only LVS GDS so spiral cannot short ct/tn/tp
        # in extraction; fab spiral is re-added when writing fab top [TOOL].
        if name == "vco_core_tank" and os.path.exists(GDS_LVS_CORE):
            gds = GDS_LVS_CORE
            self.say(f"core+tank load LVS pin-only {gds} [TOOL]")
        else:
            gds = GDS[name]
        if not os.path.exists(gds) and os.path.exists(gds + ".gz"):
            with gzip.open(gds + ".gz", "rb") as z, open(gds, "wb") as f:
                shutil.copyfileobj(z, f)
            self.say(f"unzipped {gds}.gz → {gds}")
        if not os.path.exists(gds):
            raise SystemExit(f"missing {gds} (and {gds}.gz)")
        src_ly = pya.Layout()
        src_ly.read(gds)
        src = src_ly.cell(name) or src_ly.top_cell()
        cell = self.ly.create_cell(name + "_j")
        cell.copy_tree(src)
        pins = {}
        for L, D in ((8, 25), (126, 25)):
            lyr = src_ly.layer(L, D)
            for s in src.shapes(lyr).each():
                if s.is_text():
                    t = s.text
                    pins[t.string] = (
                        t.trans.disp.x * src_ly.dbu,
                        t.trans.disp.y * src_ly.dbu,
                    )
        # Also hierarchical texts for bank g*
        for li in src_ly.layer_indexes():
            info = src_ly.get_info(li)
            if info.datatype != 25:
                continue
            for sh in src.begin_shapes_rec(li).each():
                if not sh.shape().is_text():
                    continue
                t = sh.shape().text
                nm = t.string
                if nm in pins:
                    continue
                if nm.startswith("g") or nm.startswith("bb") or nm in (
                    "tp", "tn", "vbp", "gnd", "W", "ct", "tail",
                ):
                    tp = sh.trans() * t
                    pins[nm] = (tp.x * src_ly.dbu, tp.y * src_ly.dbu)
        keep = KEEP_PINS.get(name, set())
        # Drop non-keeper texts from pin map (e.g. stray vdd on core LVS GDS)
        # so TOP_PORTS logging cannot invent island pins [TOOL LVS].
        pins = {k: v for k, v in pins.items() if k in keep}
        for L, D in ((8, 25), (8, 2), (126, 25), (126, 2)):
            lyr = self.ly.layer(L, D)
            # clear all pin texts/markers; re-add keepers after place via top
            cell.shapes(lyr).clear()
        bb = cell.bbox().to_dtype(self.ly.dbu)
        # Accepted vco_core_tank fab GDS still has six TM1.b notches (1.30 µm < 1.64)
        # south of the tank pins [TOOL DRC on place]. Fill here so the island can be
        # DRC-clean without re-opening the 2b core job. [GDS]
        if name == "vco_core_tank":
            tm1 = self.ly.layer(126, 0)
            for y0, y1 in ((-86.79, -85.49), (-89.79, -88.49), (-92.79, -91.49)):
                for x0, x1 in ((-25.23, -16.38), (16.38, 25.23)):
                    cell.shapes(tm1).insert(pya.DBox(x0, y0, x1, y1))
            self.say("patched vco_core_tank TM1.b notches (6 fills) [GDS]")
        return cell.cell_index(), pins, bb, keep

    def pin_tm1(self, cell, x, y, name):
        # TM1.a min width 1.64 µm — pin pad must be ≥ 2.0 [DS/TOOL]
        cell.shapes(self.tm1).insert(pya.DBox(x - 1.0, y - 1.0, x + 1.0, y + 1.0))
        cell.shapes(self.tm1pin).insert(pya.DBox(x - 0.8, y - 0.8, x + 0.8, y + 0.8))
        cell.shapes(self.tm1txt).insert(pya.DText(name, pya.DTrans(x, y)))

    def pin_m1(self, cell, x, y, name):
        cell.shapes(self.m1).insert(pya.DBox(x - 0.25, y - 0.25, x + 0.25, y + 0.25))
        cell.shapes(self.m1pin).insert(pya.DBox(x - 0.2, y - 0.2, x + 0.2, y + 0.2))
        cell.shapes(self.m1txt).insert(pya.DText(name, pya.DTrans(x, y)))

    def strap_m2(self, cell, x0, y0, x1, y1, w=2.0):
        """Axis-aligned M2 rectangle (horizontal or vertical segment)."""
        if abs(y1 - y0) < 1e-9:  # horizontal
            y = y0
            cell.shapes(self.m2).insert(
                pya.DBox(min(x0, x1), y - w / 2, max(x0, x1), y + w / 2))
        else:  # treat as H-only plan: use M3 for vertical
            x = x0
            cell.shapes(self.m3).insert(
                pya.DBox(x - w / 2, min(y0, y1), x + w / 2, max(y0, y1)))

    def strap_tm1(self, cell, x0, y0, x1, y1, w=4.0):
        if abs(y1 - y0) < 1e-9:
            y = y0
            cell.shapes(self.tm1).insert(
                pya.DBox(min(x0, x1), y - w / 2, max(x0, x1), y + w / 2))
        else:
            x = x0
            cell.shapes(self.tm1).insert(
                pya.DBox(x - w / 2, min(y0, y1), x + w / 2, max(y0, y1)))

    def via12(self):
        return self.pcell("via_stack", {
            "b_layer": "Metal1", "t_layer": "Metal2",
            "vn_columns": 1, "vn_rows": 1,
        })

    def via23(self):
        return self.pcell("via_stack", {
            "b_layer": "Metal2", "t_layer": "Metal3",
            "vn_columns": 1, "vn_rows": 1,
        })

    def via2t(self):
        return self.pcell("via_stack", {
            "b_layer": "Metal2", "t_layer": "TopMetal1",
            "vn_columns": 1, "vn_rows": 1,
        })

    def via1t(self):
        return self.pcell("via_stack", {
            "b_layer": "Metal1", "t_layer": "TopMetal1",
            "vn_columns": 1, "vn_rows": 1,
        })

    def via_tm12(self):
        return self.pcell("via_stack", {
            "b_layer": "TopMetal1", "t_layer": "TopMetal2",
            "vn_columns": 2, "vn_rows": 2,
        })

    def build(self, routed):
        c = self.ly.create_cell("vco_top")
        vs12 = self.via12()
        vs23 = self.via23()
        vs2t = self.via2t()
        vs1t = self.via1t()
        vs_tm12 = self.via_tm12()

        kids = {}
        for name in ("vco_bank", "vco_core_tank", "tail_block", "vco_var",
                     "ampcal_det"):
            cid, pins, bb, keep = self.load_child(name)
            kids[name] = {"cid": cid, "pins": pins, "bb0": bb, "keep": keep}

        # Tail next to core east pin; var/det north of core so the 4 mA line
        # stays short (decisions 2026-11-17). Bank south X-aligned; tn/tp bank
        # join = V stub only. [HAND / spec/p27-layout-notes.md]
        gap = 8.0
        core_pins0 = kids["vco_core_tank"]["pins"]
        bank_pins0 = kids["vco_bank"]["pins"]
        var_pins0 = kids["vco_var"]["pins"]
        det_pins0 = kids["ampcal_det"]["pins"]
        tail_pins0 = kids["tail_block"]["pins"]
        core_bb0 = kids["vco_core_tank"]["bb0"]
        bank_bb0 = kids["vco_bank"]["bb0"]
        var_bb0 = kids["vco_var"]["bb0"]
        det_bb0 = kids["ampcal_det"]["bb0"]
        tail_bb0 = kids["tail_block"]["bb0"]

        bank_h = bank_bb0.top - bank_bb0.bottom
        core_ll = (0.0, bank_h + gap)
        # core.tp island x before bank place (core at x=0)
        core_tp_x = core_pins0["tp"][0] + (core_ll[0] - core_bb0.left)
        bank_ll = (
            core_tp_x - bank_pins0["tp"][0] + bank_bb0.left,
            0.0,
        )
        bank_bb, bank_tr = self.place_ll(
            c, kids["vco_bank"]["cid"], bank_ll[0], bank_ll[1])
        core_bb, core_tr = self.place_ll(
            c, kids["vco_core_tank"]["cid"], core_ll[0], core_ll[1])
        core_tn_y = (
            core_pins0["tn"][1] + (core_ll[1] - core_bb0.bottom)
        )
        core_tail_xy = (
            core_pins0["tail"][0] + (core_ll[0] - core_bb0.left),
            core_pins0["tail"][1] + (core_ll[1] - core_bb0.bottom),
        )
        # Short east gap for the 4 mA M3 tail line (L ≤ ≈150 µm) [HAND/PDK]
        east_gap = 8.0
        # Tail west-face pin near core.tail Y; keep above bank (overlap with
        # bank TM1 → TM1.b at place) [TOOL DRC].
        tail_pin0 = tail_pins0["tail"]
        tail_y_pin = core_tail_xy[1] - (tail_pin0[1] - tail_bb0.bottom)
        tail_y_min = bank_bb.top + gap
        tail_ll = (
            core_bb.right + east_gap,
            max(tail_y_pin, tail_y_min),
        )
        tail_bb, tail_tr = self.place_ll(
            c, kids["tail_block"]["cid"], tail_ll[0], tail_ll[1])
        # Var north of core (X-align tn). Det west of var and raised so the
        # core↔var alley stays clear for the ct jog (≥1.64 µm to both TM1
        # edges) [TOOL DRC TM1.b / decisions detector-away].
        var_ll = (
            (core_pins0["tn"][0] + (core_ll[0] - core_bb0.left))
            - var_pins0["tn"][0] + var_bb0.left,
            core_bb.top + gap,
        )
        var_bb, var_tr = self.place_ll(
            c, kids["vco_var"]["cid"], var_ll[0], var_ll[1])
        var_tn_y = var_pins0["tn"][1] + (var_ll[1] - var_bb0.bottom)
        # Raise ≥ 20 µm vs tn-align so det.bottom clears y_jog under var
        det_y_aligned = var_tn_y - det_pins0["tn"][1] + det_bb0.bottom
        det_ll = (
            var_bb.left - gap - (det_bb0.right - det_bb0.left),
            max(det_y_aligned, var_bb.bottom + 20.0),
        )
        det_bb, det_tr = self.place_ll(
            c, kids["ampcal_det"]["cid"], det_ll[0], det_ll[1])
        self.say(
            f"tail-next pack LL bank={bank_ll} core={core_ll} "
            f"tail={tail_ll} var={var_ll} det={det_ll} "
            f"east_gap={east_gap} [HAND]"
        )

        def island_pins(name, tr):
            out = {}
            for k, (x, y) in kids[name]["pins"].items():
                p = tr * pya.DPoint(x, y)
                out[k] = (p.x, p.y)
            return out

        self.place_info = {
            "vco_bank": {"bb": bank_bb, "pins": island_pins("vco_bank", bank_tr)},
            "vco_core_tank": {
                "bb": core_bb, "pins": island_pins("vco_core_tank", core_tr),
            },
            "tail_block": {
                "bb": tail_bb, "pins": island_pins("tail_block", tail_tr),
            },
            "vco_var": {"bb": var_bb, "pins": island_pins("vco_var", var_tr)},
            "ampcal_det": {
                "bb": det_bb, "pins": island_pins("ampcal_det", det_tr),
            },
        }
        for nm, info in self.place_info.items():
            self.say(f"place {nm} bb={info['bb']}")
            for pk in sorted(info["pins"]):
                if pk in KEEP_PINS.get(nm, set()) or pk in TOP_PORTS or pk == "W":
                    self.say(f"  pin {pk} @ ({info['pins'][pk][0]:.2f},"
                             f"{info['pins'][pk][1]:.2f})")

        outline = c.bbox().to_dtype(self.ly.dbu)
        self.say(
            f"outline bbox={outline} area="
            f"{outline.width()*outline.height()*1e-6:.4f} mm2 [GDS]"
        )

        def export_pin(net, x, y, layer="m1"):
            if layer == "tm1":
                self.pin_tm1(c, x, y, net)
            else:
                self.pin_m1(c, x, y, net)

        cp = self.place_info["vco_core_tank"]["pins"]
        bp = self.place_info["vco_bank"]["pins"]
        tpins = self.place_info["tail_block"]["pins"]
        vp = self.place_info["vco_var"]["pins"]
        dp = self.place_info["ampcal_det"]["pins"]

        if "place" in routed or True:
            if "tp" in cp:
                export_pin("tp", *cp["tp"], "tm1")
            if "tn" in cp:
                export_pin("tn", *cp["tn"], "tm1")
            if "ct" in cp:
                export_pin("ct", *cp["ct"], "tm1")
            if "tail" in cp:
                export_pin("tail", *cp["tail"], "m1")
            if "gnd" in cp:
                export_pin("gnd", *cp["gnd"], "m1")
            if "W" in vp:
                export_pin("vt", *vp["W"], "m1")
            if "vbp" in bp:
                export_pin("vbp", *bp["vbp"], "m1")
            if "vbp_tail" in tpins:
                export_pin("vbp_tail", *tpins["vbp_tail"], "m1")
            if "vdd" in tpins:
                export_pin("vdd", *tpins["vdd"], "m1")
            for i in range(12):
                g = f"g{i}"
                if g in bp:
                    export_pin(g, *bp[g], "m1")
            for i in range(5):
                g = f"code{i}"
                if g in tpins:
                    export_pin(g, *tpins[g], "m1")
            for nm in ("cmp", "hold", "rep", "en", "vthn"):
                if nm in dp:
                    export_pin(nm, *dp[nm], "m1")

        # ---- power ----
        if "power" in routed:
            tops = [info["bb"].top for info in self.place_info.values()]
            bots = [info["bb"].bottom for info in self.place_info.values()]
            lefts = [info["bb"].left for info in self.place_info.values()]
            rights = [info["bb"].right for info in self.place_info.values()]
            # +10 leaves room for tail north M2 ring at max(tops)+2 without
            # overlapping this spine (was +4 → tail|vdd short) [TOOL LVS]
            y_vdd = max(tops) + 10.0
            y_gnd = min(bots) - 4.0
            x0, x1 = min(lefts) - 2.0, max(rights) + 2.0
            w_pwr = 4.0
            c.shapes(self.m2).insert(
                pya.DBox(x0, y_vdd - w_pwr / 2, x1, y_vdd + w_pwr / 2))
            c.shapes(self.m2).insert(
                pya.DBox(x0, y_gnd - w_pwr / 2, x1, y_gnd + w_pwr / 2))
            self.say(f"power spines y_vdd={y_vdd:.2f} y_gnd={y_gnd:.2f} "
                     f"x=[{x0:.1f},{x1:.1f}] w={w_pwr} [HAND]")

            # Fixed unique M3 columns (avoid tail@256 shorting gnd@256) [TOOL LVS]
            # ampcal_det.vdd: short stub east of pin only — a column at det.right
            # made an M2 H-pad (pad=4) span x≈209→340 at y≈383 and short child
            # cmp Via1/M2 at (270,385) into vdd [TOOL LVS net tracer].
            x_col = {
                ("tail_block", "vdd"): tail_bb.right + 3.0,
                # gnd pin is SW of the cell; column stays south of the short
                # east-gap M3 tail bus (do not use core.right−8 — that sat in
                # the core) [HAND / TOOL LVS].
                ("tail_block", "gnd"): tail_bb.left - 4.0,
                ("ampcal_det", "vdd"): (
                    dp["vdd"][0] + 8.0 if "vdd" in dp else det_bb.left - 8.0),
                ("ampcal_det", "gnd"): det_bb.left - 4.0,
                ("vco_core_tank", "gnd"): core_bb.left - 10.0,
                ("vco_bank", "gnd"): bank_bb.right + 3.0,
                ("vco_var", "gnd"): var_bb.right + 3.0,
            }
            m2_ready = {
                ("ampcal_det", "vdd"), ("ampcal_det", "gnd"),
                ("tail_block", "gnd"),
            }

            def drop_power(px, py, rail_y, block, net):
                # M2 pads oversized to merge into child pin M2 (M2.b ≥ 0.21) [TOOL]
                # Keep pad height small on ampcal_det.vdd so it cannot cover cmp.
                # tail_block.vdd: do NOT extend M2 west of the pin into the cell —
                # child gnd M2 plane ends ~0.5 µm west of the vdd pin M2; a fat
                # pad (px−2 … xc) shorted vdd→gnd [TOOL LVS; POWER_DROPS probe].
                xc = x_col[(block, net)]
                m3w = 2.0
                if (block, net) == ("ampcal_det", "vdd"):
                    pad = 2.0
                else:
                    pad = 4.0
                if (block, net) == ("tail_block", "vdd") and xc >= px:
                    # M1 pin→column only; M2/Via2 only at column east of cell.
                    # Child has a vertical gnd M2 at x≈387 crossing y_vdd pin; any
                    # parent M2 over the cell east edge shorts vdd→gnd [TOOL LVS].
                    c.shapes(self.m1).insert(
                        pya.DBox(px - 0.25, py - 0.8, xc + 0.25, py + 0.8))
                    c.shapes(self.m2).insert(
                        pya.DBox(xc - 2.0, py - 1.0, xc + 2.0, py + 1.0))
                    c.insert(pya.DCellInstArray(
                        vs12, pya.DTrans(pya.DVector(xc, py))))
                else:
                    c.shapes(self.m2).insert(
                        pya.DBox(min(px, xc) - 2.0, py - pad,
                                 max(px, xc) + 2.0, py + pad))
                    c.shapes(self.m2).insert(
                        pya.DBox(px - 3.0, py - pad, px + 3.0, py + pad))
                    if (block, net) not in m2_ready:
                        c.shapes(self.m1).insert(
                            pya.DBox(min(px, xc) - 0.2, py - 0.8,
                                     max(px, xc) + 0.2, py + 0.8))
                        c.insert(pya.DCellInstArray(
                            vs12, pya.DTrans(pya.DVector(xc, py))))
                c.shapes(self.m3).insert(
                    pya.DBox(xc - m3w / 2, min(py, rail_y),
                             xc + m3w / 2, max(py, rail_y)))
                c.shapes(self.m2).insert(
                    pya.DBox(xc - 2.0, rail_y - 2.0, xc + 2.0, rail_y + 2.0))
                c.insert(pya.DCellInstArray(
                    vs23, pya.DTrans(pya.DVector(xc, py))))
                c.insert(pya.DCellInstArray(
                    vs23, pya.DTrans(pya.DVector(xc, rail_y))))
                self.say(f"power {block}.{net} col x={xc:.1f}")

            # Optional filter for short debug: POWER_DROPS=all|none|vdd|gnd|block.net,...
            drop_filter = os.environ.get("POWER_DROPS", "all").strip().lower()
            self.say(f"power drop filter={drop_filter}")

            def want(block, net):
                if drop_filter in ("all", ""):
                    return True
                if drop_filter == "none":
                    return False
                if drop_filter == net:
                    return True
                return f"{block}.{net}" in {
                    x.strip() for x in drop_filter.split(",")
                }

            for src, blk in (
                (tpins, "tail_block"),
                (dp, "ampcal_det"),
            ):
                if "vdd" in src and want(blk, "vdd"):
                    drop_power(src["vdd"][0], src["vdd"][1], y_vdd, blk, "vdd")
            for src, blk in (
                (cp, "vco_core_tank"),
                (bp, "vco_bank"),
                (tpins, "tail_block"),
                (vp, "vco_var"),
                (dp, "ampcal_det"),
            ):
                if "gnd" in src and want(blk, "gnd"):
                    drop_power(src["gnd"][0], src["gnd"][1], y_gnd, blk, "gnd")
            if want("_top", "vdd"):
                export_pin("vdd", x1 - 2.0, y_vdd, "m1")
                c.insert(pya.DCellInstArray(
                    vs12, pya.DTrans(pya.DVector(x1 - 2.0, y_vdd))))
            # Surgical M2.b notch fills (drawing↔filler / pin edge) [TOOL DRC]
            # Dropped former ampcal east fill (325.5,385.5)–(328.5,386.5): it sat
            # on the long vdd H-pad that shorted cmp and would orphan-short child M2.
            if drop_filter == "all":
                for box in (
                    (10.5, 6.4, 12.0, 7.0),         # bank-area filler notch
                ):
                    c.shapes(self.m2).insert(pya.DBox(*box))
                self.say("power M2.b notch fills applied [TOOL]")

        # ---- ct: TM2 west of inductor spiral (l2n0 TM2 ≈ x∈[-58.6,195.4],
        # y∈[461,715] on fab GDS) [GDS/TOOL]. TM1 alley hit tn/tp; M3 hit power.
        if "ct" in routed and "ct" in cp:
            cx, cy = cp["ct"]
            w_ct = 2.0  # TM2.a min width [DS]
            # Keep ≥2 µm clear of inductor TM2 left edge −58.61 [DS TM2.b]
            x_west = min(det_bb.left - 4.0, -58.61 - 4.0)
            y_ct = max(
                det_bb.top + 4.0,
                715.26 + 4.0,  # above inductor TM2 [GDS]
            )
            x_ct_end = x_west  # port on west corridor, not over spiral

            def tm2_strap(x0, y0, x1, y1):
                c.shapes(self.tm2).insert(
                    pya.DBox(min(x0, x1) - w_ct / 2, min(y0, y1) - w_ct / 2,
                             max(x0, x1) + w_ct / 2, max(y0, y1) + w_ct / 2))

            def tm2_node(px, py):
                c.shapes(self.tm2).insert(
                    pya.DBox(px - w_ct / 2, py - w_ct / 2,
                             px + w_ct / 2, py + w_ct / 2))
                c.shapes(self.tm1).insert(
                    pya.DBox(px - w_ct / 2, py - w_ct / 2,
                             px + w_ct / 2, py + w_ct / 2))
                c.insert(pya.DCellInstArray(
                    vs_tm12, pya.DTrans(pya.DVector(px, py))))

            # H west below inductor TM2 (y<461), then V north in west corridor
            tm2_node(cx, cy)
            tm2_strap(cx, cy, x_west, cy)
            tm2_node(x_west, cy)
            tm2_strap(x_west, cy, x_west, y_ct)
            tm2_node(x_west, y_ct)
            export_pin("ct", x_ct_end, y_ct, "tm1")
            if "ct" in dp:
                dx, dy = dp["ct"]
                # Drop on TM2 to pin Y west of spiral; TM1 stub east to pin
                # (det.ct x≈−53 is west of inductor TM1 left 34.2) [GDS]
                tm2_strap(x_west, y_ct, x_west, dy)
                tm2_node(x_west, dy)
                # TM1 only for the last stub into the detector pin
                c.shapes(self.tm1).insert(
                    pya.DBox(min(x_west, dx) - 1.0, dy - 1.0,
                             max(x_west, dx) + 1.0, dy + 1.0))
                c.shapes(self.m1).insert(
                    pya.DBox(dx - 0.8, dy - 0.8, dx + 0.8, dy + 0.8))
                c.insert(pya.DCellInstArray(
                    vs1t, pya.DTrans(pya.DVector(dx, dy))))
                self.say(
                    f"ct TM2 west-of-spiral x_west={x_west:.1f} "
                    f"y_ct={y_ct:.1f} → det.ct ({dx:.1f},{dy:.1f}) [TOOL/GDS]"
                )
            self.say(f"ct TM2/TM1 port y={y_ct:.2f} → ({x_ct_end:.1f},{y_ct:.1f})")

        # ---- tail: short M3 in the core–tail east gap (4 mA) ----
        # Long north ring rejected (IR / J / C) [decisions 2026-11-17]. Face pin
        # on tail_block west; own corridor; w from JMAX @125 °C [PDK/HAND].
        if "tail" in routed and "tail" in cp and "tail" in tpins:
            x0, y0 = cp["tail"]
            x1, y1 = tpins["tail"]
            w = 4.0  # ≥ 2.9 µm @125 °C / 4 mA [DS JMAX 0.7× HAND]
            # Lift just east of core (gap), not over child metal [TOOL LVS]
            x_lift = core_bb.right + 3.0
            pitch = 0.50
            n_via_r, n_via_c = 8, 2  # ≥15 vias @125 °C [DS/HAND]
            # M2 from core.tail pin to lift column
            c.shapes(self.m2).insert(
                pya.DBox(min(x0, x_lift) - 0.3, y0 - 1.0,
                         max(x0, x_lift) + 0.3, y0 + 1.0))
            c.shapes(self.m2).insert(
                pya.DBox(x_lift - 1.0, y0 - 2.2, x_lift + 1.0, y0 + 2.2))
            c.shapes(self.m3).insert(
                pya.DBox(x_lift - 1.0, y0 - 2.2, x_lift + 1.0, y0 + 2.2))
            for i in range(n_via_r):
                for j in range(n_via_c):
                    vx = x_lift - 0.25 + j * pitch
                    vy = y0 - 1.75 + i * pitch
                    c.insert(pya.DCellInstArray(
                        vs23, pya.DTrans(pya.DVector(vx, vy))))
            # M3 H in the gap to the west-face pin (may include small V jog)
            y_bus = 0.5 * (y0 + y1)
            c.shapes(self.m3).insert(
                pya.DBox(x_lift - w / 2, y_bus - w / 2,
                         x1 + 1.0, y_bus + w / 2))
            if abs(y1 - y0) > 0.05:
                c.shapes(self.m3).insert(
                    pya.DBox(x_lift - w / 2, min(y0, y_bus) - w / 2,
                             x_lift + w / 2, max(y0, y_bus) + w / 2))
                c.shapes(self.m3).insert(
                    pya.DBox(x1 - w / 2, min(y1, y_bus) - w / 2,
                             x1 + w / 2, max(y1, y_bus) + w / 2))
            # Land on face M3/M2/M1 pad (child already has via array)
            c.shapes(self.m3).insert(
                pya.DBox(x1 - 1.0, y1 - 2.2, x1 + 1.2, y1 + 2.2))
            L_tot = abs(x_lift - x0) + abs(x1 - x_lift) + abs(y1 - y0)
            # R @25 °C typ; ×1.35 @125 °C [DS TC1 / HAND]
            r_25 = 0.088 * L_tot / w
            r_125 = r_25 * 1.35
            j_line = 4.0 / w  # mA/µm
            C_tail = L_tot * 0.10  # [HAND] C'≈0.10 fF/µm M3
            self.say(
                f"tail short M3 x_lift={x_lift:.1f} w={w:.1f} µm "
                f"L={L_tot:.1f} µm R25={r_25:.2f} Ω R125={r_125:.2f} Ω "
                f"J={j_line:.2f} mA/µm C≈{C_tail:.1f} fF "
                f"pins=({x0:.1f},{y0:.1f})→({x1:.1f},{y1:.1f}) [HAND/PDK/GDS]"
            )

        # ---- tn / tp: wide tank path to var; thin taps to detector ----
        # decisions 2026-11-17: var next to tank (wide); det further (thin).
        # Never H through det/var at pin Y [TOOL LVS].
        if "tn_tp" in routed:
            tank_y = cp["tn"][1]
            w_tank = 2.0
            w_tap = 0.5
            hw = w_tank / 2
            ht = w_tap / 2
            ct_x = cp["ct"][0] if "ct" in cp else tank_y
            ct_x_clear = ct_x + 4.0 + 1.64 + hw
            track_tank = {"tn": tank_y + 4.0, "tp": tank_y - 5.0}
            # Tap alley south of det and below var.tp (tn jogs above) [TOOL]
            vy_tp0 = vp["tp"][1] if "tp" in vp else det_bb.bottom
            y_tap_base = min(det_bb.bottom - 4.0, vy_tp0 - 6.0)
            y_tap_net = {"tn": y_tap_base, "tp": y_tap_base - 2.5}
            # tn column west of tp so tn V does not cross tp H [TOOL LVS]
            x_west_net = {
                "tn": det_bb.left - 12.5,
                "tp": det_bb.left - 10.0,  # west of gnd col [GDS]
            }
            # Separate approach Y so tn/tp M2 do not merge (M2.b / LVS) [TOOL]
            # Window between det gnd pad top≈516.5 and vdd pad bot≈523.8
            y_appr_net = {"tn": 521.0, "tp": 518.0}

            def pour(x0, y0, x1, y1, half):
                c.shapes(self.tm1).insert(
                    pya.DBox(min(x0, x1) - half, min(y0, y1) - half,
                             max(x0, x1) + half, max(y0, y1) + half))

            def pin_pad(px, py, y_sp, net, pad_x, tight):
                # TM1.a min width 1.64 µm on both axes [DS]
                margin = 1.0
                if tight:
                    if net == "tn":
                        y0, y1 = py - 0.82, max(py, y_sp) + margin
                    else:
                        y0, y1 = min(py, y_sp) - margin, py + 0.82
                else:
                    y0, y1 = min(py, y_sp) - margin, max(py, y_sp) + margin
                if (y1 - y0) < 1.64:
                    mid = 0.5 * (y0 + y1)
                    y0, y1 = mid - 0.82, mid + 0.82
                if (2.0 * pad_x) < 1.64:
                    pad_x = 0.82
                c.shapes(self.tm1).insert(
                    pya.DBox(px - pad_x, y0, px + pad_x, y1))

            lengths = {"tn": 0.0, "tp": 0.0}
            C_tank = {}
            C_tap = {}
            for net in ("tn", "tp"):
                if net not in cp or net not in bp or net not in vp:
                    self.say(f"{net}: need core+bank+var pins")
                    continue
                y_tank = track_tank[net]
                L_w = 0.0
                L_t = 0.0
                cx_p, cy_p = cp[net]
                bx_p, by_p = bp[net]
                vx_p, vy_p = vp[net]
                # --- bank ↔ core (wide) ---
                x_join = max(cx_p, ct_x_clear) if net == "tn" else min(cx_p, bx_p)
                if net == "tn":
                    y_h = by_p + 3.0
                    pour(bx_p, by_p, bx_p, y_h, hw)
                    L_w += abs(y_h - by_p)
                    pour(bx_p, y_h, x_join, y_h, hw)
                    L_w += abs(x_join - bx_p)
                    pour(x_join, y_h, x_join, y_tank, hw)
                    L_w += abs(y_tank - y_h)
                    pin_pad(bx_p, by_p, y_h, net, 2.5, tight=False)
                else:
                    pour(bx_p, by_p, bx_p, y_tank, hw)
                    L_w += abs(by_p - y_tank)
                    pin_pad(bx_p, by_p, y_tank, net, 2.5, tight=False)
                pour(cx_p, cy_p, cx_p, y_tank, hw)
                L_w += abs(y_tank - cy_p)
                pin_pad(cx_p, cy_p, y_tank, net, 2.0, tight=True)
                pour(x_join, y_tank, cx_p, y_tank, hw)
                L_w += abs(cx_p - x_join)
                c.shapes(self.tm1).insert(
                    pya.DBox(cx_p - hw, y_tank - hw, cx_p + hw, y_tank + hw))

                # --- wide to var ---
                # var.tn and var.tp share west-face X; tn V at that X through
                # var.tp Y shorts tn|tp [TOOL]. Jog tn east around tp pin.
                vy_tp = vp["tp"][1] if "tp" in vp else vy_p
                if net == "tn" and abs(vy_p - vy_tp) > 1.0:
                    y_below = vy_tp - (2 * hw + 1.64 + 0.2)
                    x_jog = vx_p + (2 * hw + 1.64 + 0.2)
                    pour(cx_p, y_tank, cx_p, y_below, hw)
                    L_w += abs(y_below - y_tank)
                    pour(cx_p, y_below, x_jog, y_below, hw)
                    L_w += abs(x_jog - cx_p)
                    pour(x_jog, y_below, x_jog, vy_p, hw)
                    L_w += abs(vy_p - y_below)
                    pour(x_jog, vy_p, vx_p, vy_p, hw)
                    L_w += abs(vx_p - x_jog)
                    self.say(
                        f"tn jog east of var.tp x_jog={x_jog:.1f} "
                        f"y_below={y_below:.1f} [TOOL]"
                    )
                elif abs(vx_p - cx_p) > 0.05:
                    # tp: V at core.tp x, M2 underpass to var.tp (no TM1 on
                    # shared face X except tiny land via M1) [TOOL]
                    pour(cx_p, y_tank, cx_p, vy_p, hw)
                    L_w += abs(vy_p - y_tank)
                    gap = 2 * hw + 1.64 + 0.2
                    x_stop = vx_p - gap if cx_p < vx_p else vx_p + gap
                    pour(cx_p, vy_p, x_stop, vy_p, hw)
                    L_w += abs(x_stop - cx_p)
                    c.shapes(self.tm1).insert(
                        pya.DBox(x_stop - hw, vy_p - hw,
                                 x_stop + hw, vy_p + hw))
                    c.shapes(self.m2).insert(
                        pya.DBox(x_stop - hw, vy_p - hw,
                                 x_stop + hw, vy_p + hw))
                    c.insert(pya.DCellInstArray(
                        vs2t, pya.DTrans(pya.DVector(x_stop, vy_p))))
                    c.shapes(self.m2).insert(
                        pya.DBox(min(x_stop, vx_p) - 0.5, vy_p - 0.5,
                                 max(x_stop, vx_p) + 0.5, vy_p + 0.5))
                    L_w += abs(vx_p - x_stop)
                    # Land var.tp on M1/M2 only — TM1 land ≡ tn face [TOOL]
                    c.shapes(self.m2).insert(
                        pya.DBox(vx_p - 1.0, vy_p - 1.0,
                                 vx_p + 1.0, vy_p + 1.0))
                    c.shapes(self.m1).insert(
                        pya.DBox(vx_p - 0.8, vy_p - 0.8,
                                 vx_p + 0.8, vy_p + 0.8))
                    c.insert(pya.DCellInstArray(
                        vs12, pya.DTrans(pya.DVector(vx_p, vy_p))))
                    self.say(
                        f"{net} M2 underpass to var "
                        f"x_stop={x_stop:.1f}→({vx_p:.1f},{vy_p:.1f}) [TOOL]"
                    )
                else:
                    pour(cx_p, y_tank, cx_p, vy_p, hw)
                    L_w += abs(vy_p - y_tank)
                    pin_pad(vx_p, vy_p, vy_p, net, 2.0, tight=False)
                    for lyr in (self.m1, self.m2, self.tm1):
                        c.shapes(lyr).insert(
                            pya.DBox(vx_p - 1.2, vy_p - 1.2,
                                     vx_p + 1.2, vy_p + 1.2))
                    c.insert(pya.DCellInstArray(
                        vs1t, pya.DTrans(pya.DVector(vx_p, vy_p))))
                if net == "tn":
                    pin_pad(vx_p, vy_p, vy_p, net, 2.0, tight=False)
                    for lyr in (self.m1, self.m2, self.tm1):
                        c.shapes(lyr).insert(
                            pya.DBox(vx_p - 1.2, vy_p - 1.2,
                                     vx_p + 1.2, vy_p + 1.2))
                    c.insert(pya.DCellInstArray(
                        vs1t, pya.DTrans(pya.DVector(vx_p, vy_p))))

                # --- thin det taps: tn on M2, tp on M1 after branch so the
                # west-corridor crossings do not short [TOOL LVS tn|tp].
                if net in dp:
                    dx_p, dy_p = dp[net]
                    y_tap = y_tap_net[net]
                    x_west = x_west_net[net]
                    y_appr = y_appr_net[net]
                    use_m1 = (net == "tp")
                    lyr = self.m1 if use_m1 else self.m2

                    def pour_l(x0, y0, x1, y1):
                        c.shapes(lyr).insert(
                            pya.DBox(min(x0, x1) - ht, min(y0, y1) - ht,
                                     max(x0, x1) + ht, max(y0, y1) + ht))

                    # Branch from TM1 riser
                    c.shapes(self.tm1).insert(
                        pya.DBox(cx_p - 1.0, y_tap - 1.0, cx_p + 1.0, y_tap + 1.0))
                    if use_m1:
                        c.shapes(self.m1).insert(
                            pya.DBox(cx_p - 0.8, y_tap - 0.8,
                                     cx_p + 0.8, y_tap + 0.8))
                        c.insert(pya.DCellInstArray(
                            vs1t, pya.DTrans(pya.DVector(cx_p, y_tap))))
                    else:
                        c.shapes(self.m2).insert(
                            pya.DBox(cx_p - 1.0, y_tap - 1.0,
                                     cx_p + 1.0, y_tap + 1.0))
                        c.insert(pya.DCellInstArray(
                            vs2t, pya.DTrans(pya.DVector(cx_p, y_tap))))

                    pour_l(cx_p, y_tap, x_west, y_tap)
                    L_t += abs(x_west - cx_p)
                    pour_l(x_west, y_tap, x_west, y_appr)
                    L_t += abs(y_appr - y_tap)
                    pour_l(x_west, y_appr, dx_p, y_appr)
                    L_t += abs(dx_p - x_west)
                    pour_l(dx_p, y_appr, dx_p, dy_p)
                    L_t += abs(dy_p - y_appr)
                    c.shapes(self.m1).insert(
                        pya.DBox(dx_p - 0.42, dy_p - 0.42,
                                 dx_p + 0.42, dy_p + 0.42))
                    if not use_m1:
                        c.shapes(self.m2).insert(
                            pya.DBox(dx_p - 0.42, dy_p - 0.42,
                                     dx_p + 0.42, dy_p + 0.42))
                        c.insert(pya.DCellInstArray(
                            vs12, pya.DTrans(pya.DVector(dx_p, dy_p))))
                    self.say(
                        f"{net} det thin "
                        f"{'M1' if use_m1 else 'M2'} tap w={w_tap} "
                        f"x_west={x_west:.1f} y_tap={y_tap:.1f} "
                        f"y_appr={y_appr:.1f} L_tap={L_t:.1f} [HAND/GDS]"
                    )

                lengths[net] = L_w + L_t
                C_tank[net] = L_w * 0.10
                C_tap[net] = L_t * 0.05  # M2 w=0.5 [HAND]
                self.say(
                    f"{net} wide L={L_w:.1f} µm C≈{C_tank[net]:.1f} fF; "
                    f"tap L={L_t:.1f} µm C≈{C_tap[net]:.1f} fF; "
                    f"total C≈{C_tank[net]+C_tap[net]:.1f} fF [HAND/GDS]"
                )
            if C_tank and C_tap:
                self.say(
                    f"tn/tp island C≈{C_tank.get('tn',0)+C_tap.get('tn',0):.1f}/"
                    f"{C_tank.get('tp',0)+C_tap.get('tp',0):.1f} fF "
                    f"(wide TM1 C'=0.10, M2 tap C'=0.05) [HAND]"
                )

        # ---- vt shielded (south of bank; clear of gnd spine at y_gnd≈−4) ----
        if "vt" in routed and "W" in vp:
            vx, vy = vp["W"]
            # gnd spine occupies ≈ [y_gnd−2, y_gnd+2]; keep vt + shields below it
            y_gnd = min(b.bottom for b in (
                bank_bb, core_bb, var_bb, det_bb, tail_bb)) - 4.0
            y_vt = y_gnd - 8.0  # shield at ±2.5 stays ≤ y_gnd−5.5 [TOOL LVS]
            x_west = min(bank_bb.left, var_bb.left) - 10.0
            x_col = var_bb.left - 6.0  # clear of tail M3
            c.shapes(self.m2).insert(
                pya.DBox(min(vx, x_col) - 0.2, vy - 1.0,
                         max(vx, x_col) + 0.2, vy + 1.0))
            c.shapes(self.m3).insert(
                pya.DBox(x_col - 1.0, min(vy, y_vt), x_col + 1.0, max(vy, y_vt)))
            c.shapes(self.m2).insert(
                pya.DBox(min(x_west, x_col), y_vt - 1.0,
                         max(x_west, x_col), y_vt + 1.0))
            for dy in (-2.5, 2.5):
                c.shapes(self.m2).insert(
                    pya.DBox(min(x_west, x_col), y_vt + dy - 0.7,
                             max(x_west, x_col), y_vt + dy + 0.7))
            c.shapes(self.m2).insert(
                pya.DBox(vx - 1.0, vy - 1.0, vx + 1.0, vy + 1.0))
            c.insert(pya.DCellInstArray(vs12, pya.DTrans(pya.DVector(vx, vy))))
            c.insert(pya.DCellInstArray(vs23, pya.DTrans(pya.DVector(vx, vy))))
            c.insert(pya.DCellInstArray(vs23, pya.DTrans(pya.DVector(x_col, vy))))
            c.insert(pya.DCellInstArray(vs23, pya.DTrans(pya.DVector(x_col, y_vt))))
            export_pin("vt", x_west, y_vt, "m1")
            c.insert(pya.DCellInstArray(
                vs12, pya.DTrans(pya.DVector(x_west, y_vt))))
            self.say(f"vt shielded escape y={y_vt:.2f} (gnd_spine={y_gnd:.2f}) "
                     f"x_col={x_col:.1f}")

        # ---- controls: vbp only on island; gates/codes exported ----
        if "controls" in routed:
            if "vbp" in bp and "vbp" in vp:
                x0, y0 = bp["vbp"]
                x1, y1 = vp["vbp"]
                # Stay south of tank: use bank mid Y, columns outside cells
                y_ctrl = min(y0, 80.0)
                x_col0 = bank_bb.left - 3.0
                x_col1 = var_bb.right + 3.0
                # pin → south/west column → H → east column → pin
                c.shapes(self.m2).insert(
                    pya.DBox(min(x0, x_col0) - 0.2, y0 - 1.0,
                             max(x0, x_col0) + 0.2, y0 + 1.0))
                c.shapes(self.m3).insert(
                    pya.DBox(x_col0 - 1.0, min(y0, y_ctrl),
                             x_col0 + 1.0, max(y0, y_ctrl)))
                c.shapes(self.m2).insert(
                    pya.DBox(min(x_col0, x_col1), y_ctrl - 1.0,
                             max(x_col0, x_col1), y_ctrl + 1.0))
                c.shapes(self.m3).insert(
                    pya.DBox(x_col1 - 1.0, min(y_ctrl, y1),
                             x_col1 + 1.0, max(y_ctrl, y1)))
                c.shapes(self.m2).insert(
                    pya.DBox(min(x_col1, x1) - 0.2, y1 - 1.0,
                             max(x_col1, x1) + 0.2, y1 + 1.0))
                c.shapes(self.m2).insert(
                    pya.DBox(x0 - 1.0, y0 - 1.0, x0 + 1.0, y0 + 1.0))
                c.shapes(self.m2).insert(
                    pya.DBox(x1 - 1.0, y1 - 1.0, x1 + 1.0, y1 + 1.0))
                c.insert(pya.DCellInstArray(
                    vs12, pya.DTrans(pya.DVector(x0, y0))))
                c.insert(pya.DCellInstArray(
                    vs23, pya.DTrans(pya.DVector(x_col0, y0))))
                c.insert(pya.DCellInstArray(
                    vs23, pya.DTrans(pya.DVector(x_col0, y_ctrl))))
                c.insert(pya.DCellInstArray(
                    vs23, pya.DTrans(pya.DVector(x_col1, y_ctrl))))
                c.insert(pya.DCellInstArray(
                    vs23, pya.DTrans(pya.DVector(x_col1, y1))))
                c.insert(pya.DCellInstArray(
                    vs12, pya.DTrans(pya.DVector(x1, y1))))
                self.say(f"vbp bank↔var via y_ctrl={y_ctrl:.1f}")
            self.say("controls: gate/code pins exported; AFE buses at synthesizer top")

        # LVS GDS: pin-only inductor (what extract must see) [TOOL]
        gds_lvs = os.path.join(OUT, "vco_top_lvs.gds")
        self.ly.write(gds_lvs)
        self.say(f"wrote {gds_lvs} (pin-only inductor) [TOOL]")

        # Fab GDS: same island routing, fab core with l2n0_em spiral [TOOL]
        gds = os.path.join(OUT, "vco_top.gds")
        fab_core = GDS_FAB["vco_core_tank"]
        if not os.path.exists(fab_core) and os.path.exists(fab_core + ".gz"):
            with gzip.open(fab_core + ".gz", "rb") as z, open(fab_core, "wb") as f:
                shutil.copyfileobj(z, f)
        if os.path.exists(fab_core):
            self._write_fab_with_spiral(fab_core, gds_lvs, gds)
        else:
            shutil.copyfile(gds_lvs, gds)
            self.say(f"wrote {gds} (copy of LVS; no fab core) [TOOL]")
        with open(gds, "rb") as f, gzip.open(gds + ".gz", "wb") as z:
            shutil.copyfileobj(f, z)
        self.say(f"wrote {gds}.gz")
        self.write_spice()
        open(os.path.join(OUT, "summary_build_log.txt"), "w").write(
            "\n".join(self.log) + "\n")
        return outline

    def _write_fab_with_spiral(self, fab_core_gds, gds_lvs, gds_out):
        """Copy LVS top, replace pin-only core instance with fab core + spiral."""
        ly = pya.Layout()
        ly.read(gds_lvs)
        top = ly.top_cell()
        core_inst = None
        for inst in top.each_inst():
            if inst.cell.name.startswith("vco_core_tank"):
                core_inst = inst
                break
        if core_inst is None:
            shutil.copyfile(gds_lvs, gds_out)
            self.say("fab write: no core instance; copied LVS [TOOL]")
            return
        tr = core_inst.dcplx_trans
        src = pya.Layout()
        src.read(fab_core_gds)
        src_top = src.cell("vco_core_tank") or src.top_cell()
        new_cell = ly.create_cell("vco_core_tank_fab")
        new_cell.copy_tree(src_top)
        for L, D in ((8, 25), (126, 25), (8, 2), (126, 2)):
            lyr = ly.layer(L, D)
            for s in list(new_cell.shapes(lyr).each()):
                if s.is_text() or (L, D) in ((8, 2), (126, 2)):
                    new_cell.shapes(lyr).erase(s)
        core_inst.delete()
        top.insert(pya.DCellInstArray(new_cell.cell_index(), tr))
        ly.write(gds_out)
        self.say(f"wrote fab {gds_out} with spiral from {fab_core_gds} [TOOL]")

    def write_spice(self):
        """Hierarchical LVS spice from proven leaf netlists [TOOL]."""
        chunks = []
        for name, path in SPICE_LEAF.items():
            txt = open(path).read()
            # drop .end
            lines = [ln for ln in txt.splitlines()
                     if not ln.strip().lower().startswith(".end")]
            chunks.append("\n".join(lines))
        ports = " ".join(TOP_PORTS)
        # bb* local float nets for bank
        bbs = " ".join(f"bb{i}" for i in range(12))
        top = f"""
* P2.7.2c vco_top hierarchical LVS netlist [layout leaf spices]
.subckt vco_top {ports}
Xc tp tn tail ct gnd vco_core_tank
Xb tp tn vbp gnd g0 bb0 g1 bb1 g2 bb2 g3 bb3 g4 bb4 g5 bb5 g6 bb6 g7 bb7 g8 bb8 g9 bb9 g10 bb10 g11 bb11 vco_bank
Xv tp tn vt vbp gnd G1 G2 vco_var
Xt tail vdd gnd vbp_tail nb nbf pbias xraw code_gnd code0 code1 code2 code3 code4 code_vdd ss tail_f tail_block
Xd tp tn ct vdd gnd cmp hold rep en vthn ampcal_det
.ends
.end
"""
        # Note: G1/G2/nb/... are local floats unless exported — OK for LVS dangling
        body = "\n\n".join(chunks) + "\n" + top
        path = os.path.join(OUT, "vco_top.spice")
        open(path, "w").write(body)
        self.say(f"wrote {path}")


def main():
    nets = "place"
    argv = sys.argv[1:]
    i = 0
    while i < len(argv):
        if argv[i] == "--nets" and i + 1 < len(argv):
            nets = argv[i + 1]
            i += 2
        else:
            i += 1
    order = ["place", "power", "ct", "tail", "tn_tp", "vt", "controls"]
    if nets == "all":
        routed = set(order)
    else:
        routed = set()
        for part in nets.split(","):
            part = part.strip()
            if part not in order and part != "all":
                raise SystemExit(f"unknown net group {part}")
            # include all prior groups (incremental)
            for g in order:
                routed.add(g)
                if g == part:
                    break
    print(f"routed groups: {sorted(routed)}", flush=True)
    a = Asm()
    a.build(routed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
