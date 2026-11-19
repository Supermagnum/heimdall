#!/usr/bin/env python3
"""P2.7.4a2 LO circuit: step-3 defaults with real MOSFET tails and no 1 GOhm.

Builds on analog/lo/step3 (accepted). Substitutions for xschem / LVS:
  - CML isource tails -> NMOS mirrors gated from nb_lo (nbias via lo_bias TG)
  - TSPC r=1G holds -> weak half-latch keepers on a/b/q
"""
from __future__ import annotations

import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

# 0.5 mA MOSFET-tail chain fails UHF/VHF ss @ 125 °C (Johnson miscount /
# dead outputs). 0.75 mA restores ÷N and phase at ss [SCH out_a2_fix].
I_LATCH = 0.75e-3
SWING = 0.5
K_REGEN = 1.5
B2 = 4.0
# Short-L 1:1 with TB diode (UHF/VHF smoke PASS). Do not widen to 500u@2u —
# that slows VHF and was only a TB OP hack [SCH].
TAIL_L = "0.13u"
# µm per mA of I_latch for MOSFET tails. 20 was headroom-starved at ss
# (tail V_DS≪V_dsat) [SCH summary_vhf_headroom_budget]. Wider → lower V_DS
# in linear region at fixed Id.
TAIL_UM_PER_MA = 20.0
# VHF ÷3 only: ground latch clock-pair sources (step1 VARIANT tailless).
# Leaves ÷2 path unchanged when band=='uhf'. Owner pick after combo FAIL.
VHF_TAILLESS = False


def _load_step3():
    path = os.path.join(REPO, "analog", "lo", "step3", "run_step3.py")
    spec = importlib.util.spec_from_file_location("lo_step3_p274", path)
    m = importlib.util.module_from_spec(spec)
    # Avoid argv options from our callers affecting step3 OPT parse
    old = sys.argv
    sys.argv = [path]
    try:
        spec.loader.exec_module(m)
    finally:
        sys.argv = old
    return m


L3 = _load_step3()
L2 = L3.L2
L1 = L3.L1


def tail_w(i=None):
    """NMOS tail / diode width (um) at TAIL_L for ~I_latch [HAND].

    Default 20 µm/mA; raise TAIL_UM_PER_MA to cut linear-region V_DS at ss.
    """
    i = I_LATCH if i is None else i
    return max(5.0, TAIL_UM_PER_MA * i / 1e-3)


def lo_bias_netlist(vdd_name="vdd"):
    """en_lodiv + nbias -> nb_lo (TG + pull-down)."""
    return (
        f"xenb_p (en_n en_lodiv {vdd_name} {vdd_name}) sg13_lv_pmos w=1u l=0.13u\n"
        f"xenb_n (en_n en_lodiv 0 0) sg13_lv_nmos w=0.5u l=0.13u\n"
        "tgn (nb_lo en_lodiv nbias 0) sg13_lv_nmos w=4u l=0.13u\n"
        f"tgp (nb_lo en_n nbias {vdd_name}) sg13_lv_pmos w=8u l=0.13u\n"
        "mpd (nb_lo en_n 0 0) sg13_lv_nmos w=2u l=0.13u\n"
    )


def replace_tails(body: str, i_latch=None) -> str:
    """Replace CML isource tails (dc or pulsed enable) with MOSFET to nb_lo."""
    i_latch = I_LATCH if i_latch is None else i_latch
    w = tail_w(i_latch)

    def repl_tail(m):
        name = m.group(1)
        return (f"mt{name} (t{name} nb_lo 0 0) sg13_lv_nmos "
                f"w={w:g}u l={TAIL_L}\n")

    # iNAME (tNAME 0) isource dc=...  OR pulse enable form
    body = re.sub(
        r"^i(\S+) \(t\1 0\) isource .*$",
        repl_tail,
        body,
        flags=re.M,
    )
    body = re.sub(
        r"^ig \(tg 0\) isource .*$",
        f"mtg (tg nb_lo 0 0) sg13_lv_nmos w={w:g}u l={TAIL_L}\n",
        body,
        flags=re.M,
    )
    return body


def replace_holds(body: str) -> str:
    """Remove 1 GOhm TSPC holds; add weak keepers.

    step-2 puts rk{n}0..5 on (q, a, b, x1, x2, x3). Half-latches on a/b fought
    the TSPC at ss/125 °C (UHF Johnson miscount → ~÷2) [SCH out_a2_c27].
    Keep: weak Q staticizer only + 100 MΩ on a/b for DC OP [HAND].
    """
    holds = re.findall(
        r"^rk(\S+)([0-5]) \((\S+) 0\) resistor r=1G\s*$", body, flags=re.M)
    by_tag: dict[str, dict[str, str]] = {}
    for tag, idx, node in holds:
        by_tag.setdefault(tag, {})[idx] = node
    body = re.sub(r"^rk\S+ \(\S+ 0\) resistor r=1G\s*$", "", body, flags=re.M)
    extra = []
    for tag, nodes in by_tag.items():
        if "0" in nodes:  # Q
            nd = nodes["0"]
            mid = f"x_{tag}_kq"
            # ~1/8 of size-1 — hold leakage, do not fight ss edges.
            extra.append(
                f"x{tag}kq1p ({mid} {nd} vdg vdg) sg13_lv_pmos "
                f"w=0.3u l=0.13u\n"
                f"x{tag}kq1n ({mid} {nd} 0 0) sg13_lv_nmos "
                f"w=0.15u l=0.13u\n"
                f"x{tag}kq2p ({nd} {mid} vdg vdg) sg13_lv_pmos "
                f"w=0.3u l=0.13u\n"
                f"x{tag}kq2n ({nd} {mid} 0 0) sg13_lv_nmos "
                f"w=0.15u l=0.13u\n"
            )
        for key in ("1", "2"):  # a, b — soft DC only
            if key in nodes:
                extra.append(
                    f"rk{tag}{key} ({nodes[key]} 0) resistor r=100Meg\n"
                )
    return body + "".join(extra)


