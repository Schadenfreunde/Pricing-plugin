# Price realization at a comparable price level

Use this reference to measure realized price movement separately from volume/mix changes, or to construct a proposed-price scenario. A list increase does not establish an equivalent net or pocket increase: discounts, rebates and other adjustments can offset it. Start with the company's defined price level and [waterfall](../price-waterfall.md).

## Evidence and comparison

Establish product/customer scope, time period, observation grain, realized sales/quantity mapping, price units, currency and the treatment of credits, returns and adjustments. Compare like-for-like prices; an average selling price can change just because the basket changes. A matched customer/product/period basis may be necessary when customer terms differ. Regional list changes or accounting changes can invalidate nominal discount comparisons.

For a historical price comparison, use observed realized prices on matched records. For a proposed change, name the proposed realization assumptions and do not treat them as observed facts. A suggested peer price is not automatically attainable. If only sales totals exist without comparable quantities/detail, report the narrower performance measure rather than inventing a pure-price index.

## Prior-period fixed-basket convention

**Project analytical convention:** when demand response is unknown, hold the previous relevant period's quantities `q0_i` fixed on both sides. With comparable baseline prices `p_base_i` and comparison/proposed prices `p_comp_i`:

```text
Baseline revenue = Σ q0_i × p_base_i
Comparison revenue = Σ q0_i × p_comp_i
Price-only difference = Σ q0_i × (p_comp_i − p_base_i)
Fixed-basket price movement = comparison revenue / baseline revenue − 1
```

Use prior-period realized baseline prices when available and appropriate. If the decision explicitly uses documented current effective prices as the baseline, apply those prices to the same prior quantities and name that alternative basis. Use the index only with a meaningful nonzero revenue denominator; handle returns/credits and signed quantities explicitly rather than silently deleting them or taking absolute values.

Fixing quantities by item also fixes composition. This isolates price in a constructed comparison; it does not explain every change in actual sales or margin. A proposed-price calculation is a **fixed-volume scenario**, not a forecast or demand estimate. For actual historical margin attribution, retain the declared [margin-driver method](../margin-drivers.md).

State the prior period, covered population, price level, quantities, currency/units and assumptions in a brief method note. Disclose unmatched items, missing prior quantities, new/discontinued products and exclusions. Use a supported subset when useful; missing quantity is not zero and current quantity is not a substitute. Flag an unrepresentative prior period; do not automatically annualize it. Obtain supported adjustment mappings before converting a list-price proposal into net realization.

For contribution, changed costs, breakeven and separately assumed downside scenarios, consult [price-change economics](price-change-economics.md).

**Source locator:** *CPM Training 2026 Spring Amsterdam Module 5 Execution.pdf*, physical PDF p. 40, “Price monitoring around price increase is important,” supports tracking pocket versus list prices and using indices to eliminate mix changes. The specific prior-period basket formula and coverage rules above are project guidance, not a formula asserted from that slide.
