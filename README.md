# Pricing Plugin

A pilot plugin for pricing professionals working with industrial products and spare parts. `pricing-intake` helps establish reusable company facts, saving only what the user validates. `pricing-analyze` answers ad hoc pricing and margin questions: it checks a reported change before explaining it, separates calculated effects from unproven business causes, and adapts the depth of its answer to the user's request.

The skills use the host's available tools for calculation and report creation. There is no bundled calculation script or MCP server. A company's validated facts belong in `.pricing/context.md` in its **working project**, outside the installed plugin.

## Runtime package

The ten runtime files are:

- `plugin.json`
- `README.md`
- `skills/pricing-intake/SKILL.md`
- `skills/pricing-intake/references/context-outline.md`
- `skills/pricing-analyze/SKILL.md`
- `skills/pricing-analyze/references/html-reporting.md`
- `knowledge/index.md`
- `knowledge/metric-verification.md`
- `knowledge/margin-drivers.md`
- `knowledge/price-waterfall.md`

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

Restart the ChatGPT desktop app, select the marketplace in the Plugins Directory, install the plugin, and test both skills in a fresh supported local session. Installed skill discovery and loading of relative references have not yet been verified for this pilot.

The [synthetic evaluation cases](evals/README.md) document checks for margin analysis and company-context handling. Their model-visible inputs are in `evals/cases/`; independent evaluator keys are in `evals/expected/` and must stay out of the evaluated assistant's workspace. The [sample HTML analysis](examples/margin-analysis.html) shows a reviewed presentation; PDF export and page-by-page PDF inspection remain unverified.
