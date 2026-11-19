#!/usr/bin/env python3
"""P2.7.4b — sanity sim from hierarchical netlist source [SCH].

VHF tt 4.20 GHz and ss / 125 °C at V_min 1.181 V. Body ≡ lo_*_hier.vacask
(fingerprint PASS vs accepted flat).
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault("LO_SCH_OUT", "out")
sys.path.insert(0, HERE)

import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

OUT = os.path.join(HERE, "out")


def main():
    C.apply_knobs(i_latch=0.75e-3, vhf_i_latch=0.30e-3, b2=4.0,
                  vhf_tailless=True)
    cases = [
        ("vhf", "tt", 4.20e9),
        ("vhf", "ss", 4.20e9),
    ]
    lines = [
        "# P2.7.4b sanity from hierarchical netlist [SCH]\n",
        "Source: circuit.build_band_body ≡ netlists/lo_*_hier.vacask "
        "(fingerprint PASS vs accepted flat).\n\n",
        "| Case | Divides | LO mA | max |phi| deg | Duty % | note |\n",
        "|---|---|---:|---:|---:|---|\n",
    ]
    # Accepted reference (P2.7.4a3 / step0) [SCH]
    ref = {
        ("vhf", "tt"): {"ph": 0.08, "i_lo": 9.79},  # loose upper from ff precheck
        ("vhf", "ss"): {"ph": 0.5, "i_lo": 8.66},
    }
    for band, ctag, f in cases:
        corner = E.CORNERS[ctag]
        path, names, ideal, ndiv, duty, vdd = E.build(
            band, f, corner, tag="_hier")
        print(f"RUN {band} {ctag} {f/1e9:.2f} VDD={vdd} …", flush=True)
        try:
            d = E.run(path)
            res = E.analyse(d, names, ideal, ndiv, duty, vdd, f)
            print("RES", {k: res[k] for k in res if k != "rows"}, flush=True)
            divides = bool(res["ok"])
            ph = float(res["max_phase_err"])
            dmin, dmax = res["duty_min"], res["duty_max"]
            # LO current from TB supply sources if present in raw
            i_tot = float("nan")
            try:
                import numpy as np
                parts = []
                for nm in ("vbufs", "vdvs", "vcvs", "vdgs", "vdds"):
                    if nm in d:
                        # vacask may store current as i(vbufs) etc.
                        pass
                for key in d.keys():
                    kl = str(key).lower()
                    if kl.startswith("i(") and any(
                            s in kl for s in (
                                "vbufs", "vdvs", "vcvs", "vdgs", "vdds")):
                        parts.append(abs(float(np.mean(np.real(d[key])[-200:]))))
                if parts:
                    i_tot = sum(parts)
            except Exception:
                pass
            duty_s = (f"{dmin:.1f}/{dmax:.1f}"
                      if dmin is not None else "—")
            tag = "PASS" if divides else "FAIL"
            lines.append(
                f"| {band} {ctag} {f/1e9:.2f} | {tag} | "
                f"{i_tot*1e3:.2f} | {ph:.3f} | {duty_s} | "
                f"VDD={vdd} [SCH] |\n")
        except Exception as e:
            lines.append(
                f"| {band} {ctag} {f/1e9:.2f} | ERROR | — | — | — | {e} |\n")
            print("ERR", e, flush=True)
    path = os.path.join(OUT, "summary_hier_sanity.txt")
    open(path, "w").write("".join(lines))
    print("".join(lines), flush=True)
    print("WROTE", path, flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
