# ValidateQuoteResponseLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_line_number** | **str** | The reseller&#39;s line item number for reference in their system. | [optional] 
**ingram_part_number** | **str** | Unique Ingram Micro part number. | [optional] 
**quantity** | **str** | The quantity of the line item. | [optional] 
**vmf_additional_attributes_lines** | [**List[ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner]**](ValidateQuoteResponseLinesInnerVmfAdditionalAttributesLinesInner.md) | The object containing the list of fields required at a line level by the vendor. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.validate_quote_response_lines_inner import ValidateQuoteResponseLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateQuoteResponseLinesInner from a JSON string
validate_quote_response_lines_inner_instance = ValidateQuoteResponseLinesInner.from_json(json)
# print the JSON string representation of the object
print ValidateQuoteResponseLinesInner.to_json()

# convert the object into a dict
validate_quote_response_lines_inner_dict = validate_quote_response_lines_inner_instance.to_dict()
# create an instance of ValidateQuoteResponseLinesInner from a dict
validate_quote_response_lines_inner_form_dict = validate_quote_response_lines_inner.from_dict(validate_quote_response_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


