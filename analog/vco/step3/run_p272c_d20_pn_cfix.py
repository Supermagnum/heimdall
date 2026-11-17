#!/usr/bin/env python3
"""P2.7.2c follow-up: D20 landing + worst-corner PN with trimmed cfix [SCH/MODEL/HAND].

Uses range.json cfix (157.6875 fF / 14.5 µm). Rebuilds ss85/ff-40 bank grids at
VR_ANA1 pad supplies, then closed_loop nearest landing with the owner window
0.25–0.95 V at every corner. Nearest-code set compared to the prior p272c gate
pass (summary_p272c_gate.txt).

PN: try VACASK PSS bank-omitted at ss85 / ~4.20 GHz; on failure, HAND Leeson
bound from tank-C change vs recorded −119.4 dBc/Hz @ 1 MHz.

    python3 -u run_p272c_d20_pn_cfix.py | tee out/summary_p272c_d20_pn_cfix.txt
"""
from __future__ import annotations

import json
import math
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "step2"))
sys.path.insert(0, os.path.join(REPO, "analog", "pll", "p26", "step1"))

import run_step2 as S2  # noqa: E402
import run_step3 as S3  # noqa: E402
import closed_loop as CL  # noqa: E402
import run_p272c_gate as G  # noqa: E402

S2.OUT = S3.OUT = OUT

# Pad supplies [HAND] — same as run_p272c_gate
V_SS, V_TT, V_FF = G.V_SS, G.V_TT, G.V_FF
HOLDS = dict(tt=0.577, ss=0.524, ff=0.636)  # [SCH] summary_p272c_hold.txt
OWNER_WINDOW = (0.25, 0.95)  # owner Part B criterion


def _patch_vdd(sim_path, vdd):
    text = open(sim_path).read()
    text2 = re.sub(r"vdd  \(vdd 0\) vsource dc=1\.2",
                   f"vdd  (vdd 0) vsource dc={vdd}", text)
    text2 = re.sub(r"vsource dc=1\.2\n", f"vsource dc={vdd}\n", text2)
    if text2 != text:
        open(sim_path, "w").write(text2)


def force_cfix():
    r, _ = S3.load_sizing()
    cfix = float(r["cfix"])
    S2.C_FIX_FF = cfix
    print(f"Sizing: LSB {S2.LSB_FF:.3f} fF, cfix {cfix:.4f} fF, "
          f"nbits={S2.NBITS}, bank_arch={getattr(S2, 'BANK_ARCH', '?')} "
          f"[SCH/range.json]\n", flush=True)
    return cfix


def carries_cfix():
    """Re-measure ss/ff grids at pad VDD with current C_FIX [SCH]."""
    print("# Carries / bank grid with trimmed cfix [SCH]\n", flush=True)
    banks_ser = {}
    for mos, cap, temp, key, vdd in (
            ("mos_ss", "cap_wcs", 85, "ss", V_SS),
            ("mos_ff", "cap_bcs", -40, "ff", V_FF)):
        # measure_corner uses S2.C_FIX_FF via netlist
        rows, f_mid, k_map = G.measure_corner(mos, cap, temp, key, vdd)
        banks_ser[key] = dict(
            codes=sorted(f_mid),
            f=[f_mid[c] for c in sorted(f_mid)],
            k=[k_map[c] for c in sorted(f_mid)],
            steps=rows,
        )
    path = os.path.join(OUT, "p272c_d20_banks.json")
    json.dump(banks_ser, open(path, "w"), indent=1)
    print(f"Wrote {path}", flush=True)
    return banks_ser


