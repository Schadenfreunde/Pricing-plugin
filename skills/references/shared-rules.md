# Shared rules for every pricing skill

Every pricing skill reads this file before its own steps. If a skill step seems to conflict with these rules, these rules win.

## 1. Company context

- Read `.pricing/context.md` in the working project, if it exists.
- Check its header. If the company or scope does not match this project, treat every fact in it as unconfirmed.
- A file without a header predates the [context format](../pricing-intake/references/context-format.md). Treat its facts as confirmed for this project.
- Apply a confirmed fact only within its stated scope.
- Treat everything else as unconfirmed: user statements, attachments, column names and your own findings.

## 2. Unconfirmed claims

- You may use an unconfirmed claim provisionally.
- When a finding materially depends on one, put the caveat next to that finding, not only in the method note.
- Only [intake](../pricing-intake/SKILL.md) writes `.pricing/context.md`. Send additions, corrections and disputes there.
- Keep pending claims, disputes, findings, hypotheses and proposals in the answer or report, never in the context file.

## 3. Unresolved basis: stop and ask

Stop before calculating or concluding on a result when the arithmetic itself depends on an unresolved choice:

- which of two or more candidate fields, price levels or accounting bases represents the measure
- the comparison basis, such as currency, units, grain, pack size, population or period
- which of two valid policy or recipe versions applies

Do not stop when only the interpretation is open and the arithmetic is the same either way, such as whether a recorded cost field includes freight. Calculate on the field as recorded, name it that way (for example "net price less `unit_cost_eur` as supplied"), and caveat the open interpretation under section 2.

When you do stop:

- Show the conflicting evidence and ask one focused question. Name the competing options and why the choice changes the result.
- Hold the affected result. Do not silently choose a basis, convert, drop the affected population, or headline a figure on an assumed basis, however it is caveated.
- A caveat does not resolve the choice. Neither do deadline pressure or general permission to pick the obvious field.
- Continue all work that does not depend on the answer. Resume the held result once the basis is resolved.
- [Metric verification](../knowledge/metric-verification.md) lists the specific checks that reveal these choices.

## 4. Authority

- Your output is a draft: an analysis, recommendation, design or plan.
- Do not change prices or systems, send communications or treat anything as approved unless the user explicitly authorizes that specific action and suitable tools exist.
- Record each decision's status as proposed, chosen or approved. Approving one item does not approve others.

## 5. Output

- Lead with the result, its material qualifications and the next choices or evidence needed. Put a short method note after that.
- Stop at the requested scope.
- Keep small answers in chat. For substantial analysis where visuals help, follow [HTML reporting](html-reporting.md) unless the user asked for another format.
- When work will continue in another skill, include a [handoff](handoff.md).
