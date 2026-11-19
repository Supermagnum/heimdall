#!/usr/bin/env python3
"""Shared P2.7.3b/c PEX-RC lumped parasitic snippet [PEX-RC]."""
from __future__ import annotations

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
LAYOUT = os.path.join(HERE, "..", "layout", "p272c", "out")

# Matches the injected PEX block (from comment through last C/R before control)
_PEX_BLOCK_RE = re.compile(
    r"\n// PEX-RC lumped[^\n]*\n(?:[^\n]*\n)*?(?=control\n)"
)


def load_lump():
    for p in (
        os.path.join(LAYOUT, "pex_pn_lumped.json"),
        os.path.join(LAYOUT, "pex_vco_top", "pex_pn_lumped.json"),
    ):
        if os.path.exists(p):
            return json.load(open(p)), p
    raise SystemExit("missing pex_pn_lumped.json")


def parasitic_extra(
    L: dict | None = None,
    *,
    tie_vbp: bool = False,
    omit_ctl: bool = False,
    fold_vbp_into_cr: bool = False,
) -> str:
    """Lumped tank/tail/coupling [PEX-RC lumped].

    tie_vbp: add C to vbp (needs vbp driven).
    omit_ctl: drop C(tail−tn/tp); fold into C_tail_pn (+ Rtail series).
    fold_vbp_into_cr: merge C(tn/tp−vbp) into Cr (topo B). Else separate
    Ccvbp_*_gnd (topo C when omit_ctl). D22 SAR OP at 85 °C is code-coupled:
    some codes need B, others need C — dual-attempt in run_p273c_search [TOOL].
    """
    if L is None:
        L, _ = load_lump()
    c = float(L["c_side_ff"])
    r = L["r_series_ohm"]
    ct = float(L["c_tail_pn_ff"])
    c_tn = float(L.get("c_tail_tn_ff", 0.0) or 0.0)
    c_tp = float(L.get("c_tail_tp_ff", 0.0) or 0.0)
    c_vbp_n = float(L.get("c_tn_vbp_ff", 0.0) or 0.0)
    c_vbp_p = float(L.get("c_tp_vbp_ff", 0.0) or 0.0)
    c_n, c_p = c, c
    note = L.get("_src", "pex_pn")
    if omit_ctl:
        fold_ctl = (c_tn if c_tn >= 1.0 else 0.0) + (c_tp if c_tp >= 1.0 else 0.0)
        ct = ct + fold_ctl
        note = f"{note}; omit Cctl (fold {fold_ctl:.2f} fF → C_tail_pn={ct:.2f} fF)"
    if fold_vbp_into_cr and not tie_vbp:
        vn = c_vbp_n if c_vbp_n >= 1.0 else 0.0
        vp = c_vbp_p if c_vbp_p >= 1.0 else 0.0
        c_n = c + vn
        c_p = c + vp
        note = f"{note}; vbp→Cr (+{vn:.2f}/+{vp:.2f} fF)"
    lines = [
        f"// PEX-RC lumped from {note}\n",
        f"Rr_p (tp nr_p) resistor r={r}\n",
        f"Cr_p (nr_p 0) capacitor c={c_p}f\n",
        f"Rr_n (tn nr_n) resistor r={r}\n",
        f"Cr_n (nr_n 0) capacitor c={c_n}f\n",
        # Series R on C_tail: bare C(tail,0) breaks VACASK OP at 85 °C on
        # some D22 codes; 10 Ω ≪ tank R [TOOL]
        f"Rtail_pn (tail ntail_pn) resistor r=10\n",
        f"Ctail_pn (ntail_pn 0) capacitor c={ct}f\n",
    ]
    couples = [
        ("cvt_n", "tn", "vt", "c_tn_vt_ff"),
        ("cvt_p", "tp", "vt", "c_tp_vt_ff"),
        ("cvdd_n", "tn", "vdd", "c_tn_vdd_ff"),
        ("cvdd_p", "tp", "vdd", "c_tp_vdd_ff"),
    ]
    if not omit_ctl:
        couples.extend((
            ("ctl_n", "tail", "tn", "c_tail_tn_ff"),
            ("ctl_p", "tail", "tp", "c_tail_tp_ff"),
        ))
    if tie_vbp:
        couples.extend((
            ("cvbp_n", "tn", "vbp", "c_tn_vbp_ff"),
            ("cvbp_p", "tp", "vbp", "c_tp_vbp_ff"),
        ))
    elif not fold_vbp_into_cr:
        for key in ("c_tn_vbp_ff", "c_tp_vbp_ff"):
            v = float(L.get(key, 0.0) or 0.0)
            if v >= 1.0:
                side = "n" if "tn" in key else "p"
                lines.append(
                    f"Ccvbp_{side}_gnd (t{side} 0) capacitor c={v}f\n"
                )
    for tag, n1, n2, key in couples:
        v = float(L.get(key, 0.0) or 0.0)
        if v >= 1.0:
            lines.append(f"C{tag} ({n1} {n2}) capacitor c={v}f\n")
    return "".join(lines)


