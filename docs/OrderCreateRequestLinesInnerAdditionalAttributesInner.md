# OrderCreateRequestLinesInnerAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | SAP requested and country-specific line level details. | [optional] 
**attribute_value** | **str** | Line-level additional attributes. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_create_request_lines_inner_additional_attributes_inner import OrderCreateRequestLinesInnerAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestLinesInnerAdditionalAttributesInner from a JSON string
order_create_request_lines_inner_additional_attributes_inner_instance = OrderCreateRequestLinesInnerAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestLinesInnerAdditionalAttributesInner.to_json()

# convert the object into a dict
order_create_request_lines_inner_additional_attributes_inner_dict = order_create_request_lines_inner_additional_attributes_inner_instance.to_dict()
# create an instance of OrderCreateRequestLinesInnerAdditionalAttributesInner from a dict
order_create_request_lines_inner_additional_attributes_inner_form_dict = order_create_request_lines_inner_additional_attributes_inner.from_dict(order_create_request_lines_inner_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


