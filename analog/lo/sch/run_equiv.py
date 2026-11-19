#!/usr/bin/env python3
"""P2.7.4a2 step 2 — equivalence on xschem inventory netlist [SCH].

Uses step-3 topology with MOSFET tails + bleeder keepers (circuit.py).
"""
from __future__ import annotations

import math
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
# Private out dir avoids races with parallel sibling agents on out/tr.raw.
OUT = os.path.join(HERE, os.environ.get("LO_SCH_OUT", "out_sole"))
sys.path.insert(0, HERE)
import circuit as C  # noqa: E402

REF = {
    "uhf_phase_max_deg": 0.46,
    "vhf_phase_max_deg": 0.13,
    "uhf_duty": (22.6, 25.8),
    "vhf_duty": (47.9, 51.1),
}
# ss VDD = VR_ANA1 V_min at divider (LDO ss/125 + route IR) [SCH/HAND]
# analog/vco/ldo/out/summary_vrana1_corner_vmin.txt — replaces 1.08 V.
CORNERS = {
    "tt": ("tt", "mos_tt", 1.20, 27),
    "ss": ("ss", "mos_ss", 1.181, 125),
}
CASES = {"uhf": [3.20e9, 3.84e9], "vhf": [3.12e9, 4.20e9]}
MM = {"n": (3.9e-3, 0.005), "p": (2.2e-3, 0.0033)}
DW, DL = 4e-9, 2e-9


def tank_amp(f):
    # Step-3 pessimistic floor, +10 % so MOSFET-tail chain starts cleanly [SCH].
    return float(np.interp(f, [3.12e9, 4.20e9], [0.30, 0.55]))


def mismatch(text, rng):
    pat = re.compile(
        r"^(\S+) \((\S+) (\S+) (\S+) (\S+)\) sg13_lv_(n|p)mos "
        r"w=([\d.]+)u l=([\d.]+)u(.*)$"
    )
    out, k = [], 0
    for ln in text.splitlines():
        m = pat.match(ln)
        if not m:
            out.append(ln)
            continue
        name, d, g, s, b, typ, w, l, rest = m.groups()
        w, l = float(w), float(l)
        avt, ab = MM[typ]
        dvt = rng.normal(0, avt / math.sqrt(max(w * l, 1e-6)))
        beta = rng.normal(1, ab / math.sqrt(max(w * l, 1e-6)))
        w2 = (w + rng.normal(0, DW * 1e6)) * beta
        l2 = l + rng.normal(0, DL * 1e6)
        k += 1
        out.append(f"vmm{k} (x_mmg{k} {g}) vsource dc={dvt:.5e}")
        out.append(
            f"{name} ({d} x_mmg{k} {s} {b}) sg13_lv_{typ}mos "
            f"w={max(w2, 0.15):.4f}u l={max(l2, 0.13):.4f}u{rest}"
        )
    return "\n".join(out) + "\n"


def nbias_standin(i_latch):
    """TB diode+I for nbias; 1:1 with CML tails (same W, TAIL_L) [HAND]."""
    w = C.tail_w(i_latch)
    return (
        f"iref_nb (vdd nbias) isource dc={i_latch:.4e}\n"
        f"mdi_tb (nbias nbias 0 0) sg13_lv_nmos w={w:g}u l={C.TAIL_L}\n"
    )