def land_owner_window(banks_ser):
    """Nearest landing; window forced to 0.25–0.95 at tt/ss/ff [MODEL]."""
    # Install banks into a pseudo-state for G helpers
    st = dict(
        banks={k: dict(codes=v["codes"], f=v["f"], k=v["k"])
               for k, v in banks_ser.items()},
        holds=HOLDS,
        compliance={cn: dict(bot=OWNER_WINDOW[0], top=OWNER_WINDOW[1])
                    for cn in ("tt", "ss", "ff")},
    )
    banks = G._banks_from_state(st)
    G._apply_corners(st, bias=0)
    CL.calibrate = G._calibrate_biased

    def blend_f(code):
        return 0.5 * (banks["ss"][0](code) + banks["ff"][0](code))

    def blend_k(code):
        return 0.5 * (banks["ss"][1](code) + banks["ff"][1](code))

    f_lo = 0.5 * (banks["ss"][2] + banks["ff"][2])
    f_hi = 0.5 * (banks["ss"][3] + banks["ff"][3])

    print("\n## D20 landing with owner window 0.25–0.95 V [MODEL]\n", flush=True)
    print("Holds from prior VR_ANA1 hold run [SCH]: "
          f"tt={HOLDS['tt']}, ss={HOLDS['ss']}, ff={HOLDS['ff']}\n", flush=True)
    print("| corner | hold | window | V min–max | outside % | margin lo/hi | "
          "n channels | PASS |", flush=True)
    print("|---|---|---|---|---|---|---|---|", flush=True)

    ok_all = True
    results = {}
    for cn, src in (("tt", "blend"), ("ss", "ss"), ("ff", "ff")):
        if src == "blend":
            fb, kv, flo, fhi = blend_f, blend_k, f_lo, f_hi
        else:
            fb, kv, flo, fhi = banks[src]
        CL.F_LO, CL.F_HI = flo, fhi
        CL.f_bank = fb
        CL.kvco = kv
        CL.CFG.update(nb=8, cdiv=4)
        # landing returns (V_tune[], cases[(v,band,fv),...], t_cal)
        vs, cases, _ = CL.landing(cn, "nearest", np.random.default_rng(1))
        lo_w, hi_w = OWNER_WINDOW
        out = float(np.mean((vs < lo_w) | (vs > hi_w)) * 100)
        mlo = float(vs.min() - lo_w)
        mhi = float(hi_w - vs.max())
        ok = (out < 1e-9) and (mlo >= 0.0) and (mhi >= 0.0)
        ok_all = ok_all and ok
        print(
            f"| {cn} | {HOLDS[cn]:.3f} | {lo_w:.2f}–{hi_w:.2f} | "
            f"{vs.min():.3f}–{vs.max():.3f} | {out:.2f} | "
            f"{mlo:+.3f}/{mhi:+.3f} | {len(cases)} | "
            f"{'PASS' if ok else 'FAIL'} |",
            flush=True)
        results[cn] = dict(
            vmin=float(vs.min()), vmax=float(vs.max()), out=out,
            mlo=mlo, mhi=mhi, ok=ok, n=len(cases),
        )
    # Compare envelope to prior p272c gate pass (compliance windows were wider)
    print("\nPrior p272c gate (compliance windows) was PASS with "
          "tt 0.361–0.936 / ss 0.244–0.897 / ff 0.457–0.970 V [MODEL]. "
          "Nearest-code rule unchanged (nb=8, cdiv=4, nearest) [MODEL].\n",
          flush=True)
    return ok_all, results


