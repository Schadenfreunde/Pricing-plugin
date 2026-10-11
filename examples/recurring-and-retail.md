# Promotion and recurring revenue: synthetic illustrations

These two synthetic cases show how Pricing Plugin states a recipe before it reports a number. They are not customer results, a causal finding or evidence of installed-host performance.

## Promotion: sales up, contribution down

A product costs 70 per unit. At a price of 100, 100 units sold; during a promotion at 80, 150 units sold.

| Measure | Before | Promotion | Change |
| --- | ---: | ---: | ---: |
| Revenue | 10,000 | 12,000 | +20% |
| Contribution, `(price − cost) × units` | 3,000 | 1,500 | −50% |

Observed revenue grew while contribution halved. The comparison is descriptive: it does not show that the promotion caused the extra units, and stockpiling, substitution, retailer pass-through and later demand are not measured. Revenue growth cannot stand in for profit improvement.

## Recurring revenue: annual charge, setup and cash

A customer is invoiced 1,500 up front: an eligible annual recurring charge of 1,200 plus a one-time setup fee of 300.

| Measure | Value | Basis |
| --- | ---: | --- |
| MRR | 100 | 1,200 ÷ 12 under the simple eligible-recurring recipe |
| ARR | 1,200 | 12 × MRR, a compatible run-rate recipe only |
| Setup | 300 | One-time; outside MRR |
| Invoice and cash | 1,500 | Billing and collection, not MRR |

Recognized revenue is separate and needs the finance team's policy.

## Retention: opening cohort only

Two accounts open the period at 500 each (opening recurring revenue 1,000). They end at 1,200 and 0. A new customer adds 300 and is outside the opening cohort.

| Measure | Value | Calculation |
| --- | ---: | --- |
| NRR | 120% | (1,200 + 0) ÷ 1,000 |
| GRR, account grain | 50% | (min(500, 1,200) + min(500, 0)) ÷ 1,000 |
| Closing MRR | 1,500 | 1,200 + 0 + 300 new customer |

The new customer raises closing MRR but not NRR or GRR. GRR changes with the declared grain and with the retained-amount cap, so a report names both.

[Return to examples](README.md) · [Return to Pricing Plugin](../README.md)
