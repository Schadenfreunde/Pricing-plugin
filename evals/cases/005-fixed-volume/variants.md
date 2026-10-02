# Controller instructions for isolated variants

This file is for constructing runs, not an additional attachment to the evaluated assistant. Use a fresh workspace for each variant. Copy `prompt.md` and transform a copy of `data.csv` as below; update the supplied facts where needed. Attach only that variant's prompt and data. Do not attach reviewer keys or other variants.

| Variant | Input transformation |
| --- | --- |
| No cost evidence | Remove both cost columns. Replace the sentence confirming unchanged costs with: “Relevant costs are unavailable.” |
| Missing prior quantity | Leave B's `prior_qty` blank. Add: “B's prior quantity is missing, rather than zero.” |
| New item | Append C with blank `prior_qty`, current quantity 5, baseline price 40, proposed price 44, baseline/proposed cost 25, EUR/unit. Replace “both quarters cover products A and B” with “A and B are matched; C first appears in the supplied current-quarter extract, with no prior quantity supplied.” |
| Changed unit costs | Set A proposed cost to 65 and B proposed cost to 32. Replace the unchanged-cost fact with: “The proposed costs represent the supplied variable-cost scenario, not confirmed cost forecasts.” |
| List-price-only proposal | Rename `proposed_unit_price` to `proposed_list_price`. Replace the proposed-price fact with: “Proposed prices are list prices. The effect on invoice discounts and rebates is unknown; baseline prices remain realized net prices.” |

If later assessing sensitivity, give any assumed quantity response as a separate, explicit scenario rather than altering the fixed-volume base silently.
