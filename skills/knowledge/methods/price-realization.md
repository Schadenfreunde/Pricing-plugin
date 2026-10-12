# Measure comparable realized-price movement

## Check the basis

- Use observed prices at a defined level.
- A list increase may differ from net or pocket realization. Resolve adjustment mappings with the [waterfall](../price-waterfall.md) when needed.
- Verify matched scope, periods, grain, units and currency, sales and quantity mappings, and adjustments.
- Customer or product matching may be needed where terms differ.
- Changed list or accounting bases can invalidate discount comparisons.
- Average selling price can move solely because the basket changes.
- Aggregate sales without comparable quantities or detail cannot identify pure price movement.

## Fixed-basket convention

- Hold prior-period item quantities `q0_i` fixed when comparing observed baseline prices `p0_i` with later prices `p1_i`.
- This applies regardless of known demand response, but only where price, quantity and service or entitlement are comparable.
- For nonlinear schedules or lifecycle and package movements, use [recurring scenarios](recurring-scenarios.md).

```text
Baseline basket revenue = Σ q0_i × p0_i
Comparison basket revenue = Σ q0_i × p1_i
Price-only difference = Σ q0_i × (p1_i − p0_i)
Fixed-basket price movement = comparison / baseline basket revenue − 1
```

- Fixing item quantities fixes composition.
- This constructed comparison isolates price. It does not explain every actual revenue or margin change, or establish causation.
- Use a meaningful nonzero denominator.
- Handle signed quantities, returns and credits explicitly.

## Report

- State period, coverage, price level, and units and currency.
- Disclose matching limits, exclusions, new or discontinued items and missing history.
- For actual margin attribution, use [margin drivers](../margin-drivers.md).
- For assumed proposed prices, contribution and response scenarios, use [price-change economics](price-change-economics.md).
