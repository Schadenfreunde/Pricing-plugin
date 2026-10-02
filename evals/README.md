# Synthetic pricing evaluation fixtures

These three synthetic cases compare an ordinary assistant and the pricing plugin. `cases/` contains model-visible inputs. `expected/` contains independent evaluator keys; never put those keys or this repository root in an evaluated assistant's workspace. For each run, use a fresh workspace containing only one case's files. Keep outputs and persistent company context outside the next run's workspace. Reviewers should open the keys only after saving the outputs.

Run each case once in each condition: six initial analyses. Re-run only if a result is unstable or a change warrants it. Use the case `prompt.md` verbatim as the user request and attach its other files. Give both conditions the same tool access and this instruction: “Use only the attached evidence for business claims; show calculations and caveats at a useful level of detail.” For case 001, also give both: “Create an HTML analysis and a printable PDF of it.” Do not add reviewer calculations to either prompt. Record each answer, artifacts, time, and token use when available. Supply equivalent confirmed facts to the baseline if plugin context is preloaded, and isolate runs so neither inherits a prior answer.

Compare premise correction, arithmetic and reconciliation, evidence discipline, scope of confirmed context, handling of conflicts, and usefulness. Score HTML and PDF readability separately from analytical correctness. Check numerical differences against the stated calculation convention and display rounding, rather than an arbitrary tolerance. Case 001's selected presentation separates price, mix, and their shared effect; it does not prescribe a general multi-driver method.

## Intake: validate a proposed fact

In a fresh workspace, present the case 003 unvalidated note as a candidate company fact. Ask the assistant to review it, then have the evaluation user explicitly validate or reject a scoped statement. Inspect the proposed save before persistence. Save only the exact validated statement, reload it in a new session, and confirm the assistant distinguishes it from the original unvalidated note. Check the context files before and after; the note must not be saved automatically. Give the baseline condition the same validated fact when comparing later analysis.

## Intake: partial confirmation preserves existing context

In a fresh project workspace, seed `.pricing/context.md` with a confirmed exception for Customer C1 on Product P1. Supply a document proposing two new company facts: the fiscal calendar starts in April, and gross margin excludes freight. Ask the intake skill to review the document. It should show both as proposals in the conversation and save neither yet. The evaluation user then confirms only the April fiscal calendar. Inspect the proposed edit and saved file: the C1/P1 exception remains intact, the April fiscal calendar is added, and the freight claim is absent. Reload `.pricing/context.md` in a fresh session and verify that only the exception and fiscal calendar are treated as confirmed. This scenario defines expected behavior, not a completed installed-skill result.

## Supplementary analysis checks

- **Ambiguous comparison:** In a fresh workspace, ask, “How did gross margin change for this product group?” Supply comparable quarterly data across two years but no requested baseline. The assistant should ask which comparison matters and offer quarter-on-quarter and year-on-year without launching a full intake interview. Then have the evaluation user request **both**; the assistant should calculate and label both comparisons using the supplied data, verify any reported premise, and state material limits. A single forced comparison fails this check.
- **Small factual answer:** In a fresh workspace, provide validated company context defining one price-waterfall term, then ask, “What does our net price include?” The assistant should answer concisely from that confirmed definition, cite its scope if relevant, and avoid a broad intake interview or unnecessary HTML. A missing definition should prompt one targeted clarification rather than an invented company rule.

These are scenarios and outcome checks. Installed-host evaluation remains open; development-only manual trials do not establish that the installed plugin passes them.
