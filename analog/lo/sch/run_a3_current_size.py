#!/usr/bin/env python3
"""P2.7.4a3 — size currents to floor with ≈1 dB margin; report vs D7 [SCH].

UHF path keeps I_latch ≥ floor/ss need. VHF ÷3 I_latch swept down (tailless
current scales with device W ∝ I). Converter / logic left at defaults unless
needed. Buffer B2 stays 4 if swing ≥ 0.5 V/side.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
V_MIN = 1.181
VCO_TYP = 3.59e-3
PLL_HAND = 1.5e-3
D7 = 10e-3
# Floor targets with ≈1 dB margin on the requirement
# UHF requirement ≤ −151 (layout C_ck note / a2); with 1 dB → aim ≤ −152
REQ_UHF, AIM_UHF = -151.0, -152.0
# VHF: chain floor ≤ −150 [PROP] lo-divider-topology §1; +1 dB → aim ≤ −151
REQ_VHF, AIM_VHF = -150.0, -151.0
UHF_I = 0.75e-3
B2 = 4.0
# VHF I_latch candidates (mA)
VHF_I_SWEEP = (0.75, 0.60, 0.50, 0.40, 0.35, 0.30)


def buf_sw(d):
    n0 = int(0.7 * len(np.real(d["time"])))
    ckp = np.real(d["ckp"])[n0:]
    ckn = np.real(d["ckn"])[n0:]
    return float(0.25 * ((ckp.max() - ckp.min()) + (ckn.max() - ckn.min())))


def mean_flow(d, src):
    n0 = int(0.7 * len(np.real(d["time"])))
    for key in (f"{src}:flow(br)",):
        try:
            return float(np.mean(np.abs(np.real(d[key])[n0:])))
        except Exception:
            continue
    return float("nan")


def check_vhf(i_vhf):
    C.apply_knobs(i_latch=i_vhf, b2=B2, vhf_tailless=True)
    E.CORNERS["ss"] = ("ss", "mos_ss", V_MIN, 125)
    rows = []
    for f in (3.12e9, 4.20e9):
        path, names, ideal, ndiv, duty, v = E.build(
            "vhf", f, E.CORNERS["ss"], tag=f"_sz_{i_vhf*1e3:.2f}")
        d = E.run(path)
        r = E.analyse(d, names, ideal, ndiv, duty, v, f)
        sw = buf_sw(d)
        ib = mean_flow(d, "vbufs")
        ic = mean_flow(d, "vdvs")
        iv = mean_flow(d, "vcvs")
        ig = mean_flow(d, "vdgs")
        rows.append(dict(f=f, ok=bool(r["ok"]), phase=r["max_phase_err"],
                         sw=sw, ib=ib, ic=ic, iv=iv, ig=ig,
                         dmin=r.get("duty_min"), dmax=r.get("duty_max")))
        print(f"  VHF I={i_vhf*1e3:.2f} f={f/1e9:.2f} ok={r['ok']} "
              f"ph={r['max_phase_err']:.2f} sw={sw:.3f} "
              f"Icml={ic*1e3:.3f}", flush=True)
    return rows


def check_uhf():
    C.apply_knobs(i_latch=UHF_I, b2=B2, vhf_tailless=True)
    E.CORNERS["ss"] = ("ss", "mos_ss", V_MIN, 125)
    path, names, ideal, ndiv, duty, v = E.build(
        "uhf", 3.84e9, E.CORNERS["ss"], tag="_sz_uhf")
    d = E.run(path)
    r = E.analyse(d, names, ideal, ndiv, duty, v, 3.84e9)
    print(f"  UHF I={UHF_I*1e3:.2f} ss 3.84 ok={r['ok']} "
          f"ph={r['max_phase_err']:.2f}", flush=True)
    return bool(r["ok"]), r["max_phase_err"]


def run_noise(i_uhf, i_vhf):
    """Per-band noise: UHF at i_uhf, VHF at i_vhf (two invocations)."""
    env = os.environ.copy()
    env["LO_SCH_OUT"] = OUT
    # UHF
    subprocess.run(
        [sys.executable, "-u", os.path.join(os.path.dirname(__file__),
         "run_stage_noise.py"), "uhf", f"i={i_uhf*1e3:g}", f"b2={B2:g}"],
        cwd=os.path.dirname(__file__), env=env, check=False)
    sn_u = json.load(open(os.path.join(OUT, "stage_noise.json")))
    # VHF overwrites json — save UHF then run VHF
    Lu = sn_u.get("uhf", {}).get("L_sum", float("nan"))
    parts_u = sn_u.get("uhf", {}).get("parts", [])
    subprocess.run(
        [sys.executable, "-u", os.path.join(os.path.dirname(__file__),
         "run_stage_noise.py"), "vhf", f"i={i_vhf*1e3:g}", f"b2={B2:g}"],
        cwd=os.path.dirname(__file__), env=env, check=False)
    sn_v = json.load(open(os.path.join(OUT, "stage_noise.json")))
    Lv = sn_v.get("vhf", {}).get("L_sum", float("nan"))
    parts_v = sn_v.get("vhf", {}).get("parts", [])
    # restore combined json
    open(os.path.join(OUT, "stage_noise.json"), "w").write(json.dumps({
        "uhf": {"L_sum": Lu, "parts": parts_u},
        "vhf": {"L_sum": Lv, "parts": parts_v},
        "i_uhf": i_uhf, "i_vhf": i_vhf,
    }, indent=2) + "\n")
    return Lu, Lv, parts_u, parts_v


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(E.OUT, exist_ok=True)
    lines = [
        "# P2.7.4a3 — current sizing to floor + D7 [SCH]",
        "",
        f"UHF I_latch fixed {UHF_I*1e3:g} mA; B2={B2:g}; VHF_TAILLESS.",
        f"VHF requirement ≤ {REQ_VHF:.0f} dBc/Hz [PROP §1]; aim ≤ {AIM_VHF:.0f} "
        f"(≈1 dB margin).",
        f"UHF requirement ≤ {REQ_UHF:.0f}; aim ≤ {AIM_UHF:.0f}.",
        f"ss V_min={V_MIN} V. I_bias TB excluded from D7 (in PLL HAND).",
        "",
        "## Sweep VHF I_latch (divide + swing + current)",
        "",
        "| I_vhf | 3.12 | 4.20 | sw@4.20 | I_buf | I_CML | I_conv | I_logic | "
        "LO tot |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    print("\n".join(lines[:8]), flush=True)
    cand = []
    for ima in VHF_I_SWEEP:
        i = ima * 1e-3
        rows = check_vhf(i)
        ok = all(r["ok"] for r in rows)
        r420 = [r for r in rows if abs(r["f"] - 4.20e9) < 1][0]
        sw_ok = r420["sw"] >= 0.50 - 1e-3
        ib, ic, iv, ig = r420["ib"], r420["ic"], r420["iv"], r420["ig"]
        lo = ib + ic + iv + ig + VCO_TYP + PLL_HAND
        line = (
            f"| {ima:.2f} | {'OK' if rows[0]['ok'] else 'FAIL'} | "
            f"{'OK' if r420['ok'] else 'FAIL'} | {r420['sw']:.3f} | "
            f"{ib*1e3:.3f} | {ic*1e3:.3f} | {iv*1e3:.3f} | {ig*1e3:.3f} | "
            f"{lo*1e3:.2f} |"
        )
        print(line, flush=True)
        lines.append(line)
        if ok and sw_ok:
            cand.append(dict(i=i, lo=lo, ic=ic, ib=ib, iv=iv, ig=ig, sw=r420["sw"]))

    uhf_ok, uhf_ph = check_uhf()
    lines += [
        "",
        f"UHF ss 3.84 @ {UHF_I*1e3:g} mA: "
        f"{'OK' if uhf_ok else 'FAIL'} φ={uhf_ph:.2f}°",
        "",
        "## Pick smallest I_vhf that divides + swing, then check floors",
        "",
    ]
    if not cand:
        lines.append("**No candidate** met divide + 0.5 V/side.")
        open(os.path.join(OUT, "summary_a3_current_size.txt"), "w").write(
            "\n".join(lines) + "\n")
        print("SIZE_FAIL", flush=True)
        return 1

    # Prefer lowest LO total among candidates that we'll floor-check
    pick = min(cand, key=lambda c: c["lo"])
    # Actually want smallest I that still meets floor — walk from low I up
    cand_sorted = sorted(cand, key=lambda c: c["i"])
    chosen = None
    floor_rows = []
    for c in cand_sorted:
        print(f"floor check I_vhf={c['i']*1e3:.2f}…", flush=True)
        Lu, Lv, pu, pv = run_noise(UHF_I, c["i"])
        u_ok = Lu <= AIM_UHF
        v_ok = Lv <= AIM_VHF
        floor_rows.append((c, Lu, Lv, u_ok, v_ok, pu, pv))
        lines.append(
            f"- I_vhf={c['i']*1e3:.2f}: UHF {Lu:.1f} "
            f"({'PASS' if u_ok else 'FAIL'} vs {AIM_UHF:.0f}); "
            f"VHF {Lv:.1f} ({'PASS' if v_ok else 'FAIL'} vs {AIM_VHF:.0f}); "
            f"LO={c['lo']*1e3:.2f} mA"
        )
        print(f"  Lu={Lu:.1f} Lv={Lv:.1f} LO={c['lo']*1e3:.2f}", flush=True)
        if u_ok and v_ok:
            chosen = (c, Lu, Lv, pu, pv)
            break

    if chosen is None:
        # take best floor attempt
        best = floor_rows[-1] if floor_rows else None
        lines += [
            "",
            "**No I_vhf meets both floor aims.** Report best attempt and D7.",
            "",
        ]
        if best:
            c, Lu, Lv, _, _, pu, pv = best
            chosen = (c, Lu, Lv, pu, pv)

    c, Lu, Lv, pu, pv = chosen
    overrun = c["lo"] - D7
    d7_ok = c["lo"] <= D7 + 0.05e-3

    # Persist knobs
    knobs = dict(i_uhf=UHF_I, i_vhf=c["i"], b2=B2, vhf_tailless=True,
                 L_uhf=Lu, L_vhf=Lv, lo_vhf=c["lo"], lo_uhf=None)
    # UHF LO from measured at UHF_I — re-measure quickly
    C.apply_knobs(i_latch=UHF_I, b2=B2, vhf_tailless=True)
    E.CORNERS["tt"] = ("tt", "mos_tt", 1.20, 27)
    path, names, ideal, ndiv, duty, v = E.build(
        "uhf", 3.84e9, E.CORNERS["tt"], tag="_sz_uhf_tt")
    d = E.run(path)
    ib = mean_flow(d, "vbufs")
    ic = mean_flow(d, "vdvs")
    iv = mean_flow(d, "vcvs")
    ig = mean_flow(d, "vdgs")
    lo_u = ib + ic + iv + ig + VCO_TYP + PLL_HAND
    knobs["lo_uhf"] = lo_u
    open(os.path.join(OUT, "current_size_knobs.json"), "w").write(
        json.dumps(knobs, indent=2) + "\n")

    lines += [
        "",
        "## Selected",
        "",
        f"| Knob | Value |",
        f"|---|---|",
        f"| I_latch UHF | {UHF_I*1e3:g} mA |",
        f"| I_latch VHF | {c['i']*1e3:g} mA |",
        f"| B2 | {B2:g} µm |",
        f"| sw @ 4.20 ss | {c['sw']:.3f} V/side |",
        "",
        "## Per-stage noise (selected) [SCH]",
        "",
        f"| Band | Floor | Aim | Gate |",
        f"|---|---:|---:|---|",
        f"| UHF | {Lu:.1f} | ≤ {AIM_UHF:.0f} | "
        f"{'PASS' if Lu <= AIM_UHF else 'FAIL'} |",
        f"| VHF | {Lv:.1f} | ≤ {AIM_VHF:.0f} | "
        f"{'PASS' if Lv <= AIM_VHF else 'FAIL'} |",
        "",
        "### UHF stages (L→LO)",
        "",
        "| Stage | L→LO |",
        "|---|---:|",
    ]
    for p in pu:
        lines.append(f"| {p.get('stage')} | {p.get('L_lo', p.get('L')):.1f} |")
    lines += ["", "### VHF stages (L→LO)", "", "| Stage | L→LO |", "|---|---:|"]
    for p in pv:
        lines.append(f"| {p.get('stage')} | {p.get('L_lo', p.get('L')):.1f} |")

    lines += [
        "",
        "## LO current vs D7 [SCH chain + HAND VCO/PLL]",
        "",
        f"| Mode | I_buf | I_CML | I_conv | I_logic | +VCO+PLL | LO total |",
        f"|---|---:|---:|---:|---:|---:|---:|",
        f"| UHF tt | {ib*1e3:.3f} | {ic*1e3:.3f} | {iv*1e3:.3f} | "
        f"{ig*1e3:.3f} | 5.09 | **{lo_u*1e3:.2f}** |",
        f"| VHF ss | {c['ib']*1e3:.3f} | {c['ic']*1e3:.3f} | "
        f"{c['iv']*1e3:.3f} | {c['ig']*1e3:.3f} | 5.09 | "
        f"**{c['lo']*1e3:.2f}** |",
        "",
        f"D7 ≤ 10 mA: "
        f"{'PASS' if d7_ok else f'FAIL — VHF over by {overrun*1e3:.2f} mA'}.",
        "",
    ]
    if not d7_ok:
        lines += [
            "## STOP — D7 still over after sizing",
            "",
            f"Smallest VHF LO with floor aims met (or best attempt): "
            f"**{c['lo']*1e3:.2f} mA** (over by {overrun*1e3:.2f} mA).",
            "Options for owner:",
            "1. Raise D7 by ≥ that overrun for VHF typ.",
            "2. Accept weaker floor aim (drop 1 dB margin) / raise C_ck layout "
            "budget to allow lower I.",
            "3. Further shrink tailless clock W independent of I_latch "
            "(new knob) — not tried here.",
            "4. Cut converter clock-driver taper / logic size.",
            "",
        ]

    path = os.path.join(OUT, "summary_a3_current_size.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    print("WROTE", path, flush=True)
    print("SIZE_DONE", flush=True)
    return 0 if d7_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
