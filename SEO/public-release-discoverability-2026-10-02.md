# Pricing Plugin: public-release discoverability

Updated packaging: 2026-10-02. Skills now bundle their own knowledge and license notices; the current runtime contains 94 files, including the maintained `skills/knowledge/` directory. README installation uses an agent-neutral Git-based plugin workflow without local-pilot setup. Earlier inventory counts below record historical checks.

Reviewed: 2026-10-02. Scope: pre-public-release repository content, reviewed on `codex/core-pricing-skills` and prepared for delivery directly on `main`. The repository is private, as confirmed by its owner. This is a content and release-readiness review, not an assessment of live indexing, rankings, traffic, or installed-host performance.

## Findings and content changes

| Finding | Change prepared | Why it matters |
| --- | --- | --- |
| The generic “Pricing Plugin” title did not identify the type of pricing work. | README title and opening identify AI-assisted B2B pricing analysis for industrial products and spare parts. | Visitors can distinguish the project from ecommerce pricing-table plugins or model-token pricing tools. |
| Package inventory appeared before installation and the practical demonstration. | README brings use cases, the worked example, and local installation forward; the inventory remains available in an expandable section. | A new visitor can assess usefulness and find the next step quickly. |
| The HTML sample required reading source or downloading before seeing its result. | `examples/README.md` now explains inputs, verified results, reconciliation, and limitations in text; HTML title and description identify the example. | The demonstration is understandable in GitHub's normal Markdown view. The HTML metadata becomes useful if the report is later hosted. |
| Common capability questions were scattered across implementation prose. | README FAQ covers data requirements, price realization, scenarios, execution boundaries, privacy, and host status. | Answers help readers determine fit without interpreting skill instructions. This is a usability recommendation, not a special AI-ranking requirement. |
| The manifest lacked repository identification and discovery keywords. | Added the canonical repository URL and eight supported subject keywords; clarified the description. | Package readers receive consistent identity and scope. Manifest metadata does not replace GitHub About settings or public web content. |

The discoverability pass preserved the skills, analytical conventions, version number, and original 21-file runtime inventory. The subsequent MIT license addition increases the runtime inventory to 22 files, including `LICENSE`.