def _sync_cml_params():
    """Keep step1 cml_params RL/W in lockstep with I_LATCH / SWING."""
    i = I_LATCH
    sw = SWING
    L3.I_LATCH = i
    L1.cml_params = lambda _i, _vdd, _ii=i, _sw=sw: (
        _ii, _sw / _ii, max(1.0, 10.0 * _ii / 1e-3)
    )


def apply_knobs(i_latch=None, b2=None, k=None, swing=None,
                tail_um_per_ma=None, tail_l=None, vhf_tailless=None):
    global I_LATCH, B2, SWING, K_REGEN, TAIL_UM_PER_MA, TAIL_L, VHF_TAILLESS
    if i_latch is not None:
        I_LATCH = i_latch
    if swing is not None:
        SWING = swing
    if tail_um_per_ma is not None:
        TAIL_UM_PER_MA = float(tail_um_per_ma)
    if tail_l is not None:
        TAIL_L = str(tail_l)
    if vhf_tailless is not None:
        VHF_TAILLESS = bool(vhf_tailless)
    # Always resync — module default I_LATCH alone does not update L1.
    _sync_cml_params()
    if b2 is not None:
        B2 = b2
        L2.B2 = b2
    if k is not None:
        K_REGEN = k
        L1.VARIANT["k"] = k


# Sync once at import so default I_LATCH=0.75 mA sizes RL correctly.
_sync_cml_params()


def build_band_body(band: str, vdd: float, i_latch=None) -> tuple[str, list, dict, int, float]:
    """Return LO body (buffer+chain) with MOSFET tails / keepers, plus meta."""
    apply_knobs(i_latch=I_LATCH if i_latch is None else i_latch)
    # ÷3 only: tailless clock pair. ÷2 (UHF) keeps stacked tails.
    if band == "vhf" and VHF_TAILLESS:
        L1.VARIANT["tailless"] = True
    else:
        L1.VARIANT["tailless"] = False
    # Force step3 defaults already loaded; rebuild converter/buffer as step3
    body, names, ideal, ndiv, duty = L2.chain(band, vdd)
    body = body.replace("(vdd ", "(vdv ")
    buf = L2.buffer()
    lo = buf + body
    lo = replace_tails(lo, I_LATCH)
    lo = replace_holds(lo)
    # Keep body vref (VHF CML NOR); vacask rejects dc=0.9500 — use 3 decimals.
    lo = re.sub(
        r"^(vref \(vref 0\) vsource dc=)([0-9.]+)",
        lambda m: m.group(1) + f"{float(m.group(2)):.3f}",
        lo,
        flags=re.M,
    )
    # Callers must not inject a second vref.
    lo = lo_bias_netlist("vdd") + lo
    return lo, names, ideal, ndiv, duty


# --- inventory for xschem (parse vacask lines into DeviceRec-like) ---
from dataclasses import dataclass, field


@dataclass
class Dev:
    kind: str
    name: str
    nodes: list
    params: dict = field(default_factory=dict)


def parse_body(body: str) -> list[Dev]:
    devs = []
    mos = re.compile(
        r"^(\S+) \((\S+) (\S+) (\S+) (\S+)\) sg13_lv_(n|p)mos "
        r"w=([\d.]+)u l=([\d.]+)u"
    )
    res = re.compile(r"^(\S+) \((\S+) (\S+)\) resistor r=(\S+)")
    cap = re.compile(r"^(\S+) \((\S+) (\S+)\) capacitor c=(\S+)")
    for ln in body.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        m = mos.match(ln)
        if m:
            name, d, g, s, b, typ, w, l = m.groups()
            devs.append(Dev(
                "nmos" if typ == "n" else "pmos", name, [d, g, s, b],
                {"w": f"{w}u", "l": f"{l}u",
                 "model": f"sg13_lv_{typ}mos", "ng": "1"}))
            continue
        m = res.match(ln)
        if m:
            devs.append(Dev("res", m.group(1), [m.group(2), m.group(3)],
                            {"r": m.group(4)}))
            continue
        m = cap.match(ln)
        if m:
            devs.append(Dev("capa", m.group(1), [m.group(2), m.group(3)],
                            {"c": m.group(4)}))
            continue
    return devs


def vacask_line(d: Dev) -> str:
    n = " ".join(d.nodes)
    if d.kind in ("nmos", "pmos"):
        return (f"{d.name} ({n}) {d.params['model']} "
                f"w={d.params['w']} l={d.params['l']}\n")
    if d.kind == "res":
        return f"{d.name} ({n}) resistor r={d.params['r']}\n"
    if d.kind == "capa":
        return f"{d.name} ({n}) capacitor c={d.params['c']}\n"
    raise ValueError(d)


def build_band(band: str, i_latch=None, vdd=1.2):
    body, names, ideal, ndiv, duty = build_band_body(band, vdd, i_latch)
    return parse_body(body), names, ideal, ndiv, duty, body


HEADER = L1.HEADER  # already has clk.va format fields


def write_vacask(path, title, devices, mos="mos_tt", extra="", **clk):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    kw = dict(title=title, mos=mos, vcm=0.6, amp=0.5, shape=0.0, f=3.84e9,
              offs=0.0, t0=-1.0, tr=1e-12)
    kw.update(clk)
    body = "".join(vacask_line(d) for d in devices)
    open(path, "w").write(HEADER.format(**kw) + extra + body)
    return path
