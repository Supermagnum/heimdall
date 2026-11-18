#!/usr/bin/env python3
"""Intermediate pin fan-out check for P2.7.2c net-group joins [decisions 2026-11-18].

For each routed net, every schematic child pin that should sit on that net must
reach the same labelled metal net in the assembled LVS GDS (geometric flood).
Opens of nets not yet in EXPECTED for the accumulated groups are ignored.

Usage (from p272c/):
  python3 check_pin_fanout.py --group tail
  # reads out/pin_map.json + out/vco_top_lvs.gds
Exit 0 = PASS, 1 = FAIL (prints mismatches).
"""
from __future__ import annotations

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")

# Cumulative joins required after each group (schematic child pins) [SCH/TOOL].
# Format: net -> [(block, pin_name_in_pin_map), ...]
JOINS = {
    "place": {},
    "power": {
        "vdd": [("tail_block", "vdd"), ("ampcal_det", "vdd")],
        "gnd": [
            ("vco_core_tank", "gnd"), ("vco_bank", "gnd"),
            ("tail_block", "gnd"), ("vco_var", "gnd"), ("ampcal_det", "gnd"),
        ],
    },
    "ct": {
        "ct": [("vco_core_tank", "ct"), ("ampcal_det", "ct")],
    },
    "tail": {
        "tail": [("vco_core_tank", "tail"), ("tail_block", "tail")],
    },
    "tn_tp": {
        "tn": [
            ("vco_core_tank", "tn"), ("vco_bank", "tn"),
            ("vco_var", "tn"), ("ampcal_det", "tn"),
        ],
        "tp": [
            ("vco_core_tank", "tp"), ("vco_bank", "tp"),
            ("vco_var", "tp"), ("ampcal_det", "tp"),
        ],
    },
    "vt": {
        # pin_map keeps local name W; label on metal is vt after assemble [TOOL]
        "vt": [("vco_var", "W")],
    },
    "controls": {
        "vbp": [("vco_bank", "vbp"), ("vco_var", "vbp")],
    },
}
ORDER = ["place", "power", "ct", "tail", "tn_tp", "vt", "controls"]


def expected_for(group: str) -> dict:
    out = {}
    for g in ORDER:
        for net, pins in JOINS.get(g, {}).items():
            out[net] = list(pins)
        if g == group:
            break
    return out