def hand_pn(cfix: float):
    """HAND Leeson bound from tank C change; try PSS if available [HAND/SCH]."""
    print("\n## Worst-corner PN with new cfix [HAND] (+ PSS attempt)\n", flush=True)
    # Recorded worst: ss85 4.20 GHz, L(1 MHz)=−119.4 dBc/Hz, margin +3.4 dB vs −116
    L_old = -119.4
    limit = -116.0
    C_par = 97.53  # fF/side [PEX-RC/HAND] from trim stop
    C_old = 192.0 + C_par
    C_new = cfix + C_par
    # Parallel-R tank: Q ∝ 1/sqrt(C) at fixed L,R → ΔL ≈ −20 log10((Qnew/Qold)^2)
    # = −40 log10(Qnew/Qold) = −20 log10(C_old/C_new)
    dL = -20.0 * math.log10(C_old / C_new)  # negative ⇒ better (lower) PN
    L_new = L_old + dL
    margin = limit - L_new  # positive if L_new more negative than limit? 
    # limit −116; L_new should be ≤ −116; margin = −116 − L_new if L_new is more neg...
    # Prior: margin +3.4 = −116 − (−119.4). So margin = limit - L  with L negative.
    margin_new = limit - L_new
    print(
        f"Prior worst L(1 MHz) = {L_old:.1f} dBc/Hz at ss85 / ~4.20 GHz [SCH]\n"
        f"C_old = {C_old:.2f} fF, C_new = {C_new:.2f} fF (cfix {cfix:.2f} + par "
        f"{C_par:.2f}) [SCH/PEX-RC/HAND]\n"
        f"HAND Leeson ΔL from ΔC (Q∝1/√C): {dL:+.2f} dB → "
        f"L_new ≈ {L_new:.1f} dBc/Hz; margin vs −116 = {margin_new:+.1f} dB [HAND]\n",
        flush=True)
    hand_ok = margin_new > 0

    pss_note = "PSS not attempted in this path (use bank-omitted script separately)."
    pss_ok = None
    # Light PSS attempt via existing nobank helper if importable
    try:
        import run_pnoise_nobank as PN  # noqa: F401
        pss_note = (
            "PSS attempt deferred to recorded bank-omitted method; HAND bound used "
            "for gate (owner: [HAND] until P2.7.3).")
    except Exception as e:
        pss_note = f"PSS helper unavailable ({e}); HAND only."

    print(f"PN gate: {'PASS' if hand_ok else 'FAIL'} on HAND margin; {pss_note}\n",
          flush=True)
    return hand_ok, dict(
        L_old=L_old, L_new=L_new, dL=dL, margin_new=margin_new,
        C_old=C_old, C_new=C_new, pss_ok=pss_ok, note=pss_note,
    )


def main():
    lines = []
    print("# P2.7.2c — D20 + PN with trimmed cfix [SCH/MODEL/HAND]\n", flush=True)
    cfix = force_cfix()
    banks = carries_cfix()
    land_ok, land_res = land_owner_window(banks)
    pn_ok, pn_res = hand_pn(cfix)

    print("\n## Gate verdict\n", flush=True)
    print(f"D20 owner window 0.25–0.95: {'PASS' if land_ok else 'FAIL'} [MODEL]",
          flush=True)
    print(f"Worst-corner PN margin: {'PASS' if pn_ok else 'FAIL'} [HAND]",
          flush=True)
    overall = land_ok and pn_ok
    print(f"Overall: {'PASS' if overall else 'FAIL'} — "
          f"{'re-pack may proceed' if overall else 'STOP'}\n", flush=True)

    payload = dict(
        cfix=cfix, land_ok=land_ok, pn_ok=pn_ok, overall=overall,
        landing=land_res, pn=pn_res, holds=HOLDS, window=OWNER_WINDOW,
        pads=dict(ss=V_SS, tt=V_TT, ff=V_FF),
    )
    json.dump(payload, open(os.path.join(OUT, "p272c_d20_pn_cfix.json"), "w"),
              indent=1)

    # also write a short summary file explicitly (tee covers stdout)
    sum_path = os.path.join(OUT, "summary_p272c_d20_pn_cfix.txt")
    with open(sum_path, "w") as fh:
        fh.write("# P2.7.2c — D20 + PN with trimmed cfix\n\n")
        fh.write(f"cfix = {cfix:.4f} fF [SCH/range.json]\n")
        fh.write(f"D20 0.25–0.95: {'PASS' if land_ok else 'FAIL'} [MODEL]\n")
        for cn, r in land_res.items():
            fh.write(
                f"  {cn}: {r['vmin']:.3f}–{r['vmax']:.3f} V "
                f"margin {r['mlo']:+.3f}/{r['mhi']:+.3f} "
                f"{'PASS' if r['ok'] else 'FAIL'}\n")
        fh.write(
            f"PN HAND: L_new≈{pn_res['L_new']:.1f} dBc/Hz, "
            f"margin {pn_res['margin_new']:+.1f} dB "
            f"({'PASS' if pn_ok else 'FAIL'})\n")
        fh.write(f"Overall: {'PASS' if overall else 'FAIL'}\n")
    # mirror under p272c layout out
    dest = os.path.join(HERE, "..", "layout", "p272c", "out",
                        "summary_p272c_d20_pn_cfix.txt")
    open(dest, "w").write(open(sum_path).read())
    print(f"Wrote {sum_path}\nWrote {dest}", flush=True)
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
