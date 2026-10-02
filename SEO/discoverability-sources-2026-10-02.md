# Discoverability research: official sources

Researched: 2026-10-02. Scope: a public GitHub repository distributing an instruction-based pricing plugin with a documented local Codex pilot, with an optional documentation website. This note records platform guidance; it does not establish whether this repository is currently indexed or ranking.

## Documented guidance

### GitHub discovery

- GitHub's ordinary repository search searches **name, description, and topics** by default. README content is searched when a user adds `in:readme`. Put accurate product-category and platform terms in the repository description and relevant topics; README improvements alone do not cover default GitHub repository search. [GitHub repository search](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)
- Topics explicitly help people find projects by purpose and subject. They also provide topic browsing and topic search. GitHub allows up to 20 topics, using lowercase letters, numbers, and hyphens, with a maximum of 50 characters per topic. Choose a focused, truthful set rather than filling every slot. [GitHub topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- The README is commonly a visitor's first view. GitHub recommends explaining what the project does, why it is useful, how to start, where to get help, and who maintains it. GitHub automatically surfaces READMEs from `.github`, the root, or `docs`, in that priority order. [GitHub README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

### Google search and AI answers

- Google AI features depend on ordinary SEO fundamentals: indexable pages eligible for snippets, crawler access, internal links, useful text, good page experience, and structured data that agrees with visible content. Eligibility does not guarantee crawling, indexing, ranking, or inclusion in an AI answer. [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- Google's newer guide, updated July 2026, recommends unique, useful content rooted in experience and a clear technical structure. It explicitly says Google Search ignores `llms.txt`; there is no required AI-specific schema, fixed page length, tiny-chunk format, or special writing style. Generating many pages for query variations to manipulate AI responses can violate its scaled-content policy. [Google generative AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- **Current control to check on an owned docs site:** Search Console → Settings → Search generative AI. Google says the control rolled out worldwide on August 31, 2026. Inclusion is the default; child properties can inherit a parent's setting. Exclusion prevents links/content from appearing in covered generative AI features without excluding ordinary Search. This is separate from training controls. [Search generative AI control](https://support.google.com/webmasters/answer/16908024)
- **Current measurement:** Google's generative AI performance report covers impressions in AI Overviews and AI Mode, with page, country, date, and device dimensions. Google says it rolled out worldwide on August 31, 2026; a site with too few impressions may not see it. Use this newer guidance rather than assuming AI visibility is observable only in aggregate Web reports. [Generative AI performance report](https://support.google.com/webmasters/answer/16984139)

### ChatGPT and Claude web visibility

- `OAI-SearchBot` handles ChatGPT search discovery. OpenAI recommends allowing it in `robots.txt` and permitting its published IP ranges. Blocking it excludes sites from ChatGPT search answers, although navigational links may remain. `GPTBot` controls potential training collection independently. `ChatGPT-User` handles user-triggered retrieval and is not the search inclusion control. [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots)
- Anthropic separates `Claude-SearchBot` (search indexing), `Claude-User` (user-directed access), and `ClaudeBot` (potential training collection). Its documentation says blocking SearchBot or User may reduce visibility or prevent relevant retrieval. It honors `robots.txt` and does not bypass CAPTCHA restrictions. [Anthropic crawler documentation](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)

## Application to this project — recommendations, not platform guarantees

1. Make the GitHub description and topics describe **pricing strategy**, the documented **local Codex pilot** environment (with installed-host acceptance still pending), and the real plugin/skill format. Avoid terms such as “LLM pricing calculator” if the product does not calculate model-token costs.
2. Lead the README with a concrete definition, intended audience, outputs, supported platforms, installation, and one worked example. Explain boundaries and requirements plainly so a person or an assistant can identify whether it fits their problem.
3. Publish a small set of useful public documentation pages if broader non-GitHub discovery matters: installation, an end-to-end example, supported pricing methods, troubleshooting, and FAQ. Use text and meaningful headings; an FAQ helps users answer actual questions, but is not a guaranteed AI-citation tactic.
4. For an owned docs site, inspect actual crawler responses, `robots.txt`, noindex/snippet controls, CDN challenges, internal links, and Search Console indexing. Repository files cannot override crawler policy for `github.com`; implement website controls only on a domain/hosting surface under your control.
5. Measure GitHub traffic and install/adoption outcomes alongside owned-site search impressions and AI referral traffic. Repeat a consistent set of relevant search questions to observe changes, while recognizing that an assistant's answer can vary.

## Tactics not established by these sources

- No cited platform promises ranking or assistant citations from a README rewrite, schema, keyword placement, stars, or crawler allowance.
- `llms.txt` can be a convenience for systems that explicitly support it, but Google says it does not help Google visibility or rankings. The cited OpenAI and Anthropic crawler pages do not prescribe it as an inclusion requirement.
- Allowing training crawlers is not a documented prerequisite for search visibility. Search and training controls are separate.
- A plugin manifest or local skill description may affect local activation or marketplace presentation; it does not replace public, crawlable documentation for web discovery.
