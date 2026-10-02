# Isolated routing requests

Evaluation controller: run each request in a separate fresh workspace. Supply only that row's request and material, without this matrix, other rows or evaluator keys. Use an existing matching synthetic case where specified; do not attach its separate prompt or controller instructions. Seed only that row's stated confirmed context. Save each answer before assessment.

| Row | User request | Supplied material / confirmed context |
| --- | --- | --- |
| A | Find pricing opportunities in this export. | Case 004 `data.csv` and `notes.md`; seed its `confirmed-context.md`. |
| B | Why did gross margin fall? | Case 001 `data.csv` and `supplied-facts.md`, without the original analytical request or artifact instruction. |
| C | Design pricing for our new pump. | Case 006 `brief.md`; seed its `confirmed-context.md`. |
| D | Redesign our regional lists and discounts. | Case 006 `brief.md`; seed its `confirmed-context.md`. |
| E | Plan the agreed price increase. | Case 007 brief and confirmed context, but replace the first brief bullet with “Management has approved a 5% list-price increase for eligible business; launch dates and discount-policy changes remain undecided.” Other constraints remain unchanged. |
| F | What does our net price include? | Seed: “For our industrial pumps in EUR, net price is invoice price after invoice discounts and subsequent rebates, excluding VAT. Freight and other off-invoice concessions are outside this definition.” No dataset. |
| G | Can you sort out our pricing? We have lower margins, regional lists and a possible increase, but I don't know where to start. | No dataset or confirmed context; intended decision and priority are unspecified. |

For F's separate missing-definition variant, remove the seeded fact rather than attach this instruction to the evaluated assistant.
