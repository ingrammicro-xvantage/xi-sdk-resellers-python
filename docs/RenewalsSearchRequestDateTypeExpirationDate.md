# RenewalsSearchRequestDateTypeExpirationDate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_start_date** | **str** | Custom start date for expiration date. | [optional] 
**custom_end_date** | **str** | Custom end date for expiration date. | [optional] 

## Example

```python
from xi.sdk.resellers.models.renewals_search_request_date_type_expiration_date import RenewalsSearchRequestDateTypeExpirationDate

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsSearchRequestDateTypeExpirationDate from a JSON string
renewals_search_request_date_type_expiration_date_instance = RenewalsSearchRequestDateTypeExpirationDate.from_json(json)
# print the JSON string representation of the object
print(RenewalsSearchRequestDateTypeExpirationDate.to_json())

# convert the object into a dict
renewals_search_request_date_type_expiration_date_dict = renewals_search_request_date_type_expiration_date_instance.to_dict()
# create an instance of RenewalsSearchRequestDateTypeExpirationDate from a dict
renewals_search_request_date_type_expiration_date_from_dict = RenewalsSearchRequestDateTypeExpirationDate.from_dict(renewals_search_request_date_type_expiration_date_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


