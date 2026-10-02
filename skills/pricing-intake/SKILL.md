---
name: pricing-intake
description: Use when establishing or updating a company's pricing context from a task, documents, or user corrections.
---

# Pricing intake

Build company understanding incrementally around the current question. Read the available task material and the working project's `.pricing/context.md` if it exists. That file belongs to the user's project, independent of this skill's installation. Treat its existing entries as confirmed context unless the user corrects or disputes them. Never create an empty outline or require a full intake interview. Consult [the optional context outline](references/context-outline.md) only when it helps identify a relevant gap; the link is relative to this SKILL.md.

Extract only reusable company facts relevant to the task. Summarize proposed additions or corrections concisely in the conversation, grouped where useful, and distinguish them from existing confirmed facts and unresolved claims. State the scope of a rule or exception. Ask for validation of the specific proposals before persisting them; a user's clear, direct correction validates that corrected fact without a second approval request. Silence, a supplied document, and approval of a different proposal do not validate a fact. Clarify conflicting definitions or policies rather than choosing one silently.

Use unvalidated document claims provisionally for the current task when useful, with a clear caveat. Visibly flag any material finding that depends on such a claim. Keep proposals, hypotheses, and disputes out of `.pricing/context.md` until the user validates them. If a dispute blocks only part of the work, continue the supported part and identify what needs resolution.

After validation, inspect the current context file again and apply only the confirmed additions or scoped corrections. Preserve unrelated entries, including exceptions; do not replace the file with the outline or an unreviewed summary. If the file is absent, create it with only the validated facts. Keep it short, readable Markdown, with no required metadata or fixed section count. Record a minimal exception as the exception plus the customers/products to which it applies. If a new fact conflicts with existing context, clarify its scope or replacement before changing the stored fact. Report what was saved and what remains unconfirmed.