def label_at_point(ly, top, x, y, dbu, metals, vias):
    """Flood M1–M3/TM1/TM2 from (x,y); return */25 text strings on that net.

    Prefer TopMetal seed when present so ct (TM2 west corridor) is not lost
    under a local M1 island that lacks TopVia2 [TOOL].
    """
    import pya
    bx = pya.Box(int((x - 1.0) / dbu), int((y - 1.0) / dbu),
                 int((x + 1.0) / dbu), int((y + 1.0) / dbu))
    m1, m2, m3, tm1, tm2 = metals
    v1, v2, v2t, vt2 = vias  # Via1, Via2, TopVia1, TopVia2
    seed_tm1 = tm1 & pya.Region(bx)
    seed_tm2 = tm2 & pya.Region(bx)
    c1 = pya.Region()
    c2 = pya.Region()
    c3 = pya.Region()
    ct = seed_tm1
    ctm2 = seed_tm2
    if ct.is_empty() and ctm2.is_empty():
        c1 = m1 & pya.Region(bx)
        if c1.is_empty():
            c2 = m2 & pya.Region(bx)
            if c2.is_empty():
                c3 = m3 & pya.Region(bx)
                if c3.is_empty():
                    return set(), "no_metal"
    for _ in range(400):
        t12 = v1.interacting(c1) + v1.interacting(c2)
        t23 = v2.interacting(c2) + v2.interacting(c3)
        t2t = v2t.interacting(c2) + v2t.interacting(ct)
        tt12 = vt2.interacting(ct) + vt2.interacting(ctm2)
        n1 = m1.interacting(c1 + t12)
        n2 = m2.interacting(c2 + t12 + t23 + t2t)
        n3 = m3.interacting(c3 + t23)
        nt = tm1.interacting(ct + t2t + tt12)
        nt2 = tm2.interacting(ctm2 + tt12)
        if (n1.area() == c1.area() and n2.area() == c2.area()
                and n3.area() == c3.area() and nt.area() == ct.area()
                and nt2.area() == ctm2.area()):
            break
        c1, c2, c3, ct, ctm2 = n1, n2, n3, nt, nt2
    names = set()
    regions = [c1, c2, c3, ct, ctm2]
    for li in ly.layer_indexes():
        info = ly.get_info(li)
        if info.datatype != 25:
            continue
        for sh in top.begin_shapes_rec(li).each():
            if not sh.shape().is_text():
                continue
            t = sh.shape().text
            tp = sh.trans() * t
            px, py = int(tp.x), int(tp.y)
            pt = pya.Region(pya.Box(px - 50, py - 50, px + 50, py + 50))
            for r in regions:
                if not r.is_empty() and not (r & pt).is_empty():
                    names.add(t.string)
                    break
    return names, "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", required=True,
                    help="Current net group just completed")
    ap.add_argument("--gds", default=os.path.join(OUT, "vco_top_lvs.gds"))
    ap.add_argument("--pin-map", default=os.path.join(OUT, "pin_map.json"))
    ap.add_argument("--out", default=os.path.join(OUT, "summary_pin_fanout.txt"))
    args = ap.parse_args()

    if not os.path.exists(args.pin_map):
        print(f"FAIL: missing pin map {args.pin_map}", flush=True)
        return 1
    if not os.path.exists(args.gds):
        print(f"FAIL: missing GDS {args.gds}", flush=True)
        return 1

    pin_map = json.load(open(args.pin_map))
    expected = expected_for(args.group)
    lines = [
        f"# Pin fan-out check group={args.group} [TOOL]",
        f"gds={os.path.basename(args.gds)}",
        "",
    ]
    if not expected:
        lines.append("no joined nets required yet — PASS")
        open(args.out, "w").write("\n".join(lines) + "\n")
        print("fanout: PASS (nothing required)", flush=True)
        return 0

    import pya
    ly = pya.Layout()
    ly.read(args.gds)
    top = ly.top_cell()
    dbu = ly.dbu
    metals = (
        pya.Region(top.begin_shapes_rec(ly.layer(8, 0))),    # M1
        pya.Region(top.begin_shapes_rec(ly.layer(10, 0))),   # M2
        pya.Region(top.begin_shapes_rec(ly.layer(30, 0))),   # M3
        pya.Region(top.begin_shapes_rec(ly.layer(126, 0))),  # TM1
        pya.Region(top.begin_shapes_rec(ly.layer(134, 0))),  # TM2
    )
    vias = (
        pya.Region(top.begin_shapes_rec(ly.layer(19, 0))),   # Via1
        pya.Region(top.begin_shapes_rec(ly.layer(29, 0))),   # Via2
        pya.Region(top.begin_shapes_rec(ly.layer(125, 0))),  # TopVia1
        pya.Region(top.begin_shapes_rec(ly.layer(133, 0))),  # TopVia2
    )

    fails = []
    for net, pins in sorted(expected.items()):
        lines.append(f"## net {net}")
        reached = {}
        for block, pname in pins:
            info = pin_map.get(block, {}).get("pins", {})
            if pname not in info:
                fails.append(f"{net}: missing pin_map {block}.{pname}")
                lines.append(f"  {block}.{pname}: MISSING in pin_map")
                continue
            x, y = info[pname]
            names, st = label_at_point(ly, top, x, y, dbu, metals, vias)
            reached[(block, pname)] = (names, st, x, y)
            lines.append(
                f"  {block}.{pname} @ ({x:.2f},{y:.2f}) labels={sorted(names) or ['(none)']} [{st}]"
            )
            if net not in names:
                fails.append(
                    f"{net}: {block}.{pname} not on '{net}' (labels={sorted(names)})"
                )
            # Any other *named* top-ish conflict (a|b style not in GDS texts)
            others = {n for n in names if n != net and not n.startswith("$")}
            # Allow only the expected net name on this pin for joined nets
            if others - {net}:
                # gnd/vdd may share fill labels — only flag if a different
                # *join* net from EXPECTED appears
                join_nets = set(expected.keys())
                bad = others & join_nets
                if bad:
                    fails.append(
                        f"{net}: {block}.{pname} also reaches {sorted(bad)}"
                    )
        lines.append("")

    lines.append("## result")
    if fails:
        lines.append("FAIL")
        for f in fails:
            lines.append(f"- {f}")
        open(args.out, "w").write("\n".join(lines) + "\n")
        print("fanout: FAIL", flush=True)
        for f in fails:
            print(f"  {f}", flush=True)
        return 1
    lines.append("PASS")
    open(args.out, "w").write("\n".join(lines) + "\n")
    print("fanout: PASS", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
