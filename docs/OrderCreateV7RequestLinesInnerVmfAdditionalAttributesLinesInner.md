# OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner

The object containing the list of fields required at a line level by the vendor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the line level field. | [optional] 
**attribute_value** | **str** | The value of the line level field. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_vmf_additional_attributes_lines_inner import OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner from a JSON string
order_create_v7_request_lines_inner_vmf_additional_attributes_lines_inner_instance = OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner.to_json())

# convert the object into a dict
order_create_v7_request_lines_inner_vmf_additional_attributes_lines_inner_dict = order_create_v7_request_lines_inner_vmf_additional_attributes_lines_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner from a dict
order_create_v7_request_lines_inner_vmf_additional_attributes_lines_inner_from_dict = OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner.from_dict(order_create_v7_request_lines_inner_vmf_additional_attributes_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


