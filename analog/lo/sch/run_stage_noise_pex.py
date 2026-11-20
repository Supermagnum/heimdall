#!/usr/bin/env python3
"""P2.7.4b — per-stage LO floor with extracted latch wiring C [SCH + PEX-RC].

Accepted floor (summary_a3_floor_d7 / summary_stage_noise) used C_ck=15 fF
only on clock nets (buffer ckp/ckn, CML ckp/ckn, converter/logic clocks).
No extra C on latch qp/qn or tail [SCH].

This run loads substrate+coupling wiring C from the latch PEX tables and
places it on clock (+0.87 fF assembly [HAND]), qp/qn-class, and tail nets
inside the CML stage. Buffer/converter/logic keep C_ck = clock_max+asm so
the path load is consistent.
"""
from __future__ import annotations

import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.environ["LO_SCH_OUT"] = "out"
sys.path.insert(0, HERE)
import circuit as C  # noqa: E402
import run_stage_noise as SN  # noqa: E402

# Extracted wiring C [PEX-RC] — summary_pex_wiring_cml_latch_*.txt (sub+coup)
UHF = dict(ckp=8.38e-15, ckn=3.54e-15, qp=19.49e-15, qn=23.33e-15, ta=17.53e-15)
VHF = dict(ckp=8.28e-15, ckn=3.44e-15, qp=18.42e-15, qn=22.24e-15, ta=0.0)
C_ASM = 0.87e-15  # latch↔latch + buffer→latch on clock [HAND]
TARGET_UHF = -151.0
TARGET_VHF = -151.0  # ≤ −150 with ≈1 dB margin [PROP/owner]


def caps_for(band: str) -> dict:
    d = UHF if band == "uhf" else VHF
    return {
        "ckp": d["ckp"] + C_ASM,
        "ckn": d["ckn"] + C_ASM,
        "qp": d["qp"],
        "qn": d["qn"],
        "ta": d["ta"],
        "ck_max": max(d["ckp"], d["ckn"]) + C_ASM,
        "q_max": max(d["qp"], d["qn"]),
    }


def add_caps(body: str, nodes_c: list[tuple[str, float]]) -> str:
    lines = []
    for i, (n, c) in enumerate(nodes_c):
        if c <= 0:
            continue
        lines.append(f"cpex{i} ({n} 0) capacitor c={c:.6e}\n")
    return "".join(lines) + body


def stage_buffer_pex(band, f_vco, corner):
    caps = caps_for(band)
    SN.C_CK = caps["ck_max"]
    return SN.stage_buffer(band, f_vco, corner)


def stage_cml_pex(band, f_vco, corner):
    caps = caps_for(band)
    ctag, mos, vdd, temp = corner
    i_ = C.I_LATCH if band == "uhf" else C.VHF_I_LATCH
    C.apply_knobs(i_latch=i_, vhf_i_latch=C.VHF_I_LATCH, b2=C.B2,
                  vhf_tailless=True)
    ii, rl, w = C.L1.cml_params(i_, vdd)
    if band == "vhf" and C.VHF_TAILLESS:
        C.L1.VARIANT["tailless"] = True
    else:
        C.L1.VARIANT["tailless"] = False
    body_cml, out = C.L1.div_body(2 if band == "uhf" else 3, ii, rl, w, vdd)
    body_cml = body_cml.replace("(vdd ", "(vdv ")
    body_cml = C.replace_tails(body_cml, i_)
    f_out = f_vco / (2 if band == "uhf" else 3)

    # Latch-class nets: every differential Q / intermediate load, tails
    if band == "uhf":
        q_nodes = [("map", caps["qp"]), ("man", caps["qn"]),
                   ("qp", caps["qp"]), ("qn", caps["qn"])]
        t_nodes = [("tam", caps["ta"]), ("tas", caps["ta"])]
    else:
        q_nodes = [
            ("orp", caps["qp"]), ("orn", caps["qn"]),
            ("map", caps["qp"]), ("man", caps["qn"]),
            ("q1p", caps["qp"]), ("q1n", caps["qn"]),
            ("mbp", caps["qp"]), ("mbn", caps["qn"]),
            ("q2p", caps["qp"]), ("q2n", caps["qn"]),
        ]
        # tailless latches: only NOR MOSFET tail tg — no latch extract yet;
        # use UHF ta as stand-in until NOR PEX [HAND]
        t_nodes = [("tg", UHF["ta"])]

    extra = ([(n, c) for n, c in q_nodes + t_nodes]
             + [("ckp", caps["ckp"]), ("ckn", caps["ckn"])])
    body = (f"vdvs (vdv 0) vsource dc={vdd}\nvdds (vdd 0) vsource dc={vdd}\n"
            + SN.nbias_standin()
            + add_caps("", extra)
            + SN.noisy(body_cml))
    hdr = C.HEADER.format(title="cml_pex", mos=mos, f=f_vco, amp=0.55,
                          vcm=vdd - 0.55, shape=0.0, offs=0.0, t0=-1, tr=1e-12)
    hdr += "xck (ckp ckn) clk\n"
    th_cml = vdd - ii * rl / 2
    return SN.write_run(f"st_{band}_cml_pex", mos, temp, hdr, body, out[0],
                        f_out, vdd, th=th_cml)


