#!/usr/bin/env python3
"""P2.7.3b — post-layout VCO PN [PEX-RC lumped].

Netlist: schematic PDK devices + L2n0 EM + extracted wiring C/R + coupling
caps + separated tail C (pex_pn_lumped.json). Bank bypass MOS omitted (PSS);
tail+var bypass kept — same method as run_pnoise_nobank.py.

Points: ss85 @ 4.20 GHz; tt @ 3.65 (mid); top 4.20 and bottom 3.12 at tt;
VHF/UHF VCO freqs for duplex (175×24, 480×8 → 4.20; 130×24→3.12, 400×8→3.20).

Pass @ 1 MHz: ≤ −116 (VHF) / ≤ −115 (UHF) with margin; report 100 kHz.
On PSS fail: bank-omitted SCH + bank-switch bound [HAND].
"""
from __future__ import annotations

import json
import os
import sys
import traceback

import numpy as np
from vacask.rawfile import rawread

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
LAYOUT = os.path.join(HERE, "..", "layout", "p272c", "out")
os.makedirs(OUT, exist_ok=True)

sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "step2"))
import run_step2 as S2  # noqa: E402
import run_step3 as S3  # noqa: E402
from compare import fundamental_amplitude  # noqa: E402

S2.OUT = S3.OUT = OUT
GROUPS = ("tail", "var")  # bank omitted
LIM_VHF = -116.0
LIM_UHF = -115.0
BANK_SW_DB = 0.59  # tt bound [SCH]
DET_DB = 0.0       # [HAND] powered down
CML_DB = 0.5       # [HAND] ≤ +0.5 layout notes; real_load ≤ +0.3


def load_lump():
    for p in (
        os.path.join(LAYOUT, "pex_pn_lumped.json"),
        os.path.join(LAYOUT, "pex_vco_top", "pex_pn_lumped.json"),
    ):
        if os.path.exists(p):
            return json.load(open(p)), p
    raise SystemExit("missing pex_pn_lumped.json — run analyze_pex_pn_parasitics.py")


def parasitic_extra(L: dict) -> str:
    """Lumped tank + tail + key couplings [PEX-RC lumped]."""
    c = L["c_side_ff"]
    r = L["r_series_ohm"]
    ct = L["c_tail_pn_ff"]
    lines = [
        f"// P2.7.3b PEX-RC lumped parasitics from {L.get('_src', 'pex_pn')}\n",
        f"Rr_p (tp nr_p) resistor r={r}\n",
        f"Cr_p (nr_p 0) capacitor c={c}f\n",
        f"Rr_n (tn nr_n) resistor r={r}\n",
        f"Cr_n (nr_n 0) capacitor c={c}f\n",
        f"Ctail_pn (tail 0) capacitor c={ct}f\n",
    ]
    # Explicit couplings > 1 fF that matter for PN (vt, vbp, tail already in C_side
    # partially; add differential-ish extras that wiring-add undercounts)
    c_tn_tp = L.get("c_tn_tp_ff", 0.0)
    # tn−tp already in wiring partners; optional half for diff — skip double count
    for tag, n1, n2, key in (
        ("cvt_n", "tn", "vt", "c_tn_vt_ff"),
        ("cvt_p", "tp", "vt", "c_tp_vt_ff"),
        ("cvbp_n", "tn", "vbp", "c_tn_vbp_ff"),
        ("cvbp_p", "tp", "vbp", "c_tp_vbp_ff"),
        ("cvdd_n", "tn", "vdd", "c_tn_vdd_ff"),
        ("cvdd_p", "tp", "vdd", "c_tp_vdd_ff"),
        ("ctl_n", "tail", "tn", "c_tail_tn_ff"),
        ("ctl_p", "tail", "tp", "c_tail_tp_ff"),
    ):
        v = float(L.get(key, 0.0) or 0.0)
        if v >= 1.0:
            lines.append(f"C{tag} ({n1} {n2}) capacitor c={v}f\n")
    _ = c_tn_tp
    return "".join(lines)


