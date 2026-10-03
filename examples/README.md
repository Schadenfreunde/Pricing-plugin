# Gross margin analysis: a synthetic worked example

This example shows how Pricing Plugin checks a reported gross margin change and reconciles the supported price and product-mix effects. It uses synthetic industrial-product data; it is not a customer case study or evidence of installed-host performance.

## Question and inputs

The question reports a 300 basis point decline in product-group margin. The [input CSV](../evals/cases/001-margin-price-mix/data.csv) and [supplied facts](../evals/cases/001-margin-price-mix/supplied-facts.md) describe two products across two quarters. Total quantity stays at 100 units, prices fall from €100 to €98 for both products, and sales shift toward product B. Unit costs stay at €60 for A and €80 for B.

## Verified answer

Gross margin falls from **30.00% to 26.53%**, a **346.94 basis point decline**, rather than the reported 300 basis points.

| Measure | Previous quarter | Current quarter |
| --- | ---: | ---: |
| Product A / B quantities | 50 / 50 | 40 / 60 |
| Sales | €10,000 | €9,800 |
| Cost of goods sold | €7,000 | €7,200 |
| Gross profit | €3,000 | €2,600 |
| Gross margin | 30.00% | 26.53% |

Gross margin equals `(sales − cost of goods sold) / sales`. Compute the group rate from group totals rather than taking an unweighted average of product margin percentages.

Using the project's declared two-factor convention with unchanged unit costs, the decline reconciles to:

| Contribution | Margin movement |
| --- | ---: |
| Realized price | −142.86 basis points |
| Product mix / quantity | −200.00 basis points |
| Shared price/mix effect | −4.08 basis points |
| Total | −346.94 basis points |

The unrounded contributions reconcile to the full movement. The shared effect is an arithmetic overlap between factors, not unexplained commercial loss. See the [margin-driver reference](../skills/knowledge/margin-drivers.md) for the formula and its scope; this two-factor method is not a universal decomposition for changing costs.

## What remains unknown

The data establishes lower realized prices and a changed product mix. It does not explain why either changed. Without list prices, discount records, contracts, or policy evidence, the report cannot attribute the decline to discounting or an unauthorized pricing decision.

## Open the sample report

Download [the HTML margin analysis](margin-analysis.html) and open it in a browser. GitHub's file view shows the source; this repository does not provide a hosted live preview. The report contains the group totals, reconciled bridge, method, and possible next investigations.

The landscape print layout reflects review of the HTML sample. An actual PDF export and inspection of every PDF page have not been confirmed.

The [legacy inputs](../evals/README.md) remain for arithmetic and historical reference. Fresh end-to-end acceptance with new data and cases is planned.

[Return to Pricing Plugin](../README.md)