def build(band, f, corner, rng=None, tag="", amp=None, i_latch=None):
    ctag, mos, vdd, temp = corner
    body, names, ideal, ndiv, duty = C.build_band_body(band, vdd, i_latch)
    if rng is not None:
        body = mismatch(body, rng)
    i_l = C.I_LATCH if i_latch is None else i_latch
    # D15: enable after supplies/clock settle (2 ns matches step-3 default)
    en = ('en_lodiv (en_lodiv 0) vsource type="pulse" val0=0 '
          f'val1={vdd} delay=2n rise=100p fall=100p width=1\n')
    sup = (f'type="pulse" val0=0 val1={vdd} delay=0.2n rise=1n '
           f"fall=1n width=1")
    # VHF CML NOR vref lives in div_body — do not inject a second TB source.
    # Force vacask-safe dc=.3f (rejects 0.9500 in some builds).
    _, rl, _ = C.L1.cml_params(i_l, vdd)
    vref = vdd - i_l * rl / 2
    body = re.sub(
        r"^vref \(vref 0\) vsource dc=\S+",
        f"vref (vref 0) vsource dc={vref:.3f}",
        body,
        flags=re.M,
    )
    tb = (
        f"vbufs (vbuf 0) vsource {sup}\n"
        f"vdvs (vdv 0) vsource {sup}\n"
        f"vcvs (vcv 0) vsource {sup}\n"
        f"vdgs (vdg 0) vsource {sup}\n"
        f"vdds (vdd 0) vsource {sup}\n"
        + en + nbias_standin(i_l)
    )
    stop = 3e-9 + (24 * 8 if band == "uhf" else 20 * 24) / f
    name = f"lo_eq_{band}_{ctag}_{f/1e9:.2f}{tag}"
    path = os.path.join(OUT, name + ".sim")
    a = amp if amp is not None else tank_amp(f)
    # Unique binary raw name avoids races with peak-MC / parallel vacask on tr.raw.
    open(path, "w").write(
        C.HEADER.format(title=f"P2.7.4a2 equiv {name}", mos=mos,
                        f=f, amp=a, vcm=vdd / 2, shape=0.0, offs=0.0,
                        t0=-1.0, tr=1e-12)
        + tb + "xtank (tp tn) clk\n" + body
        + "\ncontrol\n  abort always\n  options rawfile=\"binary\"\n"
        f"  options temp={temp}\n"
        f"  analysis tr tran stop={stop:.4e} step=5p maxstep=5p\nendc\n"
    )
    return path, names, ideal, ndiv, duty, vdd


def run(path):
    """Run vacask in a unique work dir; flock + atomic rename for tr.raw."""
    import fcntl
    import shutil
    import tempfile
    import time
    from vacask.rawfile import rawread
    name = os.path.basename(path)[:-4]
    log = os.path.join(OUT, name + ".log")
    raw_mine = os.path.join(OUT, name + ".tr.raw")
    raw_tmp = raw_mine + f".{os.getpid()}.tmp"
    # Serialize same-case writers (sibling agents) on one flock file.
    lock_path = os.path.join(OUT, f".vacask_{name}.lock")
    work = tempfile.mkdtemp(prefix=f"_w_{name}_", dir=OUT)
    try:
        with open(lock_path, "w") as lk:
            fcntl.flock(lk.fileno(), fcntl.LOCK_EX)
            sim_in_work = os.path.join(work, name + ".sim")
            shutil.copy2(path, sim_in_work)
            with open(log, "w") as fh:
                r = subprocess.run(["vacask", name + ".sim"], cwd=work,
                                   stdout=fh, stderr=subprocess.STDOUT)
            if r.returncode:
                raise RuntimeError(
                    f"vacask {name} failed: " + open(log).read()[-600:])
            raw_shared = os.path.join(work, "tr.raw")
            if not os.path.isfile(raw_shared) or os.path.getsize(raw_shared) < 64:
                raise RuntimeError(f"vacask {name}: missing/empty tr.raw in {work}")
            shutil.copy2(raw_shared, raw_tmp)
            os.replace(raw_tmp, raw_mine)
            # Brief settle so a parallel reader never sees a half write.
            time.sleep(0.05)
            try:
                return rawread(raw_mine).get()
            except Exception as e:
                raise RuntimeError(f"rawread {name}.tr.raw: {e}") from e
    finally:
        shutil.rmtree(work, ignore_errors=True)
        if os.path.isfile(raw_tmp):
            try:
                os.remove(raw_tmp)
            except OSError:
                pass


def edges(t, v, th):
    s = v > th
    i = np.where(~s[:-1] & s[1:])[0]
    return t[i] + (th - v[i]) * (t[i + 1] - t[i]) / (v[i + 1] - v[i])


