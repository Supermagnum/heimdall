#!/usr/bin/env python3
import sys
sys.path.insert(0, ".")
import circuit as C
import run_equiv as E
import numpy as np

C.apply_knobs(i_latch=0.75e-3, swing=0.5, vhf_tailless=True, b2=8.0)
E.CORNERS["ss"] = ("ss", "mos_ss", 1.08, 125)
f = 4.20e9
for amp in (0.55, 0.65, 0.70):
    path, names, ideal, ndiv, duty, v = E.build(
        "vhf", f, E.CORNERS["ss"], tag=f"_b8a{int(amp * 100)}", amp=amp)
    d = E.run(path)
    r = E.analyse(d, names, ideal, ndiv, duty, v, f)
    n0 = int(0.7 * len(np.real(d["time"])))
    ckp = np.real(d["ckp"])[n0:]
    ckn = np.real(d["ckn"])[n0:]
    sw = 0.25 * ((ckp.max() - ckp.min()) + (ckn.max() - ckn.min()))
    print(f"amp={amp} ok={r['ok']} ph={r['max_phase_err']:.3f} sw={sw:.3f}",
          flush=True)
E.CORNERS["ss"] = ("ss", "mos_ss", 1.05, 125)
path, names, ideal, ndiv, duty, v = E.build(
    "vhf", 3.12e9, E.CORNERS["ss"], tag="_b8m105", amp=0.40)
d = E.run(path)
r = E.analyse(d, names, ideal, ndiv, duty, v, 3.12e9)
print("margin 1.05/3.12", r["ok"], r["max_phase_err"], flush=True)
print("DONE", flush=True)
