#!/usr/bin/env python3
"""P2.7.3c — transient peak MC at worst-peak corner [PEX-RC lumped].

Corner: mos_ss / cap_bcs / 85 °C / top (fab retune worst Amp_peak).
Comparator Vos MC as run_peak_mc; PEX lumped injected.
Pass: peak + 3σ ≤ 1.50 V.

Same dual PEX OP attempt as run_p273c_search (B then C) [PEX-RC lumped / TOOL].
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np
from vacask.rawfile import rawread

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
LAYOUT = os.path.join(HERE, "..", "layout", "p272c", "out")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
AMPCAL = os.path.join(REPO, "analog", "vco", "ampcal")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "step2"))
sys.path.insert(0, AMPCAL)

import amp_common as A  # noqa: E402
import run_peak_mc as PM  # noqa: E402
import run_search as RS  # noqa: E402
import pex_lumped_extra as PX  # noqa: E402

A.load_sizing()
SAR_OUT = os.path.join(OUT, "p273c_peak")
os.makedirs(SAR_OUT, exist_ok=True)
A.OUT = SAR_OUT
RS.A.OUT = SAR_OUT
RS.S2.OUT = SAR_OUT
PM.RS.A.OUT = SAR_OUT
PM.RS.S2.OUT = SAR_OUT

_L, _SRC = PX.load_lump()
_L["_src"] = _SRC

_orig_prep_vos = PM.prep_vos
_PEX_MODE = "C"


def _inject_mode(sim, mode: str) -> None:
    PX.inject_pex(
        sim,
        _L,
        tie_vbp=False,
        omit_ctl=True,
        fold_vbp_into_cr=(mode == "B"),
        replace=True,
        rtb_op=True,
    )


def _ensure_rtb(sim: str) -> None:
    text = open(sim).read()
    if "Rtb_op" in text or "ctb (tb 0) capacitor c=2e-12" not in text:
        return
    open(sim, "w").write(
        text.replace(
            "ctb (tb 0) capacitor c=2e-12",
            "ctb (tb 0) capacitor c=2e-12\nRtb_op (tb 0) resistor r=1e6",
            1,
        )
    )


def prep_vos_pex(sim, bias_code, vos=(0.0, 0.0)):
    _orig_prep_vos(sim, bias_code, vos)
    _ensure_rtb(sim)
    _inject_mode(sim, _PEX_MODE)


PM.prep_vos = prep_vos_pex


def measure_vos_dual(mos, cap, temp, bcode, bias, tag, vos):
    global _PEX_MODE
    A.set_corner(mos, cap)
    vt = RS.S2.VTUNE_MID if bcode < 128 else 0.3
    stop = 40e-9 + RS.SETTLE
    last_err = None
    for mode in ("C", "B"):
        _PEX_MODE = mode
        sim = RS.S2.netlist(
            tag, bcode, vt, itail=A.itail(bias), bypass=True, drive_vbp=False,
            bypass_groups=("tail",),
            analysis=(
                f"  options temp={temp}\n"
                "  save v(tp) v(tn) v(cmp) v(hold) v(rep)\n"
                f"  analysis tr tran stop={stop:.6g} step={RS.TRAN_STEP} "
                f"maxstep={RS.TRAN_STEP}"
            ),
        )
        prep_vos_pex(sim, bias, vos)
        t0 = time.time()
        try:
            RS.S2.run(sim)
        except RuntimeError as e:
            last_err = e
            log = os.path.join(SAR_OUT, f"{tag}.log")
            tip = open(log).read()[-800:] if os.path.exists(log) else str(e)
            if "Operating point" in tip or "NaN found" in tip or "Homotopy" in tip:
                continue
            raise
        dt = time.time() - t0
        try:
            d = rawread(os.path.join(RS.A.OUT, "tr.raw")).get()
        except Exception as e:
            last_err = e
            continue
        t = np.real(d["time"])
        m = t >= t[-1] - 20e-9
        v = np.real(d["tp"])[m] - np.real(d["tn"])[m]
        amp = float(v.max() - v.min()) / 2
        v_all = np.real(d["tp"]) - np.real(d["tn"])
        amp_peak_run = float(v_all.max() - v_all.min()) / 2
        vh = float(np.real(d["hold"])[m][-1])
        vr = float(np.real(d["rep"])[m][-1])
        cmpv = float(np.real(d["cmp"])[m][-1])
        return dict(
            amp=amp, amp_peak_run=amp_peak_run, high=cmpv > A.CMP_HIGH,
            cmp=cmpv, dt=dt, vsense=vh - vr, pex_topo=mode,
        )
    raise RuntimeError(f"measure_vos_dual failed both PEX topos: {last_err}")


PM.measure_vos = measure_vos_dual


def main():
    quick = "quick" in sys.argv
    n = 5 if quick else PM.N
    lines = [
        "# P2.7.3c transient peak MC [PEX-RC lumped]\n\n",
        f"Corner: {PM.MOS} / {PM.CAP} / {PM.TEMP} °C / {PM.BAND}; "
        f"N={n}; Vos σ={PM.SIG*1e3:.2f} mV. "
        f"PEX C_side={_L['c_side_ff']:.2f} fF; Rtb_op=1 MΩ; omit Cctl; "
        f"Rtail=10 Ω; dual OP C→B (C=Ccvbp; B=vbp→Cr) [PEX-RC lumped / TOOL]. "
        f"Limit peak+3σ ≤ {A.A_HARD_TRANSIENT:.2f} V.\n\n",
    ]
    print(lines[0], flush=True)
    nom = PM.sar_vos((0.0, 0.0), "p273c_peak_nom")
    lines.append(
        f"Nominal: code={nom['code']} peak={nom['amp_peak']:.3f} "
        f"at bit={nom['peak_step']['bit']} "
        f"trial={nom['peak_step']['trial']} [PEX-RC lumped]\n\n"
    )
    print(lines[-1], flush=True)

    rng = np.random.default_rng(20261118)
    peaks = []
    overs = []
    for i in range(n):
        vos = (float(rng.normal(0, PM.SIG)), float(rng.normal(0, PM.SIG)))
        r = PM.sar_vos(vos, f"p273c_peak_mc{i}")
        peaks.append(r["amp_peak"])
        mark = ""
        if r["amp_peak"] > A.A_HARD_TRANSIENT + 1e-3:
            overs.append(dict(i=i, vos=vos, **r))
            mark = " OVER"
        print(
            f"  [{i+1}/{n}] peak={r['amp_peak']:.3f} "
            f"@bit{r['peak_step']['bit']}/c{r['peak_step']['trial']}{mark}",
            flush=True,
        )

    arr = np.array(peaks, dtype=float)
    mean = float(arr.mean())
    sig = float(arr.std(ddof=1)) if n > 1 else 0.0
    p3 = 3.0 * sig
    hi = mean + p3
    ok = hi <= A.A_HARD_TRANSIENT + 1e-3
    lines.append("## Results [PEX-RC lumped]\n\n")
    lines.append(f"- peak mean = {mean:.4f} V\n")
    lines.append(f"- peak σ = {sig*1e3:.2f} mV; 3σ = {p3*1e3:.2f} mV\n")
    lines.append(
        f"- peak + 3σ = **{hi:.4f} V** (limit {A.A_HARD_TRANSIENT:.2f} V) → "
        f"{'PASS' if ok else f'OVER by {(hi - A.A_HARD_TRANSIENT)*1e3:.1f} mV'}\n"
    )
    lines.append(f"- observed min/max = {arr.min():.3f} / {arr.max():.3f} V\n")
    if overs:
        lines.append(f"\nSamples > 1.50 V: {len(overs)}/{n}\n")
    lines.append(
        f"\nPeak MC gate: {'PASS' if ok else 'FAIL — stop for owner'} "
        f"[PEX-RC lumped]\n"
    )
    text = "".join(lines)
    for p in (
        os.path.join(OUT, "summary_pex_vco_peak_mc.txt"),
        os.path.join(LAYOUT, "summary_pex_vco_peak_mc.txt"),
    ):
        open(p, "w").write(text)
    print(text)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
