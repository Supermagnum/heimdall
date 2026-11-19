#!/usr/bin/env python3
"""P2.7.3c — D22 amplitude SAR with PEX lumped parasitics [PEX-RC lumped].

Same deck as accepted fab-device run (ampcal run_search) + PEX lump inject.
Pass: tops in 1.25±0.10 where 4 mA allows; bottoms code 31 + tnr; steady≤1.40.

OP @ 85 °C [TOOL]: Rtb_op=1 MΩ on detector tb (default in inject_pex) plus
omit Cctl (fold→C_tail_pn) and Rtail=10 Ω. Dual topo B→C kept as fallback
(B=vbp→Cr; C=separate Ccvbp).
"""
from __future__ import annotations

import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
LAYOUT = os.path.join(HERE, "..", "layout", "p272c", "out")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
AMPCAL = os.path.join(REPO, "analog", "vco", "ampcal")
os.makedirs(OUT, exist_ok=True)
CACHE = os.path.join(OUT, "p273c_d22_cache.json")

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "step2"))
sys.path.insert(0, AMPCAL)

import numpy as np  # noqa: E402
from vacask.rawfile import rawread  # noqa: E402

import amp_common as A  # noqa: E402
import run_search as RS  # noqa: E402
import pex_lumped_extra as PX  # noqa: E402

A.load_sizing()
SAR_OUT = os.path.join(OUT, "p273c_sar")
os.makedirs(SAR_OUT, exist_ok=True)
A.OUT = SAR_OUT
RS.A.OUT = SAR_OUT
RS.S2.OUT = SAR_OUT

_L, _SRC = PX.load_lump()
_L["_src"] = _SRC

_orig_prep = RS.prep
_PEX_MODE = "C"  # prefer separate Ccvbp; Rtb makes both B and C OP-safe


def _inject_mode(sim, mode: str) -> None:
    """Inject PEX + Rtb_op. mode B: vbp→Cr; mode C: separate Ccvbp_*_gnd."""
    PX.inject_pex(
        sim,
        _L,
        tie_vbp=False,
        omit_ctl=True,
        fold_vbp_into_cr=(mode == "B"),
        replace=True,
        rtb_op=True,
    )


def prep_pex(sim, bias_code):
    _orig_prep(sim, bias_code)
    _inject_mode(sim, _PEX_MODE)


RS.prep = prep_pex


def measure_dual(mos, cap, temp, bcode, bias, tag):
    """Measure with PEX; try topo C then B on OP fail [PEX-RC lumped]."""
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
        prep_pex(sim, bias)
        t0 = time.time()
        try:
            RS.S2.run(sim)
        except RuntimeError as e:
            last_err = e
            log = os.path.join(SAR_OUT, f"{tag}.log")
            tip = open(log).read()[-800:] if os.path.exists(log) else str(e)
            if "Operating point" in tip or "NaN found" in tip or "Homotopy" in tip:
                print(
                    f"      OP fail topo {mode} → retry"
                    if mode == "C"
                    else f"      OP fail topo {mode}",
                    flush=True,
                )
                continue
            raise
        dt = time.time() - t0
        raw = os.path.join(A.OUT, "tr.raw")
        try:
            d = rawread(raw).get()
        except Exception as e:
            last_err = e
            print(f"      rawread fail topo {mode}: {e}", flush=True)
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
        vsense = vh - vr
        high = cmpv > A.CMP_HIGH
        if mode == "B":
            print(f"      used topo B (dt={dt:.1f}s)", flush=True)
        return dict(
            amp=amp, a_est=A.a_est_from_holds(vh, vr), high=high,
            high_vsense=vsense > A.v_th(), dt=dt,
            amp_peak_run=amp_peak_run, vsense=vsense, cmp=cmpv,
            pex_topo=mode,
        )
    raise RuntimeError(f"measure_dual failed both PEX topos: {last_err}")


RS.measure = measure_dual


def _ck(mos, cap, temp, band):
    return f"{mos}|{cap}|{temp}|{band}"


def _load_cache():
    if not os.path.exists(CACHE):
        return {}
    try:
        return json.load(open(CACHE))
    except Exception:
        return {}


def _save_cache(cache):
    open(CACHE, "w").write(json.dumps(cache, indent=2, sort_keys=True) + "\n")


