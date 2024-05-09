# InvoiceDetailsv61ResponseSummaryLines


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_line_count** | **int** | Number of lines in the order. | [optional] 
**product_line_total_quantity** | **int** | Total quantity of the order. | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_detailsv61_response_summary_lines import InvoiceDetailsv61ResponseSummaryLines

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61ResponseSummaryLines from a JSON string
invoice_detailsv61_response_summary_lines_instance = InvoiceDetailsv61ResponseSummaryLines.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailsv61ResponseSummaryLines.to_json())

# convert the object into a dict
invoice_detailsv61_response_summary_lines_dict = invoice_detailsv61_response_summary_lines_instance.to_dict()
# create an instance of InvoiceDetailsv61ResponseSummaryLines from a dict
invoice_detailsv61_response_summary_lines_from_dict = InvoiceDetailsv61ResponseSummaryLines.from_dict(invoice_detailsv61_response_summary_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


