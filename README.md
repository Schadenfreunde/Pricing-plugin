# Pricing Plugin: AI-assisted pricing analysis for industrial products

Pricing Plugin provides reusable AI skills for B2B pricing professionals working with industrial products and spare parts. Use it to analyze gross margin changes, compare realized prices, investigate pricing opportunities, design pricing strategies, and plan price-increase rollouts.

The plugin combines seven skills with nine curated pricing references. It checks calculations and comparison assumptions, separates observed changes from unproven business causes, and saves company context only after you validate it. Calculation and report creation use tools available in your AI host.

**Version:** `0.2.0`

[Install the plugin](#install-the-plugin) · [Set up company context](#first-step-set-up-company-context) · [Explore the skills](#pricing-skills-and-example-questions) · [See the worked example](#gross-margin-analysis-example) · [Read the FAQ](#frequently-asked-questions)

## What you can use it for

- **Gross margin analysis:** verify a reported movement and reconcile supported price, cost, and mix effects.
- **Pricing opportunity analysis:** investigate comparable price differences, commercial exceptions, and data issues before recommending actions.
- **Pricing strategy:** compare segmentation, value-based pricing considerations, price structures, and list/discount approaches for new or existing offers.
- **Price-increase planning:** evaluate conditional revenue and contribution scenarios, then plan rollout timing, responsibilities, exceptions, and monitoring.

Start with `pricing-intake` to establish your company context. Then use the skill that fits your pricing question, combining skills when useful.

## Install the plugin

Installation depends on your coding agent. Tell your agent:

```text
Fetch and follow the installation instructions from:
https://raw.githubusercontent.com/Schadenfreunde/Pricing-plugin/refs/heads/main/INSTALL.md
```

Or install [Schadenfreunde/Pricing-plugin](https://github.com/Schadenfreunde/Pricing-plugin) through your agent's Git-based plugin installer. Start a new session after installation.

## First step: set up company context

**Run `pricing-intake` before your first pricing analysis or recommendation.** It establishes the company context that the other skills reuse: your products, customers, markets, pricing policies, metric definitions, and relevant exceptions.

Tell your agent:

```text
Use pricing-intake to set up our company pricing context. Ask focused questions about our business and review the information I provide. Propose the facts to retain, then save the facts I confirm to .pricing/context.md in this working project.
```

Share a brief company overview and any relevant pricing policies or definitions. The skill asks for missing information, lets you confirm what to retain, and creates `.pricing/context.md` with the validated facts. You can update it through intake as your policies or understanding change.

Once the context is saved, attach your data and ask the appropriate pricing question. For example:

> Use pricing-analyze to analyze gross margin across these two periods. Verify the change before explaining it, reconcile the drivers supported by the data, and state what remains unknown.

## Gross margin analysis example

In the [synthetic worked example](https://github.com/Schadenfreunde/Pricing-plugin/blob/c46965c769edb82084fd43843d01e6f433f19ff2/examples/README.md), the question reports a 300 basis point margin decline. The supplied product data instead shows gross margin falling from **30.00% to 26.53%**, a **346.94 basis point decline**.

The report reconciles the movement to lower realized prices, a shift toward the higher-cost product, and a shared price/mix effect. Unit costs are unchanged. It explains what changed without inventing why prices fell: the data contains no discount records or contract evidence.

Browse the [example explanation and input data](https://github.com/Schadenfreunde/Pricing-plugin/blob/c46965c769edb82084fd43843d01e6f433f19ff2/examples/README.md), or download the [HTML margin report](https://github.com/Schadenfreunde/Pricing-plugin/blob/c46965c769edb82084fd43843d01e6f433f19ff2/examples/margin-analysis.html) and open it in your browser. GitHub's file view displays HTML source rather than a hosted report. This is a synthetic illustration, not a customer result or a performance benchmark.

## Pricing skills and example questions

| Skill name | Description | Example use |
| --- | --- | --- |
| [pricing-intake](skills/pricing-intake/SKILL.md) | Establish or update reusable company context: metric definitions, commercial policies, and scoped exceptions. Save only facts you validate, preserving existing context. | “Review these pricing policies and propose what to retain as company context.” |
| [pricing-analyze](skills/pricing-analyze/SKILL.md) | Analyze pricing and margin performance. Verify reported movements, reconcile supported price/cost/mix effects, and distinguish calculations from unproven business causes. | “Why did gross margin fall?” or “Compare price realization across these periods.” |
| [pricing-scan](skills/pricing-scan/SKILL.md) | Explore commercial data for data issues, unusual pricing, structural differences, exceptions, and opportunities. Rank opportunities by evidence confidence before considering their monetary scale. | “Find pricing opportunities in this transaction export.” |
| [pricing-recommend](skills/pricing-recommend/SKILL.md) | Choose and prioritize actions from pricing evidence. Assess how value could be captured, with profitability, feasibility, and customer risk shown separately. | “Which of these opportunities should we act on first, and why?” |
| [pricing-design](skills/pricing-design/SKILL.md) | Develop a strategy for a new offer or redesign existing pricing. Compare alternatives for segmentation, price structure, list/discount logic, and governance, with a practical validation or transition path. | “Design pricing for our new pump” or “Redesign our regional lists and discounts.” |
| [pricing-execute](skills/pricing-execute/SKILL.md) | Draft a high-level implementation plan covering eligibility, contract timing, channel constraints, responsibilities, sales readiness, communication, exceptions, and realized-price monitoring. | “Plan the rollout of our agreed price increase.” |
| [pricing-triage](skills/pricing-triage/SKILL.md) | Frame an unclear or mixed request and select the smallest useful workflow. Keep small factual questions concise and ask only material clarifying questions. | “We have lower margins and a possible price increase; where should we start?” |

## Pricing methods and knowledge base

The skills select relevant references through the [bundled pricing knowledge index](skills/knowledge/index.md).

| Reference | What it supports |
| --- | --- |
| [Metric verification](skills/knowledge/metric-verification.md) | Check metric definitions, comparable populations, periods, and calculations before explaining a reported change. |
| [Margin drivers](skills/knowledge/margin-drivers.md) | Quantify and reconcile supported price, cost, and mix effects; separate shared effects, residuals, and commercial causes. |
| [Price waterfall](skills/knowledge/price-waterfall.md) | Interpret defined list, invoice, net, and pocket price steps and the policies or exceptions governing adjustments. |
| [Value estimation](skills/knowledge/methods/value-estimation.md) | Assess differentiated customer value against a credible alternative, with uncertainty, negative effects, and overlapping benefits made explicit. |
| [Segmentation](skills/knowledge/methods/segmentation.md) | Identify economically meaningful customer/product differences and workable, enforceable pricing boundaries. |
| [Peer comparisons](skills/knowledge/methods/peer-comparisons.md) | Assess comparable price differences without treating an observed peer gap as an attainable target or guaranteed opportunity. |
| [Price realization](skills/knowledge/methods/price-realization.md) | Measure comparable realized-price changes while controlling the basket mix and distinguishing list changes from net or pocket outcomes. |
| [Discount governance](skills/knowledge/methods/discount-governance.md) | Apply scoped guidance, approval rules, and exceptions; assess deviations without assuming that every discount is leakage. |
| [Price-change economics](skills/knowledge/methods/price-change-economics.md) | Calculate conditional revenue and contribution scenarios, separate cost effects, and state the limits of unknown demand response. |

## Frequently asked questions

### What is Pricing Plugin?

Pricing Plugin is an instruction-based AI plugin for industrial and spare-parts pricing work. It bundles skills and reference notes for analysis, opportunity assessment, strategy, and execution planning. It uses the host's available calculation and artifact tools; it has no bundled calculation engine or MCP server.

### Who is it for?

It is intended for pricing professionals working with B2B industrial products and spare parts. The examples address product/customer comparisons, list and realized prices, discounts, commercial policies, and margin performance.

### What data do I need for gross margin analysis?

Start with comparable periods, sales, and cost of goods sold, together with your margin definition. Product-level quantities, realized prices, and unit costs support a more detailed price/cost/mix analysis. Aggregate totals can establish a margin movement but may not explain its drivers. The plugin should state that limit rather than invent a breakdown.

### How does it measure price realization?

It compares defined realized prices on a comparable basis. Under the project's fixed-basket convention, prior-period item quantities are held constant on both sides so that changes in volume and product mix do not masquerade as price changes. See the [price-realization method](skills/knowledge/methods/price-realization.md) for formulas, coverage rules, and limitations.

### Can it predict the revenue benefit of a price increase?

When demand response is unknown, it can calculate a conditional fixed-volume scenario using prior-period item quantities and explicit proposed-price assumptions. That scenario is not a demand forecast or a guaranteed benefit. Contribution analysis also requires supported costs; see [price-change economics](skills/knowledge/methods/price-change-economics.md).

### Does it automatically update prices or approve discounts?

The included skills analyze evidence and draft recommendations or implementation plans. The package does not include an integration that changes ERP prices, approves exceptions, or executes a rollout. Detailed account/product targets and negotiation support are outside the current scope.

### Does it keep company data local?

The plugin stores validated context in your working project's `.pricing/context.md`; it does not bundle a separate data service. How supplied files and prompts are processed depends on your AI host, connected tools, account settings, and provider terms. Local context storage alone does not establish local-only processing.

## Validation and limitations

The [synthetic evaluation fixtures](https://github.com/Schadenfreunde/Pricing-plugin/blob/c46965c769edb82084fd43843d01e6f433f19ff2/evals/README.md) cover margin analysis, company context, evidence ranking, fixed-volume economics, strategy, rollout, and routing. They define expected behavior; their presence alone does not show that an installed plugin passes them.

For development validation, use a full repository checkout and run:

```sh
python3 evals/check_package.py
```

The checker and evaluation fixtures are not included in the runtime ZIP. This checks metadata, file presence, and runtime reference closure. It does not test model behavior. Evaluation inputs are in `evals/cases/`; independent evaluator keys are in `evals/expected/` and must stay out of an evaluated assistant's workspace. Keep trial outputs and context separate between runs.

The sample HTML report illustrates presentation and arithmetic for one synthetic case. PDF export and page-by-page PDF inspection remain unverified. Numerical outputs and business recommendations depend on the evidence supplied and require review before commercial action.

## License

This project is licensed under the [MIT License](LICENSE). Include the copyright and license notice when redistributing copies or substantial portions of the plugin.

## Project and feedback

Source and project updates: [Schadenfreunde/Pricing-plugin](https://github.com/Schadenfreunde/Pricing-plugin). For a reproducible issue, describe the skill, host/version, expected behavior, and a synthetic or redacted input rather than confidential customer data.
