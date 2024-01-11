# RenewalsSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**RenewalsSearchRequestStatus**](RenewalsSearchRequestStatus.md) |  | [optional] 
**data_type** | [**RenewalsSearchRequestDataType**](RenewalsSearchRequestDataType.md) |  | [optional] 
**vendor** | **str** | The name of the Vendor. | [optional] 
**end_user** | **str** | The name of the enduser.  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.renewals_search_request import RenewalsSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsSearchRequest from a JSON string
renewals_search_request_instance = RenewalsSearchRequest.from_json(json)
# print the JSON string representation of the object
print RenewalsSearchRequest.to_json()

# convert the object into a dict
renewals_search_request_dict = renewals_search_request_instance.to_dict()
# create an instance of RenewalsSearchRequest from a dict
renewals_search_request_form_dict = renewals_search_request.from_dict(renewals_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


