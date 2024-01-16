# RenewalsSearchRequestStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opporutiny_status** | [**RenewalsSearchRequestStatusOpporutinyStatus**](RenewalsSearchRequestStatusOpporutinyStatus.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.renewals_search_request_status import RenewalsSearchRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsSearchRequestStatus from a JSON string
renewals_search_request_status_instance = RenewalsSearchRequestStatus.from_json(json)
# print the JSON string representation of the object
print RenewalsSearchRequestStatus.to_json()

# convert the object into a dict
renewals_search_request_status_dict = renewals_search_request_status_instance.to_dict()
# create an instance of RenewalsSearchRequestStatus from a dict
renewals_search_request_status_form_dict = renewals_search_request_status.from_dict(renewals_search_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


