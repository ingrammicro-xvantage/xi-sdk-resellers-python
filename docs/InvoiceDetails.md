# InvoiceDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceresponse** | [**InvoiceDetailResponseServiceresponse**](InvoiceDetailResponseServiceresponse.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.invoice_details import InvoiceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetails from a JSON string
invoice_details_instance = InvoiceDetails.from_json(json)
# print the JSON string representation of the object
print InvoiceDetails.to_json()

# convert the object into a dict
invoice_details_dict = invoice_details_instance.to_dict()
# create an instance of InvoiceDetails from a dict
invoice_details_form_dict = invoice_details.from_dict(invoice_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


