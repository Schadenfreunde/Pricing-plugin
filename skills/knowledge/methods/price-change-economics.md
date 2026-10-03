# Economics of a proposed price change

Establish eligibility, period, comparable realized-price basis and relevant costs. Proposed prices are assumptions; a precise scenario does not prove capture. List-to-net/pocket proposals need supported discount/rebate mappings. Missing quantities or realization evidence limit revenue sizing; missing relevant costs limit contribution/profit sizing.

## Fixed-volume base

When future demand response is unknown, use prior-period item quantities `q0_i` on both sides. Use prior realized baseline prices `p_base_i`, or a documented current effective baseline explicitly named against the same quantities. With assumed proposed realized prices `p_prop_i`:

```text
Baseline revenue = Σ q0_i × p_base_i
Proposed revenue = Σ q0_i × p_prop_i
Price-only difference = Σ q0_i × (p_prop_i − p_base_i)
```

State period, coverage, units/currency and fixed volume/mix. Disclose unmatched/new items, missing history and exclusions; use supported subsets rather than zero/fabricated quantities or current-volume substitutions. Flag unrepresentative history and avoid automatic annualization. This is conditional, not guaranteed uplift or a demand forecast.

## Contribution and response

Recorded COGS/allocated overhead are not automatically relevant incremental/avoidable costs. With defined unit costs:

```text
Baseline contribution = Σ q0_i × (p_base_i − c_base_i)
Proposed contribution = Σ q0_i × (p_prop_i − c_prop_i)
Contribution difference = price-only difference − Σ q0_i × (c_prop_i − c_base_i)
```

Explicitly unchanged costs make revenue and contribution differences equal before incremental action costs. Otherwise separate price/cost effects. Subtract supported implementation costs for a defined profit measure; recompute margin rates from scenario totals.

Keep quantity-response sensitivities separate and explicit. Historical price/volume association does not identify elasticity; distributor shipments do not establish end-user demand.

For one product, unchanged incremental fixed costs, `CM0 = p0 − c0` and absolute unit-price/cost changes `Δp, Δc`:

```text
Contribution-preserving Δq / q0 = −(Δp − Δc) / (CM0 + Δp − Δc)
```

Require consistent units and positive proposed unit contribution. Changed capacity/fixed costs, nonpositive contribution or portfolio mix require another scenario. This describes breakeven; future response requires separate evidence.
