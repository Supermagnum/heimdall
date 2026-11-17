#!/usr/bin/env python3
"""P2.7.2c — ff landing check at trimmed-cfix vmax 0.955 V [SCH]+[MODEL].

Accepted P2.7.2c landing gate (decisions.md 2026-11-12 / 2026-11-17 D20 landing):
  per-corner compliance window (INL ≤ 30 ps, |ΔI_cp| ≤ 10 %, lock UP, spur within
  accepted limit), not the nominal 0.25–0.95 V.
  ff compliance / prior landing envelope: 0.457–0.970 V [MODEL].
  Spur absolute limit −95 dBc (ss −102.9 accepted); margin target −105 retired.

With cfix 157.7 fF, ff nearest-code envelope is 0.469–0.955 V [MODEL].
This run measures the pump at ff 1.295 V / −40 °C, V_tune = 0.955 V.

    python3 -u run_p272c_ff_land955.py 2>&1 | tee out/summary_p272c_ff_land955.txt
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

import importlib.util

spec4 = importlib.util.spec_from_file_location(
    "pll_step4_lin", os.path.join(HERE, "run_step4.py"))
S4 = importlib.util.module_from_spec(spec4)
spec4.loader.exec_module(S4)
S2 = S4.S2
S2.OUT = OUT
S4.OUT = OUT

sys.path.insert(0, os.path.join(REPO, "analog", "pll", "step3"))
import pll_behav as B  # noqa: E402

DTS = [1e-9, 2e-9, 3e-9, 4e-9, 5e-9]
ICP = S2.ICP
INL_LIM = 30e-12
DICP_LIM = 0.10
SPUR_ABS = -95.0   # duplex [decisions P2.7.2 pump-linearity gate]
SPUR_POST = -100.0  # post-layout target at ss extreme; use as report only

# Accepted ff window from P2.7.2c gate [MODEL]
FF_WIN = (0.457, 0.970)
VT_HI = 0.955
VT_MID = 0.636
VDD, TEMP, MOS, CN = 1.295, -40, "mos_ff", "ff"


def measure(vt):
    corner = (CN, MOS, VDD, TEMP)
    qs, st_last = [], None
    for dt in DTS:
        name = f"p272c_ff955_{vt:.3f}_{dt*1e9:.0f}"
        q, _, _, _, st = S2.run(
            name, corner, vt, dt, ICP, ioff=True,
            post=lambda x: S4.use_bias(x + S4.biasgen()),
        )
        qs.append(q / ICP)
        st_last = st
    da, qa = np.array(DTS), np.array(qs)
    k, c = np.polyfit(da, qa, 1)
    inl = float(np.max(np.abs(qa - (k * da + c))))
    lock = float(-c / k)
    return dict(
        vt=vt, dts=DTS, qs=[float(x) for x in qs],
        slope=float(k), lock=lock, inl=inl,
        ioff=float(st_last["ioff"]), ivdd=float(st_last["ivdd"]),
    )


def main():
    print("# P2.7.2c — ff landing at 0.955 V with trimmed cfix [SCH]+[MODEL]\n")
    print(f"ff compliance / prior landing window: {FF_WIN[0]:.3f}–{FF_WIN[1]:.3f} V "
          f"[MODEL] (P2.7.2c gate).\n")
    print(f"New ff landing high: {VT_HI:.3f} V [MODEL] (cfix 157.7 fF).\n")
    inside = FF_WIN[0] <= VT_HI <= FF_WIN[1]
    print(f"0.955 V inside ff window: {'YES' if inside else 'NO'} "
          f"(margin to top {FF_WIN[1] - VT_HI:+.3f} V) [MODEL].\n")

    print("Q(dt) 1–5 ns, offset on, bias generator, I_cp 100 µA. "
          "Spur from pll_behav (D19 loop) [MODEL].\n")
    print("| V_tune | INL (ps) | Lock (ns) | Slope | ΔI_cp (%) | "
          "Spur VHF/UHF (dBc) | PASS |")
    print("|---|---|---|---|---|---|---|")

    mid = measure(VT_MID)
    r = measure(VT_HI)
    dicp = r["slope"] / mid["slope"] - 1.0
    inl_f = B.inl_from_curve(r["dts"], np.array(r["qs"]))
    sp_vhf = B.spur("VHF", inl_f)["spur_rf"]
    sp_uhf = B.spur("UHF", inl_f)["spur_rf"]
    # Reference spur model: leakage-dominated; use mid ioff scale as bound [MODEL]
    # pll_behav has no separate ref-spur call here — report boundary fractional only;
    # ref spur previously ≤ −109 dBc at 5 µA [MODEL] (prompt 01).
    lock_ok = r["lock"] > 0.0
    inl_ok = r["inl"] <= INL_LIM
    dicp_ok = abs(dicp) <= DICP_LIM
    spur_ok = (sp_vhf <= SPUR_ABS) and (sp_uhf <= SPUR_ABS)
    ok = inside and inl_ok and dicp_ok and lock_ok and spur_ok
    flag = "PASS" if ok else "FAIL"
    print(f"| {VT_HI:.3f} | {r['inl']*1e12:.1f} | {r['lock']*1e9:.2f} | "
          f"{r['slope']:.3f} | {dicp*100:+.1f} | {sp_vhf:.1f}/{sp_uhf:.1f} | "
          f"{flag} |", flush=True)
    inl_f_m = B.inl_from_curve(mid["dts"], np.array(mid["qs"]))
    sp_vhf_m = B.spur("VHF", inl_f_m)["spur_rf"]
    sp_uhf_m = B.spur("UHF", inl_f_m)["spur_rf"]
    print(f"| {VT_MID:.3f} mid | {mid['inl']*1e12:.1f} | {mid['lock']*1e9:.2f} | "
          f"{mid['slope']:.3f} | +0.0 | {sp_vhf_m:.1f}/{sp_uhf_m:.1f} | ref |",
          flush=True)

    print("\n## Gate checks\n")
    print(f"| Check | Result | Limit | Tag |")
    print(f"|---|---|---|---|")
    print(f"| Inside ff window {FF_WIN[0]}–{FF_WIN[1]} | "
          f"{'YES' if inside else 'NO'} | window | [MODEL] |")
    print(f"| INL | {r['inl']*1e12:.1f} ps | ≤ 30 ps | [SCH] |")
    print(f"| |ΔI_cp| | {abs(dicp)*100:.1f} % | ≤ 10 % | [SCH] |")
    print(f"| Lock UP | {r['lock']*1e9:.2f} ns | > 0 | [SCH] |")
    print(f"| Fractional boundary spur VHF | {sp_vhf:.1f} dBc | ≤ −95 dBc | [MODEL] |")
    print(f"| Fractional boundary spur UHF | {sp_uhf:.1f} dBc | ≤ −95 dBc | [MODEL] |")
    print(f"| Reference spur | not re-run this job | TX ≤ −67 / RX ≤ −84; "
          f"prior ≤ −109 at 5 µA | [MODEL prior] |")

    print("\n## Verdict\n")
    if ok:
        print("PASS — 0.955 V inside ff compliance window; INL / ΔI_cp / UP / "
              "boundary spur within accepted limits. Proceed to direct re-pack.\n")
    else:
        print("FAIL — nudge cfix or stop.\n")

    out = dict(
        pass_=ok, inside_window=inside, ff_window=list(FF_WIN), vt=VT_HI,
        inl_ps=r["inl"] * 1e12, dicp_pct=dicp * 100, lock_ns=r["lock"] * 1e9,
        spur_vhf=sp_vhf, spur_uhf=sp_uhf, mid_slope=mid["slope"], slope=r["slope"],
    )
    json.dump(out, open(os.path.join(OUT, "p272c_ff_land955.json"), "w"), indent=1)

    # Mirror under p272c layout out for the join job
    p272c = os.path.join(REPO, "analog", "vco", "layout", "p272c", "out")
    os.makedirs(p272c, exist_ok=True)
    with open(os.path.join(p272c, "summary_p272c_ff_land955.txt"), "w") as f:
        f.write(f"pass={ok} inside={inside} vt={VT_HI} "
                f"inl_ps={r['inl']*1e12:.1f} dicp_pct={dicp*100:+.1f} "
                f"lock_ns={r['lock']*1e9:.2f} spur_vhf={sp_vhf:.1f} "
                f"spur_uhf={sp_uhf:.1f}\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
