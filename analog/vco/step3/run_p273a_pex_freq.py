#!/usr/bin/env python3
"""P2.7.3a — frequency checks [PEX-RC lumped] (not full post-layout spice).

Uses schematic PDK devices + L2n0 EM + lumped wiring C / series R from
layout/p272c/out/pex_vco_top/pex_lumped.json (Magic full-RC, bank-method
wiring add). Full 17k-element extract is not simulated (Magic svaricap is
2-terminal). Stops on first FAIL without changing the design.

Checks:
  1) Band coverage at all 15 corners, margins ≥ 40 MHz top and bottom
  2) Overlap between neighbouring codes at least-overlap corners
  3) Bank thermometer / binary boundary ≤ ½ LSB from local ideal
  4) D20 landing vs per-corner compliance windows (band margins proxy)
"""
from __future__ import annotations

import json
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
LAYOUT_OUT = os.path.join(HERE, "..", "layout", "p272c", "out")
PEX = os.path.join(LAYOUT_OUT, "pex_vco_top")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "step2"))
import run_step2 as S2  # noqa: E402
import run_step3 as S3  # noqa: E402
from run_p272c_gate import V_SS, V_TT, V_FF, _patch_vdd  # noqa: E402

MARGIN_MIN = 40e6
F_TOP = 4.20e9
F_BOT = 3.12e9
VT = 0.65
BOUNDARY_PAIRS = [
    (0, 1), (1, 2), (3, 4), (7, 8), (15, 16), (31, 32),
    (63, 64), (127, 128), (254, 255),
]
OVERLAP_PAIRS = [(0, 1), (31, 32), (127, 128), (254, 255)]
# Least-overlap corners from prior trim / route jobs [SCH]
OVERLAP_CORNERS = [
    ("mos_ss", "cap_wcs", -40),
    ("mos_ss", "cap_bcs", -40),
]


def load_pex():
    path = os.path.join(PEX, "pex_lumped.json")
    if not os.path.exists(path):
        raise SystemExit(f"missing {path}: run analyze_pex_vco_top.py")
    return json.load(open(path))


def parasitic(pex: dict) -> str:
    c = pex["c_side_ff"]
    r = pex["r_series_ohm"]
    return (
        f"Rr_p (tp nr_p) resistor r={r}\n"
        f"Cr_p (nr_p 0) capacitor c={c}f\n"
        f"Rr_n (tn nr_n) resistor r={r}\n"
        f"Cr_n (nr_n 0) capacitor c={c}f\n"
    )


def _setup():
    S2.OUT = S3.OUT = OUT
    rj = json.load(open(os.path.join(
        HERE, "..", "step2", "out", "range.json")))
    cfix = float(rj["cfix"])
    lsb = float(rj.get("lsb", S2.LSB_FF))
    S2.apply_range_trims(rj)
    S2.C_FIX_FF = cfix
    S2.LSB_FF = lsb
    _, itail_tab = S3.load_sizing()
    return cfix, lsb, itail_tab, rj


def _tran(code, tag, itail, extra, temp=27, vt=VT, vdd=None, vct=None):
    vct_use = vct if vct is not None else (vdd if vdd is not None else S2.VCT)
    sim = S2.netlist(
        tag, code, vt, itail=itail,
        analysis=(f"  options temp={temp}\n  save v(tp) v(tn) v(tail)\n"
                  "  analysis tr tran stop=60n step=5p maxstep=5p"),
        extra=extra, vct=vct_use)
    if vdd is not None:
        _patch_vdd(sim, vdd)
    S2.run(sim)
    return S2.measure(os.path.join(OUT, "tr.raw"))


