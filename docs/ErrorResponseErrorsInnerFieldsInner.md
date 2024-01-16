# ErrorResponseErrorsInnerFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Contains the name of the field. | [optional] 
**value** | **str** | Value sent in the input for the specific field. | [optional] 
**message** | **str** | Gives the description of the field message. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.error_response_errors_inner_fields_inner import ErrorResponseErrorsInnerFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseErrorsInnerFieldsInner from a JSON string
error_response_errors_inner_fields_inner_instance = ErrorResponseErrorsInnerFieldsInner.from_json(json)
# print the JSON string representation of the object
print ErrorResponseErrorsInnerFieldsInner.to_json()

# convert the object into a dict
error_response_errors_inner_fields_inner_dict = error_response_errors_inner_fields_inner_instance.to_dict()
# create an instance of ErrorResponseErrorsInnerFieldsInner from a dict
error_response_errors_inner_fields_inner_form_dict = error_response_errors_inner_fields_inner.from_dict(error_response_errors_inner_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


