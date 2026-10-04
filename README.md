# Pricing Plugin: AI-assisted pricing analysis for industrial products

Pricing Plugin provides seven connected AI skills for B2B industrial-products and spare-parts pricing: analyze margins and realized prices, discover opportunities, choose actions, design structures and plan rollouts.

The skills share curated pricing knowledge, check comparison assumptions and retain company facts only after validation. Calculation and artifacts use the tools available in your AI host.

**Version:** `0.2.0`

[Install](#install-the-plugin) · [Company context](#recommended-first-step-company-context) · [Skills](#pricing-skills-and-example-questions) · [Worked example](#gross-margin-analysis-example) · [FAQ](#frequently-asked-questions)

## Install the plugin

Install the complete plugin so all seven skills and shared references are available together. Tell your coding agent:

```text
Fetch and follow the installation instructions from:
https://raw.githubusercontent.com/Schadenfreunde/Pricing-plugin/refs/heads/main/INSTALL.md
```

Or use your agent's Git-based plugin installer for [Schadenfreunde/Pricing-plugin](https://github.com/Schadenfreunde/Pricing-plugin). Start a fresh session if required. Skills load only the instructions and methods needed for the task.

## Recommended first step: company context

Use `pricing-intake` to establish reusable context, or start directly with your pricing question when enough information is available.

```text
Use pricing-intake to review our company pricing context. Propose relevant facts and save only those I confirm to .pricing/context.md in this working project.
```

In a new directory, you can supply a `context.md` from another project. Intake checks its company/scope and applicability, reuses previously validated facts and clarifies changes. Otherwise share a brief overview and relevant definitions or policies; no complete intake interview is required.

Context can retain validated price/metric definitions, calendar, units/currencies, reusable data mappings, policies and scoped exceptions. For data-backed intake, confirm which revenue, COGS and other fields serve the requested analysis, with their accounting, currency and unit basis. Each new dataset still needs numeric-consistency, coverage and like-for-like comparison checks. A material unresolved basis choice pauses the affected calculation for clarification while independently valid work continues. Analysis findings and proposals stay with the answer/report; a separate handoff brief is saved only when requested.

Attach data and ask the relevant skill, for example:

> Use pricing-analyze to explain the gross margin movement. Verify the change, reconcile supported drivers and state what remains unknown.

## Gross margin analysis example

The [synthetic worked example](examples/README.md) reports a 300 basis point decline. Its data instead shows margin falling from **30.00% to 26.53%**, a **346.94 basis point decline**.

The [HTML report](examples/margin-analysis.html) reconciles realized-price, product-mix and shared effects with unchanged unit costs. It identifies accounting changes without inventing why prices fell. Download/open the HTML in a browser; GitHub displays source. This illustration establishes neither customer results nor installed-host performance.

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

## Frequently asked questions

### What data supports gross margin analysis?

Comparable periods, sales, COGS and the margin definition establish the movement. Matched item quantities, realized prices and unit costs support driver analysis. Aggregate totals alone usually cannot identify price/cost/mix effects.

### How are price measurement and price scenarios different?

Historical realization compares observed prices using the same prior-period item quantities, regardless of known demand response. This controls basket mix. For proposed prices with unknown future response, those quantities create a conditional fixed-volume scenario. It is not a demand forecast or guaranteed benefit; contribution also needs relevant costs.

### Does the plugin update prices or approve discounts?

The skills draft analyses, recommendations and plans. System changes and communications need explicit authorization and suitable tools. Detailed account/product targets and negotiation support remain outside this version.

### Does company data stay local?

Validated context is saved in the working project's `.pricing/context.md`. Processing of prompts/files depends on the AI host, connected tools, settings and provider terms; local context storage does not establish local-only processing. The plugin has no separate data service, calculation engine or MCP server.

## Validation and limitations

From a full checkout, run:

```sh
python3 -B evals/check_package.py
python3 -B evals/test_skill_packaging.py
```

These development checks validate metadata, the shared inventory, references and documentation links. Behavioral and installed-host acceptance remain pending. The [legacy synthetic fixtures](evals/README.md) retain historical/arithmetic context; a new end-to-end suite with fresh data and cases is planned. Keep evaluator keys and earlier outputs out of evaluated workspaces.

The HTML sample's actual PDF export remains unverified. Review numerical outputs and commercial recommendations against supplied evidence before action.

## License and feedback

[MIT License](LICENSE), copyright `2026 Schadenfreunde`. Retain its notice when redistributing the plugin.

Source: [Schadenfreunde/Pricing-plugin](https://github.com/Schadenfreunde/Pricing-plugin). For issues, supply host/version, expected behavior and synthetic/redacted inputs.