def analyse(d, names, ideal, ndiv, duty_ideal, vdd, f_vco):
    if d is None:
        raise RuntimeError("analyse: raw dataset is None (empty/missing tr.raw)")
    try:
        t = np.real(d["time"])
    except Exception as e:
        raise RuntimeError(f"analyse: no time vector in raw ({e})") from e
    if t.size < 2:
        raise RuntimeError(
            f"analyse: empty/short raw time vector (n={t.size}; vacask no. points?)")
    keep = t >= t[-1] * 0.45
    tk = t[keep]
    if tk.size < 2:
        raise RuntimeError("analyse: keep-window empty after settle cut")
    rows = []
    ref = None
    f_lo = f_vco / ndiv
    ok_div = True
    for lab, node in names:
        try:
            v = np.real(d[node])[keep]
        except Exception as e:
            rows.append((lab, None, None, None, None))
            ok_div = False
            continue
        e = edges(tk, v, vdd / 2)
        if len(e) < 3:
            rows.append((lab, None, None, None, None))
            ok_div = False
            continue
        period = np.mean(np.diff(e))
        fo = 1 / period
        duty = 100 * np.mean(v > vdd / 2)
        if ref is None:
            ref = (node, e, period)
            ph = 0.0
        else:
            de = np.array([(x - ref[1][np.argmin(np.abs(ref[1] - x))])
                           for x in e])
            ang = 2 * np.pi * de / ref[2]
            ph = float(np.degrees(np.angle(np.mean(np.exp(1j * ang)))) % 360)
        if abs(fo / f_lo - 1) > 0.02:
            ok_div = False
        err = None
        if node in ideal:
            diff = (ph - ideal[node] + 180) % 360 - 180
            err = abs(diff)
        rows.append((lab, fo, duty, ph, err))
    max_err = max((r[4] for r in rows if r[4] is not None), default=999.0)
    duties = [r[2] for r in rows if r[2] is not None]
    return dict(ok=ok_div, rows=rows, max_phase_err=max_err,
                duty_min=min(duties) if duties else None,
                duty_max=max(duties) if duties else None)


def fmax_slow(band):
    corner = CORNERS["ss"]
    freqs = [x * 1e9 for x in (2.9, 3.2, 3.5, 3.84, 4.2, 4.41, 5.0)]
    fmax, marks = 0.0, []
    for f in freqs:
        try:
            path, names, ideal, ndiv, duty, vdd = build(
                band, f, corner, tag="_fmax")
            d = run(path)
            r = analyse(d, names, ideal, ndiv, duty, vdd, f)
            ok = r["ok"]
        except Exception:
            ok = False
        marks.append(f"{f/1e9:g}{'+' if ok else '-'}")
        if ok:
            fmax = f
        else:
            break
    return fmax, " ".join(marks)


