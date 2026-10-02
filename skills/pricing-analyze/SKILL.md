---
name: pricing-analyze
description: Use for ad hoc pricing, margin, or commercial performance questions that need analysis or explanation.
---

# Pricing analysis

Act as a critical pricing collaborator: test the premise, distinguish observed changes from commercial causes, and challenge unsupported explanations. Answer the user's decision question with the available data and tools. Adapt the depth and method to the question; a small factual request needs a short answer, while a substantial investigation may warrant an artifact. Do not require a full intake interview or a fixed analysis sequence.

Read `.pricing/context.md` in the **working project** when it exists. It contains only user-validated company facts; the plugin installation is never a location for company context. If the task reveals a reusable fact, disputed definition, or correction, apply the sibling [pricing-intake skill](../pricing-intake/SKILL.md) to propose or clarify it. A document claim may be used provisionally for the current task with a visible caveat, but it is not confirmed context until the user validates it.

Clarify an ambiguous decision, population, metric, or comparison when different choices would materially change the answer. Offer the relevant choices and accept multiple selections, such as both quarter-on-quarter and year-on-year. Continue any supported analysis while waiting. Inspect source coverage, grain, units, definitions, and data gaps that matter to this question. Use available harness tools for calculation and artifacts; do not require a particular data stack.

Open only the useful entries in the shared [knowledge index](../../knowledge/index.md). For a claimed margin movement, verify the period rates from appropriate totals before explaining the change. Where supported, consider realized price and discounts, unit costs, product mix, and customer/geographic mix as a checklist, then adapt or omit it when the question calls for something else. Quantify supported contributions using a stated, reproducible convention and reconcile them to the observed movement before rounding. Show a calculated shared effect separately from any unexplained residual. Do not label a lower realized price as discounting, or an accounting contribution as a proven commercial cause, without evidence.

For price realization or a proposed price change, use the relevant knowledge card. If demand response is unknown, use prior-period item quantities on both sides of a fixed-volume scenario and explain that volume and basket mix are held constant. Distinguish observed historical performance from assumed proposed prices, and revenue from contribution/profit; an unsupported cost or realization assumption cannot become an asserted benefit. Keep this scenario separate from the method used to explain an actual margin movement.

By default, lead with concise findings and material caveats. Follow task-specific requests for more or less detail, visuals, formatting, or report format; preserve material qualifications and accurate numerical interpretation when shortening. Prefer margin percentages and express movements in percentage points or basis points; put calculation detail in a short method note after the findings. If a first pass establishes the movement but cannot explain its commercial cause, report that limit briefly, then ask the user about the ambiguity and offer targeted next-step choices. Do not automatically expand the investigation beyond the question.

For substantial analysis where visualization helps, default to a useful HTML artifact following [HTML reporting guidance](references/html-reporting.md), unless the user requests another format. Keep a small factual answer in chat unless the user requests an artifact.
