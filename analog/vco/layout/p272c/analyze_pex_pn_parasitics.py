#!/usr/bin/env python3
"""P2.7.3b — separate tail vs cbf, inductor pad vs MIM, coupling >1 fF [PEX-RC].

Reads Magic .ext from P2.7.3a. Writes:
  out/summary_pex_vco_pn_parasitics.txt
  out/pex_vco_top/pex_pn_lumped.json
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
PEX = os.path.join(OUT, "pex_vco_top")
EXT = os.path.join(PEX, "vco_top.ext")
SPICE = os.path.join(PEX, "vco_top.pex.spice")

sys.path.insert(0, os.path.join(HERE, "..", "p272b"))
import analyze_pex_ext as A  # noqa: E402

# Intentional device plate area (fF) from PDK 1.5 fF/µm² — subtract from
# substrate node C when attributing interconnect / pad [PDK].
CAP_AREA = 1.5


def to_ff(af: float) -> float:
    return af / 1000.0


def mim_plates_on_ports(spice_path: str) -> dict[str, float]:
    """Sum W*L*1.5 for cap_* devices whose top port roots to tn/tp/ct/tail/nbf."""
    plates: dict[str, float] = defaultdict(float)
    if not os.path.exists(spice_path):
        return plates
    for ln in open(spice_path):
        s = ln.strip()
        if "cap_rfcmim" not in s and "cap_cmim" not in s:
            continue
        toks = s.replace("(", " ").replace(")", " ").split()
        nodes, w, l = [], None, None
        for t in toks[1:]:
            if t.startswith("w="):
                w = float(t[2:].rstrip("u"))
            elif t.startswith("l="):
                l = float(t[2:].rstrip("u"))
            elif t.startswith("cap_"):
                continue  # model name sits between nodes and w=/l=
            elif "=" in t:
                continue
            else:
                nodes.append(t)
        if w is None or l is None or len(nodes) < 1:
            continue
        c = w * l * CAP_AREA
        # Magic extresist names like tp.t4 — root before '.'
        for n in nodes[:2]:
            root = n.split(".")[0].lower()
            if root in ("tn", "tp", "ct", "tail", "nbf"):
                plates[root] += c
    return dict(plates)


def analyze():
    find, node_c, caps = A.parse_ext(EXT)
    # Aggregate substrate and couplings after merge
    sub = defaultdict(float)
    for n, c in node_c.items():
        sub[find(n)] += c

    coup = defaultdict(lambda: defaultdict(float))
    for a, b, c in caps:
        ra, rb = find(a), find(b)
        if ra == rb:
            continue
        coup[ra][rb] += c
        coup[rb][ra] += c

    def wiring(port: str) -> float:
        return to_ff(sum(coup[port].values()))

    def couple_ff(a: str, b: str) -> float:
        return to_ff(coup[a].get(b, 0.0))

    # --- Tail vs filter (nbf / cbf) ---
    # Magic may name filter mid-node as nbf or anonymized. Prefer named nbf;
    # also look for large C between tail and a node that is mostly substrate
    # (cbf bottoms to gnd). Report C(tail−nbf), C(tail−gnd-like), C(nbf).
    gnd_like = {"gnd", "sub!", "0"}
    c_tail_gnd = sum(
        v for k, v in coup["tail"].items()
        if find(k) in gnd_like or str(k).endswith("gnd")
    )
    c_tail_nbf = coup["tail"].get("nbf", 0.0)
    # anonymous partners > 5 fF on tail (likely filter / metal)
    tail_partners = sorted(
        ((to_ff(v), k) for k, v in coup["tail"].items()), reverse=True
    )

    # Heuristic: filter-node C ≈ substrate on nbf if present; else largest
    # non-gnd, non-tn/tp partner of tail that looks like a big MIM island.
    sub_nbf = to_ff(sub.get("nbf", 0.0))
    wire_nbf = wiring("nbf") if "nbf" in sub or "nbf" in coup else 0.0

    # Tail-node interconnect for PN: wiring add on tail + C(tail−tn/tp)
    # excluding C(tail−nbf) if separable. Hand was 9.9 fF line C.
    c_tail_tn = couple_ff("tail", "tn")
    c_tail_tp = couple_ff("tail", "tp")
    wire_tail = wiring("tail")
    # Separated: remove coupling to nbf from "tail wiring" if present
    wire_tail_core = wire_tail - to_ff(c_tail_nbf)
    # Real tail C for PN ≈ wiring among RF/core nets + modest substrate
    # residual after removing estimated cbf plate from sub_tail.
    plates = mim_plates_on_ports(SPICE)
    sub_tail = to_ff(sub["tail"])
    # cbf is 7× cmim ~68.94² → ~7140 fF total on nbf, not on tail. If Magic
    # merged nbf into tail, sub_tail would be huge — check.
    cbf_est = plates.get("nbf", 0.0) + plates.get("tail", 0.0) * 0  # noqa
    # From spice: devices on nbf
    # Use partner list: if nbf missing, attribute excess sub_tail over hand
    # line to filter merge.
    HAND_TAIL = 9.9
    if sub_nbf > 1.0 or to_ff(c_tail_nbf) > 0.5:
        # Clean separation available
        c_tail_pn = wire_tail_core + min(sub_tail, HAND_TAIL * 1.5)
        method = "nbf named: wiring(tail)−C(tail−nbf) + capped substrate"
    else:
        # No nbf port: take wiring partners excluding tn/tp/gnd as "other"
        # and treat large anonymous C as filter; keep tn/tp/gnd + small.
        keep = 0.0
        filter_like = 0.0
        for v_ff, k in tail_partners:
            rk = find(k) if k in node_c or True else k
            name = str(k)
            if name in ("tn", "tp", "ct", "vdd") or name in gnd_like:
                keep += v_ff
            elif v_ff >= 5.0:
                filter_like += v_ff
            else:
                keep += v_ff
        c_tail_pn = keep
        method = (
            f"no nbf label: keep tn/tp/supply/small; "
            f"filter-like (≥5 fF anon) = {filter_like:.2f} fF excluded"
        )

    # --- Inductor pad C vs MIM-plate substrate ---
    # Pad estimate: substrate on tn/tp minus estimated MIM top-plate merge,
    # floored at 0. Cross-check with C to ct (pad-ish) and EM cp.
    sub_tn, sub_tp = to_ff(sub["tn"]), to_ff(sub["tp"])
    mim_tn = plates.get("tn", 0.0)
    mim_tp = plates.get("tp", 0.0)
    # Prior bank: substrate ≈ MIM tops; pad/interconnect residual:
    pad_tn = max(0.0, sub_tn - mim_tn)
    pad_tp = max(0.0, sub_tp - mim_tp)
    # If mim_plates parse failed (0), fall back: pad ≈ fraction of wiring
    # already counted; report substrate and MIM estimate separately.
    if mim_tn < 1.0 and mim_tp < 1.0:
        pad_method = (
            "MIM plate parse from spice ports failed (fingered names); "
            "report substrate raw; pad C not separated numerically — "
            "use EM cp + wiring add only for PN [TOOL]"
        )
        pad_tn = pad_tp = float("nan")
    else:
        pad_method = "sub(tn/tp) − Σ(cap_* W·L·1.5 on port) [PEX-RC/PDK]"

    # --- Coupling > 1 fF from tn/tp ---
    interesting = {"vt", "vbp", "tail", "vdd", "ct", "hold", "en", "rep",
                   "vbp_tail", "nbf", "gnd"}
    rows = []
    for port in ("tn", "tp"):
        for k, v in coup[port].items():
            ff = to_ff(v)
            if ff < 1.0:
                continue
            name = str(k)
            if name in interesting or name in ("tn", "tp") or ff >= 1.0:
                # skip pure anonymous unless ≥ 2 fF
                if name.startswith("a_") and ff < 2.0:
                    continue
                rows.append((ff, port, name))
    rows.sort(reverse=True)

    # Lumped bundle for PN
    wire_tn = wiring("tn")
    wire_tp = wiring("tp")
    c_side = max(wire_tn, wire_tp)
    # series R from prior pex_lumped
    prev = {}
    pj = os.path.join(PEX, "pex_lumped.json")
    if os.path.exists(pj):
        prev = json.load(open(pj))
    r_ser = float(prev.get("r_series_ohm", 0.24))

    lump = {
        "c_side_ff": round(c_side, 4),
        "wire_tn_ff": round(wire_tn, 4),
        "wire_tp_ff": round(wire_tp, 4),
        "c_tn_tp_ff": round(couple_ff("tn", "tp"), 4),
        "r_series_ohm": r_ser,
        "c_tail_pn_ff": round(c_tail_pn, 4),
        "c_tail_wiring_ff": round(wire_tail, 4),
        "c_tail_nbf_ff": round(to_ff(c_tail_nbf), 4),
        "c_tail_tn_ff": round(c_tail_tn, 4),
        "c_tail_tp_ff": round(c_tail_tp, 4),
        "sub_tail_ff": round(sub_tail, 4),
        "sub_nbf_ff": round(sub_nbf, 4),
        "c_tn_vt_ff": round(couple_ff("tn", "vt"), 4),
        "c_tp_vt_ff": round(couple_ff("tp", "vt"), 4),
        "c_tn_vbp_ff": round(couple_ff("tn", "vbp"), 4),
        "c_tp_vbp_ff": round(couple_ff("tp", "vbp"), 4),
        "c_tn_vdd_ff": round(couple_ff("tn", "vdd"), 4),
        "c_tp_vdd_ff": round(couple_ff("tp", "vdd"), 4),
        "pad_tn_ff": None if pad_tn != pad_tn else round(pad_tn, 4),
        "pad_tp_ff": None if pad_tp != pad_tp else round(pad_tp, 4),
        "sub_tn_ff": round(sub_tn, 4),
        "sub_tp_ff": round(sub_tp, 4),
        "hand_tail_ff": HAND_TAIL,
        "hand_side_ff": float(prev.get("hand_side_ff", 96.2)),
    }
    open(os.path.join(PEX, "pex_pn_lumped.json"), "w").write(
        json.dumps(lump, indent=2) + "\n"
    )
    open(os.path.join(OUT, "pex_pn_lumped.json"), "w").write(
        json.dumps(lump, indent=2) + "\n"
    )

    lines = [
        "# P2.7.3b PN parasitics from P2.7.3a Magic .ext [PEX-RC]\n\n",
        f"Source: `{os.path.relpath(EXT, HERE)}` [PEX-RC].\n\n",
        "## 1) Tail-node C vs cbf / filter node\n\n",
        f"- Method: {method} [PEX-RC].\n",
        f"- Tail wiring add (all partners): **{wire_tail:.2f} fF** [PEX-RC]\n",
        f"- C(tail−tn)/C(tail−tp): {c_tail_tn:.2f} / {c_tail_tp:.2f} fF "
        f"[PEX-RC]\n",
        f"- C(tail−nbf): {to_ff(c_tail_nbf):.2f} fF; nbf substrate: "
        f"{sub_nbf:.2f} fF [PEX-RC]\n",
        f"- Tail substrate node C: {sub_tail:.2f} fF [PEX-RC]\n",
        f"- **C_tail for PN (separated): {c_tail_pn:.2f} fF** "
        f"(hand line {HAND_TAIL} fF) [PEX-RC]/[HAND]\n",
        "- Note: cbf (7× cmim) belongs on the bias-filter node (nbf), not "
        "the oscillating tail; do not load the PN tail with cbf area "
        "[PDK/SCH].\n\n",
        "Top tail coupling partners:\n",
    ]
    for v_ff, k in tail_partners[:12]:
        lines.append(f"- `{k}`: {v_ff:.3f} fF\n")

    lines += [
        "\n## 2) Inductor pad C vs substrate / MIM plate\n\n",
        f"- {pad_method}\n",
        f"- Substrate tn/tp: {sub_tn:.2f} / {sub_tp:.2f} fF [PEX-RC]\n",
        f"- MIM plate Σ on tn/tp (spice parse): {mim_tn:.1f} / "
        f"{mim_tp:.1f} fF [PDK]\n",
    ]
    if pad_tn == pad_tn:
        lines.append(
            f"- **Pad residual tn/tp: {pad_tn:.2f} / {pad_tp:.2f} fF** "
            f"[PEX-RC]\n"
        )
    else:
        lines.append(
            "- Pad residual: **not separated** this job — PN uses wiring "
            "add + L2n0 EM `cp` only; substrate/MIM mix left as extract "
            "caveat [TOOL].\n"
        )

    lines += [
        "\n## 3) Coupling > 1 fF (tn/tp ↔ vt, controls, tail, supply)\n\n",
        "| C (fF) | from | to |\n|---:|---|---|\n",
    ]
    for ff, a, b in rows[:40]:
        lines.append(f"| {ff:.2f} | {a} | {b} |\n")

    lines += [
        "\n## PN lumped bundle\n\n",
        f"- C_side (wiring max) = **{c_side:.2f} fF**, R = **{r_ser:.3f} Ω** "
        f"[PEX-RC]\n",
        f"- C_tail_pn = **{c_tail_pn:.2f} fF** [PEX-RC]\n",
        f"- Explicit: C(tn−tp)={lump['c_tn_tp_ff']:.2f}, "
        f"C(tn/tp−vt)={lump['c_tn_vt_ff']:.2f}/{lump['c_tp_vt_ff']:.2f}, "
        f"C(tn/tp−vbp)={lump['c_tn_vbp_ff']:.2f}/{lump['c_tp_vbp_ff']:.2f}, "
        f"C(tn/tp−vdd)={lump['c_tn_vdd_ff']:.2f}/{lump['c_tp_vdd_ff']:.2f}, "
        f"C(tail−tn/tp)={c_tail_tn:.2f}/{c_tail_tp:.2f} fF [PEX-RC]\n",
        f"- Wrote `out/pex_pn_lumped.json`\n",
    ]
    path = os.path.join(OUT, "summary_pex_vco_pn_parasitics.txt")
    open(path, "w").writelines(lines)
    print("".join(lines))
    print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    if not os.path.exists(EXT):
        raise SystemExit(f"missing {EXT}: run P2.7.3a extract first")
    raise SystemExit(analyze())
