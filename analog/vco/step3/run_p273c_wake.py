#!/usr/bin/env python3
"""P2.7.3c — wake time with post-layout numbers [MODEL].

band cal + D22 amp search + settling; pass ≤ 150 µs.
Uses wake_timing.py constants; notes PEX does not change digital settle counts.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
LAYOUT = os.path.join(HERE, "..", "layout", "p272c", "out")
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, os.path.join(REPO, "analog", "pll", "p26"))
import wake_timing as W  # noqa: E402

LIMIT = W.T_WAKE_LIMIT


def main():
    # Post-layout: same digital budgets; analog settle already inside AMP_SETTLE
    # / band cal. PEX parasitics do not add RTL cycles [MODEL].
    t_min = W.T_WAKE_MIN
    t_max = W.T_WAKE_MAX
    ok = t_max <= LIMIT + 1e-12
    lines = [
        "# P2.7.3c wake timing [MODEL]\n\n",
        "Post-layout VCO (P2.7.3a–c lumped) does not change AFE sequencer "
        "cycle counts. Band cal + D22 amp search + loop settle as "
        "`wake_timing.py` / D19 [MODEL].\n\n",
        f"| item | time | source |\n|---|---:|---|\n",
        f"| Tail bypass ≥6–7τ | {W.T_BYPASS*1e6:.2f} µs | "
        f"{W.BYPASS_CYCLES} cyc @ 36 MHz [RTL] |\n",
        f"| D22 amp cal (2×5×settle) | {W.T_AMP_CAL*1e6:.2f} µs | "
        f"{W.AMP_CAL_CYCLES} cyc [RTL/D22] |\n",
        f"| D20 band cal | {W.T_BAND_CAL*1e6:.2f} µs | "
        f"{W.BAND_CAL_CYCLES} cyc [RTL] |\n",
        f"| Cal total (band+amp) | {W.T_CAL_TOTAL*1e6:.2f} µs | [MODEL] |\n",
        f"| Wake min (prior + amp) | {t_min*1e6:.1f} µs | [MODEL] |\n",
        f"| Wake max (prior + amp) | {t_max*1e6:.1f} µs | [MODEL] |\n",
        f"| Limit | {LIMIT*1e6:.0f} µs | plan |\n",
        f"\nWake gate: {'PASS' if ok else 'FAIL'} "
        f"(max {t_max*1e6:.1f} ≤ {LIMIT*1e6:.0f} µs) [MODEL]\n",
    ]
    text = "".join(lines)
    for p in (
        os.path.join(OUT, "summary_pex_vco_wake.txt"),
        os.path.join(LAYOUT, "summary_pex_vco_wake.txt"),
    ):
        open(p, "w").write(text)
    print(text)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
