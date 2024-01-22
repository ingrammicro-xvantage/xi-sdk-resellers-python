# ErrorResponseDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.error_response_dto import ErrorResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseDTO from a JSON string
error_response_dto_instance = ErrorResponseDTO.from_json(json)
# print the JSON string representation of the object
print ErrorResponseDTO.to_json()

# convert the object into a dict
error_response_dto_dict = error_response_dto_instance.to_dict()
# create an instance of ErrorResponseDTO from a dict
error_response_dto_form_dict = error_response_dto.from_dict(error_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


