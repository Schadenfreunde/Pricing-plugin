---
name: pricing-scan
description: Use when exploring commercial data for pricing anomalies and opportunity leads.
---

# Pricing scan

**Before step 1, read the [shared rules](../references/shared-rules.md).**

## 1. Check data fitness

- Apply [metric verification](../knowledge/metric-verification.md). Establish measure mappings, numeric consistency, grain, comparable basis, dated coverage, adjustments and matching.
- Isolate known invalid records.
- An unresolved basis holds only the affected calculations (shared rules, section 3).

## 2. Classify findings

- Sort each finding into one class:
  - data issue
  - billing, collections or entitlement defect
  - unresolved structural difference
  - confirmed exception
  - commercial lead
- Match the breadth to the request. Explore broadly for an open opportunity request; run focused checks for a narrow question.
- Pick the cards that apply from the [knowledge index](../knowledge/index.md). Where relevant, explore promotion, recurring-discount, renewal and usage-margin leads.
- Use [peer comparisons](../knowledge/methods/peer-comparisons.md) and [discount governance](../knowledge/methods/discount-governance.md) where relevant.
- Look for meaningful combinations, such as low revenue with low margin, or generous terms without commitments.
- Treat a low price or a rare pattern as a lead that needs validation.

## 3. Rank leads

- Apply [evidence ranking](../knowledge/methods/evidence-ranking.md).
- For each lead, state its observation, scope, observation confidence, action confidence and next validation step.
- Show scale, feasibility and risk separately from confidence.
- Size useful [conditional scenarios](../knowledge/methods/price-change-economics.md) even when response or capture is unknown. The method sets which inputs are required.

## 4. Return

- Return a concise shortlist of leads and the validation choices.
- For a requested deeper explanation, continue in [analyze](../pricing-analyze/SKILL.md). For choosing an action, continue in [recommend](../pricing-recommend/SKILL.md).
