# InvoiceDetailsv61ResponseSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lines** | [**InvoiceDetailsv61ResponseSummaryLines**](InvoiceDetailsv61ResponseSummaryLines.md) |  | [optional] 
**misc_charges** | [**List[InvoiceDetailsv61ResponseSummaryMiscChargesInner]**](InvoiceDetailsv61ResponseSummaryMiscChargesInner.md) | Miscellaneous charges. | [optional] 
**totals** | [**InvoiceDetailsv61ResponseSummaryTotals**](InvoiceDetailsv61ResponseSummaryTotals.md) |  | [optional] 
**foreign_fx_totals** | [**InvoiceDetailsv61ResponseSummaryForeignFxTotals**](InvoiceDetailsv61ResponseSummaryForeignFxTotals.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.invoice_detailsv61_response_summary import InvoiceDetailsv61ResponseSummary

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61ResponseSummary from a JSON string
invoice_detailsv61_response_summary_instance = InvoiceDetailsv61ResponseSummary.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailsv61ResponseSummary.to_json()

# convert the object into a dict
invoice_detailsv61_response_summary_dict = invoice_detailsv61_response_summary_instance.to_dict()
# create an instance of InvoiceDetailsv61ResponseSummary from a dict
invoice_detailsv61_response_summary_form_dict = invoice_detailsv61_response_summary.from_dict(invoice_detailsv61_response_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


