#!/usr/bin/env python3
"""VHF ss divide debug matrix."""
from __future__ import annotations

import importlib
import re
import sys

import circuit as C
import run_equiv as E


def run_case(tag, amp=None, no_hold=False, ideal=False, i=0.75e-3):
    importlib.reload(C)
    importlib.reload(E)
    C.apply_knobs(i_latch=i)
    if no_hold:
        C.replace_holds = lambda body: re.sub(
            r"^rk\S+ \(\S+ 0\) resistor r=1G\s*$", "", body, flags=re.M)
    if ideal:
        C.replace_tails = lambda body, i_latch=None: body
    kw = {"amp": amp} if amp is not None else {}
    print("TRY", tag, "I", C.I_LATCH, "amp", amp, flush=True)
    path, names, ideal_ph, ndiv, duty, vdd = E.build(
        "vhf", 3.12e9, E.CORNERS["ss"], tag="_" + tag, **kw)
    d = E.run(path)
    r = E.analyse(d, names, ideal_ph, ndiv, duty, vdd, 3.12e9)
    print(" ", tag, "ok", r["ok"], "phase", r["max_phase_err"],
          "duty", r["duty_min"], r["duty_max"], flush=True)
    return r["ok"]


def main():
    trials = [
        ("amp55", dict(amp=0.55)),
        ("nohold", dict(no_hold=True, amp=0.55)),
        ("ideal55", dict(ideal=True, amp=0.55)),
        ("i1_amp55", dict(i=1.0e-3, amp=0.55)),
    ]
    for tag, kwargs in trials:
        if run_case(tag, **kwargs):
            break
    print("MATRIX_DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
