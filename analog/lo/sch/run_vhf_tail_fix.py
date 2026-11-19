#!/usr/bin/env python3
"""P2.7.4a3 step 3a: widen MOSFET tails; re-check VHF ss [SCH]."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

# Pad ss min [HAND]; also keep historical 1.08 floor.
SUPPLIES = (("pad_ss", 1.108), ("floor", 1.08))
# µm/mA sweeps — cheapest headroom fix.
DENSITIES = (20.0, 40.0, 60.0, 80.0, 120.0)


def one(tag, vdd, dens, f_ghz=3.12):
    C.apply_knobs(tail_um_per_ma=dens)
    # Patch CORNERS ss VDD for this trial
    E.CORNERS["ss"] = ("ss", "mos_ss", vdd, 125)
    path, names, ideal, ndiv, duty, v = E.build(
        "vhf", f_ghz * 1e9, E.CORNERS["ss"],
        tag=f"_tw{int(dens)}_{tag}")
    print(f"TRY dens={dens} vdd={vdd} w={C.tail_w():.1f}u L={C.TAIL_L} "
          f"I={C.I_LATCH*1e3:.2f}mA", flush=True)
    d = E.run(path)
    r = E.analyse(d, names, ideal, ndiv, duty, v, f_ghz * 1e9)
    ok = bool(r["ok"])
    print(f"  -> ok={ok} phase={r['max_phase_err']} "
          f"duty={r['duty_min']}/{r['duty_max']}", flush=True)
    return ok, r


def main():
    rows = []
    best = None
    for dens in DENSITIES:
        for tag, vdd in SUPPLIES:
            ok, r = one(tag, vdd, dens)
            rows.append((dens, vdd, ok, r["max_phase_err"],
                         r["duty_min"], r["duty_max"]))
            if ok and best is None:
                best = (dens, vdd)
            # If pad_ss fails, still try floor; if dens works at pad, try floor
        if best and best[0] == dens and best[1] == 1.108:
            # confirm floor for same dens
            pass
        # Early exit when both supplies pass at this dens
        passed = [x for x in rows if x[0] == dens and x[2]]
        if len(passed) >= 2:
            break
        if any(x[0] == dens and x[1] == 1.108 and x[2] for x in rows):
            # continue to next dens only if floor also needed — already in loop
            pass

    out = os.path.join(E.OUT, "summary_vhf_tail_fix.txt")
    # Also copy to shared out/
    lines = [
        "# P2.7.4a3 step 3a — MOSFET tail widen for VHF ss [SCH]",
        "",
        f"I_latch={C.I_LATCH*1e3:.3f} mA; SWING={C.SWING}; L={C.TAIL_L}.",
        "",
        "| µm/mA | VDD | divide | max|φ| | duty |",
        "|---:|---:|---|---:|---|",
    ]
    for dens, vdd, ok, ph, d0, d1 in rows:
        ds = f"{d0:.1f}/{d1:.1f}" if d0 is not None else "—"
        lines.append(
            f"| {dens:.0f} | {vdd:.3f} | {'OK' if ok else 'FAIL'} | "
            f"{ph:.2f} | {ds} |")
    if best:
        lines += ["", f"**First PASS:** {best[0]:.0f} µm/mA at VDD={best[1]} V."]
    else:
        lines += ["", "**No PASS** in density sweep — try R_L (step 3b)."]
    text = "\n".join(lines) + "\n"
    open(out, "w").write(text)
    shared = os.path.join(os.path.dirname(E.OUT) if False else
                          os.path.join(os.path.dirname(__file__), "out"),
                          "summary_vhf_tail_fix.txt")
    # E.OUT may be out_sole; always write analog/lo/sch/out/
    shared = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "out", "summary_vhf_tail_fix.txt")
    os.makedirs(os.path.dirname(shared), exist_ok=True)
    open(shared, "w").write(text)
    print("WROTE", out, shared, flush=True)
    print("TAIL_FIX_DONE", "PASS" if best else "FAIL", best, flush=True)
    return 0 if best else 1


if __name__ == "__main__":
    raise SystemExit(main())
