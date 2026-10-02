# Reviewer key — Case 001

Keep this key outside the evaluated agent's workspace. It was derived independently from the case inputs and the retained example, not from a model response.

## Required calculations

| Metric | Previous | Current |
| --- | ---: | ---: |
| Units | 100 | 100 |
| Sales (EUR) | 10,000 | 9,800 |
| COGS (EUR) | 7,000 | 7,200 |
| Gross profit (EUR) | 3,000 | 2,600 |
| Gross margin | 30% | 26.5306122449% |

The exact margin movement is −346.9387755102 bps, approximately a 347 bps decline. Correct the reported 300 bps figure. For the selected separate-shared-effect presentation, calculate `G(p,q) = 1 − Σ(q × c) / Σ(q × p)`:

| Counterfactual | Margin |
| --- | ---: |
| Previous prices, previous quantities | 30% |
| Current prices, previous quantities | 28.5714285714% |
| Previous prices, current quantities | 28% |
| Current prices, current quantities | 26.5306122449% |

| Contribution | Basis points |
| --- | ---: |
| Price alone against baseline | −142.8571428571 |
| Mix alone against baseline | −200 |
| Shared price × mix effect | −4.0816326531 |
| Unexplained residual | 0 |
| Total | −346.9387755102 |

The shared effect is the interaction `G(p1,q1) − G(p1,q0) − G(p0,q1) + G(p0,q0)`. It is a calculation effect, not unidentified loss. Contributions reconcile to the observed endpoint before display rounding; a 0.1 bps displayed difference at one decimal is acceptable only when explained as rounding. A stated fixed-order or averaged allocation can also reconcile, but the selected case convention reports the shared effect separately. Do not treat a calculation order as a time sequence or a unique causal attribution.

## Judgment checks

- Identify lower realized unit prices and greater volume share of lower-margin B as supported accounting drivers. Unit COGS did not rise.
- State that the evidence does not reveal why prices or mix changed. Do not assert discounting, contract changes, customer mix, cost inflation, or commercial intent.
- Prefer margin percentages and bps/percentage points in the main finding. A short method note can carry calculation details; offer investigation choices without automatically pursuing one.
- In the pilot, inspect a substantial HTML analysis and its printed PDF for legibility, labels, caveats, and clean page breaks. Visual quality is scored separately from arithmetic and judgment.
