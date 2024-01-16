# OrderDetailResponseLinesInnerAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Line level custom field names. | [optional] 
**attribute_value** | **str** | Value of the custom fields. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_detail_response_lines_inner_additional_attributes_inner import OrderDetailResponseLinesInnerAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseLinesInnerAdditionalAttributesInner from a JSON string
order_detail_response_lines_inner_additional_attributes_inner_instance = OrderDetailResponseLinesInnerAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseLinesInnerAdditionalAttributesInner.to_json()

# convert the object into a dict
order_detail_response_lines_inner_additional_attributes_inner_dict = order_detail_response_lines_inner_additional_attributes_inner_instance.to_dict()
# create an instance of OrderDetailResponseLinesInnerAdditionalAttributesInner from a dict
order_detail_response_lines_inner_additional_attributes_inner_form_dict = order_detail_response_lines_inner_additional_attributes_inner.from_dict(order_detail_response_lines_inner_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


