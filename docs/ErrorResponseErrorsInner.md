# ErrorResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique Id to identify error. | [optional] 
**type** | **str** | Describes the type of the error. | [optional] 
**message** | **str** | Describes the error message. | [optional] 
**fields** | [**List[ErrorResponseErrorsInnerFieldsInner]**](ErrorResponseErrorsInnerFieldsInner.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.error_response_errors_inner import ErrorResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseErrorsInner from a JSON string
error_response_errors_inner_instance = ErrorResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print ErrorResponseErrorsInner.to_json()

# convert the object into a dict
error_response_errors_inner_dict = error_response_errors_inner_instance.to_dict()
# create an instance of ErrorResponseErrorsInner from a dict
error_response_errors_inner_form_dict = error_response_errors_inner.from_dict(error_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


