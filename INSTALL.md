# Install Pricing Plugin

Install the complete plugin through the host's supported mechanism. The [README](README.md#install-the-plugin) provides Claude upload instructions, Claude Code catalog commands and a Codex local-setup prompt.

Repository:

```text
https://github.com/Schadenfreunde/Pricing-plugin
```

1. Inspect the host's supported installation mechanism. The portable manifest is root `plugin.json`, name `pricing-plugin`. Claude metadata is already supplied in `.claude-plugin/plugin.json`; `.claude-plugin/marketplace.json` exposes the complete plugin for Claude Code. Use supplied local files when working from an extracted ZIP.
2. Preserve the `skills/` layout and root MIT license. Keep all seven skills, shared `skills/knowledge/` and `skills/references/` available together; preserve existing plugins/settings. Do not upload individual skill folders or rewrite the workflows and relative references.
3. For Claude web/desktop/Cowork, explain the complete ZIP upload through Customize → Plugins and the code-execution requirement for Claude chat. No conversion or MCP server is required. For Claude Code, add the supplied catalog from the repository or a local folder and install `pricing-plugin@danial-kodvavi-pricing`. For Codex desktop, register the complete package in a supported local plugin catalog and explain installation from the Plugins Directory. Preparing files or attaching them to a chat is not confirmation of installation.
4. After installation, verify discovery of all seven skills and loading of shared knowledge/reporting references in the installed copy. Report any host-specific requirement or missing capability instead of claiming unverified success.
5. Start a fresh session if required. Intake is recommended onboarding; clear pricing tasks can start directly. ZIP-based installations need a fresh download and repeated setup to update; preserve the working project's company context.

Company context belongs in the working project's `.pricing/context.md`. Intake saves validated facts and can reuse an applicable confirmed context file supplied from another project.

## Build a Claude upload ZIP

Maintainers can run `python3 -B scripts/build_plugin_zip.py` from the full repository. It validates the source and writes `output/pricing-plugin-claude.zip`, containing the manifests, license and complete skills/shared files in one `pricing-plugin/` folder. Local company context, evaluation fixtures and installation documentation are excluded. The repository README remains the installation guide. Use `--output PATH` for another output location.
