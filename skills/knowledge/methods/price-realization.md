# Measure comparable realized-price movement

Use observed prices at a defined level. A list increase may differ from net/pocket realization; resolve adjustment mappings with the [waterfall](../price-waterfall.md) when needed.

Verify matched scope, periods, grain, units/currency, sales/quantity mappings and adjustments. Customer/product matching may be needed for differing terms. Changed list/accounting bases can invalidate discount comparisons. Average selling price can move solely because the basket changes; aggregate sales without comparable quantities/detail cannot identify pure price movement.

**Historical fixed-basket convention:** hold prior-period item quantities `q0_i` fixed when comparing observed baseline prices `p0_i` and later prices `p1_i`. This measurement applies regardless of known demand response.

```text
Baseline basket revenue = Σ q0_i × p0_i
Comparison basket revenue = Σ q0_i × p1_i
Price-only difference = Σ q0_i × (p1_i − p0_i)
Fixed-basket price movement = comparison / baseline basket revenue − 1
```

Fixing item quantities fixes composition. This constructed comparison isolates price; it does not explain every actual revenue/margin change or establish causation. Use a meaningful nonzero denominator; handle signed quantities, returns and credits explicitly.

State period, coverage, price level and units/currency. Disclose matching limits, exclusions, new/discontinued items and missing history; missing prior quantity is neither zero nor replaceable by current quantity. Flag unrepresentative history and avoid automatic annualization.

For actual margin attribution use [margin drivers](../margin-drivers.md); for assumed proposed prices, contribution and response scenarios use [price-change economics](price-change-economics.md).
