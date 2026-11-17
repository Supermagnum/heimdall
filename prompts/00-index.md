# Agent prompts for HT13G-M (heimdall)


Each prompt does one job and stands on its own. Paste one into the AI client, or put this folder in the repo as `prompts/` and say "run prompts/0N-….md". Every prompt carries the full set of project rules: no fabrication, the owner decides topologies, the PCB files are read only, nothing is pushed outside this repo, and so on.

| # | Prompt | Job | Writes | Changes design files? |
|---|---|---|---|---|
| 01 | `01-audit-and-verify.md` | What is done; re-run and check the recorded results | `reports/status-*.md` | No |
| 02 | `02-pdk-tool-issues.md` | Known IHP PDK and tool bugs: fixed, worked around or open | `reports/pdk-tool-issues-*.md`, draft upstream issues | No |
| 03 | `03-readme-pdk-links.md` | IHP SG13G2 links section in the main README | `README.md` (that section only) | No |
| 04 | *(in SDR-repeater)* `04-pcb-pinout-check.md` | PCB pinout check | SDR-repeater reports | No |
| 05 | *(in SDR-repeater)* `05-parts-list.md` | Module BOM | SDR-repeater `PCB/BOM.*` | No |
| 06 | `06-design-next-step.md` | The next single design item, then stop for review | design files, specs | Yes, one item |

## Suggested order

1. **02, then 01.** A known PDK or tool bug can make a recorded result wrong, and 01 re-runs whatever 02 flags.
2. **03** at any time; it is small.
3. **04, then 05** run from the [SDR-repeater](https://github.com/Supermagnum/SDR-repeater) checkout (PCB stays there).
4. **06**, run again for each step in this repo. Check `decisions.md` and `spec/phase2-plan.md` for the current next item. Before each run, check that the newest status report from 01 has no failed or unverified result that the item depends on.

Prompts 01–05 only write reports and documentation. Prompt 06 is the only one that changes the design.