def pnoise(code, vt, f0, itail, temp, tag, extra, harm=32, npts=16000,
           reltol="1e-6", tolscale="1e-3"):
    vals = ", ".join(f"{x:.0f}" for x in S3.OFFS)
    attempts = [
        (reltol, tolscale, npts, harm),
        (reltol, tolscale, 8000, harm),
        (reltol, "1e-2", 8000, 16),
        ("1e-5", "1e-2", 4000, 16),
    ]
    last_err = None
    for rt, ts, np_, h in attempts:
        sim = S2.netlist(
            f"pex_pn_{tag}", code, vt, itail=itail,
            bypass=True, bypass_groups=GROUPS,
            analysis=(
                f"  options temp={temp} reltol={rt} pss_tolscale={ts} "
                f"pss_minpts={np_}\n"
                '  analysis warm tran stop=80n step=5p maxstep=5p store="ss"\n'
                f'  analysis pn pnoise oscillator=1 tper={1/f0:.6e} tstab=0 '
                f'ic="ss" icmode="uic" maxharm={h} truncharm={max(8, h//2)} '
                f'in="iin" out=["tp", "tn"] outharm=1 values=[{vals}] writepss=1'
            ),
            extra="iin (0 tp) isource dc=0\n" + extra,
        )
        try:
            S2.run(sim)
            break
        except RuntimeError as e:
            last_err = e
            print(f"  pss fail {tag} reltol={rt} npts={np_} harm={h}: "
                  f"{[x for x in str(e).splitlines() if x.strip()][-1:]}",
                  flush=True)
    else:
        return None, last_err
    pss = rawread(os.path.join(OUT, "pn.pss.raw")).get()
    a, fp = fundamental_amplitude(
        pss["time"], np.real(pss["tp"]) - np.real(pss["tn"]))
    pn = rawread(os.path.join(OUT, "pn.raw")).get()
    off = np.real(pn["frequency"])
    l = 10 * np.log10(np.real(pn["onoise"]) / (a * a / 2))
    return dict(f=fp, amp=a, L={float(o): float(x) for o, x in zip(off, l)}), None


