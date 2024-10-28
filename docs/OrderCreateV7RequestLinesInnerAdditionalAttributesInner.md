# OrderCreateV7RequestLinesInnerAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | SAP requested and country-specific line level details. | [optional] 
**attribute_value** | **str** | TLine-level additional attributes. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_additional_attributes_inner import OrderCreateV7RequestLinesInnerAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestLinesInnerAdditionalAttributesInner from a JSON string
order_create_v7_request_lines_inner_additional_attributes_inner_instance = OrderCreateV7RequestLinesInnerAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestLinesInnerAdditionalAttributesInner.to_json())

# convert the object into a dict
order_create_v7_request_lines_inner_additional_attributes_inner_dict = order_create_v7_request_lines_inner_additional_attributes_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestLinesInnerAdditionalAttributesInner from a dict
order_create_v7_request_lines_inner_additional_attributes_inner_from_dict = OrderCreateV7RequestLinesInnerAdditionalAttributesInner.from_dict(order_create_v7_request_lines_inner_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