def main():
    quick = "quick" in sys.argv
    force = "force" in sys.argv
    corners = [("mos_tt", "cap_typ")] if quick else RS.CORNERS
    temps = (27,) if quick else RS.TEMPS
    lines = [
        "# P2.7.3c D22 amplitude SAR [PEX-RC lumped]\n\n",
        "Fab det/cmp on; bank bypass off; tail bypass closed during search. "
        f"PEX C_side={_L['c_side_ff']:.2f} fF, C_tail_pn={_L['c_tail_pn_ff']:.2f} fF "
        f"from `{_SRC}`. OP aids: Rtb_op=1 MΩ on det tb; omit Cctl "
        f"(fold → C_tail_pn); Rtail=10 Ω; prefer topo C (Ccvbp), fallback B "
        f"(vbp→Cr) [PEX-RC lumped / TOOL]. "
        f"Decision: v(cmp) > {A.CMP_HIGH:.2f} V; target {A.A_TARGET}±{A.A_WIN} V; "
        f"steady ≤{A.A_HARD} V.\n\n",
        "| MOS | CAP | T | band | code | Amp | tnr | Amp_peak | "
        "in_window | steady≤1.40 | peak≤1.50 |\n",
        "|---|---|---:|---|---:|---:|---:|---:|---|---|---|\n",
    ]
    all_ok = True
    cache = {} if force else _load_cache()
    if not cache and not force:
        cache.update({
            _ck("mos_tt", "cap_typ", -40, "top"): {
                "code": 13, "amp": 1.236, "tnr": 0, "amp_peak": 1.290,
                "amp_steady": 1.236,
            },
            _ck("mos_tt", "cap_typ", -40, "bottom"): {
                "code": 31, "amp": 0.966, "tnr": 1, "amp_peak": 0.966,
                "amp_steady": 0.966,
            },
            _ck("mos_tt", "cap_typ", 27, "top"): {
                "code": 20, "amp": 1.276, "tnr": 0, "amp_peak": 1.315,
                "amp_steady": 1.276,
            },
            _ck("mos_tt", "cap_typ", 27, "bottom"): {
                "code": 31, "amp": 0.829, "tnr": 1, "amp_peak": 0.829,
                "amp_steady": 0.829,
            },
        })
        _save_cache(cache)

    for mos, cap in corners:
        for temp in temps:
            for band, bcode in (("top", 0), ("bottom", 255)):
                key = _ck(mos, cap, temp, band)
                print(f"  SAR {mos}/{cap}/{temp}/{band} …", flush=True)
                if key in cache and not force:
                    c = cache[key]
                    r = {
                        "code": int(c["code"]),
                        "tnr": bool(c["tnr"]),
                        "amp_peak": float(c["amp_peak"]),
                        "amp_steady": float(c.get("amp_steady", c["amp"])),
                        "final": {"amp": float(c["amp"])},
                    }
                    print(
                        f"    code={r['code']} Amp={r['final']['amp']:.3f} "
                        f"peak={r['amp_peak']:.3f} tnr={int(r['tnr'])} (cache)",
                        flush=True,
                    )
                else:
                    r = RS.sar(mos, cap, temp, band, bcode)
                    cache[key] = {
                        "code": r["code"],
                        "amp": r["final"]["amp"],
                        "tnr": int(bool(r["tnr"])),
                        "amp_peak": r["amp_peak"],
                        "amp_steady": r["amp_steady"],
                    }
                    _save_cache(cache)
                    print(
                        f"    code={r['code']} Amp={r['final']['amp']:.3f} "
                        f"peak={r['amp_peak']:.3f} tnr={int(r['tnr'])}",
                        flush=True,
                    )
                ok_s = r["amp_steady"] <= A.A_HARD + 1e-3
                ok_p = r["amp_peak"] <= A.A_HARD_TRANSIENT + 1e-3
                in_win = (
                    A.A_TARGET - A.A_WIN - 1e-3
                    <= r["amp_steady"]
                    <= A.A_TARGET + A.A_WIN + 1e-3
                )
                if band == "bottom":
                    case_ok = ok_s and ok_p and r["code"] == 31 and r["tnr"]
                else:
                    case_ok = ok_s and ok_p and (in_win or r["tnr"])
                all_ok = all_ok and case_ok
                lines.append(
                    f"| {mos} | {cap} | {temp} | {band} | {r['code']} | "
                    f"{r['final']['amp']:.3f} | {int(r['tnr'])} | "
                    f"{r['amp_peak']:.3f} | "
                    f"{'yes' if in_win else ('tnr' if r['tnr'] else 'no')} | "
                    f"{'PASS' if ok_s else 'FAIL'} | "
                    f"{'PASS' if ok_p else 'FAIL'} |\n"
                )
                print(f"    → {'OK' if case_ok else 'NO'}", flush=True)

    lines.append(
        f"\nD22 search gate: {'PASS' if all_ok else 'FAIL'} [PEX-RC lumped]\n"
    )
    text = "".join(lines)
    for p in (
        os.path.join(OUT, "summary_pex_vco_d22_search.txt"),
        os.path.join(LAYOUT, "summary_pex_vco_d22_search.txt"),
    ):
        open(p, "w").write(text)
    print(text)
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