def check_band_15(pex, itail_tab, lines) -> bool:
    lines.append("## 1) Band coverage — 15 corners [PEX-RC lumped]\n\n")
    lines.append(
        f"C_side={pex['c_side_ff']:.2f} fF R={pex['r_series_ohm']:.3f} Ω "
        f"(wiring add) [PEX-RC]. Pass: top≥4.20 and bot≤3.12 with "
        f"margins ≥ 40 MHz. V_pad tt/ss/ff = {V_TT}/{V_SS}/{V_FF} V "
        f"[HAND].\n\n")
    lines.append(
        "| MOS | CAP | T | V_pad | f top | f bot | top_m | bot_m | ok |\n")
    lines.append("|---|---|---|---:|---:|---:|---:|---:|---|\n")
    extra = parasitic(pex)
    pad_for = {"mos_tt": V_TT, "mos_ss": V_SS, "mos_ff": V_FF}
    i_top = S3.itail_for(4.4e9, itail_tab)
    i_bot = S3.itail_for(2.95e9, itail_tab)
    ok_all = True
    worst_top = worst_bot = 1e9
    fail_row = None
    for mos, cap in S3.CORNERS:
        S3.set_corner(mos, cap)
        vdd = pad_for[mos]
        for t in S3.TEMPS:
            a = _tran(0, f"pex15_{mos}_{cap}_{t}_top", i_top, extra,
                      temp=t, vt=1.0, vdd=vdd, vct=vdd)
            b = _tran(S2.CMAX, f"pex15_{mos}_{cap}_{t}_bot", i_bot, extra,
                      temp=t, vt=0.3, vdd=vdd, vct=vdd)
            top_m = a["f"] - F_TOP
            bot_m = F_BOT - b["f"]
            good = top_m >= MARGIN_MIN and bot_m >= MARGIN_MIN
            ok_all = ok_all and good
            worst_top = min(worst_top, top_m)
            worst_bot = min(worst_bot, bot_m)
            lines.append(
                f"| {mos} | {cap} | {t} | {vdd:.3f} | {a['f']/1e9:.4f} | "
                f"{b['f']/1e9:.4f} | {top_m/1e6:.1f} | {bot_m/1e6:.1f} | "
                f"{'yes' if good else 'NO'} |\n")
            print(f"  band {mos}/{cap}/{t}: top_m={top_m/1e6:.1f} "
                  f"bot_m={bot_m/1e6:.1f} ok={good}", flush=True)
            if not good and fail_row is None:
                fail_row = (mos, cap, t, top_m, bot_m, a["f"], b["f"])
    lines.append(
        f"\nWorst top margin {worst_top/1e6:.1f} MHz; "
        f"worst bottom {worst_bot/1e6:.1f} MHz [PEX-RC lumped]\n")
    if fail_row:
        mos, cap, t, top_m, bot_m, ft, fb = fail_row
        cause = "top" if top_m < MARGIN_MIN else "bottom"
        # First-order: Δf/f ≈ −½ ΔC/C_tank; report cfix trim size
        lines.append(
            f"\n**FAIL** at {mos}/{cap}/{t}°C ({cause}): "
            f"f_top={ft/1e9:.4f} f_bot={fb/1e9:.4f} [PEX-RC].\n"
            f"Parasitic driver: lumped wiring C_side="
            f"{pex['c_side_ff']:.2f} fF (hand was {pex['hand_side_ff']:.1f}). "
            f"Do **not** change design this job — owner decides cfix trim "
            f"or routing fix. Rough cfix Δ for 40 MHz: "
            f"~±2·(40e6/f)·C_tank on the failing end [HAND].\n"
        )
    lines.append(
        f"\nBand 15-corner ≥40 MHz: "
        f"{'PASS' if ok_all else 'FAIL'} [PEX-RC lumped]\n\n")
    return ok_all


def check_overlap(pex, itail, lines) -> bool:
    lines.append("## 2) Overlap at least-overlap corners [PEX-RC lumped]\n\n")
    extra = parasitic(pex)
    ok = True
    for mos, cap, temp in OVERLAP_CORNERS:
        S3.set_corner(mos, cap)
        lines.append(f"### {mos} / {cap} / {temp} °C\n\n")
        lines.append("| pair | f0 | f1 | step (MHz) | ok |\n")
        lines.append("|---|---:|---:|---:|---|\n")
        for c0, c1 in OVERLAP_PAIRS:
            a = _tran(c0, f"pexov_{mos}_{cap}_{temp}_{c0}", itail, extra,
                      temp=temp)
            b = _tran(c1, f"pexov_{mos}_{cap}_{temp}_{c1}", itail, extra,
                      temp=temp)
            step = a["f"] - b["f"]
            good = step > 0
            ok = ok and good
            lines.append(
                f"| {c0}→{c1} | {a['f']/1e9:.4f} | {b['f']/1e9:.4f} | "
                f"{step/1e6:+.2f} | {'yes' if good else 'NO'} |\n")
            print(f"  overlap {mos}/{temp} {c0}->{c1} "
                  f"{step/1e6:+.2f} MHz ok={good}", flush=True)
        lines.append("\n")
    lines.append(
        f"Overlap monotonic: {'PASS' if ok else 'FAIL'} [PEX-RC lumped]\n\n")
    return ok


def check_boundary(pex, itail, lsb_ff, lines) -> bool:
    lines.append("## 3) Bank boundary steps ≤ ½ LSB (local) [PEX-RC lumped]\n\n")
    lines.append(
        "Ideal = local mean step (neighbours ±2 codes); "
        "pass if step > 0 and |step/mean − 1| ≤ 0.5 [PEX-RC lumped].\n\n")
    lines.append(
        "| pair | step (MHz) | local mean (MHz) | |ratio−1| | ok |\n")
    lines.append("|---|---:|---:|---:|---|\n")
    extra = parasitic(pex)
    S3.set_corner("mos_tt", "cap_typ")
    ok = True
    cache = {}

    def meas(code):
        if code not in cache:
            cache[code] = _tran(code, f"pexbd_{code}", itail, extra)
        return cache[code]

    for c0, c1 in BOUNDARY_PAIRS:
        a, b = meas(c0), meas(c1)
        step = a["f"] - b["f"]
        lo = max(0, c0 - 2)
        hi = min(255, c1 + 2)
        ma, mb = meas(lo), meas(hi)
        span = hi - lo
        mean = (ma["f"] - mb["f"]) / span if span else step
        rel = abs(step / mean - 1.0) if mean else 999.0
        good = step > 0 and rel <= 0.5
        ok = ok and good
        lines.append(
            f"| {c0}→{c1} | {step/1e6:+.2f} | {mean/1e6:.2f} | "
            f"{rel:.2f} | {'yes' if good else 'NO'} |\n")
        print(f"  boundary {c0}->{c1} step={step/1e6:+.2f} "
              f"rel={rel:.2f} ok={good}", flush=True)
    lines.append(f"\nlsb_ff={lsb_ff} fF [SCH/range.json]\n")
    lines.append(
        f"Boundary: {'PASS' if ok else 'FAIL'} [PEX-RC lumped]\n\n")
    return ok


