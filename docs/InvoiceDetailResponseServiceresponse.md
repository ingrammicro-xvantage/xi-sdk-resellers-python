# InvoiceDetailResponseServiceresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsepreamble** | [**InvoiceDetailResponseServiceresponseResponsepreamble**](InvoiceDetailResponseServiceresponseResponsepreamble.md) |  | [optional] 
**invoicedetailresponse** | [**InvoiceDetailResponseServiceresponseInvoicedetailresponse**](InvoiceDetailResponseServiceresponseInvoicedetailresponse.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.invoice_detail_response_serviceresponse import InvoiceDetailResponseServiceresponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailResponseServiceresponse from a JSON string
invoice_detail_response_serviceresponse_instance = InvoiceDetailResponseServiceresponse.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailResponseServiceresponse.to_json()

# convert the object into a dict
invoice_detail_response_serviceresponse_dict = invoice_detail_response_serviceresponse_instance.to_dict()
# create an instance of InvoiceDetailResponseServiceresponse from a dict
invoice_detail_response_serviceresponse_form_dict = invoice_detail_response_serviceresponse.from_dict(invoice_detail_response_serviceresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


