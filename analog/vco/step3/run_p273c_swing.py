#!/usr/bin/env python3
"""P2.7.3c — swing at accepted D22 codes [PEX-RC lumped].

Netlist: schematic + L2n0 EM + PEX lumped + D22 detector/cmp on.
Pass: bottom ff/wcs/85 °C top DAC ≥ 0.54 V; every corner steady ≤ 1.40 V.

vbp singularity fix: inject_pex(tie_vbp=False) folds C(tn/tp−vbp) to gnd
(vbp is ideal/absent with bypass_groups=tail only).
"""
from __future__ import annotations

import json
import os
import shutil
import sys
import time

import numpy as np
from vacask.rawfile import rawread

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
LAYOUT = os.path.join(HERE, "..", "layout", "p272c", "out")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "step2"))
sys.path.insert(0, os.path.join(REPO, "analog", "vco", "ampcal"))
import amp_common as A  # noqa: E402
import run_step2 as S2  # noqa: E402
import pex_lumped_extra as PX  # noqa: E402

A.load_sizing()
A.OUT = OUT
S2.OUT = OUT

PASS_LO = 0.54
PASS_HI = 1.40
CACHE = os.path.join(OUT, "p273c_swing_cache.json")

# Accepted fab-retune D22 codes [SCH summary_search_fab_retune.txt]
CODES = {
    ("mos_tt", "cap_typ", -40, "top"): 12,
    ("mos_tt", "cap_typ", -40, "bottom"): 31,
    ("mos_tt", "cap_typ", 27, "top"): 15,
    ("mos_tt", "cap_typ", 27, "bottom"): 31,
    ("mos_tt", "cap_typ", 85, "top"): 19,
    ("mos_tt", "cap_typ", 85, "bottom"): 31,
    ("mos_ss", "cap_wcs", -40, "top"): 11,
    ("mos_ss", "cap_wcs", -40, "bottom"): 31,
    ("mos_ss", "cap_wcs", 27, "top"): 14,
    ("mos_ss", "cap_wcs", 27, "bottom"): 31,
    ("mos_ss", "cap_wcs", 85, "top"): 18,
    ("mos_ss", "cap_wcs", 85, "bottom"): 31,
    ("mos_ss", "cap_bcs", -40, "top"): 9,
    ("mos_ss", "cap_bcs", -40, "bottom"): 31,
    ("mos_ss", "cap_bcs", 27, "top"): 12,
    ("mos_ss", "cap_bcs", 27, "bottom"): 31,
    ("mos_ss", "cap_bcs", 85, "top"): 16,
    ("mos_ss", "cap_bcs", 85, "bottom"): 31,
    ("mos_ff", "cap_wcs", -40, "top"): 14,
    ("mos_ff", "cap_wcs", -40, "bottom"): 31,
    ("mos_ff", "cap_wcs", 27, "top"): 18,
    ("mos_ff", "cap_wcs", 27, "bottom"): 31,
    ("mos_ff", "cap_wcs", 85, "top"): 22,
    ("mos_ff", "cap_wcs", 85, "bottom"): 31,
    ("mos_ff", "cap_bcs", -40, "top"): 13,
    ("mos_ff", "cap_bcs", -40, "bottom"): 31,
    ("mos_ff", "cap_bcs", 27, "top"): 16,
    ("mos_ff", "cap_bcs", 27, "bottom"): 31,
    ("mos_ff", "cap_bcs", 85, "top"): 20,
    ("mos_ff", "cap_bcs", 85, "bottom"): 31,
}


def _cache_key(mos, cap, temp, band, bias):
    return f"{mos}|{cap}|{temp}|{band}|{bias}"


def _load_cache():
    if not os.path.exists(CACHE):
        return {}
    try:
        return json.load(open(CACHE))
    except Exception:
        return {}


def _save_cache(cache):
    open(CACHE, "w").write(json.dumps(cache, indent=2, sort_keys=True) + "\n")


def measure(mos, cap, temp, band, bias, *, retries=2):
    A.set_corner(mos, cap)
    bcode = 0 if band == "top" else 255
    vt = S2.VTUNE_MID if bcode < 128 else 0.3
    tag = f"p273c_sw_{mos}_{cap}_{temp}_{band}_c{bias}"
    last_err = None
    for attempt in range(1, retries + 1):
        sim = S2.netlist(
            tag, bcode, vt, itail=A.itail(bias), bypass=True, drive_vbp=False,
            bypass_groups=("tail",),
            analysis=(
                f"  options temp={temp}\n"
                "  save v(tp) v(tn)\n"
                "  analysis tr tran stop=60n step=20p maxstep=20p"
            ),
        )
        A.inject_dac_det(sim, bias, det=True, det_en=True)
        text = open(sim).read()
        text = text.replace(
            "vbptailtie (vbp_tail 0) vsource dc=0",
            "vbptailtie (vbp_tail 0) vsource dc=1.2",
        )
        open(sim, "w").write(text)
        # tie_vbp=False: fold C(tn/tp−vbp)→gnd (no C onto ideal/absent vbp)
        PX.inject_pex(sim, tie_vbp=False)
        t0 = time.time()
        S2.run(sim)
        raw_src = os.path.join(OUT, "tr.raw")
        raw_dst = os.path.join(OUT, f"{tag}.tr.raw")
        if not os.path.exists(raw_src):
            last_err = f"missing {raw_src} after vacask ({time.time()-t0:.1f}s)"
            print(f"    WARN attempt {attempt}: {last_err}", flush=True)
            continue
        shutil.copy2(raw_src, raw_dst)
        try:
            d = rawread(raw_dst).get()
            t = np.real(d["time"])
            m = t >= t[-1] - 20e-9
            v = np.real(d["tp"])[m] - np.real(d["tn"])[m]
            return float(v.max() - v.min()) / 2
        except Exception as e:
            last_err = f"rawread {raw_dst}: {e}"
            print(f"    WARN attempt {attempt}: {last_err}", flush=True)
            # quarantine bad raw so next attempt cannot reuse it
            bad = raw_dst + f".bad{attempt}"
            try:
                os.replace(raw_dst, bad)
            except OSError:
                pass
            time.sleep(0.5)
    raise RuntimeError(
        f"measure failed {mos}/{cap}/{temp}/{band} c{bias}: {last_err}"
    )


