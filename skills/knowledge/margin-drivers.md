# Explain a margin movement with supported drivers

After verifying endpoints, examine consistent realized prices, unit costs and product/customer/geographic composition. Uniform volume changes need not change a margin rate; composition, tiers or cost behavior can. Distinguish unit costs from allocations and greater total COGS from unit-cost inflation.

Declare a reproducible bridge's counterfactuals, order and denominator. Revenue variance differs from margin-rate variance; calculation order does not establish event order. Reconcile contributions to the verified movement before rounding.

**Project convention for two factors with verified unchanged unit costs:** let `G(p,q) = 1 − Σ(qᵢcᵢ) / Σ(qᵢpᵢ)`, with realized prices `p`, quantities `q`, unchanged unit costs `c`, and periods 0/1:

```text
Price = G(p₁,q₀) − G(p₀,q₀)
Mix/quantity = G(p₀,q₁) − G(p₀,q₀)
Shared effect = G(p₁,q₁) − G(p₁,q₀) − G(p₀,q₁) + G(p₀,q₀)
```

These terms sum to the endpoint movement. Changing costs or additional factors require a declared method covering them; this narrow expression is not universal.

An interaction/shared effect is calculated overlap. An unexplained residual is a remaining reconciliation gap, potentially from missing factors, data or calculation errors; show it separately.

Accounting attribution establishes what changed. Commercial causation requires supporting contracts, adjustments, policy or behavior. Lower realized price alone does not establish increased discounting. If causes remain unsupported, state the limit and relevant next investigations.
