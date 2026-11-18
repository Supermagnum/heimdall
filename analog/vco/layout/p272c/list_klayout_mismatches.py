#!/usr/bin/env python3
"""List every KLayout-unpaired device with sch vs layout parameters [TOOL].

Reads out/lvs_vco_top/vco_top_lvs.lvsdb (or --lvsdb). Writes
out/summary_klayout_mismatches.txt and prints a short class tally.
"""
from __future__ import annotations

import argparse
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")


def param_dict(dev) -> dict:
    if dev is None:
        return {}
    out = {}
    dc = dev.device_class()
    names = []
    try:
        for pd in dc.parameter_definitions():
            n = pd.name
            names.append(n() if callable(n) else n)
    except Exception:
        names = ["W", "L", "w", "l", "AS", "AD", "PS", "PD", "NG", "ng",
                 "M", "m", "WFEED", "wfeed", "B", "b", "A", "C", "P",
                 "RFMODE", "rfmode"]
    for name in names:
        try:
            if not dc.has_parameter(name):
                continue
            out[name] = float(dev.parameter(name))
        except Exception:
            try:
                out[name] = str(dev.parameter(name))
            except Exception:
                pass
    return out


def fmt_params(d: dict) -> str:
    prefer = ["W", "L", "w", "l", "NG", "ng", "M", "m", "WFEED", "wfeed",
              "B", "b"]
    seen = set()
    parts = []
    for k in prefer:
        if k in d and k.lower() not in seen:
            v = d[k]
            parts.append(f"{k}={v:g}" if isinstance(v, float) else f"{k}={v}")
            seen.add(k.lower())
    for k, v in sorted(d.items()):
        if k.lower() in seen:
            continue
        if isinstance(v, float):
            parts.append(f"{k}={v:g}")
        else:
            parts.append(f"{k}={v}")
        seen.add(k.lower())
    return " ".join(parts) if parts else "(no params)"


