# Verify the metric before explaining it

## Meaning and comparability

Use the user's confirmed definitions and measure-to-field mappings, scoped to source/schema and analysis purpose. Revenue, realized price and COGS may have alternative accounting, currency or unit bases; a column name does not settle the choice. For each requested measure, establish its basis before calculation: use applicable confirmed mappings, or stop and ask under the [shared rules](../references/shared-rules.md#3-unresolved-basis-stop-and-ask). Confirmation is needed for the current analysis, not merely for saving future defaults. Reuse applicable confirmed choices without reopening intake.

Verify like-for-like definitions, price levels, currency/FX basis, units, periods and populations within matched records and across sources. A customer/product match alone does not establish comparability. If a material change or ambiguity has no confirmed reconciliation or conversion basis, such as per-unit versus per-line grain or a pack conversion, the comparison's basis is unresolved: stop and ask under the shared rules.

When valid policy or recipe versions overlap and precedence is unresolved, stop and ask under the shared rules before calculating or publishing the affected result. Keep the valid records in scope; unrequested conditional alternatives or dropped records do not resolve precedence. If the user explicitly requests a comparison under each valid version, calculate those branches as labelled scenarios while keeping the governed single result unresolved.

For lifecycle or recurring analysis, establish the commercial actor, metric and recipe version/formula, population and grain, snapshot and service period, status/eligibility policy, adjustment treatment, units, and commitment/usage basis. Keep company and provider variants under distinct names. For retail economics, use [retail economics](retail-economics.md) for the actor and gross/net/proceeds and cost boundaries.

## Actual data checks

Execute checks relevant to the metric and risk with available tools; saved mappings do not establish a new export's correctness:
- Inspect raw numeric representations, types and parsing outcomes, including mixed decimal/grouping conventions. Normalize only an evidenced, unambiguous interpretation and verify amounts/scale afterward; ambiguous separators need clarification. Preserve source values and expose parse failures rather than coercing them to zero or silently losing rows.
- Establish grain, identifiers, join cardinality, effective-date matches/overlaps and coverage. Where relevant, check contract/item replacement lineage, event/consumption versus processing/posting time, meter corrections and cutoffs, exposure maturity, and settlement state. Check cancellations, signed credits/returns, classification contradictions and changes in definitions.
- Verify usable prices/costs are numeric, present, dated and on the required currency/unit/accounting basis. Blank or unmatched cost is unavailable, not zero; a valid recorded zero is different. Pack metadata alone does not establish a conversion. Resolve or explicitly quarantine contradictory classification evidence.
- Reconcile signed adjustments and accounting treatment. Validate source line/invoice, business-event and obligation links, including exceptions outside the headline population. Recognize an event once by its business key; cash settlement is not another revenue event and credits already in invoices are not deducted again.
- Distinguish authorization errors, truncated pagination, omitted/undefined fields, successful empty responses and unavailable history. Report the retrieved scope; never turn an error or truncation into zero or complete history.

State the supported scope and missing/excluded coverage in counts, quantities and value where available. Known invalid records may support a clearly bounded partial result; that result does not replace a requested complete comparison or bypass an unresolved business-basis choice. Keep unknown amounts distinct from measured zero.

## Calculations and display

For gross margin defined as `(sales − COGS) / sales`, calculate both period rates from totals, then subtract earlier from later. A group rate is `sum(sales − COGS) / sum(sales)`, equivalent to consistent sales-weighted product rates; an unweighted average generally fails. Express movement in percentage points or basis points: 1 percentage point = 100 bps. Correct material differences from the reported movement before building a bridge.

For transaction data, verify that quantity × unit price/cost is a mapping to realized sales/COGS, not a universal rating function; separately recorded rebates, credits or allocations may alter it, and tiers, commitments, entitlements or lifecycle effects use the [recurring-scenario method](methods/recurring-scenarios.md). Handle zero/negative denominators and unusual signed transactions explicitly. Use exact decimal or scaled-integer arithmetic for monetary thresholds and classify on unrounded values. Reconcile before display rounding; if independently rounded displayed components differ from a displayed total, show a rounding note or residual.

Aggregate-only totals can verify the movement but generally cannot identify price, unit-cost or mix contributions. State that limit and request relevant matched item/customer-period detail, quantities, realized prices, costs and adjustments.