def main():
    os.makedirs(OUT, exist_ok=True)
    quick = "quick" in sys.argv
    do_mc = "mc" in sys.argv or not quick
    n_mc = next((int(a[2:]) for a in sys.argv if a.startswith("n=")), 25)
    i_mA = next((float(a[2:]) for a in sys.argv if a.startswith("i=")), None)
    if i_mA is not None:
        C.apply_knobs(i_latch=i_mA * 1e-3)
    corners = ["tt"] if quick else ["tt", "ss"]
    lines = [
        "# P2.7.4a2 equivalence — xschem inventory netlist [SCH]\n\n",
        f"Step-3 topology; MOSFET CML tails (nbias TG); TSPC weak keepers "
        f"(no 1 GOhm). I_latch={C.I_LATCH*1e3:g} mA.\n\n",
    ]
    print(lines[0], flush=True)
    print("## Cases\n", flush=True)
    print("| Band | Corner | f_VCO | divide | max |φ−ideal| | duty | gate |",
          flush=True)
    print("|---|---|---|---|---|---|---|", flush=True)
    lines.append("## Cases\n\n| Band | Corner | f_VCO | divide | max |φ−ideal| | "
                 "duty | gate |\n|---|---|---|---|---|---|---|\n")
    for band in ("uhf", "vhf"):
        for cname in corners:
            for f in CASES[band]:
                try:
                    path, names, ideal, ndiv, duty, vdd = build(
                        band, f, CORNERS[cname])
                    d = run(path)
                    r = analyse(d, names, ideal, ndiv, duty, vdd, f)
                    lim = (REF["uhf_phase_max_deg"] if band == "uhf"
                           else REF["vhf_phase_max_deg"] + 0.5)
                    ph_ok = r["max_phase_err"] <= lim + 0.2
                    gate = ("PASS" if r["ok"] and ph_ok else
                            "FAIL" if not r["ok"] else "PHASE")
                    dmin, dmax = r["duty_min"], r["duty_max"]
                    duty_s = (f"{dmin:.1f}/{dmax:.1f}"
                              if dmin is not None and dmax is not None
                              else "—")
                    mpe = r["max_phase_err"]
                    mpe_s = f"{mpe:.2f}°" if mpe is not None else "—"
                    row = (f"| {band} | {cname} | {f/1e9:.2f} | "
                           f"{'OK' if r['ok'] else 'FAIL'} | "
                           f"{mpe_s} | {duty_s} | {gate} |")
                except Exception as e:
                    row = (f"| {band} | {cname} | {f/1e9:.2f} | error | — | — | "
                           f"FAIL ({str(e)[-80:]}) |")
                print(row, flush=True)
                lines.append(row + "\n")

    print("\n## Max frequency at slow corner\n", flush=True)
    lines.append("\n## Max frequency at slow corner\n\n")
    if not quick:
        for band in ("uhf", "vhf"):
            try:
                fmax, pat = fmax_slow(band)
                row = f"- {band}: f_max ≈ {fmax/1e9:.2f} GHz [{pat}] [SCH]\n"
            except Exception as e:
                row = f"- {band}: ERROR {e}\n"
            print(row, flush=True)
            lines.append(row)

    if do_mc and not quick:
        print(f"\n## Monte Carlo n={n_mc}\n", flush=True)
        lines.append(f"\n## Monte Carlo n={n_mc}\n\n")
        lines.append("| Case | pass | phase σ | duty σ |\n|---|---|---|---|\n")
        for band, cname, f in (("uhf", "tt", 3.84e9), ("uhf", "ss", 3.84e9),
                               ("vhf", "tt", 4.20e9), ("vhf", "ss", 4.20e9)):
            rng = np.random.default_rng(42)
            ok_n, phs, dus = 0, [], []
            for i in range(n_mc):
                try:
                    path, names, ideal, ndiv, duty, vdd = build(
                        band, f, CORNERS[cname], rng=rng, tag=f"_mc{i}")
                    d = run(path)
                    r = analyse(d, names, ideal, ndiv, duty, vdd, f)
                    if r["ok"]:
                        ok_n += 1
                        phs.append(r["max_phase_err"])
                        dus.append((r["duty_max"] or 0) - (r["duty_min"] or 0))
                except Exception:
                    pass
            ps = float(np.std(phs)) if len(phs) > 1 else float("nan")
            ds = float(np.std(dus)) if len(dus) > 1 else float("nan")
            row = (f"| {band} {cname} {f/1e9:.2f} | {ok_n}/{n_mc} | "
                   f"{ps:.2f} | {ds:.2f} |")
            print(row, flush=True)
            lines.append(row + "\n")

    lines.append(
        "\n## Diff vs Python decks (ideal tails / 1 GOhm)\n\n"
        "- MOSFET tails + nbias TG vs isource: mirror mismatch may shift "
        "f_max / phase slightly [SCH].\n"
        "- Weak half-latch keepers vs 1 GOhm: small duty/phase shift possible.\n"
    )
    open(os.path.join(OUT, "summary_equiv_lo.txt"), "w").write("".join(lines))
    print("\nWrote out/summary_equiv_lo.txt", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
