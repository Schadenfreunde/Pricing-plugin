# Pricing Plugin: AI-assisted pricing analysis for B2B, consumer and subscription businesses

Pricing Plugin provides seven connected AI skills for pricing analysis, opportunity assessment, offer and charging-model design and rollout planning. It covers industrial products and spare parts, ecommerce, consumer apps, B2B SaaS, physical subscriptions and installed-equipment hybrids.

The skills share curated pricing knowledge, check comparison assumptions and retain company facts only after validation. Calculation and artifacts use the tools available in your AI host.

**Version:** `0.3.0`

[Install](#install-the-plugin) · [System structure](PRICING_SYSTEM.md) · [Company context](#recommended-first-step-company-context) · [Skills](#pricing-skills-and-example-questions) · [FAQ](#frequently-asked-questions)

See the [system structure diagram](PRICING_SYSTEM.md) for how the seven skills, shared pricing knowledge, company context and reporting tools work together.

## Install the plugin

Paste this into your AI agent:

```text
Install the Pricing Plugin by fetching and following the instructions at https://raw.githubusercontent.com/Schadenfreunde/Pricing-plugin/refs/heads/main/INSTALL.md
```

## Recommended first step: company context

Use `pricing-intake` to establish reusable context, or start directly with your pricing question when enough information is available.

```text
Use pricing-intake to review our company pricing context. Propose relevant facts and save only those I confirm to .pricing/context.md in this working project.
```

In a new directory, you can supply a `context.md` from another project. Intake checks its company/scope and applicability, reuses previously validated facts and clarifies changes. Otherwise share a brief overview and relevant definitions or policies; no complete intake interview is required.

Context can retain validated price/metric definitions, calendar, units/currencies, reusable data mappings, policies and scoped exceptions. For data-backed intake, confirm which revenue, COGS and other fields serve the requested analysis, with their accounting, currency and unit basis. Each new dataset still needs numeric-consistency, coverage and like-for-like comparison checks. A material unresolved basis choice pauses the affected calculation for clarification while independently valid work continues. Analysis findings and proposals stay with the answer/report; a separate handoff brief is saved only when requested.

Attach data and ask the relevant skill, for example:

> Use pricing-analyze to explain the gross margin movement. Verify the change, reconcile supported drivers and state what remains unknown.

## Pricing skills and example questions

| Skill | Result | Example |
| --- | --- | --- |
| [pricing-intake](skills/pricing-intake/SKILL.md) | Validated reusable company context | “Review these policies and propose what to retain.” |
| [pricing-analyze](skills/pricing-analyze/SKILL.md) | Verified calculations and performance explanations | “Why did gross margin fall?” |
| [pricing-scan](skills/pricing-scan/SKILL.md) | Data fitness → classified findings → evidence-ranked leads | “Find opportunities in this export.” |
| [pricing-recommend](skills/pricing-recommend/SKILL.md) | Action choice with capture mechanism and tradeoffs | “Which leads should we act on?” |
| [pricing-design](skills/pricing-design/SKILL.md) | Chosen strategy or pricing structure | “Design pump pricing” or “Redesign our discounts.” |
| [pricing-execute](skills/pricing-execute/SKILL.md) | High-level rollout, dependencies and readiness | “Plan our agreed price increase.” |
| [pricing-triage](skills/pricing-triage/SKILL.md) | Focused clarification, routing or brief definitions | “Where should we start?” |

Explicit tasks enter directly. Combine workflows when useful, carrying existing evidence and decision status forward.

Business type and charging model are independent: a business or consumer offer can be one-time, recurring, usage-based or hybrid. Only the methods a request needs are loaded.

### Example questions by business

Each question names the skill that handles it. Attach the relevant export or supply the figures.

**Industrial manufacturers and spare parts**

- “Gross margin fell this quarter. Verify the movement and split it into price, mix and cost effects.” (`pricing-analyze`)
- “Did our January list-price increase actually realize, measured on the same basket of parts we sold in the prior period?” (`pricing-analyze`)
- “Scan this customer-by-part export for price outliers and rank the leads by evidence.” (`pricing-scan`)
- “We have three leads: spare-part list prices, aged quotes and one distributor's discounts. Which should we pursue first?” (`pricing-recommend`)
- “Design a spare-parts price structure: list prices, volume discounts and exception rules.” (`pricing-design`)
- “We agreed a 4% increase. Which contracts and open quotes are protected, and what notice is needed?” (`pricing-execute`)

**Distributors and wholesalers**

- “Which accounts receive discounts above policy, and which of those have an approved, unexpired exception?” (`pricing-scan`)
- “Compare what our distributors actually paid for comparable items in the same region. Which differences are meaningful?” (`pricing-analyze`)
- “Redesign our distributor discount structure so volume is rewarded without eroding list price.” (`pricing-design`)
- “Plan a price increase through distributors who already hold stock bought at the old price.” (`pricing-execute`)

**B2B software and services**

- “What are NRR and GRR for the Q3 renewal cohort, at account level and at item level?” (`pricing-analyze`)
- “Bridge MRR from last quarter into seat, price, package and currency effects.” (`pricing-analyze`)
- “Did the annual-prepay discount raise contribution, or only bookings?” (`pricing-analyze`)
- “Should our API usage pricing use graduated or volume tiers, and where does a commitment fit?” (`pricing-design`)
- “Which renewals can take an uplift on 1 January once notice windows and grandfathering are applied?” (`pricing-execute`)

**Installed equipment and hybrid offers**

- “How many installed machines are eligible for the attached software, and what is the attach rate?” (`pricing-analyze`)
- “What are first-year and renewal contribution for a monitoring contract with setup, hardware and annual service?” (`pricing-analyze`)
- “How should we split setup and recurring charges for an offer of sensors, a gateway, installation and annual service?” (`pricing-design`)

**Ecommerce and consumer apps**

- “Did the promotion raise contribution or only sales?” (`pricing-analyze`)
- “After returns and marketplace fees, what do we keep per order, and does it reconcile to the payout?” (`pricing-analyze`)
- “Did the paywall test change paid conversion?” (`pricing-analyze`)

A [synthetic illustration](examples/recurring-and-retail.md) covers a promotion and recurring-revenue metrics with their recipes stated.

## Shared pricing methods

All pricing knowledge lives in [skills/knowledge](skills/knowledge/index.md); reporting and handoffs use shared workflow references.

| Reference | Supports |
| --- | --- |
| [Metric verification](skills/knowledge/metric-verification.md) | Definitions, comparable populations and verified calculations |
| [Margin drivers](skills/knowledge/margin-drivers.md) | Reconciled price/cost/mix attribution and causation limits |
| [Price waterfall](skills/knowledge/price-waterfall.md) | Defined list, invoice, net and pocket levels |
| [Value estimation](skills/knowledge/methods/value-estimation.md) | Differentiated value against credible buyer alternatives |
| [Segmentation](skills/knowledge/methods/segmentation.md) | Economically meaningful, enforceable differentiation |
| [Peer comparisons](skills/knowledge/methods/peer-comparisons.md) | Comparable price dispersion and its limits |
| [Price realization](skills/knowledge/methods/price-realization.md) | Historical fixed-basket realized-price measurement |
| [Discount governance](skills/knowledge/methods/discount-governance.md) | Applicable rules, approval and scoped exceptions |
| [Price-change economics](skills/knowledge/methods/price-change-economics.md) | Conditional revenue/contribution and breakeven scenarios |
| [Evidence ranking](skills/knowledge/methods/evidence-ranking.md) | Observation/action confidence and separate commercial overlays |
| [Retail economics](skills/knowledge/retail-economics.md) | Actor-specific order, channel and contribution views |
| [Recurring metrics](skills/knowledge/recurring-metrics.md) | MRR, ARR, retention and lifecycle recipes |
| [Recurring scenarios](skills/knowledge/methods/recurring-scenarios.md) | Tariffs, commitments and recurring bridges |
| [Experiments and promotions](skills/knowledge/methods/experiments-and-promotions.md) | Causal evidence, promotion economics and outcome maturity |
| [Offer architecture](skills/knowledge/methods/offer-architecture.md) | Value unit, package, cadence and charging structure |
| [Renewals and migration](skills/knowledge/methods/renewals-and-migration.md) | Protected, eligible and unresolved existing customers |
| [Hybrid offers](skills/knowledge/methods/hybrid-offers.md) | Assets, fulfillment and recurring services together |

## Frequently asked questions

### What data supports gross margin analysis?

Comparable periods, sales, COGS and the margin definition establish the movement. Matched item quantities, realized prices and unit costs support driver analysis. Aggregate totals alone usually cannot identify price/cost/mix effects.

### How are price measurement and price scenarios different?

Historical realization compares observed prices using the same prior-period item quantities, regardless of known demand response. This controls basket mix. For proposed prices with unknown future response, those quantities create a conditional fixed-volume scenario. It is not a demand forecast or guaranteed benefit; contribution also needs relevant costs.

### What data sources work?

CSV or spreadsheet exports, several related files, or a governed source your host already provides. The plugin installs no Stripe, Shopify, PostHog or warehouse connector: it checks which tools exist and asks for an export when needed. A current-state snapshot cannot rebuild earlier cohorts, and your confirmed MRR, churn or retention recipe, not a provider's label, defines the metric.

### Does the plugin update prices or approve discounts?

The skills draft analyses, recommendations and plans. System changes and communications need explicit authorization and suitable tools. Detailed account/product targets and negotiation support remain outside this version.

### Does company data stay local?

Validated context is saved in the working project's `.pricing/context.md`. Processing of prompts/files depends on the AI host, connected tools, settings and provider terms; local context storage does not establish local-only processing. The plugin has no separate data service, calculation engine or MCP server.

## Validation and limitations

From a full checkout, run:

```sh
python3 -B scripts/check_package.py
```

This development check validates the manifests, skill metadata, references, unlinked package files and documentation links. They do not test model behavior.

**What V2 behavior testing covered (2026-10-11).** Twenty case families gave 22 cases, because one family was split into two and a supplemental scan-and-recommend case was added. Each case was run once as a Claude Sonnet 5.5 (high effort) subagent inside Claude Code, reading a file copy of the plugin. The families: ecommerce returns and fees, manufacturer promotion, higher sales with lower contribution, pack and stock change, SaaS recurring metrics and retention, cancellation recipes, usage tiers, usage cutoffs, seat/package/FX bridge, app trial, offer design, renewal readiness, installed-equipment and physical-subscription economics, source coverage, plus the original industrial control and context handling. Outputs were graded against independently calculated keys. Twenty cases passed first time. Two first gave a headline figure on an assumed basis; one sentence was tightened and those two plus five regression cases passed on rerun. The other cases were not rerun after that sentence. Follow-ups covering a corrected fact, a changed metric policy, an unsupported cost and an expired approval behaved as intended.

**What it did not cover.** Plugin discovery was observed once in Claude Code with a session-only load. There is no installed-plugin test, no Claude web, Cowork or Codex run, no other model, no connected-source parity and no repeat runs. File reads in the traces are self-reported. One generated HTML report and its PDF were inspected by hand. Treat results as evidence about these cases, not a performance guarantee.

The HTML sample's actual PDF export remains unverified. Review numerical outputs and commercial recommendations against supplied evidence before action.

## License and feedback

[MIT License](LICENSE), copyright `2026 Danial Kodvavi`. Retain its notice when redistributing the plugin.

Source: [Pricing Plugin by Danial Kodvavi](https://github.com/Schadenfreunde/Pricing-plugin). For issues, supply host/version, expected behavior and synthetic/redacted inputs.
