# Validation

## Structural checks

From the full repository, run:

```sh
python3 -B evals/check_package.py
python3 -B evals/test_skill_packaging.py
```

The standard-library checks validate skill metadata, matching portable/Claude manifests, root MIT license, one shared knowledge tree, explicit runtime inventory, reference closure and local documentation file/heading links. Counts are derived from the inventory. Tests copy original sources without repairing them and reject incomplete installs, missing/undeclared resources, symlinks, manifest version drift and duplicate knowledge. The ZIP regression verifies all seven skills and shared references survive packaging while local context and evaluation fixtures stay excluded.

To build a Claude upload ZIP, run `python3 -B scripts/build_plugin_zip.py`. If Claude Code is installed, also run `claude plugin validate --strict .claude-plugin/plugin.json` and `claude plugin validate --strict .claude-plugin/marketplace.json`. These validate metadata and the catalog; they do not establish live Claude chat/Cowork behavior.

These are structural checks. Installed discovery/reference loading and model behavior require separate acceptance.

## Focused regressions

[`regressions/2026-10-03-luna-review/criteria.json`](regressions/2026-10-03-luna-review/criteria.json) records review points 1–6 with portable synthetic inputs. Keep criteria separate from solver inputs. Behavioral reruns are pending; the contract-adjustment case requires its unincorporated draft method. Local review outputs are not part of the package.

## Real-Life Fix Regressions

Local-only focused evaluations cover field mapping, ambiguous and evidenced
numeric formats, comparison-basis clarification, joint proposed-price/cost
economics, accounting links and dated authority. Their inputs, evaluator criteria
and model evidence are excluded from Git. Fixture arithmetic checks do not
establish agent compliance, and focused checks do not replace a fresh full
Online Retail II rerun.

## Legacy fixtures

`cases/` and `expected/` contain historical synthetic inputs and independent keys. They are deprecated as the current acceptance suite; retain them for arithmetic and historical reference. The V2 suite below replaced them for acceptance. No additional variants or token benchmarks are being added to the legacy cases.

For future evaluated runs, isolate inputs and confirmed context from keys, previous outputs and reviewer reports. Keep actual numerical correctness, evidence use, context persistence and artifact quality distinct from static validation.

## V2 fresh acceptance suite

Inputs are under ignored `evals/runs/v2/inputs/`; evaluator keys and independent
arithmetic are under ignored `evals/reports/v2/keys/` and `evals/reports/v2/oracles.py`;
`evals/reports/v2/coverage.md` maps the 20 case families and requirements R01–R18 to
assertions. Results and limits are in `evals/reports/v2/acceptance.md`; the frozen
candidate is `evals/reports/v2/candidate.json`.

For a run:

```sh
python3 -B evals/reports/v2/orchestrator/acceptance.py freeze
python3 -B evals/reports/v2/orchestrator/acceptance.py prepare CASE DEST_ROOT
python3 -B evals/reports/v2/orchestrator/acceptance.py audit CASE DEST_ROOT
```

`prepare` builds a workspace holding only the 33 shipped runtime files and that case's
`task.md`; `audit` confirms the runtime hashes are unchanged and lists any other files
the solver wrote. Follow-ups are delivered as separate messages after the original
answer is retained. Keys, earlier outputs, reviews and public illustrations never enter
a workspace. This is separation by the operator, not OS-enforced security. Record the
candidate hash, model, effort, host and tools per run, and keep an original answer, its
follow-up and any rerun separate. A changed evaluator key can rescore a retained answer;
a changed runtime file requires a new attributed run and a new candidate.

The V2 acceptance run used Claude Sonnet 5.5 at high effort, three cases at a time, in
Claude Code. The earlier saved preference (Luna at maximum) was not available there, so
results are not comparable with Luna runs. Native host loading, other hosts and connected
sources were not exercised.
