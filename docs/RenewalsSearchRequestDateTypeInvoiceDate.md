# RenewalsSearchRequestDateTypeInvoiceDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_start_date** | **str** | Custom start date for invoice date. | [optional] 
**custom_end_date** | **str** | Custom end date for invoice date. | [optional] 

## Example

```python
from xi.sdk.resellers.models.renewals_search_request_date_type_invoice_date import RenewalsSearchRequestDateTypeInvoiceDate

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsSearchRequestDateTypeInvoiceDate from a JSON string
renewals_search_request_date_type_invoice_date_instance = RenewalsSearchRequestDateTypeInvoiceDate.from_json(json)
# print the JSON string representation of the object
print(RenewalsSearchRequestDateTypeInvoiceDate.to_json())

# convert the object into a dict
renewals_search_request_date_type_invoice_date_dict = renewals_search_request_date_type_invoice_date_instance.to_dict()
# create an instance of RenewalsSearchRequestDateTypeInvoiceDate from a dict
renewals_search_request_date_type_invoice_date_from_dict = RenewalsSearchRequestDateTypeInvoiceDate.from_dict(renewals_search_request_date_type_invoice_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


