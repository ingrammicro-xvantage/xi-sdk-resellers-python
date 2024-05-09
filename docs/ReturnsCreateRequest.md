# ReturnsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**List[ReturnsCreateRequestListInner]**](ReturnsCreateRequestListInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.returns_create_request import ReturnsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsCreateRequest from a JSON string
returns_create_request_instance = ReturnsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ReturnsCreateRequest.to_json())

# convert the object into a dict
returns_create_request_dict = returns_create_request_instance.to_dict()
# create an instance of ReturnsCreateRequest from a dict
returns_create_request_from_dict = ReturnsCreateRequest.from_dict(returns_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


