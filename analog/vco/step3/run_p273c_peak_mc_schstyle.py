#!/usr/bin/env python3
"""P2.7.3c peak MC re-run, schematic-style bench [PEX-RC lumped].

Owner open (decisions.md 2026-11-19): prior 1.250 V was final Amp at bit=−1 /
code 31, not the SCH mid-SAR peak at bit3 / code 24 (1.4935 V). Re-run with:

- Cctl included (omit_ctl=False) — C(tail−tn/tp) as extracted
- Rtb_op=1 MΩ only on detector SF bias tail tb (parallel to ctb); not on
  hold / rep / cmp / tank. Needed so VACASK OP at 85 °C converges with PEX
  [TOOL]; justified as DC path on a current-source node, not signal/hold
- Peak tracked across SAR search trials (same as run_peak_mc)
- Corner: mos_ss / cap_bcs / 85 °C / top; cmp Vos MC; det/cmp on
- Pass: peak + 3σ ≤ 1.50 V
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
SAR_OUT = os.path.join(OUT, "p273c_peak_schstyle")
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
# Rtb_op on tb only (bias). Set False to prove OP without it.
USE_RTB = "no_rtb" not in sys.argv


def _inject_mode(sim, mode: str) -> None:
    PX.inject_pex(
        sim,
        _L,
        tie_vbp=False,
        omit_ctl=False,  # Cctl included [owner]
        fold_vbp_into_cr=(mode == "B"),
        replace=True,
        rtb_op=USE_RTB,
    )


def prep_vos_pex(sim, bias_code, vos=(0.0, 0.0)):
    _orig_prep_vos(sim, bias_code, vos)
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
        # Sanity: Rtb_op must not appear on hold/rep/tank
        net = open(sim).read()
        bad = []
        for n in ("hold", "rep", "tn", "tp", "cmp"):
            if f"Rtb_op ({n} " in net or f"Rtb_op (0 {n})" in net:
                bad.append(n)
        return dict(
            amp=amp, amp_peak_run=amp_peak_run, high=cmpv > A.CMP_HIGH,
            cmp=cmpv, dt=dt, vsense=vh - vr, pex_topo=mode,
            rtb_on_tb=("Rtb_op (tb 0)" in net), rtb_bad_nodes=bad,
        )
    raise RuntimeError(f"measure_vos_dual failed both PEX topos: {last_err}")


PM.measure_vos = measure_vos_dual


def main():
    quick = "quick" in sys.argv
    n = 5 if quick else PM.N
    rtb_note = (
        "Rtb_op=1 MΩ on det tb only (bias; not hold/rep/tank)"
        if USE_RTB else "Rtb_op omitted"
    )
    lines = [
        "# P2.7.3c transient peak MC — schematic-style re-run [PEX-RC lumped]\n\n",
        f"Corner: {PM.MOS} / {PM.CAP} / {PM.TEMP} °C / {PM.BAND}; "
        f"N={n}; Vos σ={PM.SIG*1e3:.2f} mV. "
        f"PEX C_side={_L['c_side_ff']:.2f} fF; Cctl included "
        f"(c_tail_tn={_L.get('c_tail_tn_ff', 0):.2f} / "
        f"c_tail_tp={_L.get('c_tail_tp_ff', 0):.2f} fF); "
        f"{rtb_note}; Rtail=10 Ω; dual OP C→B [PEX-RC lumped / TOOL]. "
        f"Peak = max over SAR search trials (amp and amp_peak_run). "
        f"Limit peak+3σ ≤ {A.A_HARD_TRANSIENT:.2f} V.\n\n",
        "## Bench notes (owner open items)\n\n",
        "- Prior 1.250 V: final Amp at bit=−1 / code 31 after SAR landed "
        "tnr (not mid-SAR trial). SCH peak 1.4935 V was at bit3 / code 24 "
        "[SCH summary_peak_mc.txt].\n",
        "- Rtb_op: 1 MΩ from detector SF current-source node `tb` to gnd, "
        "in parallel with ctb=2 pF. Bare ib+ctb NaNs OP at 85 °C with PEX "
        "on some DAC codes [TOOL]. Not on hold, rep, cmp, or tank.\n",
        "- Cctl: C(tail−tn) and C(tail−tp) from extract; prior omit folded "
        f"{(_L.get('c_tail_tn_ff') or 0)+(_L.get('c_tail_tp_ff') or 0):.2f} fF "
        "into C_tail_pn for OP. This re-run keeps them.\n\n",
    ]
    print(lines[0], flush=True)
    print("".join(lines[1:4]), flush=True)

    nom = PM.sar_vos((0.0, 0.0), "p273c_peak_ss_nom")
    ps = nom["peak_step"]
    lines.append(
        f"Nominal: code={nom['code']} peak={nom['amp_peak']:.3f} "
        f"at bit={ps['bit']} trial={ps['trial']} kind={ps['kind']} "
        f"[PEX-RC lumped]\n\n"
    )
    print(lines[-1], flush=True)
    # Print per-bit trail for transparency
    for s in nom.get("steps", []):
        print(
            f"  nom bit{s['bit']} c{s['trial']} keep={int(s['keep'])} "
            f"Amp={s['amp']:.3f} peak_run={s['amp_peak_run']:.3f} "
            f"cmp={s['cmp']:.3f}",
            flush=True,
        )

    rng = np.random.default_rng(20261119)
    peaks = []
    overs = []
    for i in range(n):
        vos = (float(rng.normal(0, PM.SIG)), float(rng.normal(0, PM.SIG)))
        r = PM.sar_vos(vos, f"p273c_peak_ss_mc{i}")
        peaks.append(r["amp_peak"])
        mark = ""
        if r["amp_peak"] > A.A_HARD_TRANSIENT + 1e-3:
            overs.append(dict(i=i, vos=vos, **r))
            mark = " OVER"
        print(
            f"  [{i+1}/{n}] peak={r['amp_peak']:.3f} "
            f"@bit{r['peak_step']['bit']}/c{r['peak_step']['trial']}"
            f" final_code={r['code']}{mark}",
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
        f"\nPeak MC gate (sch-style): {'PASS' if ok else 'FAIL — stop for owner'} "
        f"[PEX-RC lumped]\n"
    )
    text = "".join(lines)
    for p in (
        os.path.join(OUT, "summary_pex_vco_peak_mc_schstyle.txt"),
        os.path.join(LAYOUT, "summary_pex_vco_peak_mc_schstyle.txt"),
    ):
        open(p, "w").write(text)
    open(os.path.join(OUT, "summary_pex_vco_peak_mc_schstyle_runlog.txt"), "w").write(
        text
    )
    print(text)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
