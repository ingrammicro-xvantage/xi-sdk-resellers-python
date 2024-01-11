# InvoiceDetailResponseServiceresponseInvoicedetailresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customernumber** | **str** |  | [optional] 
**invoicenumber** | **str** |  | [optional] 
**invoicedate** | **date** |  | [optional] 
**invoicetype** | **str** |  | [optional] 
**customerordernumber** | **str** |  | [optional] 
**customerfreightamount** | **float** |  | [optional] 
**customerforeignfrightamt** | **float** |  | [optional] 
**totaltaxamount** | **float** |  | [optional] 
**totalamount** | **float** |  | [optional] 
**shiptosuffix** | **str** |  | [optional] 
**billtosuffix** | **str** |  | [optional] 
**freightamount** | **float** |  | [optional] 
**paymentterms** | **str** |  | [optional] 
**orderdate** | **str** |  | [optional] 
**carrier** | **str** |  | [optional] 
**carrierdescription** | **str** |  | [optional] 
**discountamount** | **float** |  | [optional] 
**taxtype** | **str** |  | [optional] 
**enduserponumber** | **str** |  | [optional] 
**freightforwardercode** | **str** |  | [optional] 
**creditmemoreasoncode** | **str** |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.invoice_detail_response_serviceresponse_invoicedetailresponse import InvoiceDetailResponseServiceresponseInvoicedetailresponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailResponseServiceresponseInvoicedetailresponse from a JSON string
invoice_detail_response_serviceresponse_invoicedetailresponse_instance = InvoiceDetailResponseServiceresponseInvoicedetailresponse.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailResponseServiceresponseInvoicedetailresponse.to_json()

# convert the object into a dict
invoice_detail_response_serviceresponse_invoicedetailresponse_dict = invoice_detail_response_serviceresponse_invoicedetailresponse_instance.to_dict()
# create an instance of InvoiceDetailResponseServiceresponseInvoicedetailresponse from a dict
invoice_detail_response_serviceresponse_invoicedetailresponse_form_dict = invoice_detail_response_serviceresponse_invoicedetailresponse.from_dict(invoice_detail_response_serviceresponse_invoicedetailresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


