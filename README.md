# Pricing Plugin

A plugin for pricing professionals working with industrial products and spare parts. Version `0.2.0` provides seven directly usable workflows. Start with the user's decision; there is no required sequence or full intake interview.

| Skill | Purpose |
| --- | --- |
| [pricing-intake](skills/pricing-intake/SKILL.md) | Establish or update reusable company facts, saving only what the user validates. |
| [pricing-analyze](skills/pricing-analyze/SKILL.md) | Answer pricing and margin questions; verify a reported change and separate calculated effects from unproven causes. |
| [pricing-scan](skills/pricing-scan/SKILL.md) | Find data issues, unusual pricing and opportunities, ordered by evidence confidence. |
| [pricing-recommend](skills/pricing-recommend/SKILL.md) | Choose actions from evidence, with profitability, feasibility and risk shown separately. |
| [pricing-design](skills/pricing-design/SKILL.md) | Develop a new strategy or redesign pricing structures and policies. |
| [pricing-execute](skills/pricing-execute/SKILL.md) | Draft a high-level rollout plan covering eligibility, timing, responsibilities and measurement. |
| [pricing-triage](skills/pricing-triage/SKILL.md) | Frame an unclear or mixed request and choose the smallest useful workflow. |

The [knowledge index](knowledge/index.md) selects focused guidance on metric verification, margin drivers, price waterfalls, value, segmentation, peers, realization, discount governance and price-change economics. When demand response is unknown, price scenarios hold prior-period item quantities and basket mix constant on both sides and state their assumptions. Conditional revenue or contribution changes are distinct from forecasts and guaranteed benefits. Execution starts at a high level; detailed account/product targets and negotiation support are deferred.

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
