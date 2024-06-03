# GetAccesstoken500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault** | [**GetAccesstoken500ResponseFault**](GetAccesstoken500ResponseFault.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.get_accesstoken500_response import GetAccesstoken500Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccesstoken500Response from a JSON string
get_accesstoken500_response_instance = GetAccesstoken500Response.from_json(json)
# print the JSON string representation of the object
print(GetAccesstoken500Response.to_json())

# convert the object into a dict
get_accesstoken500_response_dict = get_accesstoken500_response_instance.to_dict()
# create an instance of GetAccesstoken500Response from a dict
get_accesstoken500_response_from_dict = GetAccesstoken500Response.from_dict(get_accesstoken500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


