#!/usr/bin/env python3
"""Re-report latch wiring C with corrected substrate+coupling method [PEX-RC].

Reuses existing Magic .ext if present; re-runs Magic if missing.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
sys.path.insert(0, HERE)
import wiring_c_method as W  # noqa: E402

BUDGET = 15.0


def assembly_hand():
    c_m2, c_m3, w, k = 0.03, 0.025, 0.4, 1.5
    c_l2l = k * 15.0 * w * c_m2
    c_b2l = k * 40.0 * w * c_m3
    return {
        "c_l2l_ff": round(c_l2l, 2),
        "c_b2l_ff": round(c_b2l, 2),
        "c_asm_ff": round(c_l2l + c_b2l, 2),
        "note": "M2 15 µm + M3 40 µm ×0.4 µm × dens ×1.5 [HAND]",
    }


def ensure_ext(cell: str) -> str:
    pex = os.path.join(OUT, f"pex_{cell}")
    ext = os.path.join(pex, f"{cell}.ext")
    if os.path.exists(ext):
        return ext
    script = (f"run_pex_{cell}.py" if cell != "cml_latch_vhf_tl"
              else "run_pex_cml_latch_vhf_tl.py")
    if cell == "cml_latch_uhf":
        script = "run_pex_cml_latch_uhf.py"
    print(f"missing {ext}; running {script}", flush=True)
    r = subprocess.run([sys.executable, "-u", script], cwd=HERE)
    if r.returncode not in (0, 2) or not os.path.exists(ext):
        raise SystemExit(f"PEX failed for {cell}")
    return ext


def resolve_ta(ext: str) -> dict:
    find, node_c, *_ = W.parse_ext(
        ext, ("ckp", "ckn", "qp", "qn", "ta", "nb_lo", "vdd", "gnd", "sub!", "0"))
    roots = {find(n) for n in node_c}
    if "ta" in roots:
        return {"ta": "ta"}
    cand = "a_n5476_0#"
    if cand in node_c:
        return {"ta": cand}
    return {"ta": "a_n5476_0#"}


def report_uhf(ext: str, asm: dict) -> tuple[str, str, float]:
    alias = resolve_ta(ext)
    interest = ("ckp", "ckn", "qp", "qn", "ta")
    rows = W.wiring_per_net(ext, interest, alias=alias)
    ck = max(rows["ckp"]["wire_ff"], rows["ckn"]["wire_ff"])
    total = ck + asm["c_asm_ff"]
    gate = "PASS" if total <= BUDGET else "FAIL"
    lines = [
        "# cml_latch_uhf wiring C — corrected method [PEX-RC]\n\n",
        "## Method\n",
        W.METHOD_BLURB,
        f"- GDS: `out/cml_latch_uhf.gds`; .ext reused/regenerated [TOOL].\n",
        f"- Tail mapped to `{rows['ta']['ext_name']}` [PEX-RC].\n\n",
        "## Wiring C per net (substrate + coupling; device C excluded)\n\n",
        "| net | substrate | coupling | **wiring C** | unit | tag |\n",
        "|---|---:|---:|---:|---|---|\n",
    ]
    for p in interest:
        r = rows[p]
        lines.append(
            f"| {p} | {r['sub_ff']:.2f} | {r['coup_ff']:.2f} | "
            f"**{r['wire_ff']:.2f}** | fF | [PEX-RC] |\n"
        )
    lines.extend([
        "\n## Clock vs ≤ 15 fF / side\n\n",
        f"| quantity | value | unit | tag |\n",
        f"|---|---:|---|---|\n",
        f"| clock max(ckp,ckn) | {ck:.2f} | fF | [PEX-RC] |\n",
        f"| assembly add | {asm['c_asm_ff']:.2f} | fF | [HAND] |\n",
        f"| **clock + assembly** | **{total:.2f}** | fF | [PEX-RC]+[HAND] |\n",
        f"| budget | {BUDGET:.1f} | fF/side | [SCH] |\n",
        f"| gate | **{gate}** | | |\n\n",
        "Legacy coupling-only headline superseded "
        "(was 0.70 fF clock) [PEX-RC].\n",
    ])
    path = os.path.join(OUT, "summary_pex_wiring_cml_latch_uhf.txt")
    open(path, "w").write("".join(lines))
    open(os.path.join(OUT, "pex_cml_latch_uhf", "wiring_c.json"), "w").write(
        json.dumps({"rows": rows, "asm": asm, "method": "sub+coup",
                    "ck": ck, "total": total, "gate": gate}, indent=2))
    return path, gate, total


def report_vhf(ext: str, asm: dict) -> tuple[str, str, float]:
    interest = ("ckp", "ckn", "qp", "qn")
    rows = W.wiring_per_net(ext, interest)
    ck = max(rows["ckp"]["wire_ff"], rows["ckn"]["wire_ff"])
    total = ck + asm["c_asm_ff"]
    gate = "PASS" if total <= BUDGET else "FAIL"
    lines = [
        "# cml_latch_vhf_tl wiring C — corrected method [PEX-RC]\n\n",
        "## Method\n",
        W.METHOD_BLURB,
        "- Tailless: no separate ta (clk sources ≡ gnd) [SCH].\n\n",
        "## Wiring C per net (substrate + coupling; device C excluded)\n\n",
        "| net | substrate | coupling | **wiring C** | unit | tag |\n",
        "|---|---:|---:|---:|---|---|\n",
    ]
    for p in interest:
        r = rows[p]
        lines.append(
            f"| {p} | {r['sub_ff']:.2f} | {r['coup_ff']:.2f} | "
            f"**{r['wire_ff']:.2f}** | fF | [PEX-RC] |\n"
        )
    lines.extend([
        "\n## Clock vs ≤ 15 fF / side\n\n",
        f"| quantity | value | unit | tag |\n",
        f"|---|---:|---|---|\n",
        f"| clock max(ckp,ckn) | {ck:.2f} | fF | [PEX-RC] |\n",
        f"| assembly add | {asm['c_asm_ff']:.2f} | fF | [HAND] |\n",
        f"| **clock + assembly** | **{total:.2f}** | fF | [PEX-RC]+[HAND] |\n",
        f"| budget | {BUDGET:.1f} | fF/side | [SCH] |\n",
        f"| gate | **{gate}** | | |\n\n",
        "Legacy coupling-only headline superseded "
        "(was 0.58 fF clock) [PEX-RC].\n",
    ])
    path = os.path.join(OUT, "summary_pex_wiring_cml_latch_vhf_tl.txt")
    open(path, "w").write("".join(lines))
    open(os.path.join(OUT, "pex_cml_latch_vhf_tl", "wiring_c.json"), "w").write(
        json.dumps({"rows": rows, "asm": asm, "method": "sub+coup",
                    "ck": ck, "total": total, "gate": gate}, indent=2))
    return path, gate, total


def main():
    asm = assembly_hand()
    ext_u = ensure_ext("cml_latch_uhf")
    ext_v = ensure_ext("cml_latch_vhf_tl")
    pu, gu, tu = report_uhf(ext_u, asm)
    pv, gv, tv = report_vhf(ext_v, asm)
    print(open(pu).read())
    print(open(pv).read())
    print(f"UHF gate={gu} total={tu:.2f}; VHF gate={gv} total={tv:.2f}",
          flush=True)
    return 0 if gu == "PASS" and gv == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