def stage_converter_pex(band, f_vco, corner):
    caps = caps_for(band)
    SN.C_CK = caps["ck_max"]
    return SN.stage_converter(band, f_vco, corner)


def stage_logic_pex(band, f_vco, corner):
    caps = caps_for(band)
    SN.C_CK = caps["ck_max"]
    return SN.stage_logic(band, f_vco, corner)


def main():
    os.makedirs(OUT, exist_ok=True)
    # Accepted currents: UHF 0.75 mA, VHF 0.30 mA, B2=4
    C.apply_knobs(i_latch=0.75e-3, vhf_i_latch=0.30e-3, b2=4.0,
                  vhf_tailless=True)
    lines = [
        "# P2.7.4b per-stage LO floor with extracted latch C [SCH + PEX-RC]\n\n",
        "## Prior assumption (accepted floor)\n",
        "- C_ck = **15 fF/side** on clock nets only (buffer ckp/ckn, CML ckp/ckn, "
        "converter/logic clocks) [SCH `run_stage_noise.py`].\n",
        "- **No** extra C on latch qp/qn or tail in that run [SCH].\n",
        "- Reported: UHF **−154.7**, VHF **−158.6 / −159.1** dBc/Hz [SCH "
        "`summary_a3_floor_d7.txt` / `summary_stage_noise.txt`].\n\n",
        "## This run (extracted)\n",
        "| band | ckp+asm | ckn+asm | qp | qn | ta | unit | tag |\n",
        "|---|---:|---:|---:|---:|---:|---|---|\n",
    ]
    for band, d in (("uhf", UHF), ("vhf", VHF)):
        lines.append(
            f"| {band} | {(d['ckp']+C_ASM)*1e15:.2f} | "
            f"{(d['ckn']+C_ASM)*1e15:.2f} | {d['qp']*1e15:.2f} | "
            f"{d['qn']*1e15:.2f} | {d['ta']*1e15:.2f} | fF | "
            f"[PEX-RC]+[HAND] |\n"
        )
    lines.append(
        f"\nAssembly on clock only: **{C_ASM*1e15:.2f} fF** [HAND]. "
        "VHF NOR `tg` uses UHF ta as stand-in until NOR PEX [HAND].\n\n"
    )
    open(os.path.join(OUT, "summary_floor_pex_c_assumptions.txt"), "w").write(
        "".join(lines))
    print("".join(lines), flush=True)

    all_out = {}
    report = list(lines)
    for band in ("uhf", "vhf"):
        # Band current
        if band == "uhf":
            C.apply_knobs(i_latch=0.75e-3, vhf_i_latch=0.30e-3, b2=4.0,
                          vhf_tailless=True)
        else:
            C.apply_knobs(i_latch=0.30e-3, vhf_i_latch=0.30e-3, b2=4.0,
                          vhf_tailless=True)
        f_vco = SN.F_VCO_UHF if band == "uhf" else SN.F_VCO_VHF
        f_lo = f_vco / (8 if band == "uhf" else 24)
        print(f"## {band.upper()} floor PEX\n", flush=True)
        rows = []
        for fn in (stage_buffer_pex, stage_cml_pex, stage_converter_pex,
                   stage_logic_pex):
            m = fn(band, f_vco, SN.CORNER)
            st = fn.__name__.replace("stage_", "").replace("_pex", "")
            m["stage"] = f"{band}_{st}"
            print(f"  {st}: ok={m.get('ok')} L={m.get('L', float('nan')):.1f} "
                  f"method={m.get('method')}", flush=True)
            if m.get("ok"):
                rows.append(m)
        L_sum, parts = SN.sum_to_lo(rows, f_lo)
        tgt = TARGET_UHF if band == "uhf" else TARGET_VHF
        gate = "PASS" if L_sum <= tgt else "FAIL"
        report.append(f"## {band.upper()}\n\n")
        report.append(
            "| Stage | Method | jit fs | L@f_out | L→LO |\n"
            "|---|---|---:|---:|---:|\n")
        for name, Lm, Llo, jit in parts:
            report.append(
                f"| {name} | tran-zoh | {jit*1e15:.0f} | {Lm:.1f} | {Llo:.1f} |\n"
            )
        report.append(
            f"\n**Summed LO floor:** {L_sum:.1f} dBc/Hz [SCH+PEX-RC]\n"
            f"Target ≤ {tgt:.0f} → **{gate}**\n\n")
        all_out[band] = dict(L=L_sum, gate=gate, parts=parts)
        print(f"  SUM {L_sum:.1f} {gate}\n", flush=True)

    path = os.path.join(OUT, "summary_floor_pex_c.txt")
    open(path, "w").write("".join(report))
    open(os.path.join(OUT, "floor_pex_c.json"), "w").write(
        json.dumps(all_out, indent=2, default=float))
    print("Wrote", path, flush=True)
    ok = all(v["gate"] == "PASS" for v in all_out.values())
    return 0 if ok else 2


if __name__ == "__main__":
    raise SystemExit(main())
