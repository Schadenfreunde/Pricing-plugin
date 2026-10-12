# Explain a margin movement with supported drivers

## Examine the drivers

- Verify both endpoints first.
- Then examine consistent realized prices, unit costs and product, customer and geographic composition.
- A uniform volume change need not change a margin rate. Composition, tiers or cost behavior can.
- Distinguish unit costs from allocations.
- Distinguish higher total COGS from unit-cost inflation.

## Build the bridge

- Declare the bridge's counterfactuals, order and denominator so it is reproducible.
- Revenue variance differs from margin-rate variance.
- Calculation order does not establish the order of events.
- Reconcile contributions to the verified movement before rounding.

**Project convention for two factors with verified unchanged unit costs:** let `G(p,q) = 1 − Σ(qᵢcᵢ) / Σ(qᵢpᵢ)`, with realized prices `p`, quantities `q`, unchanged unit costs `c`, and periods 0/1:

```text
Price = G(p₁,q₀) − G(p₀,q₀)
Mix/quantity = G(p₀,q₁) − G(p₀,q₀)
Shared effect = G(p₁,q₁) − G(p₁,q₀) − G(p₀,q₁) + G(p₀,q₀)
```

- These terms sum to the endpoint movement.
- This narrow expression is not universal. Changing costs or additional factors need a declared method that covers them.
- A shared (interaction) effect is calculated overlap.
- An unexplained residual is a remaining reconciliation gap, possibly from missing factors, data or calculation errors. Show it separately.

## Separate attribution from cause

- Accounting attribution establishes what changed.
- Commercial causation needs supporting contracts, adjustments, policy or behavior.
- A lower realized price alone does not establish increased discounting.
- If causes remain unsupported, state the limit and the relevant next investigations.
