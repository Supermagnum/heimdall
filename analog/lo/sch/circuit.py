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

I_LATCH = 0.5e-3
SWING = 0.5
K_REGEN = 1.5
B2 = 4.0
# Short-L 1:1 with TB diode. Long-L W=I/1µA gave Vgs≈Vt and dead CML [SCH].
TAIL_L = "0.13u"


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

    20 µm/mA at L=0.13u keeps Vgs well above Vt so CML swings [SCH].
    """
    i = I_LATCH if i is None else i
    return max(5.0, 20.0 * i / 1e-3)


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
    """Remove 1 GOhm TSPC holds; add weak half-latch keepers on a/b/q.

    step-2 puts rk{n}0..5 on (q, a, b, x1, x2, x3). Keepers on q/a/b give a
    DC OP without ideal R; x1–x3 stay floating (clocked often enough) [HAND].
    Strength ~0.15× size-2 so edges are not fought.
    """
    # Map tag -> {0:q, 1:a, 2:b, ...}
    holds = re.findall(
        r"^rk(\S+)([0-5]) \((\S+) 0\) resistor r=1G\s*$", body, flags=re.M)
    by_tag: dict[str, dict[str, str]] = {}
    for tag, idx, node in holds:
        by_tag.setdefault(tag, {})[idx] = node
    body = re.sub(r"^rk\S+ \(\S+ 0\) resistor r=1G\s*$", "", body, flags=re.M)
    extra = []
    for tag, nodes in by_tag.items():
        for key, suffix in (("0", "q"), ("1", "a"), ("2", "b")):
            if key not in nodes:
                continue
            nd = nodes[key]
            mid = f"x_{tag}_k{suffix}"
            # Weak inv pair (0.3/0.6 µm) — same as converging P2.7.4a2 smoke.
            extra.append(
                f"x{tag}k{suffix}1p ({mid} {nd} vdg vdg) sg13_lv_pmos "
                f"w=0.6u l=0.13u\n"
                f"x{tag}k{suffix}1n ({mid} {nd} 0 0) sg13_lv_nmos "
                f"w=0.3u l=0.13u\n"
                f"x{tag}k{suffix}2p ({nd} {mid} vdg vdg) sg13_lv_pmos "
                f"w=0.6u l=0.13u\n"
                f"x{tag}k{suffix}2n ({nd} {mid} 0 0) sg13_lv_nmos "
                f"w=0.3u l=0.13u\n"
            )
    return body + "".join(extra)


def apply_knobs(i_latch=None, b2=None, k=None, swing=None):
    global I_LATCH, B2, SWING, K_REGEN
    if i_latch is not None:
        I_LATCH = i_latch
        L3.I_LATCH = i_latch
        L1.cml_params = lambda i, vdd: (
            I_LATCH, SWING / I_LATCH, max(1.0, 10.0 * I_LATCH / 1e-3)
        )
    if b2 is not None:
        B2 = b2
        L2.B2 = b2
    if k is not None:
        K_REGEN = k
        L1.VARIANT["k"] = k
    if swing is not None:
        SWING = swing


def build_band_body(band: str, vdd: float, i_latch=None) -> tuple[str, list, dict, int, float]:
    """Return LO body (buffer+chain) with MOSFET tails / keepers, plus meta."""
    apply_knobs(i_latch=i_latch)
    # Force step3 defaults already loaded; rebuild converter/buffer as step3
    body, names, ideal, ndiv, duty = L2.chain(band, vdd)
    body = body.replace("(vdd ", "(vdv ")
    buf = L2.buffer()
    lo = buf + body
    lo = replace_tails(lo, I_LATCH)
    lo = replace_holds(lo)
    # Keep body vref (VHF CML NOR). Callers must not inject a second vref.
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
