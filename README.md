# Pricing Plugin

A plugin for pricing professionals working with industrial products and spare parts. Version `0.2.0` includes seven skills and nine pricing knowledge references. It expands the original intake and analysis skills with opportunity scanning, recommendations, strategy design, execution planning, and lightweight triage.

## Skills and uses

Start with your pricing question. Each skill can be used directly, and skills can work together when the task needs it. There is no required sequence or full intake interview.

| Skill name | Description | Example use |
| --- | --- | --- |
| [pricing-intake](skills/pricing-intake/SKILL.md) | Establish or update reusable company context: metric definitions, commercial policies, and scoped exceptions. Save only facts you validate, preserving existing context. | “Review these pricing policies and propose what to retain as company context.” |
| [pricing-analyze](skills/pricing-analyze/SKILL.md) | Analyze pricing and margin performance. Verify reported movements, reconcile supported price/cost/mix effects, and distinguish calculations from unproven business causes. | “Why did gross margin fall?” or “Compare price realization across these periods.” |
| [pricing-scan](skills/pricing-scan/SKILL.md) | Explore commercial data for data issues, unusual pricing, structural differences, exceptions, and opportunities. Rank opportunities by evidence confidence before considering their monetary scale. | “Find pricing opportunities in this transaction export.” |
| [pricing-recommend](skills/pricing-recommend/SKILL.md) | Choose and prioritize actions from pricing evidence. Assess how value could be captured, with profitability, feasibility, and customer risk shown separately. | “Which of these opportunities should we act on first, and why?” |
| [pricing-design](skills/pricing-design/SKILL.md) | Develop a strategy for a new offer or redesign existing pricing. Compare alternatives for segmentation, price structure, list/discount logic, and governance, with a practical validation or transition path. | “Design pricing for our new pump” or “Redesign our regional lists and discounts.” |
| [pricing-execute](skills/pricing-execute/SKILL.md) | Draft a high-level implementation plan covering eligibility, contract timing, channel constraints, responsibilities, sales readiness, communication, exceptions, and realized-price monitoring. | “Plan the rollout of our agreed price increase.” |
| [pricing-triage](skills/pricing-triage/SKILL.md) | Frame an unclear or mixed request and select the smallest useful workflow. Keep small factual questions concise and ask only material clarifying questions. | “We have lower margins and a possible price increase; where should we start?” |

## Pricing knowledge base

The skills select relevant references through the [knowledge index](knowledge/index.md). Version `0.2.0` adds six methods to the original metric-verification, margin-driver, and price-waterfall guidance.

| Reference | What it supports |
| --- | --- |
| [Metric verification](knowledge/metric-verification.md) | Check metric definitions, comparable populations, periods, and calculations before explaining a reported change. |
| [Margin drivers](knowledge/margin-drivers.md) | Quantify and reconcile supported price, cost, and mix effects; separate shared effects, residuals, and commercial causes. |
| [Price waterfall](knowledge/price-waterfall.md) | Interpret defined list, invoice, net, and pocket price steps and the policies or exceptions governing adjustments. |
| [Value estimation](knowledge/methods/value-estimation.md) | Assess differentiated customer value against a credible alternative, with uncertainty, negative effects, and overlapping benefits made explicit. |
| [Segmentation](knowledge/methods/segmentation.md) | Identify economically meaningful customer/product differences and workable, enforceable pricing boundaries. |
| [Peer comparisons](knowledge/methods/peer-comparisons.md) | Assess comparable price differences without treating an observed peer gap as an attainable target or guaranteed opportunity. |
| [Price realization](knowledge/methods/price-realization.md) | Measure comparable realized-price changes while controlling the basket mix and distinguishing list changes from net or pocket outcomes. |
| [Discount governance](knowledge/methods/discount-governance.md) | Apply scoped guidance, approval rules, and exceptions; assess deviations without assuming that every discount is leakage. |
| [Price-change economics](knowledge/methods/price-change-economics.md) | Calculate conditional revenue and contribution scenarios, separate cost effects, and state the limits of unknown demand response. |

When demand response is unknown, price scenarios hold prior-period item quantities and basket mix constant on both sides and state their assumptions. Conditional revenue or contribution changes are distinct from forecasts and guaranteed benefits. Execution starts at a high level; detailed account/product targets and negotiation support are deferred.

The skills use the host's available tools for calculation and report creation. There is no bundled calculation script or MCP server. A company's validated facts belong in `.pricing/context.md` in its **working project**, outside the installed plugin.

## Runtime package

The 21 runtime files are:

- `plugin.json`
- `README.md`
- `skills/pricing-intake/SKILL.md`
- `skills/pricing-intake/references/context-outline.md`
- `skills/pricing-analyze/SKILL.md`
- `skills/pricing-analyze/references/html-reporting.md`
- `skills/pricing-scan/SKILL.md`
- `skills/pricing-recommend/SKILL.md`
- `skills/pricing-design/SKILL.md`
- `skills/pricing-execute/SKILL.md`
- `skills/pricing-triage/SKILL.md`
- `knowledge/index.md`
- `knowledge/metric-verification.md`
- `knowledge/margin-drivers.md`
- `knowledge/price-waterfall.md`
- `knowledge/methods/value-estimation.md`
- `knowledge/methods/segmentation.md`
- `knowledge/methods/peer-comparisons.md`
- `knowledge/methods/price-realization.md`
- `knowledge/methods/discount-governance.md`
- `knowledge/methods/price-change-economics.md`

Keep their relative directory structure when packaging the plugin. Evaluation fixtures and examples in this repository are separate from the runtime package.

## Local Codex pilot

The [official plugin packaging guide](https://developers.openai.com/plugins/build/plugins) describes installing a local plugin through a repository marketplace. Place the runtime package at `plugins/pricing-plugin/` in a chosen repository, then add this `.agents/plugins/marketplace.json` file in that repository. The source path is relative to the repository root.

```json
{
  "name": "pricing-local",
  "plugins": [
    {
      "name": "pricing-plugin",
      "source": { "source": "local", "path": "./plugins/pricing-plugin" },
      "policy": { "installation": "AVAILABLE", "authentication": "ON_INSTALL" },
      "category": "Productivity"
    }
  ]
}
```

Restart the ChatGPT desktop app, select the marketplace in the Plugins Directory, install the plugin, and test all seven skills in a fresh supported local session. Installed discovery and relative-reference loading for the expanded version require fresh host acceptance; repository checks do not establish installed behavior.

The [synthetic evaluation cases](evals/README.md) cover margin analysis, company context, evidence ranking, fixed-volume economics, strategy, rollout and routing. Their model-visible inputs are in `evals/cases/`; independent evaluator keys are in `evals/expected/` and must stay out of the evaluated assistant's workspace. Run the development-only package check with `python3 evals/check_package.py`; it validates metadata, file presence and runtime reference closure, not model behavior. The [sample HTML analysis](examples/margin-analysis.html) shows a reviewed presentation; PDF export and page-by-page PDF inspection remain unverified.
