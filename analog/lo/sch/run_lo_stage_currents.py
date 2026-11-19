#!/usr/bin/env python3
"""P2.7.4a3 — measured LO stage supply currents [SCH].

Split rails (vbuf/vdv/vcv/vdg) as in step2; read *:flow(br) mean |I| after settle.
Replaces HAND 5×I_latch for VHF ÷3 with measured vdvs current.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import circuit as C  # noqa: E402
import run_equiv as E  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
V_MIN = 1.181
V_MAX = 1.208
# Corner matrix: name, mos, VDD, temp (tt/ss/ff × −40/27/125)
CORNERS = [
    ("tt_m40", "mos_tt", 1.20, -40),
    ("tt", "mos_tt", 1.20, 27),
    ("tt_125", "mos_tt", 1.20, 125),
    ("ss_m40", "mos_ss", V_MIN, -40),
    ("ss_27", "mos_ss", V_MIN, 27),
    ("ss", "mos_ss", V_MIN, 125),
    ("ff_m40", "mos_ff", V_MAX, -40),
    ("ff_27", "mos_ff", V_MAX, 27),
    ("ff_125", "mos_ff", V_MAX, 125),
]
# Representative frequencies
FREQ = {"uhf": 3.84e9, "vhf": 4.20e9}
# VCO+PLL not on LO chain rails — added in totals for D7
VCO_TYP = 3.59e-3
PLL_HAND = 1.5e-3


def mean_flow(d, src):
    """Mean |branch current| of vsource `src` [SCH]."""
    keep = np.real(d["time"])
    n0 = int(0.7 * len(keep))
    for key in (f"{src}:flow(br)", f"i({src})", src):
        try:
            arr = np.real(d[key])
            return float(np.mean(np.abs(arr[n0:])))
        except Exception:
            continue
    return float("nan")


def one(band, cname, mos, vdd, temp, f):
    C.apply_knobs(i_latch=0.75e-3, swing=0.5, b2=4.0, vhf_tailless=True)
    corner = (cname, mos, vdd, temp)
    tag = f"_ic_{cname}"
    path, names, ideal, ndiv, duty, v = E.build(band, f, corner, tag=tag)
    d = E.run(path)
    r = E.analyse(d, names, ideal, ndiv, duty, v, f)
    ib = mean_flow(d, "vbufs")
    ic = mean_flow(d, "vdvs")
    iv = mean_flow(d, "vcvs")
    ig = mean_flow(d, "vdgs")
    # vdd rail may carry bias only
    idd = mean_flow(d, "vdds")
    chain = ib + ic + iv + ig + (0.0 if math_nan(idd) else idd)
    print(
        f"{band} {cname} T={temp} V={vdd:.3f} ok={r['ok']} "
        f"Ibuf={ib*1e3:.3f} Icml={ic*1e3:.3f} Iconv={iv*1e3:.3f} "
        f"Ilogic={ig*1e3:.3f} Ibias={idd*1e3:.3f} Ichain={chain*1e3:.3f}",
        flush=True,
    )
    return dict(
        band=band, corner=cname, mos=mos, temp=temp, vdd=vdd, f=f,
        ok=bool(r["ok"]), ibuf=ib, icml=ic, iconv=iv, ilogic=ig,
        ibias=idd, ichain=chain,
        ilo=chain + VCO_TYP + PLL_HAND,
    )


def math_nan(x):
    return x != x


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(E.OUT, exist_ok=True)
    rows = []
    for band in ("uhf", "vhf"):
        f = FREQ[band]
        for cname, mos, vdd, temp in CORNERS:
            try:
                rows.append(one(band, cname, mos, vdd, temp, f))
            except Exception as e:
                print(f"FAIL {band} {cname}: {e}", flush=True)
                rows.append(dict(
                    band=band, corner=cname, mos=mos, temp=temp, vdd=vdd, f=f,
                    ok=False, ibuf=float("nan"), icml=float("nan"),
                    iconv=float("nan"), ilogic=float("nan"),
                    ibias=float("nan"), ichain=float("nan"),
                    ilo=float("nan"), err=str(e)[:80],
                ))

    def fmt(x):
        return "—" if x != x else f"{x*1e3:.3f}"

    lines = [
        "# P2.7.4a3 — measured LO stage currents [SCH]",
        "",
        "I_latch=0.75 mA; B2=4; VHF_TAILLESS=True. Split supplies; "
        "I = mean |*:flow(br)| after 70 % settle.",
        f"VCO {VCO_TYP*1e3:.2f} mA + PLL {PLL_HAND*1e3:.1f} mA [HAND] added for LO total.",
        "",
        "| Band | Corner | T | VDD | ok | I_buf | I_CML | I_conv | I_logic | "
        "I_bias | I_chain | LO total |",
        "|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        lines.append(
            f"| {r['band']} | {r['corner']} | {r['temp']} | {r['vdd']:.3f} | "
            f"{'OK' if r.get('ok') else 'FAIL'} | {fmt(r['ibuf'])} | "
            f"{fmt(r['icml'])} | {fmt(r['iconv'])} | {fmt(r['ilogic'])} | "
            f"{fmt(r['ibias'])} | {fmt(r['ichain'])} | {fmt(r['ilo'])} |"
        )

    # Highlight tt / ss VHF ÷3 measured vs HAND 5×I
    hand = 5 * 0.75e-3
    lines += [
        "",
        "## ÷3 current vs HAND 5×I_latch",
        "",
        f"HAND was {hand*1e3:.2f} mA (5 × 0.75). Measured I_CML = vdvs "
        f"(÷3 + NOR for VHF; ÷2 for UHF).",
        "",
    ]
    for lab in ("tt", "ss"):
        for band in ("uhf", "vhf"):
            hit = [r for r in rows
                   if r["band"] == band and r["corner"] == lab and r["icml"] == r["icml"]]
            if hit:
                r = hit[0]
                lines.append(
                    f"- {band} {lab}: I_CML = {r['icml']*1e3:.3f} mA "
                    f"[SCH] (HAND {hand*1e3:.2f} for VHF / "
                    f"{2*0.75:.2f} for UHF)"
                )

    path = os.path.join(OUT, "summary_lo_stage_currents.txt")
    open(path, "w").write("\n".join(lines) + "\n")
    # JSON for sizing
    import json
    open(os.path.join(OUT, "lo_stage_currents.json"), "w").write(
        json.dumps(rows, indent=2, default=float) + "\n")
    print("WROTE", path, flush=True)
    print("CURRENTS_DONE", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
