# InvoiceDetailsv61ResponseSummaryTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_invoice_amount** | **float** | Net Invoice amount. | [optional] 
**discount_amount** | **float** | Discount amount. | [optional] 
**discount_type** | **str** | Type of discount. | [optional] 
**total_tax_amount** | **float** | Total Tax amount. | [optional] 
**invoiced_amount_due** | **float** | Total amount due for the invoice. | [optional] 
**freight_amount** | **float** | Freight amount | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.invoice_detailsv61_response_summary_totals import InvoiceDetailsv61ResponseSummaryTotals

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61ResponseSummaryTotals from a JSON string
invoice_detailsv61_response_summary_totals_instance = InvoiceDetailsv61ResponseSummaryTotals.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailsv61ResponseSummaryTotals.to_json()

# convert the object into a dict
invoice_detailsv61_response_summary_totals_dict = invoice_detailsv61_response_summary_totals_instance.to_dict()
# create an instance of InvoiceDetailsv61ResponseSummaryTotals from a dict
invoice_detailsv61_response_summary_totals_form_dict = invoice_detailsv61_response_summary_totals.from_dict(invoice_detailsv61_response_summary_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


