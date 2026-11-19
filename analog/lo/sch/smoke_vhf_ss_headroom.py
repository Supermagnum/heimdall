#!/usr/bin/env python3
"""VHF ss headroom / bias path smokes."""
from __future__ import annotations

import re

import circuit as C
import run_equiv as E


def run_case(tag, swing=0.4, direct_bias=False, amp=0.55, i=0.75e-3):
    C.apply_knobs(i_latch=i, swing=swing)
    print("TRY", tag, "swing", C.SWING, "RL", C.L1.cml_params(0, 1.08),
          flush=True)
    if direct_bias:
        def rt(body, i_latch=None):
            i_latch = C.I_LATCH if i_latch is None else i_latch
            w = C.tail_w(i_latch)
            body = re.sub(
                r"^i(\S+) \(t\1 0\) isource .*$",
                lambda m: (f"mt{m.group(1)} (t{m.group(1)} nbias 0 0) "
                           f"sg13_lv_nmos w={w:g}u l={C.TAIL_L}\n"),
                body, flags=re.M)
            body = re.sub(
                r"^ig \(tg 0\) isource .*$",
                (f"mtg (tg nbias 0 0) sg13_lv_nmos "
                 f"w={w:g}u l={C.TAIL_L}\n"),
                body, flags=re.M)
            return body
        C.replace_tails = rt
    path, names, ideal, ndiv, duty, vdd = E.build(
        "vhf", 3.12e9, E.CORNERS["ss"], tag="_" + tag, amp=amp)
    d = E.run(path)
    r = E.analyse(d, names, ideal, ndiv, duty, vdd, 3.12e9)
    print(" ", tag, "ok", r["ok"], "phase", r["max_phase_err"],
          "duty", r["duty_min"], r["duty_max"], flush=True)
    return r["ok"]


def main():
    trials = [
        ("sw04", dict(swing=0.4, amp=0.55)),
        ("sw035", dict(swing=0.35, amp=0.55)),
        ("direct04", dict(swing=0.4, direct_bias=True, amp=0.55)),
        ("sw04a32", dict(swing=0.4, amp=0.32)),
        ("ideal_sw05", dict(swing=0.5, amp=0.55)),  # sanity: need ideal
    ]
    # last trial: ideal tails baseline at default swing
    any_ok = False
    for tag, kw in trials[:-1]:
        # reset replace_tails each time by re-importing would be cleaner;
        # for direct, patch; otherwise restore from module
        import importlib
        importlib.reload(C)
        importlib.reload(E)
        if run_case(tag, **kw):
            any_ok = True
            break
    if not any_ok:
        importlib.reload(C)
        importlib.reload(E)
        C.replace_tails = lambda body, i_latch=None: body
        run_case("ideal_confirm", swing=0.5, amp=0.55)
    print("HEADROOM_DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
