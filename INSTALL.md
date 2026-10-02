# Install Pricing Plugin

Use the coding agent's native Git-based plugin installation workflow for this repository:

```text
https://github.com/Schadenfreunde/Pricing-plugin
```

For an agent carrying out installation:

1. Inspect the repository and the agent's supported plugin installation mechanism. The plugin manifest is `plugin.json`; its name is `pricing-plugin`.
2. Install the repository as a plugin using that mechanism. Include the complete `skills/` folder and the MIT license. Preserve existing plugins and settings.
3. Enable the seven pricing skills. Confirm that their instructions and bundled references are available. If the agent needs a different manifest format, report the specific requirement rather than claiming installation succeeded.
4. Start a fresh session if the agent requires it. Begin with `pricing-intake` to establish company context, then use the other skills for the user's pricing question.

Company context belongs in `.pricing/context.md` in the user's working project. Intake proposes the facts to retain and saves only facts the user validates.