def main():
    L, src = load_lump()
    L["_src"] = src
    extra = parasitic_extra(L)
    lines = [
        "# P2.7.3b post-layout VCO phase noise [PEX-RC lumped]\n\n",
        "Netlist: schematic PDK devices + L2n0 EM + extracted wiring C/R "
        f"(C_side={L['c_side_ff']:.2f} fF, R={L['r_series_ohm']:.3f} Ω) + "
        f"C_tail_pn={L['c_tail_pn_ff']:.2f} fF + couplings ≥1 fF "
        "(vt/vbp/vdd/tail). Bank bypass omitted; tail+var bypass on "
        "[PEX-RC lumped / TOOL]. Magic svaricap not used (2-terminal); "
        "schematic 4-terminal PDK svaricap kept [TOOL].\n\n",
        f"Source lump: `{src}`\n\n",
    ]
    r, meas = S3.load_sizing()
    # Cases: (tag, mos, cap, temp, f0_Hz, band_limit_name)
    cases = [
        ("ss85_4.20", "mos_ss", "cap_typ", 85, 4.20e9, "VHF"),  # worst
        ("tt_3.65", "mos_tt", "cap_typ", 27, 3.65e9, "VHF"),
        ("tt_4.20", "mos_tt", "cap_typ", 27, 4.20e9, "UHF"),
        ("tt_3.12", "mos_tt", "cap_typ", 27, 3.12e9, "VHF"),
        ("tt_3.20", "mos_tt", "cap_typ", 27, 3.20e9, "UHF"),  # 400×8
    ]
    rows = []
    any_pss = False
    for tag, mos, cap, temp, f0, band in cases:
        S3.set_corner(mos, cap)
        code = S3.code_for(f0, temp, f"{tag}_c")
        it = S3.itail_for(f0, meas)
        print(f"  {tag}: code={code} itail={it*1e3:.2f} mA …", flush=True)
        pn, err = pnoise(code, S2.VTUNE_MID, f0, it, temp, tag, extra)
        rows.append((tag, mos, cap, temp, f0, band, code, it, pn, err))
        if pn:
            any_pss = True
            l1 = pn["L"].get(1e6, float("nan"))
            l100 = pn["L"].get(1e5, float("nan"))
            print(f"    f={pn['f']/1e9:.3f} Amp={pn['amp']:.2f} "
                  f"L@100k={l100:.1f} L@1M={l1:.1f}", flush=True)

    lines.append("## PSS / pnoise results [PEX-RC lumped]\n\n")
    lines.append(
        "| tag | MOS | T | f0 | code | L@100 kHz | L@1 MHz | "
        "limit | margin | ok |\n")
    lines.append("|---|---|---|---:|---:|---:|---:|---:|---:|---|\n")
    worst_m = 1e9
    all_ok = True
    for tag, mos, cap, temp, f0, band, code, it, pn, err in rows:
        lim = LIM_VHF if band == "VHF" else LIM_UHF
        if pn is None:
            lines.append(
                f"| {tag} | {mos} | {temp} | {f0/1e9:.2f} | {code} | — | "
                f"PSS fail | {lim:.0f} | — | NO |\n")
            all_ok = False
            continue
        l1 = pn["L"].get(1e6, float("nan"))
        l100 = pn["L"].get(1e5, float("nan"))
        # Apply hand bounds on top of bank-omitted PSS
        l1_tot = l1 + BANK_SW_DB + DET_DB + CML_DB
        mar = lim - l1_tot
        worst_m = min(worst_m, mar)
        ok = mar >= 0
        all_ok = all_ok and ok
        lines.append(
            f"| {tag} | {mos} | {temp} | {pn['f']/1e9:.3f} | {code} | "
            f"{l100:.1f} | {l1:.1f} (→{l1_tot:.1f} w/ bounds) | "
            f"{lim:.0f} | {mar:+.1f} | {'yes' if ok else 'NO'} |\n")

    lines.append(
        f"\nBounds added to L@1 MHz: bank-switch +{BANK_SW_DB:.2f} dB [SCH], "
        f"detector +{DET_DB:.1f} dB [HAND], CML +{CML_DB:.1f} dB [HAND].\n")
    if not any_pss:
        lines.append(
            "\n**PSS did not converge** on any setting with PEX lumped "
            "parasitics [TOOL]. Fall back: prior bank-omitted SCH "
            "(`summary_pn_nobank.txt`) tt −122.7 / ss85 −119.4 @ 1 MHz "
            "+ bank-switch bound +0.59 dB [SCH] + detector/CML [HAND].\n")
        # Fill HAND table
        hand = [
            ("ss85_4.20_HAND", -119.4, LIM_VHF),
            ("tt_3.65_HAND", -122.7, LIM_VHF),
        ]
        lines.append("\n| tag | L@1 MHz SCH nobank | +bounds | limit | margin |\n")
        lines.append("|---|---:|---:|---:|---:|\n")
        for tag, l1, lim in hand:
            tot = l1 + BANK_SW_DB + DET_DB + CML_DB
            lines.append(
                f"| {tag} | {l1:.1f} | {tot:.1f} | {lim:.0f} | "
                f"{lim-tot:+.1f} |\n")
            worst_m = min(worst_m, lim - tot)
        all_ok = worst_m >= 0
        method = "HAND/SCH bank-omitted + bounds"
    else:
        method = "PEX-RC lumped PSS" if all(
            r[8] is not None for r in rows) else "mixed PSS/HAND"

    lines.append(f"\nWorst margin @ 1 MHz (with bounds): {worst_m:+.1f} dB "
                 f"[{method}]\n")
    lines.append(
        f"\nPN gate: {'PASS' if all_ok else 'FAIL'} [{method}]\n")

    # Hand-bound sims note
    lines.append("\n## Hand bounds (bank / detector / CML)\n\n")
    if any_pss:
        lines.append(
            "- Bank-switch: not re-simulated in PEX netlist (bank devices "
            f"omitted for PSS); use accepted +{BANK_SW_DB:.2f} dB [SCH].\n"
            f"- Detector: +{DET_DB:.1f} dB [HAND] (powered down in hold).\n"
            f"- CML load: +{CML_DB:.1f} dB [HAND] (PSS with CML ÷N fails).\n"
        )
    else:
        lines.append(
            "- PSS failed with PEX lump → bounds kept [HAND]/[SCH] as above; "
            "not re-simulated in this netlist [TOOL].\n"
        )

    path = os.path.join(OUT, "summary_pex_vco_pn.txt")
    open(path, "w").writelines(lines)
    open(os.path.join(LAYOUT, "summary_pex_vco_pn.txt"), "w").writelines(lines)
    # Sidecar for system PN
    open(os.path.join(OUT, "pex_pn_l1m.json"), "w").write(json.dumps({
        "method": method,
        "any_pss": any_pss,
        "worst_margin_db": worst_m,
        "rows": [
            {
                "tag": t, "l1m": (None if pn is None else pn["L"].get(1e6)),
                "l1m_with_bounds": (
                    None if pn is None else
                    pn["L"].get(1e6) + BANK_SW_DB + DET_DB + CML_DB),
                "band": b,
            }
            for t, _, _, _, _, b, _, _, pn, _ in rows
        ],
        "fallback_ss85_l1m": -119.4 + BANK_SW_DB + DET_DB + CML_DB,
        "bank_sw_db": BANK_SW_DB, "det_db": DET_DB, "cml_db": CML_DB,
    }, indent=2) + "\n")
    print("".join(lines))
    print(f"Wrote {path}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        traceback.print_exc()
        sys.exit(2)
