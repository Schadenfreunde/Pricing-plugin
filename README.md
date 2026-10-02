# Pricing Plugin: AI-assisted pricing analysis for industrial products

Pricing Plugin provides reusable AI skills for B2B pricing professionals working with industrial products and spare parts. Use it to analyze gross margin changes, compare realized prices, investigate pricing opportunities, design pricing strategies, and plan price-increase rollouts.

The plugin combines seven skills with nine curated pricing references. It checks calculations and comparison assumptions, separates observed changes from unproven business causes, and saves company context only after you validate it. Calculation and report creation use tools available in your AI host.

**Version:** `0.2.0` · **Installation path:** local Codex pilot in the ChatGPT desktop app · **Acceptance status:** fresh installed-host validation of this version is pending.

[Install the local pilot](#install-the-local-codex-pilot) · [Explore the skills](#pricing-skills-and-example-questions) · [See the worked example](#gross-margin-analysis-example) · [Read the FAQ](#frequently-asked-questions)

## What you can use it for

- **Gross margin analysis:** verify a reported movement and reconcile supported price, cost, and mix effects.
- **Pricing opportunity analysis:** investigate comparable price differences, commercial exceptions, and data issues before recommending actions.
- **Pricing strategy:** compare segmentation, value-based pricing considerations, price structures, and list/discount approaches for new or existing offers.
- **Price-increase planning:** evaluate conditional revenue and contribution scenarios, then plan rollout timing, responsibilities, exceptions, and monitoring.

Start with your pricing question. Use a skill directly or combine skills when needed; there is no required sequence or full intake interview.

## Gross margin analysis example

In the [synthetic worked example](https://github.com/Schadenfreunde/Pricing-plugin/blob/c46965c769edb82084fd43843d01e6f433f19ff2/examples/README.md), the question reports a 300 basis point margin decline. The supplied product data instead shows gross margin falling from **30.00% to 26.53%**, a **346.94 basis point decline**.

The report reconciles the movement to lower realized prices, a shift toward the higher-cost product, and a shared price/mix effect. Unit costs are unchanged. It explains what changed without inventing why prices fell: the data contains no discount records or contract evidence.

Browse the [example explanation and input data](https://github.com/Schadenfreunde/Pricing-plugin/blob/c46965c769edb82084fd43843d01e6f433f19ff2/examples/README.md), or download the [HTML margin report](https://github.com/Schadenfreunde/Pricing-plugin/blob/c46965c769edb82084fd43843d01e6f433f19ff2/examples/margin-analysis.html) and open it in your browser. GitHub's file view displays HTML source rather than a hosted report. This is a synthetic illustration, not a customer result or a performance benchmark.

## Install the local Codex pilot

This repository provides a local pilot setup, following the [official OpenAI plugin packaging guide](https://developers.openai.com/plugins/build/plugins). Public directory availability and compatibility with other AI hosts have not been established for this package.

1. If you have the `pricing-plugin-v0.2.0.zip` release asset, extract it to obtain a `pricing-plugin/` folder, then place that folder at `plugins/pricing-plugin/` in your working repository. Alternatively, copy the files listed in [Runtime package](#runtime-package) into that location. Preserve their relative directory structure.
2. Add the following marketplace entry to `.agents/plugins/marketplace.json` in that working repository. If the file already exists, merge the entry into its `plugins` array. The source path is relative to the working repository root.

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

3. Restart the ChatGPT desktop app. Open the Plugins Directory, select the `pricing-local` marketplace, and install `pricing-plugin`.
4. Test all seven skills and their reference loading in a fresh supported local session. Repository checks do not establish installed behavior.

For a first question, supply your own transaction data and ask:

> Analyze gross margin across these two periods. Verify the change before explaining it, reconcile the drivers supported by the data, and state what remains unknown.

Keep company facts in `.pricing/context.md` in your **working project**, outside the installed plugin. The intake skill proposes context and saves only the facts you validate. Keep evaluation answer keys out of the working project used for a trial.

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

The skills select relevant references through the [pricing knowledge index](knowledge/index.md).

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

## Frequently asked questions

### What is Pricing Plugin?

Pricing Plugin is an instruction-based AI plugin for industrial and spare-parts pricing work. It bundles skills and reference notes for analysis, opportunity assessment, strategy, and execution planning. It uses the host's available calculation and artifact tools; it has no bundled calculation engine or MCP server.

### Who is it for?

It is intended for pricing professionals working with B2B industrial products and spare parts. The examples address product/customer comparisons, list and realized prices, discounts, commercial policies, and margin performance.

### What data do I need for gross margin analysis?

Start with comparable periods, sales, and cost of goods sold, together with your margin definition. Product-level quantities, realized prices, and unit costs support a more detailed price/cost/mix analysis. Aggregate totals can establish a margin movement but may not explain its drivers. The plugin should state that limit rather than invent a breakdown.

### How does it measure price realization?

It compares defined realized prices on a comparable basis. Under the project's fixed-basket convention, prior-period item quantities are held constant on both sides so that changes in volume and product mix do not masquerade as price changes. See the [price-realization method](knowledge/methods/price-realization.md) for formulas, coverage rules, and limitations.

### Can it predict the revenue benefit of a price increase?

When demand response is unknown, it can calculate a conditional fixed-volume scenario using prior-period item quantities and explicit proposed-price assumptions. That scenario is not a demand forecast or a guaranteed benefit. Contribution analysis also requires supported costs; see [price-change economics](knowledge/methods/price-change-economics.md).

### Does it automatically update prices or approve discounts?

The included skills analyze evidence and draft recommendations or implementation plans. The package does not include an integration that changes ERP prices, approves exceptions, or executes a rollout. Detailed account/product targets and negotiation support are outside the current scope.

### Does it keep company data local?

The plugin stores validated context in your working project's `.pricing/context.md`; it does not bundle a separate data service. How supplied files and prompts are processed depends on your AI host, connected tools, account settings, and provider terms. Local context storage alone does not establish local-only processing.

### Which AI hosts are supported?

The documented setup is a local Codex pilot in the ChatGPT desktop app. Fresh installation, automatic skill discovery, and reference loading for version `0.2.0` still require host acceptance. This repository does not claim tested compatibility with other hosts.

## Validation and limitations

The [synthetic evaluation fixtures](https://github.com/Schadenfreunde/Pricing-plugin/blob/c46965c769edb82084fd43843d01e6f433f19ff2/evals/README.md) cover margin analysis, company context, evidence ranking, fixed-volume economics, strategy, rollout, and routing. They define expected behavior; their presence alone does not show that an installed plugin passes them.

For development validation, use a full repository checkout and run:

```sh
python3 evals/check_package.py
```

The checker and evaluation fixtures are not included in the runtime ZIP. This checks metadata, file presence, and runtime reference closure. It does not test model behavior. Evaluation inputs are in `evals/cases/`; independent evaluator keys are in `evals/expected/` and must stay out of an evaluated assistant's workspace. Keep trial outputs and context separate between runs.

The sample HTML report illustrates presentation and arithmetic for one synthetic case. PDF export and page-by-page PDF inspection remain unverified. Numerical outputs and business recommendations depend on the evidence supplied and require review before commercial action.

## Runtime package

The runtime contains 22 files. Copy only these files for the pilot; examples and evaluation fixtures are separate repository resources.

<details>
<summary>Show the 22 runtime files</summary>

- `plugin.json`
- `LICENSE`
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

</details>

Keep their relative directory structure when packaging the plugin.

## License

This project is licensed under the [MIT License](LICENSE). Include the copyright and license notice when redistributing copies or substantial portions of the plugin.

## Project and feedback

Source and project updates: [Schadenfreunde/Pricing-plugin](https://github.com/Schadenfreunde/Pricing-plugin). For a reproducible issue, describe the skill, host/version, expected behavior, and a synthetic or redacted input rather than confidential customer data.