def strip_pex(sim_path: str) -> None:
    """Remove a previously injected PEX-RC lumped block."""
    text = open(sim_path).read()
    text2, n = _PEX_BLOCK_RE.subn("\n", text, count=1)
    if n:
        open(sim_path, "w").write(text2)


def ensure_rtb_op(sim_path: str, r_ohm: float = 1e6) -> bool:
    """Add DC path on detector buffer tail tb if the det snippet is present.

    Bare ib+ctb on tb NaNs VACASK OP at 85 °C with PEX on some DAC codes.
    Rtb_op=1 MΩ restores OP for A/C/E topologies [TOOL matrix 367605].
    Returns True if inserted or already present.
    """
    text = open(sim_path).read()
    if "Rtb_op (" in text:
        return True
    if "ctb (tb 0) capacitor" not in text:
        return False
    text2, n = re.subn(
        r"(ctb \(tb 0\) capacitor c=[^\n]+)\n",
        rf"\1\nRtb_op (tb 0) resistor r={r_ohm:.6g}\n",
        text,
        count=1,
    )
    if n != 1:
        return False
    open(sim_path, "w").write(text2)
    return True


def inject_pex(
    sim_path: str,
    L: dict | None = None,
    *,
    tie_vbp: bool = False,
    omit_ctl: bool = False,
    fold_vbp_into_cr: bool = False,
    replace: bool = False,
    rtb_op: bool = True,
) -> None:
    """Append lumped parasitics just before the control block.

    rtb_op: default True — insert Rtb_op 1 MΩ on detector tb when present.
    """
    if replace:
        strip_pex(sim_path)
    if rtb_op:
        ensure_rtb_op(sim_path)
    extra = parasitic_extra(
        L,
        tie_vbp=tie_vbp,
        omit_ctl=omit_ctl,
        fold_vbp_into_cr=fold_vbp_into_cr,
    )
    text = open(sim_path).read()
    if not replace and ("Ctail_pn" in text or "Rr_p (tp nr_p)" in text):
        return
    if "\ncontrol\n" not in text:
        raise RuntimeError(f"no control block in {sim_path}")
    if tie_vbp and "vbptie" not in text and "(vbp " not in text:
        extra = "vbptie (vbp 0) vsource dc=0\n" + extra
    open(sim_path, "w").write(
        text.replace("\ncontrol\n", "\n" + extra + "control\n", 1)
    )


def det_tank_c_from_ext() -> dict:
    """Detector tank load per side from Magic .ext couplings [PEX-RC]."""
    ext = os.path.join(LAYOUT, "pex_vco_top", "vco_top.ext")
    if not os.path.exists(ext):
        return {"ok": False, "reason": "missing vco_top.ext"}
    sys_path = os.path.join(HERE, "..", "layout", "p272b")
    if sys_path not in __import__("sys").path:
        __import__("sys").path.insert(0, sys_path)
    import analyze_pex_ext as AX  # noqa: E402

    _find, _node_c, caps = AX.parse_ext(ext)
    coup = {"tn": {}, "tp": {}}
    for a, b, af in caps:
        ff = af / 1000.0
        for port in ("tn", "tp"):
            other = None
            if a == port:
                other = b
            elif b == port:
                other = a
            if other is None:
                continue
            coup[port][other] = coup[port].get(other, 0.0) + ff
    det_nets = {"hold", "rep", "en", "cmp", "vthn"}
    out = {}
    for port in ("tn", "tp"):
        named = {k: round(v, 3) for k, v in coup[port].items() if k in det_nets}
        anon = sorted(
            ((k, round(v, 3)) for k, v in coup[port].items()
             if str(k).startswith("a_") and v >= 1.0),
            key=lambda x: -x[1],
        )[:5]
        named_sum = sum(named.values())
        device_ff = 1.0
        face = anon[0][1] if anon else 0.0
        total = named_sum + device_ff + min(face, 5.0)
        out[port] = {
            "named_ff": named,
            "named_sum_ff": round(named_sum, 3),
            "anon_top": anon,
            "device_cgg_ff": device_ff,
            "total_ff": round(total, 3),
            "pass": total <= 10.0,
        }
    return {"ok": True, "sides": out, "limit_ff": 10.0}
