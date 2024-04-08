# InvoiceSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records_found** | **int** | Total count of quotes retrieved in the request response. | [optional] 
**page_size** | **int** | Number of records (quotes) displayed per page in the quote list. | [optional] 
**page_number** | **int** | Page index or page number for the list of quotes being returned. | [optional] 
**invoices** | [**List[InvoiceSearchResponseInvoicesInner]**](InvoiceSearchResponseInvoicesInner.md) | The Invoices details for the requested criteria. | [optional] 
**next_page** | **str** | Next page of the pagination. | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_search_response import InvoiceSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceSearchResponse from a JSON string
invoice_search_response_instance = InvoiceSearchResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceSearchResponse.to_json())

# convert the object into a dict
invoice_search_response_dict = invoice_search_response_instance.to_dict()
# create an instance of InvoiceSearchResponse from a dict
invoice_search_response_form_dict = invoice_search_response.from_dict(invoice_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


