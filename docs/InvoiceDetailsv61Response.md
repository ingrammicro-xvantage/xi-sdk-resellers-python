# InvoiceDetailsv61Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_number** | **str** | The Invoice number for the order. | [optional] 
**invoice_status** | **str** | Status of the invoice. | [optional] 
**invoice_date** | **str** | Date of an Invoice. | [optional] 
**customer_order_number** | **str** | The reseller&#39;s order number for reference in their system. | [optional] 
**end_customer_order_number** | **str** | The end customer&#39;s order number for reference in their system. | [optional] 
**order_number** | **str** | The end customer&#39;s order number for reference in their system. | [optional] 
**order_date** | **str** | The date and time in UTC format that the order was created. | [optional] 
**bill_to_id** | **str** | Bill to party | [optional] 
**invoice_type** | **str** | Type of the Invoice | [optional] 
**invoice_due_date** | **str** | Date when the invoice is due. | [optional] 
**customer_country_code** | **str** | Customer country code. | [optional] 
**customer_number** | **str** | Unique customer number in Ingram&#39;s system. | [optional] 
**ingram_order_number** | **str** | The IngramMicro sales order number. | [optional] 
**notes** | **str** | Notes for the invoice. | [optional] 
**payment_terms_info** | [**InvoiceDetailsv61ResponsePaymentTermsInfo**](InvoiceDetailsv61ResponsePaymentTermsInfo.md) |  | [optional] 
**bill_to_info** | [**InvoiceDetailsv61ResponseBillToInfo**](InvoiceDetailsv61ResponseBillToInfo.md) |  | [optional] 
**ship_to_info** | [**InvoiceDetailsv61ResponseShipToInfo**](InvoiceDetailsv61ResponseShipToInfo.md) |  | [optional] 
**lines** | [**List[InvoiceDetailsv61ResponseLinesInner]**](InvoiceDetailsv61ResponseLinesInner.md) |  | [optional] 
**fx_rate_info** | [**InvoiceDetailsv61ResponseFxRateInfo**](InvoiceDetailsv61ResponseFxRateInfo.md) |  | [optional] 
**summary** | [**InvoiceDetailsv61ResponseSummary**](InvoiceDetailsv61ResponseSummary.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_detailsv61_response import InvoiceDetailsv61Response

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61Response from a JSON string
invoice_detailsv61_response_instance = InvoiceDetailsv61Response.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailsv61Response.to_json())

# convert the object into a dict
invoice_detailsv61_response_dict = invoice_detailsv61_response_instance.to_dict()
# create an instance of InvoiceDetailsv61Response from a dict
invoice_detailsv61_response_form_dict = invoice_detailsv61_response.from_dict(invoice_detailsv61_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


