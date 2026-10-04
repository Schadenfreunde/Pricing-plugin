# Validation

## Structural checks

From the full repository, run:

```sh
python3 -B evals/check_package.py
python3 -B evals/test_skill_packaging.py
```

The standard-library checks validate the complete plugin as shipped: skill metadata, root MIT license, one shared knowledge tree, explicit runtime inventory, reference closure and local documentation file/heading links. Counts are derived from the inventory. Tests copy original sources without repairing them and reject incomplete installs, missing/undeclared resources, symlinks and duplicate knowledge. Canonical edits need no synchronization.

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

`cases/` and `expected/` contain historical synthetic inputs and independent keys. They are deprecated as the current acceptance suite; retain them for arithmetic and historical reference. A fresh end-to-end suite with data and cases is planned. No additional variants or token benchmarks are being added to the legacy cases.

For future evaluated runs, isolate inputs and confirmed context from keys, previous outputs and reviewer reports. Keep actual numerical correctness, evidence use, context persistence and artifact quality distinct from static validation.
