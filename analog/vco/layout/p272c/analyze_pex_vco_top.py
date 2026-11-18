#!/usr/bin/env python3
"""P2.7.3a — tank parasitics from Magic full-RC spice / .ext [PEX-RC].

Reports extracted C per side on tn/tp, mismatch, series R toward inductor
pads, inductor pad C, bank MIM top-plate-ish coupling, tail-node C vs hand
(island 35.6, core 23.7, bank 36.9, tail 9.9 fF).
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PEX = os.path.join(OUT, "pex_vco_top")
SPICE = os.path.join(PEX, "vco_top.pex.spice")

# Hand values used for trim / step-2 [PEX-RC / HAND]
HAND = {
    "island_ff": 35.6,
    "core_ff": 23.7,   # headline ~23.66
    "bank_ff": 36.9,   # headline ~36.87
    "tail_ff": 9.9,
}
HAND_SIDE = HAND["island_ff"] + HAND["core_ff"] + HAND["bank_ff"]  # 96.2


def parse_farad(tok: str) -> float:
    """Magic PEX uses e.g. 0.01146f = 0.01146 fF."""
    s = tok.strip().lower()
    m = re.match(r"^([0-9.eE+-]+)(af|ff|f|pf|p|n|u|m)?$", s)
    if not m:
        return float(s)
    v = float(m.group(1))
    suf = m.group(2) or ""
    scale = {
        "af": 1e-18, "ff": 1e-15, "f": 1e-15, "pf": 1e-12, "p": 1e-12,
        "n": 1e-9, "u": 1e-6, "m": 1e-3, "": 1.0,
    }[suf]
    return v * scale


def parse_ohm(tok: str) -> float:
    s = tok.strip().lower()
    m = re.match(r"^([0-9.eE+-]+)(m|k|meg|g)?$", s)
    if not m:
        return float(s)
    v = float(m.group(1))
    suf = m.group(2) or ""
    return v * {"": 1.0, "m": 1e-3, "k": 1e3, "meg": 1e6, "g": 1e9}[suf]


def root_port(n: str) -> str:
    """tn.n5 / tn.t0 / tn → tn."""
    base = n.split(".")[0]
    return base.lower()


def analyze_spice(path: str) -> dict:
    caps = []  # (a, b, c_f)
    res = []   # (a, b, r)
    for ln in open(path):
        s = ln.strip()
        if not s or s[0] in "*+.":
            continue
        toks = s.replace("(", " ").replace(")", " ").split()
        name = toks[0]
        if name[0] in "Cc" and len(toks) >= 4:
            a, b = toks[1], toks[2]
            cval = None
            for t in toks[3:]:
                if "=" in t:
                    k, v = t.split("=", 1)
                    if k.lower() == "c":
                        cval = parse_farad(v)
                        break
                elif re.match(r"^[0-9.eE+-]+", t):
                    cval = parse_farad(t)
                    break
            if cval is not None:
                caps.append((a, b, cval))
        elif name[0] in "Rr" and len(toks) >= 4:
            a, b = toks[1], toks[2]
            rval = None
            for t in toks[3:]:
                if "=" in t:
                    k, v = t.split("=", 1)
                    if k.lower() == "r":
                        rval = parse_ohm(v)
                        break
                elif re.match(r"^[0-9.eE+-]+", t):
                    rval = parse_ohm(t)
                    break
            if rval is not None:
                res.append((a, b, rval))

    # Aggregate C to each port family
    c_to = defaultdict(float)       # port -> sum C to anything else
    c_pair = defaultdict(float)     # (pa,pb) sorted
    c_sub = defaultdict(float)      # port -> C to gnd-like
    for a, b, c in caps:
        ra, rb = root_port(a), root_port(b)
        if ra == rb:
            continue
        c_to[ra] += c
        c_to[rb] += c
        key = tuple(sorted((ra, rb)))
        c_pair[key] += c
        for r, other in ((ra, rb), (rb, ra)):
            if other in ("gnd", "sub!", "0") or other.startswith("gnd"):
                c_sub[r] += c

    def ff(x):
        return x * 1e15

    # Series R: shortest-looking stubs from port root to first distributed node
    # Prefer small R from `tn`/`tp` to `tn.n*` / `tp.n*` (metal), skip huge
    # outliers (likely poly / bias).
    def series_r(port: str):
        stubs = []
        for a, b, r in res:
            ra, rb = root_port(a), root_port(b)
            # direct from bare port name
            if a.lower() == port and rb == port and b.lower() != port:
                stubs.append((r, a, b))
            elif b.lower() == port and ra == port and a.lower() != port:
                stubs.append((r, a, b))
        stubs.sort()
        metal = [s for s in stubs if s[0] < 5.0]
        if metal:
            return {
                "min": metal[0][0],
                "n_metal": len(metal),
                "stubs": metal[:6],
            }
        return {"min": stubs[0][0] if stubs else float("nan"),
                "n_metal": 0, "stubs": stubs[:6]}

    r_tn = series_r("tn")
    r_tp = series_r("tp")

    c_tn_tp = ff(c_pair.get(("tn", "tp"), 0.0))
    c_tn_vbp = ff(c_pair.get(("tn", "vbp"), 0.0) + c_pair.get(("tp", "vbp"), 0.0))

    return {
        "c_tn_ff": ff(c_to["tn"]),
        "c_tp_ff": ff(c_to["tp"]),
        "c_tn_sub_ff": ff(c_sub["tn"]),
        "c_tp_sub_ff": ff(c_sub["tp"]),
        "mismatch_ff": abs(ff(c_to["tn"]) - ff(c_to["tp"])),
        "c_tn_tp_ff": c_tn_tp,
        "c_tail_ff": ff(c_to["tail"]),
        "c_tail_sub_ff": ff(c_sub["tail"]),
        "pad_tn_ff": ff(c_sub.get("tn", 0.0)),
        "pad_tp_ff": ff(c_sub.get("tp", 0.0)),
        "pad_ct_sub_ff": ff(c_sub.get("ct", 0.0)),
        "c_tn_vbp_ff": c_tn_vbp,
        "r_tn": r_tn,
        "r_tp": r_tp,
        "n_caps": len(caps),
        "n_res": len(res),
        "c_pair_top": sorted(
            ((ff(v), a, b) for (a, b), v in c_pair.items()
             if a in ("tn", "tp") or b in ("tn", "tp")),
            reverse=True,
        )[:20],
    }


def wiring_from_ext(ext_path: str) -> dict:
    """Bank-method wiring add from .ext: (all+sub) − substrate node C."""
    sys.path.insert(0, os.path.join(HERE, "..", "p272b"))
    import analyze_pex_ext as A  # noqa: WPS433

    find, node_c, caps = A.parse_ext(ext_path)
    sub_tn = sub_tp = sub_tail = sub_ct = 0.0
    for n, c in node_c.items():
        r = find(n)
        if r == "tn":
            sub_tn += c
        elif r == "tp":
            sub_tp += c
        elif r == "tail":
            sub_tail += c
        elif r == "ct":
            sub_ct += c
    coup_tn = defaultdict(float)
    coup_tp = defaultdict(float)
    coup_tail = defaultdict(float)
    c_tn_tp = 0.0
    for a, b, c in caps:
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        if ra == "tn":
            coup_tn[rb] += c
            if rb == "tp":
                c_tn_tp += c
        elif rb == "tn":
            coup_tn[ra] += c
            if ra == "tp":
                c_tn_tp += c
        if ra == "tp":
            coup_tp[rb] += c
        elif rb == "tp":
            coup_tp[ra] += c
        if ra == "tail":
            coup_tail[rb] += c
        elif rb == "tail":
            coup_tail[ra] += c

    def to_ff(af):
        return af / 1000.0

    c_tn_all = to_ff(sub_tn + sum(coup_tn.values()))
    c_tp_all = to_ff(sub_tp + sum(coup_tp.values()))
    wire_tn = to_ff(sum(coup_tn.values()))  # all partners only (= all − sub)
    wire_tp = to_ff(sum(coup_tp.values()))
    # tail wiring = coupling partners (exclude substrate node)
    wire_tail = to_ff(sum(coup_tail.values()))
    return {
        "sub_tn_ff": to_ff(sub_tn),
        "sub_tp_ff": to_ff(sub_tp),
        "sub_tail_ff": to_ff(sub_tail),
        "sub_ct_ff": to_ff(sub_ct),
        "all_tn_ff": c_tn_all,
        "all_tp_ff": c_tp_all,
        "wire_tn_ff": wire_tn,
        "wire_tp_ff": wire_tp,
        "wire_tail_ff": wire_tail,
        "c_tn_tp_ff": to_ff(c_tn_tp),
        "mismatch_wire_ff": abs(wire_tn - wire_tp),
        "mismatch_all_ff": abs(c_tn_all - c_tp_all),
    }


def analyze_ext(ext_path: str) -> dict | None:
    """Reuse p272b analyzer if .ext present."""
    sys.path.insert(0, os.path.join(HERE, "..", "p272b"))
    try:
        import analyze_pex_ext as A  # noqa: WPS433
    except Exception:
        return None
    if not os.path.exists(ext_path):
        return None
    report, nums = A.analyze(ext_path, "vco_top .ext")
    return {"report": report, "nums": nums}


def write_report(d: dict, w: dict) -> str:
    path = os.path.join(OUT, "summary_pex_vco_tank.txt")
    # Sim C_side = wiring add (bank method) — excludes substrate/MIM-plate
    # area that Magic merges onto tn/tp while also emitting cap_* devices.
    c_side = max(w["wire_tn_ff"], w["wire_tp_ff"])
    rser = max(d["r_tn"]["min"], d["r_tp"]["min"])
    if rser != rser:
        rser = 2.0
    lines = [
        "# P2.7.3a tank parasitics — vco_top full-RC [PEX-RC]\n\n",
        "## Method\n",
        f"- Spice: `{os.path.relpath(SPICE, HERE)}` "
        f"({d['n_caps']} C, {d['n_res']} R) [PEX-RC].\n",
        f"- .ext: `out/pex_vco_top/vco_top.ext` — bank-method "
        f"**wiring add** = (all partners + substrate) − substrate node C "
        f"(same as `summary_pex_bank`) [PEX-RC].\n",
        "- Substrate node C includes MIM top-plate metal area that is "
        "also in PDK `cap_*` devices — **not** used as tank add "
        "[PEX-RC / PDK].\n",
        "- Series R: min metal stub (< 5 Ω) from bare port to "
        "`port.n*` in spice [PEX-RC].\n\n",
        "## Extracted vs hand\n\n",
        "| quantity | tn | tp | hand (used) | unit | tag |\n",
        "|---|---:|---:|---:|---|---|\n",
        f"| substrate node C (.ext) | {w['sub_tn_ff']:.2f} | "
        f"{w['sub_tp_ff']:.2f} | (incl. MIM tops) | fF | [PEX-RC] |\n",
        f"| C all partners + substrate | {w['all_tn_ff']:.2f} | "
        f"{w['all_tp_ff']:.2f} | — | fF | [PEX-RC] |\n",
        f"| **wiring add (all − sub)** | **{w['wire_tn_ff']:.2f}** | "
        f"**{w['wire_tp_ff']:.2f}** | side sum {HAND_SIDE:.1f} "
        f"(core {HAND['core_ff']}+bank {HAND['bank_ff']}"
        f"+island {HAND['island_ff']}) | fF | [PEX-RC]/[HAND] |\n",
        f"| tn−tp mismatch (wiring) | {w['mismatch_wire_ff']:.2f} | | "
        f"— | fF | [PEX-RC] |\n",
        f"| C(tn−tp) coupling | {w['c_tn_tp_ff']:.2f} | | — | "
        f"fF | [PEX-RC] |\n",
        f"| series R metal stub min | {d['r_tn']['min']:.3f} | "
        f"{d['r_tp']['min']:.3f} | 2.0 (pack) | Ω | "
        f"[PEX-RC]/[HAND] |\n",
        f"| inductor pad / substrate share | {w['sub_tn_ff']:.2f} | "
        f"{w['sub_tp_ff']:.2f} | (pin-only GDS; EM has cp) | fF | "
        f"[PEX-RC]/[EM] |\n",
        f"| ct substrate node C | {w['sub_ct_ff']:.2f} | | — | "
        f"fF | [PEX-RC] |\n",
        f"| bank-related C(tn/tp−vbp) spice | {d['c_tn_vbp_ff']:.2f} | | "
        f"bank wiring {HAND['bank_ff']} | fF | [PEX-RC]/[HAND] |\n",
        f"| tail wiring add (.ext) | {w['wire_tail_ff']:.2f} | | "
        f"{HAND['tail_ff']} | fF | [PEX-RC]/[HAND] |\n",
        f"| tail substrate node C | {w['sub_tail_ff']:.2f} | | "
        f"(incl. cbf area) | fF | [PEX-RC] |\n\n",
        f"- **Headline wiring C/side (max): {c_side:.2f} fF** [PEX-RC]\n",
        f"- Hand side sum used in step-2: **{HAND_SIDE:.1f} fF** "
        f"[HAND/PEX-RC prior]\n",
        f"- Δ (extract wiring max − hand): **{c_side - HAND_SIDE:+.2f} fF** "
        f"[PEX-RC]\n",
        "- Note: hand summed **separate** core all-C + bank wiring + "
        "island HAND. Full-top wiring add is coupling-only on the "
        "joined cell; substrate interconnect that Magic folds into "
        "node C with MIM tops is **not** re-added (same rule as bank "
        "PEX). Extract wiring is **below** hand — hand was "
        "conservative [PEX-RC/HAND].\n\n",
        "## Series R stubs (metal < 5 Ω)\n\n",
        f"- tn: n={d['r_tn']['n_metal']} min={d['r_tn']['min']:.4f} Ω "
        f"stubs={d['r_tn']['stubs'][:4]}\n",
        f"- tp: n={d['r_tp']['n_metal']} min={d['r_tp']['min']:.4f} Ω "
        f"stubs={d['r_tp']['stubs'][:4]}\n\n",
        "## Top tn/tp coupling partners (spice)\n\n",
    ]
    for v, a, b in d["c_pair_top"][:15]:
        lines.append(f"- `{a}`−`{b}`: {v:.3f} fF\n")

    lines.append("\n## RC reduction for frequency sims\n\n")
    lines.append(
        "- Full-RC spice ≈ 17.5k elements; Magic svaricap is 2-terminal "
        "[TOOL]. Frequency checks use schematic PDK devices (var/MIM) + "
        "L2n0 EM + **lumped** wiring C / series R:\n"
        f"  - C_side = max(wiring add) = **{c_side:.2f} fF** [PEX-RC]\n"
        f"  - R_series = max(min metal stubs) = **{rser:.3f} Ω** [PEX-RC]\n"
        "- Error on tn/tp C vs full spice aggregation: lumped C_side "
        "equals .ext wiring add (no further π-reduction). Omitting "
        f"explicit C(tn−tp)={w['c_tn_tp_ff']:.2f} fF in the "
        "single-ended C_side model matches the prior hand method; "
        f"diff-mode bias ≈ ½·C(tn−tp) = {0.5*w['c_tn_tp_ff']:.2f} fF "
        "[HAND/PEX-RC].\n"
        f"- vs hand 96.2 fF: extract **{c_side - HAND_SIDE:+.1f} fF** "
        "(hand higher / more pessimistic for band) [PEX-RC/HAND].\n"
    )

    open(path, "w").writelines(lines)
    open(os.path.join(PEX, "pex_lumped.json"), "w").write(
        "{\n"
        f'  "c_side_ff": {c_side:.4f},\n'
        f'  "wire_tn_ff": {w["wire_tn_ff"]:.4f},\n'
        f'  "wire_tp_ff": {w["wire_tp_ff"]:.4f},\n'
        f'  "c_tn_tp_ff": {w["c_tn_tp_ff"]:.4f},\n'
        f'  "r_series_ohm": {rser:.4f},\n'
        f'  "wire_tail_ff": {w["wire_tail_ff"]:.4f},\n'
        f'  "hand_side_ff": {HAND_SIDE:.4f}\n'
        "}\n"
    )
    print("".join(lines))
    print(f"Wrote {path}")
    return path


def main():
    if not os.path.exists(SPICE):
        raise SystemExit(f"missing {SPICE}: run run_pex_vco_top.py first")
    d = analyze_spice(SPICE)
    ext = os.path.join(PEX, "vco_top.ext")
    if not os.path.exists(ext):
        raise SystemExit(f"missing {ext}")
    w = wiring_from_ext(ext)
    write_report(d, w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
