# InvoiceSearchResponseInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_terms_due_date** | **str** | Payment Terms Due date. | [optional] 
**special_bid_numbers** | **List[str]** |  | [optional] 
**erp_order_number** | **str** | Order number | [optional] 
**invoice_number** | **str** | Invoice no. | [optional] 
**invoice_status** | **str** | Invoice Status. | [optional] 
**invoice_date** | **str** | Invoice Date. | [optional] 
**invoice_due_date** | **str** | Invoice Due Date. | [optional] 
**invoiced_amount_due** | **float** | Invoice Amount. | [optional] 
**customer_order_number** | **str** | Customer Order No. | [optional] 
**end_customer_order_number** | **str** | End Customer Order number. | [optional] 
**order_create_date** | **str** | Order Create Date. | [optional] 
**invoice_amount_incl_tax** | **float** | Invoice Amount Inclusive of Taxes | [optional] 
**forgntotalamount** | **float** |  | [optional] 
**gst_invoice_number** | **str** |  | [optional] 
**isfseccenabled** | **bool** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_search_response_invoices_inner import InvoiceSearchResponseInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSearchResponseInvoicesInner from a JSON string
invoice_search_response_invoices_inner_instance = InvoiceSearchResponseInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(InvoiceSearchResponseInvoicesInner.to_json())

# convert the object into a dict
invoice_search_response_invoices_inner_dict = invoice_search_response_invoices_inner_instance.to_dict()
# create an instance of InvoiceSearchResponseInvoicesInner from a dict
invoice_search_response_invoices_inner_from_dict = InvoiceSearchResponseInvoicesInner.from_dict(invoice_search_response_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


