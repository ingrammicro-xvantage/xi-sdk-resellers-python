# ReturnsCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**returns_claims** | [**List[ReturnsCreateResponseReturnsClaimsInner]**](ReturnsCreateResponseReturnsClaimsInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.returns_create_response import ReturnsCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsCreateResponse from a JSON string
returns_create_response_instance = ReturnsCreateResponse.from_json(json)
# print the JSON string representation of the object
print ReturnsCreateResponse.to_json()

# convert the object into a dict
returns_create_response_dict = returns_create_response_instance.to_dict()
# create an instance of ReturnsCreateResponse from a dict
returns_create_response_form_dict = returns_create_response.from_dict(returns_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


