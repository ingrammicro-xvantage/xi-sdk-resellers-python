# InvoiceDetailsv61ResponsePaymentTermsInfo

Payment terms is the agreement between Ingram and the customer by what period they should pay the invoice by

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_terms_code** | **str** | Code of the payment terms. | [optional] 
**payment_terms_description** | **str** | Description of the payment terms. | [optional] 
**payment_terms_due_date** | **str** | Due date of the payment terms. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.invoice_detailsv61_response_payment_terms_info import InvoiceDetailsv61ResponsePaymentTermsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61ResponsePaymentTermsInfo from a JSON string
invoice_detailsv61_response_payment_terms_info_instance = InvoiceDetailsv61ResponsePaymentTermsInfo.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailsv61ResponsePaymentTermsInfo.to_json()

# convert the object into a dict
invoice_detailsv61_response_payment_terms_info_dict = invoice_detailsv61_response_payment_terms_info_instance.to_dict()
# create an instance of InvoiceDetailsv61ResponsePaymentTermsInfo from a dict
invoice_detailsv61_response_payment_terms_info_form_dict = invoice_detailsv61_response_payment_terms_info.from_dict(invoice_detailsv61_response_payment_terms_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


