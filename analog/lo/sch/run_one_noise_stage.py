#!/usr/bin/env python3
"""Run one stage noise case: band stage  (buffer|cml|converter|logic)."""
import json, os, sys
import run_stage_noise as N

STAGES = {
    "buffer": N.stage_buffer,
    "cml": N.stage_cml,
    "converter": N.stage_converter,
    "logic": N.stage_logic,
}

def main():
    if len(sys.argv) != 3 or sys.argv[2] not in STAGES:
        print("usage: run_one_noise_stage.py uhf|vhf buffer|cml|converter|logic",
              file=sys.stderr)
        return 2
    band, st = sys.argv[1], sys.argv[2]
    f_vco = N.F_VCO_UHF if band == "uhf" else N.F_VCO_VHF
    os.makedirs(N.OUT, exist_ok=True)
    m = STAGES[st](band, f_vco, N.CORNER)
    m["stage"] = f"{band}_{st}"
    print(json.dumps({k: m[k] for k in m if k not in ("fr", "Lspec")}, indent=2),
          flush=True)
    path = os.path.join(N.OUT, f"one_{band}_{st}.json")
    open(path, "w").write(json.dumps(
        {k: m[k] for k in m if k not in ("fr", "Lspec")}, indent=2))
    print("WROTE", path, "CASE_DONE", flush=True)
    return 0 if m.get("ok") else 1

if __name__ == "__main__":
    raise SystemExit(main())
