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

    def build(self, routed):
        c = self.ly.create_cell("vco_top")
        vs12 = self.via12()
        vs23 = self.via23()
        vs2t = self.via2t()
        vs1t = self.via1t()

        kids = {}
        for name in ("vco_bank", "vco_core_tank", "tail_block", "vco_var",
                     "ampcal_det"):
            cid, pins, bb, keep = self.load_child(name)
            kids[name] = {"cid": cid, "pins": pins, "bb0": bb, "keep": keep}

        # Direct bank–core re-pack: bank south X-aligned; var/det east Y-aligned;
        # tail NE; tn/tp bank join = V stub only (no west corridor)
        # (spec/p27-layout-notes.md P2.7.2c next re-pack) [HAND]
        gap = 8.0
        core_pins0 = kids["vco_core_tank"]["pins"]
        bank_pins0 = kids["vco_bank"]["pins"]
        var_pins0 = kids["vco_var"]["pins"]
        det_pins0 = kids["ampcal_det"]["pins"]
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
        # 12 µm core–east gap: dedicated M3 tail corridor (no metal through
        # core/bank) [decisions P2.7.2c tail escape]. tn/tp still meet budget.
        east_gap = 12.0
        var_ll = (
            core_bb.right + east_gap,
            core_tn_y - var_pins0["tn"][1] + var_bb0.bottom,
        )
        var_bb, var_tr = self.place_ll(
            c, kids["vco_var"]["cid"], var_ll[0], var_ll[1])
        det_ll = (
            var_bb.right + 4.0,
            core_tn_y - det_pins0["tn"][1] + det_bb0.bottom,
        )
        det_bb, det_tr = self.place_ll(
            c, kids["ampcal_det"]["cid"], det_ll[0], det_ll[1])
        # Tail NE of core, west-aligned with corridor; no closer without hitting var
        tail_ll = (core_bb.right + east_gap, var_bb.top + 4.0)
        tail_bb, tail_tr = self.place_ll(
            c, kids["tail_block"]["cid"], tail_ll[0], tail_ll[1])
        self.say(
            f"direct-pack LL bank={bank_ll} core={core_ll} var={var_ll} "
            f"det={det_ll} tail={tail_ll} east_gap={east_gap} [HAND]"
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
                # Was left-4 ≈144.8; collided with tail corridor. Keep clear of
                # x_col=core.right+3 and its M2 climb [TOOL LVS].
                ("tail_block", "gnd"): min(tail_bb.left - 16.0,
                                           core_bb.right - 8.0),
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

        # ---- ct: labelled TM1 port + stub to det.ct (clear of tn/tp tracks) ----
        if "ct" in routed and "ct" in cp:
            cx, cy = cp["ct"]
            w_ct = 2.0
            # Core tn/tp TM1 plates extend to core_bb.top (≈438). An H strap at
            # tank_y+10 (≈390) crossed tn TM1 → extract ct|tn [TOOL LVS].
            # Run north of the core, then east; drop to det.ct outside core.x.
            y_ct = max(cp["tn"][1] + 10.0, core_bb.top + 3.0)
            x_ct_end = det_bb.right + 3.0
            self.strap_tm1(c, cx, cy, cx, y_ct, w=w_ct)
            # Extend H strap past pin so pin pad is fully enclosed (TM1.a) [TOOL]
            self.strap_tm1(c, cx, y_ct, x_ct_end + 1.5, y_ct, w=w_ct)
            export_pin("ct", x_ct_end, y_ct, "tm1")
            if "ct" in dp:
                dx, dy = dp["ct"]
                # Drop east of core/var before going south to det.ct pin
                x_drop = max(dx, core_bb.right + 4.0, var_bb.right + 2.0)
                self.strap_tm1(c, x_ct_end, y_ct, x_drop, y_ct, w=w_ct)
                self.strap_tm1(c, x_drop, y_ct, x_drop, dy, w=w_ct)
                self.strap_tm1(c, x_drop, dy, dx, dy, w=w_ct)
                c.shapes(self.tm1).insert(
                    pya.DBox(dx - 1.5, dy - 1.0, dx + 1.5, dy + 1.0))
                c.insert(pya.DCellInstArray(
                    vs1t, pya.DTrans(pya.DVector(dx, dy))))
                self.say(
                    f"ct→det.ct via x_drop={x_drop:.1f} ({dx:.1f},{dy:.1f}) "
                    f"[TOOL]"
                )
            self.say(f"ct TM1 port y={y_ct:.2f} → ({x_ct_end:.1f},{y_ct:.1f})")

        # ---- tail: M3 escape outside all child bboxes ----
        # Prior H at mid-height crossed var/det on M3 → mega-short
        # G1|G2|W|gnd|tail|tn|tp|vbp|vdd|vt [TOOL LVS]. Stay in the core–var
        # corridor, then north of every block (below the vdd spine).
        if "tail" in routed and "tail" in cp and "tail" in tpins:
            x0, y0 = cp["tail"]
            x1, y1 = tpins["tail"]
            w = 2.0
            # Mid-gap (≈142.8) abutted tail_block.gnd power M3 at left-4
            # (≈144.8) → gnd|tn|vdd [TOOL LVS]. Stay near core.right.
            x_col = core_bb.right + 3.0
            tops = [core_bb.top, bank_bb.top, var_bb.top, det_bb.top,
                    tail_bb.top]
            # Power M3 columns run up to y_vdd=max(tops)+10. An M3 H at
            # max(tops)+2 crossed those columns → gnd|tail|tn|vdd [TOOL LVS].
            # Keep the ring above the spine (and column tops).
            y_north = max(tops) + 16.0  # = y_vdd + 6
            # East of every block (and of tail.vdd col at right+3). m3d V that
            # ended inside the tail cell → tn|vdd [TOOL bisect]; stay outside.
            x_drop = max(
                tail_bb.right, det_bb.right, var_bb.right, x1
            ) + 16.0
            # M2 climbs only above core/var/det (not into tail gnd M2 pads).
            # vs23 only (no vs12): M1 landing joined gnd|tn [TOOL bisect].
            # M3 continues past the vdd spine to y_north.
            y_lift = max(core_bb.top, var_bb.top, det_bb.top) + 2.0
            if y_lift >= tail_bb.bottom - 1.0:
                y_lift = min(y_lift, tail_bb.bottom - 3.0)
            parts = set(
                x.strip()
                for x in os.environ.get(
                    # Default stops east of the cell (LVS-clean). m2drop/endvia
                    # into the pin → gnd|tn until tail_block gets a face stub.
                    "TAIL_PARTS", "m2,via,m3v,m3h,m3d"
                ).split(",")
                if x.strip()
            )
            m2w = 0.7
            if "m2" in parts:
                c.shapes(self.m2).insert(
                    pya.DBox(min(x0, x_col) - 0.3, y0 - m2w / 2,
                             max(x0, x_col) + 0.3, y0 + m2w / 2))
                c.shapes(self.m2).insert(
                    pya.DBox(x_col - m2w / 2, min(y0, y_lift),
                             x_col + m2w / 2, max(y0, y_lift)))
                c.shapes(self.m2).insert(
                    pya.DBox(x_col - 0.5, y_lift - 0.5,
                             x_col + 0.5, y_lift + 0.5))
            if "via" in parts:
                c.insert(pya.DCellInstArray(
                    vs23, pya.DTrans(pya.DVector(x_col, y_lift))))
            if "m3v" in parts:
                c.shapes(self.m3).insert(
                    pya.DBox(x_col - w / 2, min(y_lift, y_north),
                             x_col + w / 2, max(y_lift, y_north)))
            if "m3h" in parts:
                # H above all cells to the east drop column
                c.shapes(self.m3).insert(
                    pya.DBox(min(x_col, x_drop) - w / 2, y_north - w / 2,
                             max(x_col, x_drop) + w / 2, y_north + w / 2))
            # Child has a vertical M2 at x≈395 spanning y≈492–644; an H at
            # pin Y from the east hits it → gnd|tn [TOOL LVS / GDS]. Jog above.
            y_jog = max(y1, 650.0)
            if "m3d" in parts:
                c.shapes(self.m3).insert(
                    pya.DBox(x_drop - w / 2, min(y_north, y_jog),
                             x_drop + w / 2, max(y_north, y_jog)))
                c.shapes(self.m2).insert(
                    pya.DBox(x_drop - 0.5, y_jog - 0.5,
                             x_drop + 0.5, y_jog + 0.5))
                c.insert(pya.DCellInstArray(
                    vs23, pya.DTrans(pya.DVector(x_drop, y_jog))))
            if "m2drop" in parts:
                c.shapes(self.m2).insert(
                    pya.DBox(min(x1, x_drop) - 0.25, y_jog - 0.25,
                             max(x1, x_drop) + 0.25, y_jog + 0.25))
                c.shapes(self.m2).insert(
                    pya.DBox(x1 - 0.25, min(y_jog, y1),
                             x1 + 0.25, max(y_jog, y1)))
            if "endvia" in parts:
                c.shapes(self.m2).insert(
                    pya.DBox(x1 - 0.35, y1 - 0.35, x1 + 0.35, y1 + 0.35))
            L_tot = (
                abs(x_col - x0) + abs(y_lift - y0) + abs(y_north - y_lift)
                + abs(x_drop - x_col) + abs(y_jog - y_north)
                + abs(x_drop - x1) + abs(y_jog - y1)
            )
            C_tail = L_tot * 0.10  # [HAND] C'≈0.10 fF/µm M3
            self.say(
                f"tail route M2→lift M3 x_col={x_col:.1f} y_lift={y_lift:.1f} "
                f"y_north={y_north:.1f} x_drop={x_drop:.1f} w={w:.1f} µm "
                f"L={L_tot:.1f} µm C≈{C_tail:.1f} fF parts={sorted(parts)} "
                f"[HAND/GDS]"
            )

        # ---- tn / tp: direct pack — H spine + V stubs; bank jog clear of ct ----
        if "tn_tp" in routed:
            tank_y = cp["tn"][1]
            # Core child CT TM1 occupies ≈(64.4–72.4, y≥384.65) [GDS]. Parent tn
            # must keep ≥1.64 µm to that wall [DS TM1.b] — do not heal/fill it
            # (that would short tn↔ct). Bank tn pin sits at x≈74.0, so the bank
            # stub jogs east below the CT keep-out before rising to the spine.
            #
            # tn track above pins, tp below. Core/det share pin y=tank_y so
            # pads/stubs there must not overhang toward the other net [TOOL].
            # det.tp via_stack TM1 top ≈ pin+0.82; need spine_bot ≥ that+1.64
            # → track_tn ≥ tank_y + 0.82 + 1.64 + 1 ≈ tank_y + 3.5; use +4.0.
            # Spine under det.ct is U-jogged south (see below) so the higher
            # track does not hit the ct via [TOOL TM1.b].
            track = {"tn": tank_y + 4.0, "tp": tank_y - 5.0}
            w_tank = 2.0
            hw = w_tank / 2
            # CT keep-out: no parent tn with x < ct_x_clear and y > ct_y_clear
            ct_x_clear = 72.39 + 1.64 + hw  # spine centre ≥ this
            ct_y_clear = 384.65 - 1.64       # bank stub top below CT

            def tm1_pour(x0, y0, x1, y1):
                c.shapes(self.tm1).insert(
                    pya.DBox(min(x0, x1) - hw, min(y0, y1) - hw,
                             max(x0, x1) + hw, max(y0, y1) + hw))

            def tm1_stub(px, py, y_sp, net, tight):
                # Vertical stub pin→track. When tight, do not extend ±hw past
                # the pin toward the opposite net (that ate the tn/tp gap) [TOOL]
                if abs(y_sp - py) < 1e-9:
                    return
                if tight and net == "tp":  # track below pin: stub top = pin
                    y_top, y_bot = py, y_sp - hw
                elif tight and net == "tn":  # track above pin: stub bot = pin
                    y_top, y_bot = y_sp + hw, py
                else:
                    y_top, y_bot = max(py, y_sp) + hw, min(py, y_sp) - hw
                c.shapes(self.tm1).insert(
                    pya.DBox(px - hw, min(y_bot, y_top),
                             px + hw, max(y_bot, y_top)))

            def pin_pad(px, py, y_sp, net, pad_x, tight):
                # tight=True (core/det): no overhang past pin toward other net.
                # tight=False (var/bank): full pad so child MIM/metal merges [TOOL]
                if tight:
                    if net == "tn":
                        y0, y1 = py - 0.3, max(py, y_sp) + 1.0
                    else:
                        y0, y1 = min(py, y_sp) - 1.0, py + 0.3
                else:
                    y0, y1 = min(py, y_sp) - 1.0, max(py, y_sp) + 1.0
                c.shapes(self.tm1).insert(
                    pya.DBox(px - pad_x, y0, px + pad_x, y1))

            lengths = {}
            for net in ("tn", "tp"):
                pins = {}
                for label, pp in (
                    ("core", cp), ("bank", bp), ("var", vp), ("det", dp),
                ):
                    if net in pp:
                        pins[label] = pp[net]
                if len(pins) < 2:
                    self.say(f"{net}: need ≥2 pins, have {len(pins)}")
                    continue
                y_sp = track[net]
                L = 0.0
                # Spine: for tn, start east of CT keep-out (not at bank x)
                xs_east = [pins[k][0] for k in ("core", "var", "det") if k in pins]
                if net == "tn":
                    x_lo = max(min(xs_east), ct_x_clear)
                else:
                    x_lo = min(pins[k][0] for k in pins)
                x_hi = max(pins[k][0] for k in pins)
                # tn: break spine under det.ct via (TM1 bottom ≈386.08); bridge
                # south at y_bypass so west (core/var) still meets det.tn [TOOL]
                if net == "tn" and "ct" in dp:
                    cx = dp["ct"][0]
                    # via TM1 ≈(cx±0.82); keep spine tips ≥1.64 away incl. hw
                    gap = (cx - 5.0, cx + 5.0)
                    y_bypass = tank_y - 1.5  # between tp track and tn track
                    if x_lo < gap[0]:
                        tm1_pour(x_lo, y_sp, gap[0], y_sp)
                        L += gap[0] - x_lo
                    if gap[1] < x_hi:
                        tm1_pour(gap[1], y_sp, x_hi, y_sp)
                        L += x_hi - gap[1]
                    # U-jog south under ct: down / H / up (stop at spine centre)
                    c.shapes(self.tm1).insert(
                        pya.DBox(gap[0] - hw, min(y_sp, y_bypass) - hw,
                                 gap[0] + hw, y_sp))
                    c.shapes(self.tm1).insert(
                        pya.DBox(gap[1] - hw, min(y_sp, y_bypass) - hw,
                                 gap[1] + hw, y_sp))
                    tm1_pour(gap[0], y_bypass, gap[1], y_bypass)
                    L += 2 * abs(y_sp - y_bypass) + (gap[1] - gap[0])
                    self.say(
                        f"tn spine U-jog under det.ct "
                        f"x=[{gap[0]:.1f},{gap[1]:.1f}] y_bypass={y_bypass:.2f} "
                        f"[TOOL]"
                    )
                else:
                    tm1_pour(x_lo, y_sp, x_hi, y_sp)
                    L += x_hi - x_lo

                for src in ("core", "bank", "var", "det"):
                    if src not in pins:
                        continue
                    px, py = pins[src]
                    # var: reach mim_couple TM1 (≈ pin.x+3); bank: merge child bar
                    pad_x = 3.5 if src == "var" else (2.5 if src == "bank" else 2.0)
                    tight = src in ("core", "det")
                    if net == "tn" and src == "bank":
                        # East first at pin y (below CT), then V up — a tall
                        # stub at bank.x overlaps core CT in x [TOOL TM1.b]
                        x_join = x_lo
                        y_h = py + 3.0
                        tm1_pour(px, py, px, y_h)
                        L += abs(y_h - py)
                        tm1_pour(px, y_h, x_join, y_h)
                        L += abs(x_join - px)
                        tm1_pour(x_join, y_h, x_join, y_sp)
                        L += abs(y_sp - y_h)
                        pin_pad(px, py, y_h, net, pad_x, tight=False)
                        self.say(
                            f"tn bank jog pin→y={y_h:.2f}→x={x_join:.2f}→"
                            f"track (clear of core CT) [TOOL]"
                        )
                    else:
                        tm1_stub(px, py, y_sp, net, tight)
                        L += abs(py - y_sp)
                        pin_pad(px, py, y_sp, net, pad_x, tight)
                    if src in ("var", "det"):
                        # Via landing: det.tp must not reach toward tn spine [TOOL]
                        if src == "det" and net == "tp":
                            y_via0, y_via1 = py - 1.2, py + 0.4
                        elif src == "det" and net == "tn":
                            y_via0, y_via1 = py - 0.4, py + 1.2
                        else:
                            y_via0, y_via1 = py - 1.2, py + 1.2
                        for lyr in (self.m1, self.m2, self.tm1):
                            c.shapes(lyr).insert(
                                pya.DBox(px - 1.2, y_via0, px + 1.2, y_via1))
                        c.insert(pya.DCellInstArray(
                            vs1t, pya.DTrans(pya.DVector(px, py))))
                lengths[net] = L
                self.say(
                    f"{net} TM1 direct spine y={y_sp:.2f} "
                    f"x=[{x_lo:.1f},{x_hi:.1f}] "
                    f"L={L:.1f} um w={w_tank} [GDS/HAND]"
                )
            if "tn" in lengths and "tp" in lengths:
                Cp = 0.10  # fF/µm @ w=2 [HAND]
                self.say(
                    f"tn/tp added C≈{lengths['tn']*Cp:.1f}/"
                    f"{lengths['tp']*Cp:.1f} fF (C'={Cp}) "
                    f"dL={abs(lengths['tn']-lengths['tp']):.1f} um [HAND]"
                )
            # Extra merge at core tn/tp child junctions (island coords) [TOOL]
            for px, py, y_sp, net in (
                (cp["tn"][0], cp["tn"][1], track["tn"], "tn"),
                (cp["tp"][0], cp["tp"][1], track["tp"], "tp"),
            ):
                if net == "tn":
                    y0, y1 = py - 0.3, max(py, y_sp) + 1.5
                else:
                    y0, y1 = min(py, y_sp) - 1.5, py + 0.3
                c.shapes(self.tm1).insert(
                    pya.DBox(px - 3.0, y0, px + 3.0, y1))
            # Same-net heals: ampcal east bar; var pad↔mim_couple bridges [TOOL]
            c.shapes(self.tm1).insert(
                pya.DBox(314.0, 380.5, 320.0, 383.5))
            for box in (
                # var tp: close 0.5 µm notch pad-top ↔ mim at y≈344.4–344.9
                (138.5, 343.0, 149.0, 349.5),
                # var tn: same at tank row
                (138.5, 379.5, 149.0, 386.0),
            ):
                c.shapes(self.tm1).insert(pya.DBox(*box))
            self.say("tn/tp TM1.b heal fills applied [TOOL]")

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
