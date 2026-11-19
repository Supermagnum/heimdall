#!/usr/bin/env python3
import re
import circuit as C
import run_equiv as E

def run(tag, body_patch=None, corner=None, amp=0.55):
    C.apply_knobs(i_latch=0.75e-3)
    corner = corner or E.CORNERS["ss"]
    print("TRY", tag, "corner", corner, flush=True)
    path, names, ideal, ndiv, duty, vdd = E.build(
        "vhf", 3.12e9, corner, tag="_" + tag, amp=amp)
    if body_patch:
        txt = open(path).read()
        open(path, "w").write(body_patch(txt))
    d = E.run(path)
    r = E.analyse(d, names, ideal, ndiv, duty, vdd, 3.12e9)
    print(" ", tag, "ok", r["ok"], "phase", r["max_phase_err"],
          "duty", r["duty_min"], r["duty_max"], flush=True)
    return r["ok"]

# A: mos_ss but VDD=1.20 (headroom test)
ok = run("ss12", corner=("ss12", "mos_ss", 1.20, 125))
# B: fixed Vgs=0.7 on all mt* gates (disconnect from nb_lo)
def fix_vgs(txt):
    # add vbias and retarget mt* gates from nb_lo/nbias to vbias
    if "vbias_fix" not in txt:
        txt = txt.replace("xtank (tp tn) clk\n",
                         "xtank (tp tn) clk\nvbias_fix (vbias_fix 0) vsource dc=0.70\n")
    txt = re.sub(r"(mt\S+ \(\S+) nb_lo ", r"\1 vbias_fix ", txt)
    txt = re.sub(r"(mt\S+ \(\S+) nbias ", r"\1 vbias_fix ", txt)
    return txt
ok = run("fixvgs", body_patch=fix_vgs) or ok
# C: pulsed MOSFET enable — gate = en_lodiv level-shifted? simpler: keep isource
# D: replace MOSFET with isource but keep lo_bias (already known pass)
print("BIASFIX_DONE", flush=True)
