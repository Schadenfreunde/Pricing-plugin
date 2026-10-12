# Verify the metric before explaining it

## Meaning and comparability

**Establish each measure's basis**

- Revenue, realized price and COGS may have alternative accounting, currency or unit bases.
- Before calculating each requested measure, establish its basis from a confirmed mapping that applies to this source and purpose (shared rules, section 1), or stop and ask under the [shared rules](../references/shared-rules.md#3-unresolved-basis-stop-and-ask).

**Check comparability**

- Verify like-for-like definitions, price levels, currency and FX basis, units, periods and populations, within matched records and across sources.
- A customer or product match alone does not establish comparability.

**Lifecycle, recurring and retail measures**

- For lifecycle or recurring analysis, establish:
  - commercial actor, metric and recipe version or formula
  - population and grain
  - snapshot and service period
  - status and eligibility policy
  - adjustment treatment, units, and commitment or usage basis
- Keep company and provider variants under distinct names.
- For retail, use [retail economics](retail-economics.md) to set the actor and the gross, net or proceeds basis and cost boundaries.

## Actual data checks

Run the checks relevant to the metric and risk with available tools. Saved mappings do not establish that a new export is correct.

**Parsing**

- Inspect raw numeric representations, types and parsing outcomes, including mixed decimal and grouping conventions.
- Normalize only an evidenced, unambiguous interpretation, then verify amounts and scale. Ambiguous separators need clarification.
- Preserve source values and expose parse failures.

**Structure and timing**

- Establish grain, identifiers, join cardinality, effective-date matches and overlaps, and coverage.
- Where relevant, check:
  - contract or item replacement lineage
  - event or consumption time versus processing or posting time
  - meter corrections and cutoffs
  - exposure maturity and settlement state
- Check cancellations, signed credits and returns, and definition changes.

**Prices and costs**

- Verify usable prices and costs are numeric, present, dated and on the required currency, unit and accounting basis.
- Pack metadata alone does not establish a conversion.
- Resolve, or explicitly quarantine, classification contradictions.

**Adjustments and events**

- Reconcile signed adjustments and accounting treatment.
- Validate links between source line or invoice, business event and obligation, including exceptions outside the headline population.
- Recognize an event once, by its business key.
- Cash settlement is not another revenue event. Credits already in invoices are not deducted again.

**Retrieval**

- Distinguish authorization errors, truncated pagination, omitted or undefined fields, successful empty responses and unavailable history.
- Report the retrieved scope. Never treat an error or truncation as complete history.

**Coverage**

- State the supported scope and missing or excluded coverage in counts, quantities and value where available.
- Known invalid records may support a clearly bounded partial result.
- A partial result does not replace a requested complete comparison or bypass an unresolved business-basis choice.

## Calculations and display

**Gross margin**

- For gross margin defined as `(sales − COGS) / sales`, calculate both period rates from totals, then subtract earlier from later.
- A group rate is `sum(sales − COGS) / sum(sales)`. This equals consistently sales-weighted product rates; an unweighted average generally does not.
- Express movement in percentage points or basis points: 1 percentage point = 100 bps.
- Correct material differences from the reported movement before building a bridge.

**Transaction arithmetic**

- Quantity × unit price or cost is a mapping to realized sales or COGS that must be verified, not a universal rating function.
- Separately recorded rebates, credits or allocations may alter it.
- Tiers, commitments, entitlements or lifecycle effects use the [recurring-scenario method](methods/recurring-scenarios.md).
- Handle zero or negative denominators and unusual signed transactions explicitly.
- Use exact decimal or scaled-integer arithmetic for monetary thresholds. Classify on unrounded values.
- Reconcile before display rounding. If independently rounded components differ from a displayed total, show a rounding note or residual.

**Aggregate-only data**

- Aggregate totals can verify the movement but generally cannot identify price, unit-cost or mix contributions.
- State that limit and request matched item or customer-period detail: quantities, realized prices, costs and adjustments.