GitHub recommends covering purpose, value, getting started, help, and maintenance in the README. [GitHub README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

## Before making the repository public

1. **Keep the intended release content on the default branch.** Remote verification confirmed that [pull request #1](https://github.com/Schadenfreunde/Pricing-plugin/pull/1) merged the seven-skill version into `main` on 2026-10-02 at 15:07:06 UTC (`ec63568`). The earlier observation used a stale local reference. This content pass supplies the README, example, and metadata improvements for the same default branch; its delivery is recorded in Git history.
2. **Complete fresh installation acceptance.** Verify all seven skills appear and their references load in a supported host. Replace the README's pending status only after documenting that evidence. Do not add “works with Claude” or other host claims without checking them.
3. **License selected: MIT.** The user selected MIT on 2026-10-02. The root `LICENSE` carries the copyright notice `2026 Schadenfreunde`, the manifest declares `MIT`, and runtime packaging includes the notice. Retain the license when distributing the package.
4. **Set GitHub About description and topics.** Use the copy below. These fields are GitHub settings; adding keywords to `plugin.json` does not update them.
5. **Create a versioned release once acceptance is complete.** Include the self-contained runtime package, concise release notes, exact installation requirements, and known limitations. Keep the release version consistent with `plugin.json`.
6. **Apply the selected social preview when GitHub permits upload.** The user selected A2 (price waterfall) with the exact title “B2B Pricing Companion” and no subtitle. The prepared [social-preview PNG](../assets/social-preview.png) is 1280 × 640 pixels and 971,178 bytes, below GitHub's 1 MB limit. It is illustrative artwork, not a measured report. GitHub permits a first preview upload to a public repository; a private repository must already have had an image uploaded. Upload remains pending, and visibility remains private. [GitHub social-preview guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)

### Suggested GitHub About description

> AI-assisted B2B pricing analysis and strategy for industrial products and spare parts: gross margin, price realization, opportunity assessment, and price-increase planning. Local Codex pilot.

### Suggested GitHub topics

```text
pricing
pricing-strategy
industrial-pricing
spare-parts
b2b
gross-margin
price-realization
agent-skills
codex-plugin
```

Use `codex-plugin` with the visible pilot/acceptance caveat; it identifies the intended package environment, not proof of installation success. Add other platform topics only after verifying support. Leave the About website field empty until a real documentation site exists, then link its canonical home page.

GitHub's default repository search covers name, description, and topics. README text is included with `in:readme`. Topics also enable browsing by subject. [GitHub repository search](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories), [GitHub topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)

## Next investment: a small public documentation site

For discovery beyond GitHub, publish useful documentation on a hosting surface you control. Keep a single canonical URL for each page; link the site from the repository and link installation/source back to GitHub. A static site is sufficient for these pages. The current repository has no configured documentation site.

Start with these distinct reader needs rather than generating pages for every keyword variation:

| Page | Reader's question | Content to use |
| --- | --- | --- |
| Overview | What does this plugin do, and who is it for? | README purpose, capabilities, supported host status, and next step. |
| Installation | How do I install it and verify it works? | Tested installation procedure, release download, and verified troubleshooting. |
| Gross margin worked example | How does it explain price and mix effects? | Existing synthetic inputs, arithmetic, report, and evidence limitations. |
| Price-realization worked example | How do I compare prices without confusing mix changes? | A reviewed walkthrough of case 005 and the fixed-basket method, labeled as a scenario. |
| Methods and limitations | Which methods are used, and when do they apply? | Concise explanations linked to curated method cards and sources; clearly identify project conventions. |

For hosted HTML, provide descriptive page titles, useful meta descriptions, readable text, mobile layouts, and internal links. If you add structured data, it must describe visible, accurate content; do not invent reviews, ratings, prices, or compatibility. GitHub-rendered Markdown does not give this repository control of `github.com` page metadata or crawler policy. [Google SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), [Google AI features guidance](https://developers.google.com/search/docs/appearance/ai-features)

For answer-engine discovery on an owned site, check that public pages load without login or bot challenges, and allow relevant search crawlers through both `robots.txt` and the hosting/CDN layer. OpenAI distinguishes `OAI-SearchBot` from the training crawler `GPTBot`; training access is a separate choice. A `robots.txt` file in this repository would not control crawling of GitHub's pages. [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots)

Google does not require special AEO markup or a particular writing style, and explicitly says `llms.txt` does not improve its visibility or rankings. Prioritize original worked examples, accurate claims, and accessible documentation. [Google generative AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)

## After release: distribution and measurement

- Publish one substantive walkthrough in a relevant pricing or industrial community, linking directly to installation and the example. Use synthetic data and identify the demonstrated limits.
- Seek listings in relevant skill/plugin directories only when their package requirements and host compatibility are satisfied. Public GitHub availability alone does not establish marketplace listing.
- Track repository visitors, clones, reported successful installations, and useful issue reports. For a documentation site, monitor indexing and search performance in Search Console, plus AI referrals where available. Keep a consistent small set of test questions; individual assistant answers vary and are not a reliable benchmark on their own.

Candidate questions for those spot checks are “AI pricing analysis for industrial spare parts,” “Codex pricing plugin,” and “gross margin price mix analysis example.” These are audience hypotheses, not measured high-volume keywords. No ranking or AI-citation guarantee is implied.

For current crawler and measurement details, see the [primary-source research note](discoverability-sources-2026-10-02.md). GitHub metadata settings, release creation, site deployment, and external promotion remain separate release actions; this content pass has not performed them.

## Verification of this content pass

- Package checker passed: seven skills, version `0.2.0`, 21 runtime files, and 19 runtime Markdown reference closures.
- All 35 local Markdown links and heading anchors in the four edited/new Markdown documents resolved.
- Manifest additions use fields/types supported by the published schema; README marketplace JSON parsed successfully. No installed-host metadata acceptance is claimed.
- Independently recomputed the synthetic example's margin rates and all four displayed bridge values from its CSV; the unrounded contributions reconcile exactly.
- HTML description parsed successfully; the report body is unchanged. `git diff --check` passed.

These are local content/package checks, not a live crawl, ranking assessment, hosted-page performance test, or behavioral acceptance result.

## License update

2026-10-02: Added the user-selected MIT license, manifest declaration, README license link, and runtime inclusion. Updated the package checker and current inventory documentation from 21 to 22 files. Installation acceptance remains deferred.
