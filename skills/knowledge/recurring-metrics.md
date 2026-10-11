# Recurring revenue, retention and lifecycle measures

Use for recurring subscriptions, contractual commitments and recurring portions of hybrid offers. Apply [metric verification](metric-verification.md); preserve applicable confirmed company recipes. Provider labels do not settle the economic question.

## Select the recipe

Establish the shared recipe elements through metric verification, plus treatment of discounts, tax, free/trial periods, past-due accounts, pauses, cancellation requests, expiry and reactivation.

MRR is a monthly normalized eligible recurring amount under that recipe. An annual 1,200 recurring item contributes 100 per month; its prepayment is cash/invoicing, not MRR. Setup, hardware and other one-time charges remain separate unless a differently named company measure intentionally includes them.

For a comparable monthly recurring run rate, ARR may be defined as 12 × MRR. Distinguish this from forward contracted annual value, bookings, recognized revenue and trailing actual revenue. Use supplied finance policy for recognized amounts; cadence normalization is not revenue recognition.

Show contracted minimums/commitments, consumed usage, rated/billed usage and named trailing usage run rates separately. Metered revenue is not automatically included or excluded from every provider's MRR. Recipe differences require reconciliation, not silent standardization.

## Opening-cohort retention

For a declared retention grain, horizon and policy, let C be the eligible opening cohort, b_i its opening recurring amount, e_i its eligible ending amount and B = sum(b_i) > 0. This endpoint recipe applies only when each included opening and ending amount is nonnegative; a negative credit balance makes the recipe inapplicable until its treatment is confirmed or another applicable company recipe is selected.

```text
NRR = sum(e_i for i in C) / B
GRR = sum(min(b_i, e_i) for i in C) / B
```

Confirm grain and treatment of reactivation, replacements, FX and unusual signed amounts; do not silently clamp accounting credits. Account-level and item-level GRR can differ; apply the chosen grain consistently. Exclude new customers outside C. A zero denominator yields an undefined result, not zero retention.

A movement bridge must reconcile opening to closing under the same recipe: new, expansion, contraction, churn, reactivation and other explicit movements. Document classification and netting conventions; movement totals are not inherently interchangeable with endpoint GRR.

Logo churn uses opening customers/accounts and a stated loss policy. Cancellation intent, paid-through service, payment failure and entitlement cessation are different events. Repeat retail purchase is a different measure. Short-horizon rates cannot become observed annual retention through automatic compounding.

## Supporting economics

Separate observed cohort revenue/contribution from modeled lifetime value. For cohort acquisition cost (CAC), payback and lifetime economics, define the acquired cohort and acquisition window, included acquisition costs, contribution basis, timing and finite observation/model horizon. Payback is the time until cumulative cohort contribution on that basis recovers the applicable acquisition cost; finite-horizon lifetime contribution sums the cohort's supported contribution over the declared horizon, with acquisition cost shown separately or netted explicitly. Match cohort membership, costs and timing. This recipe applies to recurring and one-time offers; it does not require MRR, ARR or subscription churn. Incomplete outcomes or costs support a conditional estimate, not precise observed lifetime value. Simple ARPA/margin/churn lifetime formulas require explicit stable-process assumptions. Use [recurring scenarios](methods/recurring-scenarios.md) for rating, bridges and future cases.
