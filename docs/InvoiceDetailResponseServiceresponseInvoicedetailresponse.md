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
**freightamount** | **float** | May not be available in all countries | [optional] 
**paymentterms** | **str** |  | [optional] 
**orderdate** | **date** |  | [optional] 
**carrier** | **str** |  | [optional] 
**carrierdescription** | **str** |  | [optional] 
**discountamount** | **float** |  | [optional] 
**taxtype** | **str** |  | [optional] 
**enduserponumber** | **str** |  | [optional] 
**freightforwardercode** | **str** |  | [optional] 
**creditmemoreasoncode** | **str** |  | [optional] 
**fulfillmentflag** | **str** |  | [optional] 
**holdreason** | **str** |  | [optional] 
**shipcomplete** | **str** |  | [optional] 
**shipdate** | **date** |  | [optional] 
**companycurrency** | **str** |  | [optional] 
**currencycode** | **str** |  | [optional] 
**currencyrate** | **str** |  | [optional] 
**globalorderid** | **str** |  | [optional] 
**originalshipcode** | **str** |  | [optional] 
**ordertype** | **str** |  | [optional] 
**orderstatus** | **str** |  | [optional] 
**totalotherfees** | **float** |  | [optional] 
**totalsales** | **str** |  | [optional] 
**weight** | **str** |  | [optional] 
**shippableswitch** | **str** |  | [optional] 
**soldto** | [**AddressType**](AddressType.md) |  | [optional] 
**billto** | [**AddressType**](AddressType.md) |  | [optional] 
**shoptoaddress** | [**AddressType**](AddressType.md) |  | [optional] 
**lines** | [**List[ProductLineType]**](ProductLineType.md) |  | [optional] 
**extendedspecs** | [**List[InvoiceDetailResponseServiceresponseInvoicedetailresponseExtendedspecsInner]**](InvoiceDetailResponseServiceresponseInvoicedetailresponseExtendedspecsInner.md) |  | [optional] 
**miscfeeline** | [**List[InvoiceDetailResponseServiceresponseInvoicedetailresponseMiscfeelineInner]**](InvoiceDetailResponseServiceresponseInvoicedetailresponseMiscfeelineInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_detail_response_serviceresponse_invoicedetailresponse import InvoiceDetailResponseServiceresponseInvoicedetailresponse

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


