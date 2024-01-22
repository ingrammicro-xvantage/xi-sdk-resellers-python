# InvoiceDetailRequestServicerequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestpreamble** | [**InvoiceDetailRequestServicerequestRequestpreamble**](InvoiceDetailRequestServicerequestRequestpreamble.md) |  | [optional] 
**invoicedetailrequest** | [**InvoiceDetailRequestServicerequestInvoicedetailrequest**](InvoiceDetailRequestServicerequestInvoicedetailrequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_detail_request_servicerequest import InvoiceDetailRequestServicerequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailRequestServicerequest from a JSON string
invoice_detail_request_servicerequest_instance = InvoiceDetailRequestServicerequest.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailRequestServicerequest.to_json()

# convert the object into a dict
invoice_detail_request_servicerequest_dict = invoice_detail_request_servicerequest_instance.to_dict()
# create an instance of InvoiceDetailRequestServicerequest from a dict
invoice_detail_request_servicerequest_form_dict = invoice_detail_request_servicerequest.from_dict(invoice_detail_request_servicerequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


