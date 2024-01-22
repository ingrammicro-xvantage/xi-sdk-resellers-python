# InvoiceDetailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servicerequest** | [**InvoiceDetailRequestServicerequest**](InvoiceDetailRequestServicerequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_detail_request import InvoiceDetailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailRequest from a JSON string
invoice_detail_request_instance = InvoiceDetailRequest.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailRequest.to_json()

# convert the object into a dict
invoice_detail_request_dict = invoice_detail_request_instance.to_dict()
# create an instance of InvoiceDetailRequest from a dict
invoice_detail_request_form_dict = invoice_detail_request.from_dict(invoice_detail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