def classify(cls_lay, cls_sch, p_lay, p_sch) -> str:
    """a=case/reader, b=grid, c=real, ?=other."""
    if cls_lay and cls_sch and cls_lay.lower() == cls_sch.lower() and cls_lay != cls_sch:
        return "a"
    if (cls_lay or "").lower() != (cls_sch or "").lower():
        # unpaired different classes often still case of same base
        if cls_lay and cls_sch and cls_lay.lower() == cls_sch.lower():
            return "a"
        if not cls_lay or not cls_sch:
            # one side missing — often case split of rfcmim
            names = {(cls_lay or "").lower(), (cls_sch or "").lower()} - {""}
            if names & {"rfcmim", "cap_rfcmim", "cap_cmim", "rhigh"}:
                return "a"
            return "?"
    # same class, compare numeric params
    keys = set()
    for d in (p_lay, p_sch):
        for k in d:
            if isinstance(d[k], float):
                keys.add(k.lower())
    # map aliases
    aliases = {"w": "W", "l": "L", "m": "M", "ng": "NG", "b": "B",
               "wfeed": "WFEED"}

    def get(d, key):
        for k, v in d.items():
            if k.lower() == key and isinstance(v, float):
                return v
        return None

    diffs = []
    for key in sorted(keys):
        a, b = get(p_lay, key), get(p_sch, key)
        if a is None or b is None:
            continue
        # normalize µm vs m: if one >> 1e-3 and other < 1e-3, scale
        aa, bb = a, b
        if aa > 1e-3 and bb < 1e-3:
            bb *= 1e6  # m → µm guess
        if bb > 1e-3 and aa < 1e-3:
            aa *= 1e6
        da = abs(aa - bb)
        if da < 1e-12:
            continue
        # Skip extract-only diffusion params (AS/AD/PS/PD) — tooling [TOOL]
        if key.lower() in ("as", "ad", "ps", "pd"):
            continue
        # PDK grid 0.01 µm for drawn [DS]; treat ≤ one grid as class b
        if max(abs(aa), abs(bb)) > 0.05:  # likely µm
            if da <= 0.01 + 1e-9:
                diffs.append(("b", key, aa, bb, da))
            else:
                diffs.append(("c", key, aa, bb, da))
        else:  # meters
            if da <= 0.01e-6 + 1e-15:
                diffs.append(("b", key, aa, bb, da))
            else:
                diffs.append(("c", key, aa, bb, da))
    # unpaired same-base after case normalize → often grid (RFCMIM) [TOOL]
    if not diffs:
        if (cls_lay or cls_sch) and (cls_lay or "").lower() == (cls_sch or "").lower():
            return "?"  # same params, net/topology cascade
        if not cls_lay or not cls_sch:
            base = ((cls_lay or cls_sch) or "").lower()
            if base in ("rfcmim", "cap_rfcmim", "cap_cmim", "rhigh"):
                return "b"  # unpaired MIM/R after casefix → grid/cascade
            return "?"
        return "?"
    if any(t[0] == "c" for t in diffs):
        return "c"
    if any(t[0] == "b" for t in diffs):
        return "b"
    return "?"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lvsdb",
                    default=os.path.join(OUT, "lvs_vco_top", "vco_top_lvs.lvsdb"))
    ap.add_argument("--out",
                    default=os.path.join(OUT, "summary_klayout_mismatches.txt"))
    args = ap.parse_args()
    if not os.path.exists(args.lvsdb):
        print(f"FAIL: missing {args.lvsdb}", flush=True)
        return 1

    import pya
    rdb = pya.LayoutVsSchematic()
    rdb.read(args.lvsdb)
    xref = rdb.xref()
    lines = [
        f"# KLayout LVS mismatch list [TOOL]",
        f"lvsdb={args.lvsdb}",
        "",
    ]
    class_counts = Counter()
    rows = []

    for cp in xref.each_circuit_pair():
        c1, c2 = cp.first(), cp.second()
        lines.append(
            f"## circuit lay={c1.name if c1 else None} "
            f"sch={c2.name if c2 else None} status={cp.status()}"
        )
        lines.append("")
        for dp in xref.each_device_pair(cp):
            st = dp.status()
            if st in (xref.Match, xref.MatchWithWarning, xref.Skipped,
                      xref.None_):
                continue
            d1, d2 = dp.first(), dp.second()
            cls1 = d1.device_class().name if d1 else None
            cls2 = d2.device_class().name if d2 else None
            if callable(cls1):
                cls1 = cls1()
            if callable(cls2):
                cls2 = cls2()
            n1 = d1.expanded_name() if d1 else None
            n2 = d2.expanded_name() if d2 else None
            p1, p2 = param_dict(d1), param_dict(d2)
            cat = classify(cls1, cls2, p1, p2)
            class_counts[cat] += 1
            class_counts[(cat, (cls1 or "").lower() or (cls2 or "").lower())] += 1
            # circuit location hint: netlist has no xy; use instance name
            row = {
                "cat": cat,
                "status": str(st),
                "cls_lay": cls1,
                "cls_sch": cls2,
                "inst_lay": n1,
                "inst_sch": n2,
                "p_lay": p1,
                "p_sch": p2,
            }
            rows.append(row)

    lines.append("## tally by class")
    for k in ("a", "b", "c", "?"):
        lines.append(f"  {k}: {class_counts[k]}")
    lines.append("")
    lines.append("## mismatches")
    for i, r in enumerate(rows, 1):
        lines.append(
            f"### {i}. class={r['cat']} status={r['status']}"
        )
        lines.append(
            f"  type lay={r['cls_lay']} sch={r['cls_sch']}"
        )
        lines.append(
            f"  inst lay={r['inst_lay']} sch={r['inst_sch']}"
        )
        lines.append(f"  layout params: {fmt_params(r['p_lay'])}")
        lines.append(f"  schem  params: {fmt_params(r['p_sch'])}")
        lines.append("")

    open(args.out, "w").write("\n".join(lines) + "\n")
    print(f"wrote {args.out}", flush=True)
    print(f"mismatches: a={class_counts['a']} b={class_counts['b']} "
          f"c={class_counts['c']} ?={class_counts['?']} "
          f"total={len(rows)}", flush=True)
    # type breakdown for a
    by_type = Counter()
    for r in rows:
        t = (r["cls_lay"] or r["cls_sch"] or "?").lower()
        by_type[(r["cat"], t)] += 1
    print("by (class,type):", dict(by_type), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
