#!/usr/bin/env python3
"""Compare every device parameter: flat sch vs extract within PDK grid [TOOL].

Used when KLayout unique fails only on a recorded tool limitation but netgen
+ connectivity pass. Multiset compare by (class, snapped key params).
Writes out/summary_device_param_compare.txt.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PDK_GRID_UM = 0.01  # [DS] SG13G2 drawn grid


def len_to_um(tok: str) -> float | None:
    s = tok.strip().rstrip(",")
    if not s:
        return None
    try:
        if s[-1] in "uU":
            return float(s[:-1])
        if s[-1] in "nN":
            return float(s[:-1]) * 1e-3
        v = float(s)
    except ValueError:
        return None
    if abs(v) < 1e-3:
        return v * 1e6
    return v


def snap(um: float) -> float:
    return round(round(um / PDK_GRID_UM) * PDK_GRID_UM, 4)


def parse_devices(path: str) -> list[tuple]:
    """Return list of (cls, key_tuple) from a flat spice/cir body."""
    txt = open(path, errors="ignore").read()
    # strip .subckt wrappers — keep device lines
    rows = []
    for ln in txt.splitlines():
        s = ln.strip()
        if not s or s.startswith("*") or s.startswith("."):
            continue
        # device: leading letter + name, then nets, then model
        parts = s.split()
        if len(parts) < 4:
            continue
        # find model token (known device names)
        model = None
        mi = None
        for i, p in enumerate(parts):
            pl = p.lower()
            if pl in (
                "rfcmim", "cap_rfcmim", "cap_cmim", "rhigh",
                "sg13_lv_nmos", "sg13_lv_pmos", "sg13_hv_nmos",
                "sg13_hv_pmos", "sg13_hv_svaricap", "sg13_hv_svaricap_fx",
                "nmosi", "pmosi", "nmosihv",
            ) or "cmim" in pl or "rfcmim" in pl:
                model = pl
                mi = i
                break
        if model is None:
            continue
        # normalize class names
        if model in ("cap_rfcmim", "rfcmim"):
            cls = "rfcmim"
        elif model == "cap_cmim":
            cls = "cap_cmim"
        elif model.endswith("_fx"):
            cls = model[:-3]
        else:
            cls = model
        params = {}
        for p in parts[mi + 1:]:
            if "=" in p:
                k, v = p.split("=", 1)
                params[k.lower()] = v
        w = len_to_um(params["w"]) if "w" in params else None
        l = len_to_um(params["l"]) if "l" in params else None
        # MOS may use W/L uppercase already captured lower
        m = float(params.get("m", params.get("mf", "1")))
        ng = float(params.get("ng", "1")) if "ng" in params else None
        b = float(params.get("b", "0")) if "b" in params else None
        wfeed = len_to_um(params["wfeed"]) if "wfeed" in params else None
        key = (
            cls,
            snap(w) if w is not None else None,
            snap(l) if l is not None else None,
            m,
            snap(wfeed) if wfeed is not None else None,
            ng,
            b,
        )
        rows.append(key)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sch", default=os.path.join(OUT, "vco_top_klayout.spice"))
    ap.add_argument("--lay",
                    default=os.path.join(OUT, "vco_top_extracted_klayout.cir"))
    ap.add_argument("--out",
                    default=os.path.join(OUT, "summary_device_param_compare.txt"))
    args = ap.parse_args()
    if not os.path.exists(args.sch) or not os.path.exists(args.lay):
        # fall back to unsapped names
        sch = args.sch if os.path.exists(args.sch) else \
            os.path.join(OUT, "vco_top_sch_flat.spice")
        lay = args.lay if os.path.exists(args.lay) else \
            os.path.join(OUT, "lvs_vco_top", "vco_top_lvs_extracted.cir")
    else:
        sch, lay = args.sch, args.lay
    if not os.path.exists(sch) or not os.path.exists(lay):
        print(f"FAIL: missing sch={sch} lay={lay}", flush=True)
        return 1

    s_rows = parse_devices(sch)
    l_rows = parse_devices(lay)
    cs, cl = Counter(s_rows), Counter(l_rows)
    only_s = cs - cl
    only_l = cl - cs
    lines = [
        "# Device parameter compare (flattened sch vs extract) [TOOL]",
        f"sch={sch}",
        f"lay={lay}",
        f"PDK_GRID_UM={PDK_GRID_UM}",
        f"sch_devices={len(s_rows)} lay_devices={len(l_rows)}",
        f"sch_unique_keys={len(cs)} lay_unique_keys={len(cl)}",
        f"only_sch={sum(only_s.values())} only_lay={sum(only_l.values())}",
        "",
    ]
    ok = sum(only_s.values()) == 0 and sum(only_l.values()) == 0
    lines.append(f"PASS={ok} (all device keys equal within PDK grid)")
    if only_s:
        lines.append("## only in schematic")
        for k, n in sorted(only_s.items(), key=lambda x: (-x[1], x[0])):
            lines.append(f"  n={n} {k}")
    if only_l:
        lines.append("## only in layout")
        for k, n in sorted(only_l.items(), key=lambda x: (-x[1], x[0])):
            lines.append(f"  n={n} {k}")
    # class count compare
    def by_cls(counter):
        c = Counter()
        for k, n in counter.items():
            c[k[0]] += n
        return c
    lines.append("")
    lines.append("## class counts")
    sc, lc = by_cls(cs), by_cls(cl)
    for name in sorted(set(sc) | set(lc)):
        lines.append(f"  {name}: sch={sc[name]} lay={lc[name]}")
    open(args.out, "w").write("\n".join(lines) + "\n")
    print(f"wrote {args.out}", flush=True)
    print(f"PASS={ok} sch={len(s_rows)} lay={len(l_rows)} "
          f"only_sch={sum(only_s.values())} only_lay={sum(only_l.values())}",
          flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
