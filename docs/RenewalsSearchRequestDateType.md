# RenewalsSearchRequestDateType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | [**RenewalsSearchRequestDateTypeStartDate**](RenewalsSearchRequestDateTypeStartDate.md) |  | [optional] 
**end_date** | [**RenewalsSearchRequestDateTypeEndDate**](RenewalsSearchRequestDateTypeEndDate.md) |  | [optional] 
**invoice_date** | [**RenewalsSearchRequestDateTypeInvoiceDate**](RenewalsSearchRequestDateTypeInvoiceDate.md) |  | [optional] 
**expiration_date** | [**RenewalsSearchRequestDateTypeExpirationDate**](RenewalsSearchRequestDateTypeExpirationDate.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.renewals_search_request_date_type import RenewalsSearchRequestDateType

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsSearchRequestDateType from a JSON string
renewals_search_request_date_type_instance = RenewalsSearchRequestDateType.from_json(json)
# print the JSON string representation of the object
print(RenewalsSearchRequestDateType.to_json())

# convert the object into a dict
renewals_search_request_date_type_dict = renewals_search_request_date_type_instance.to_dict()
# create an instance of RenewalsSearchRequestDateType from a dict
renewals_search_request_date_type_form_dict = renewals_search_request_date_type.from_dict(renewals_search_request_date_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


