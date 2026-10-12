# Rate and compare recurring or usage scenarios

- Use when linear quantity × unit-price arithmetic does not represent the contract, or when recurring or lifecycle movements matter.
- Establish the metric through [recurring metrics](../recurring-metrics.md).
- Verify inputs with [metric verification](../metric-verification.md).

## Apply the actual rating rules

**Inputs**

- Represent the relevant price or package version, entitlement, billable quantity or usage, eligibility state and time basis.
- Apply fixed fees, included units, minimums, commitments and credits, add-ons, tiers, overages, discounts and proration only as the contract or selected recipe supports.

**Tiers and timing**

- Graduated tiers charge the units within each band.
- Volume tiers can apply the reached band's rate to all qualifying units.
- Blended average prices do not identify the same schedule.
- Preserve service periods, price effective dates, billing cadence and provider rounding rules.
- Handle duplicate, corrected and late meter events under an evidenced business-key and cutoff policy. Processing time and consumption time may differ.

**Billing order**

- An unresolved material billing order is an unresolved basis: hold the affected invoice calculation and ask for the governing sequence (shared rules, section 3).

**Gaps and exclusions**

- A snapshot cannot recover absent contract or event history.
- Show unsupported rating components and affected coverage. Never fill them with assumptions presented as observed facts.
- Before delivery, reconcile inclusion and exclusion summaries against every reported result's component lines.
- If a component appears in any result, do not call it globally excluded. Scope each exclusion claim to its schedule, version, period and result.

## Explain observed change

**Bridge**

- Choose a reproducible bridge over comparable records: price-version changes, seats or usage, package or entitlement, discount expiry, lifecycle eligibility, scope and FX as relevant.
- State counterfactuals and order.
- Gross-margin-rate bridge on linear comparable items, with verified unchanged unit costs and only price and quantity or composition factors:
  - keep the [margin-drivers](../margin-drivers.md) convention and its separate shared effect, for recurring and industrial items alike
  - use a sequential allocation only if explicitly requested and named, showing its different interaction allocation
- Named revenue or MRR bridge involving tariffs or lifecycle state:
  - interactions may be shown separately or assigned by a declared sequential convention
  - show any unexplained residual separately and reconcile to verified endpoints

**Pure historical price counterfactual**

- Rate the same prior representative quantities, entitlements and eligible state under both observed price schedules.
- Applicable linear baskets keep the [price-realization](price-realization.md) convention regardless of known demand response.
- New seats or plan upgrades are not automatically price realization.
- Structural or package changes may prevent an equivalent-service comparison. Keep that limit.

## Compare proposed cases

**Setup**

- Name current and proposed schedules, eligible cohort, renewal or effective dates, horizon and quantity or usage assumptions.
- When response is unknown, hold representative prior quantities and state fixed for a conditional base.
- Show explicitly assumed adoption, churn or usage sensitivities separately.

**Costs and timing**

- Include comparable proposed costs in the principal case: fulfillment, infrastructure, support, fees, hardware or service, implementation.
- Cost response can differ from revenue tiers.
- Separate recurring contribution, recognized revenue supplied by finance, invoicing and cash timing.
- Reuse [price-change economics](price-change-economics.md) for applicable linear contributions and breakeven.
- Nonlinear schedules, delayed renewal, changing fixed costs or eligibility need scenario evaluation.

**Limits**

- Keep gross and net retention, customer counts and service constraints visible where the choice depends on them.
- Lifetime scenarios need a supported finite horizon and explicit survival and response assumptions.
- Useful conditional cases do not establish optimal pricing or capture.