def main():
    force = "force" in sys.argv
    L, src = PX.load_lump()
    L["_src"] = src
    lines = [
        "# P2.7.3c swing at accepted D22 codes [PEX-RC lumped]\n\n",
        "Netlist: schematic PDK + L2n0 EM + PEX lumped C/R/tail/couplings + "
        f"D22 det/cmp on. C_side={L['c_side_ff']:.2f} fF, "
        f"C_tail_pn={L['c_tail_pn_ff']:.2f} fF [PEX-RC]. "
        "Codes from summary_search_fab_retune.txt [SCH]. "
        "vbp C folded to gnd (tie_vbp=False) [PEX-RC].\n\n",
    ]
    # Det tank C
    det = PX.det_tank_c_from_ext()
    lines.append("## Detector tank load per side [PEX-RC]\n\n")
    if not det.get("ok"):
        lines.append(f"Extract unavailable: {det.get('reason')} [TOOL]\n\n")
        det_ok = False
    else:
        det_ok = True
        for port, s in det["sides"].items():
            lines.append(
                f"- {port}: named {s['named_sum_ff']:.2f} fF + device Cgg "
                f"~{s['device_cgg_ff']:.1f} fF + face≤5 → "
                f"**{s['total_ff']:.2f} fF** "
                f"({'PASS' if s['pass'] else 'FAIL'} ≤ {det['limit_ff']:.0f})\n"
            )
            if s["named_ff"]:
                lines.append(f"  named: {s['named_ff']}\n")
            if s["anon_top"]:
                lines.append(f"  anon top: {s['anon_top'][:3]}\n")
            det_ok = det_ok and s["pass"]
        lines.append("\n")

    lines.append(
        "| MOS | CAP | T | band | code | Amp (V) | ≤1.40 | note |\n"
        "|---|---|---:|---|---:|---:|---|---|\n"
    )
    all_hi = True
    bot_ff = None
    cache = {} if force else _load_cache()
    # Seed cache from the aborted re-run (vbp-fixed) values in runlog
    if not cache and not force:
        # known-good from summary_pex_vco_swing_runlog.txt before crash
        seed = {
            _cache_key("mos_ff", "cap_bcs", -40, "bottom", 31): 1.036,
            _cache_key("mos_ff", "cap_bcs", -40, "top", 13): 1.223,
            _cache_key("mos_ff", "cap_bcs", 27, "bottom", 31): 0.923,
            _cache_key("mos_ff", "cap_bcs", 27, "top", 16): 1.224,
            _cache_key("mos_ff", "cap_bcs", 85, "bottom", 31): 0.790,
        }
        cache.update(seed)
        _save_cache(cache)

    for (mos, cap, temp, band), code in sorted(CODES.items()):
        key = _cache_key(mos, cap, temp, band, code)
        print(f"  {mos}/{cap}/{temp}/{band} code={code} …", flush=True)
        if key in cache and not force:
            amp = float(cache[key])
            print(f"    Amp={amp:.3f} (cache)", flush=True)
        else:
            amp = measure(mos, cap, temp, band, code)
            cache[key] = amp
            _save_cache(cache)
            print(f"    Amp={amp:.3f}", flush=True)
        ok = amp <= PASS_HI + 1e-3
        all_hi = all_hi and ok
        note = ""
        if mos == "mos_ff" and cap == "cap_wcs" and temp == 85 and band == "bottom":
            bot_ff = amp
            note = f"LO min ≥{PASS_LO}"
            if amp < PASS_LO:
                note += " FAIL"
                all_hi = False
            else:
                note += " PASS"
        lines.append(
            f"| {mos} | {cap} | {temp} | {band} | {code} | {amp:.3f} | "
            f"{'PASS' if ok else 'FAIL'} | {note} |\n"
        )

    lines.append(
        f"\nBottom ff/wcs/85 top-DAC (code 31): Amp="
        f"{bot_ff if bot_ff is not None else '—'} V "
        f"(≥ {PASS_LO} V) [PEX-RC lumped]\n"
    )
    lines.append(
        f"\nSwing gate: {'PASS' if all_hi and det_ok else 'FAIL'} "
        f"[PEX-RC lumped]\n"
    )
    text = "".join(lines)
    for p in (
        os.path.join(OUT, "summary_pex_vco_swing.txt"),
        os.path.join(LAYOUT, "summary_pex_vco_swing.txt"),
    ):
        open(p, "w").write(text)
    print(text)
    return 0 if all_hi and det_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