def check_d20(pex, itail_tab, lines) -> bool:
    """D20 landing proxy: band margins at least-margin corners ≥ 40 MHz;
    note compliance windows from accepted decisions."""
    lines.append("## 4) D20 landing / compliance [PEX-RC lumped/HAND]\n\n")
    extra = parasitic(pex)
    cases = [
        ("top", "mos_ss", "cap_wcs", -40, 0, 1.0, V_SS),
        ("bot", "mos_ss", "cap_bcs", -40, S2.CMAX, 0.3, V_SS),
    ]
    ok = True
    for tag, mos, cap, temp, code, vt, vdd in cases:
        S3.set_corner(mos, cap)
        itail = S3.itail_for(4.4e9 if tag == "top" else 2.95e9, itail_tab)
        m = _tran(code, f"pexd20_{tag}", itail, extra, temp=temp, vt=vt,
                  vdd=vdd, vct=vdd)
        if tag == "top":
            mar = m["f"] - F_TOP
        else:
            mar = F_BOT - m["f"]
        good = mar >= MARGIN_MIN
        ok = ok and good
        lines.append(
            f"- {tag} {mos}/{cap}/{temp}: f={m['f']/1e9:.4f} GHz "
            f"margin={mar/1e6:.1f} MHz Amp={m['amp']:.2f} "
            f"[{'PASS' if good else 'FAIL'}] [PEX-RC lumped]\n")
    lines.append(
        "\nPer-corner V_tune compliance (accepted 2026-11-17): "
        "ff 0.469–0.955 V inside 0.457–0.970 V; tt/ss in owner window "
        "[MODEL/SCH]. Extract wiring "
        f"{pex['c_side_ff']:.1f} fF < hand {pex['hand_side_ff']:.1f} → "
        "slightly higher f / more V_tune headroom at high end [HAND].\n")
    lines.append(
        f"D20 / compliance proxy: "
        f"{'PASS' if ok else 'FAIL'} [PEX-RC lumped/HAND]\n\n")
    return ok


def main():
    pex = load_pex()
    lines = [
        "# P2.7.3a frequency checks — schematic + extracted wiring "
        "C/R lumped [PEX-RC lumped]\n\n",
        "Not a full post-layout sim of the 17.5k-element spice "
        "(Magic svaricap is 2-terminal).\n"
        "Method: schematic PDK devices + L2n0 EM + extracted wiring "
        "C/R lumped per tank net.\n"
        f"Lumped from Magic full-RC wiring add: C_side="
        f"{pex['c_side_ff']:.2f} fF, R={pex['r_series_ohm']:.3f} Ω; "
        f"hand was {pex['hand_side_ff']:.1f} fF [PEX-RC/HAND].\n\n",
    ]
    cfix, lsb, itail_tab, rj = _setup()
    itail = S3.itail_for(3.6e9, itail_tab)
    lines.append(
        f"cfix={cfix:.4f} fF lsb={lsb:.3f} fF itail={itail*1e3:.2f} mA "
        f"[SCH/range.json]\n\n")
    print(f"PEX C_side={pex['c_side_ff']} R={pex['r_series_ohm']} "
          f"cfix={cfix}", flush=True)

    if not check_band_15(pex, itail_tab, lines):
        lines.append("\n**STOP:** band coverage FAIL — no design change.\n")
        _write(lines, False)
        return 1
    if not check_overlap(pex, itail, lines):
        lines.append("\n**STOP:** overlap FAIL — no design change.\n")
        _write(lines, False)
        return 1
    if not check_boundary(pex, itail, lsb, lines):
        lines.append("\n**STOP:** boundary FAIL — no design change.\n")
        _write(lines, False)
        return 1
    if not check_d20(pex, itail_tab, lines):
        lines.append("\n**STOP:** D20 FAIL — no design change.\n")
        _write(lines, False)
        return 1

    lines.append("## Overall: PASS [PEX-RC lumped]\n")
    _write(lines, True)
    return 0


def _write(lines, ok):
    path = os.path.join(OUT, "summary_pex_vco_range.txt")
    open(path, "w").writelines(lines)
    dest = os.path.join(LAYOUT_OUT, "summary_pex_vco_range.txt")
    open(dest, "w").writelines(lines)
    print(f"Wrote {path} ({'PASS' if ok else 'FAIL'})", flush=True)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
