# Recurring revenue, retention and lifecycle measures

- Use for recurring subscriptions, contractual commitments and the recurring portion of hybrid offers.

## Select the recipe

- Establish the shared recipe elements through [metric verification](metric-verification.md).
- Also establish treatment of discounts, tax, free or trial periods, past-due accounts, pauses, cancellation requests, expiry and reactivation.

**MRR**

- MRR is the monthly normalized eligible recurring amount under that recipe.
- An annual 1,200 recurring item contributes 100 per month. Its prepayment is cash or invoicing, not MRR.
- Setup, hardware and other one-time charges stay separate, unless a differently named company measure intentionally includes them.

**ARR**

- For a comparable monthly run rate, ARR may be defined as 12 × MRR.
- Distinguish it from forward contracted annual value, bookings, recognized revenue and trailing actual revenue.
- Use supplied finance policy for recognized amounts. Cadence normalization is not revenue recognition.

**Usage and commitments**

- Show separately: contracted minimums or commitments, consumed usage, rated or billed usage, and named trailing usage run rates.
- Metered revenue is not automatically included in, or excluded from, every provider's MRR.
- Reconcile recipe differences; never standardize them silently.

## Opening-cohort retention

For a declared retention grain, horizon and policy, let C be the eligible opening cohort, b_i its opening recurring amount, e_i its eligible ending amount and B = sum(b_i) > 0:

```text
NRR = sum(e_i for i in C) / B
GRR = sum(min(b_i, e_i) for i in C) / B
```

- This endpoint recipe applies only when every included opening and ending amount is nonnegative.
- A negative credit balance makes it inapplicable until its treatment is confirmed or another applicable company recipe is selected. Never silently clamp accounting credits.
- Confirm grain and treatment of reactivation, replacements and FX.
- Account-level and item-level GRR can differ. Apply the chosen grain consistently.
- Exclude new customers outside C.
- A zero denominator gives an undefined result, not zero retention.

**Movement bridge**

- Reconcile opening to closing under the same recipe: new, expansion, contraction, churn, reactivation and other explicit movements.
- Document classification and netting conventions.
- Movement totals are not inherently interchangeable with endpoint GRR.

**Churn**

- Logo churn uses opening customers or accounts and a stated loss policy.
- Cancellation intent, paid-through service, payment failure and entitlement cessation are different events.
- Repeat retail purchase is a different measure.
- Short-horizon rates cannot become observed annual retention through automatic compounding.

## Supporting economics

- Separate observed cohort revenue or contribution from modeled lifetime value.
- For cohort acquisition cost (CAC), payback and lifetime economics, define:
  - the acquired cohort and acquisition window
  - included acquisition costs
  - contribution basis and timing
  - a finite observation or model horizon
- Payback is the time until cumulative cohort contribution on that basis recovers the applicable acquisition cost.
- Finite-horizon lifetime contribution sums the cohort's supported contribution over the declared horizon. Show acquisition cost separately or net it explicitly.
- Match cohort membership, costs and timing.
- This recipe applies to recurring and one-time offers. It does not need MRR, ARR or subscription churn.
- Incomplete outcomes or costs support a conditional estimate, not a precise observed lifetime value.
- Simple ARPA × margin / churn lifetime formulas need explicit stable-process assumptions.
- Use [recurring scenarios](methods/recurring-scenarios.md) for rating, bridges and future cases.
