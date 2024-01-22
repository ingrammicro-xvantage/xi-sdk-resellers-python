# InvoiceDetailsv61ResponseSummaryForeignFxTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foreign_currency_code** | **str** | Foreign Currency Code. | [optional] 
**foreign_currency_fx_rate** | **float** | Foreign rate. | [optional] 
**foreign_total_taxable_amount** | **str** | Foreign amount. | [optional] 
**foreign_total_tax_amount** | **float** | Foreign amount. | [optional] 
**foreign_invoice_amount_due** | **str** | Foreign due. | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_detailsv61_response_summary_foreign_fx_totals import InvoiceDetailsv61ResponseSummaryForeignFxTotals

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61ResponseSummaryForeignFxTotals from a JSON string
invoice_detailsv61_response_summary_foreign_fx_totals_instance = InvoiceDetailsv61ResponseSummaryForeignFxTotals.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailsv61ResponseSummaryForeignFxTotals.to_json()

# convert the object into a dict
invoice_detailsv61_response_summary_foreign_fx_totals_dict = invoice_detailsv61_response_summary_foreign_fx_totals_instance.to_dict()
# create an instance of InvoiceDetailsv61ResponseSummaryForeignFxTotals from a dict
invoice_detailsv61_response_summary_foreign_fx_totals_form_dict = invoice_detailsv61_response_summary_foreign_fx_totals.from_dict(invoice_detailsv61_response_summary_foreign_fx_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


