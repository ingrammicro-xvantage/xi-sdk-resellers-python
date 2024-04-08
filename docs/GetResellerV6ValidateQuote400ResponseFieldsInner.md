# GetResellerV6ValidateQuote400ResponseFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | Contains the name of the field. | [optional] 
**message** | **str** | Gives the description of the field message. | [optional] 
**value** | **str** | Value sent in the input for the specific field. | [optional] 

## Example

```python
from xi.sdk.resellers.models.get_reseller_v6_validate_quote400_response_fields_inner import GetResellerV6ValidateQuote400ResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetResellerV6ValidateQuote400ResponseFieldsInner from a JSON string
get_reseller_v6_validate_quote400_response_fields_inner_instance = GetResellerV6ValidateQuote400ResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print(GetResellerV6ValidateQuote400ResponseFieldsInner.to_json())

# convert the object into a dict
get_reseller_v6_validate_quote400_response_fields_inner_dict = get_reseller_v6_validate_quote400_response_fields_inner_instance.to_dict()
# create an instance of GetResellerV6ValidateQuote400ResponseFieldsInner from a dict
get_reseller_v6_validate_quote400_response_fields_inner_form_dict = get_reseller_v6_validate_quote400_response_fields_inner.from_dict(get_reseller_v6_validate_quote400_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


