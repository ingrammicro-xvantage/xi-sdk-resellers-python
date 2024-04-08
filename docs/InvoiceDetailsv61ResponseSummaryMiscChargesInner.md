# InvoiceDetailsv61ResponseSummaryMiscChargesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**charge_description** | **str** | Description of the charge. | [optional] 
**misc_charge_line_count** | **int** | The number of lines for which miscellaneous charges are applicable. | [optional] 
**misc_charge_line_total** | **float** | Miscellaneous charge amount. | [optional] 
**charge_line_reference** | **str** | Reference of the chargeLine. | [optional] 
**is_non_misc** | **str** | Is charge non miscellaneous. | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_detailsv61_response_summary_misc_charges_inner import InvoiceDetailsv61ResponseSummaryMiscChargesInner

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61ResponseSummaryMiscChargesInner from a JSON string
invoice_detailsv61_response_summary_misc_charges_inner_instance = InvoiceDetailsv61ResponseSummaryMiscChargesInner.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailsv61ResponseSummaryMiscChargesInner.to_json())

# convert the object into a dict
invoice_detailsv61_response_summary_misc_charges_inner_dict = invoice_detailsv61_response_summary_misc_charges_inner_instance.to_dict()
# create an instance of InvoiceDetailsv61ResponseSummaryMiscChargesInner from a dict
invoice_detailsv61_response_summary_misc_charges_inner_form_dict = invoice_detailsv61_response_summary_misc_charges_inner.from_dict(invoice_detailsv61_response_summary_misc_charges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


