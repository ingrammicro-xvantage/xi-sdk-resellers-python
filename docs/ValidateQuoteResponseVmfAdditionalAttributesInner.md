# ValidateQuoteResponseVmfAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the header level field. | [optional] 
**attribute_value** | **str** | The value of the header level field. | [optional] 
**attribute_description** | **str** | The description of the header level field. | [optional] 

## Example

```python
from xi.sdk.resellers.models.validate_quote_response_vmf_additional_attributes_inner import ValidateQuoteResponseVmfAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateQuoteResponseVmfAdditionalAttributesInner from a JSON string
validate_quote_response_vmf_additional_attributes_inner_instance = ValidateQuoteResponseVmfAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print(ValidateQuoteResponseVmfAdditionalAttributesInner.to_json())

# convert the object into a dict
validate_quote_response_vmf_additional_attributes_inner_dict = validate_quote_response_vmf_additional_attributes_inner_instance.to_dict()
# create an instance of ValidateQuoteResponseVmfAdditionalAttributesInner from a dict
validate_quote_response_vmf_additional_attributes_inner_from_dict = ValidateQuoteResponseVmfAdditionalAttributesInner.from_dict(validate_quote_response_vmf_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


