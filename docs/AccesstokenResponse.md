# AccesstokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**token_type** | **str** |  | [optional] 
**expires_in** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.accesstoken_response import AccesstokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccesstokenResponse from a JSON string
accesstoken_response_instance = AccesstokenResponse.from_json(json)
# print the JSON string representation of the object
print(AccesstokenResponse.to_json())

# convert the object into a dict
accesstoken_response_dict = accesstoken_response_instance.to_dict()
# create an instance of AccesstokenResponse from a dict
accesstoken_response_from_dict = AccesstokenResponse.from_dict(accesstoken_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


