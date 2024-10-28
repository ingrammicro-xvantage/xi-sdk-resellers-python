# OrderCreateV7RequestLinesInnerWarrantyInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_line_link** | **str** | Customer line number of the warranty product in this request for linkage, either hardwareLineLink or warrantyLineLink can be used in a line | [optional] 
**warranty_line_link** | **str** | Customer line number of the hardware product in this request for linkage, either hardwareLineLink or warrantyLineLink can be used in a line. | [optional] 
**direct_line_link** | **str** | Unique value to link hardware and warranty lines. Should be used only when products are purchased from both Ingram and/or vendor but the warranty is purchased through Ingram for them. | [optional] 
**serial_info** | [**List[OrderCreateV7RequestLinesInnerWarrantyInfoInnerSerialInfoInner]**](OrderCreateV7RequestLinesInnerWarrantyInfoInnerSerialInfoInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_warranty_info_inner import OrderCreateV7RequestLinesInnerWarrantyInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestLinesInnerWarrantyInfoInner from a JSON string
order_create_v7_request_lines_inner_warranty_info_inner_instance = OrderCreateV7RequestLinesInnerWarrantyInfoInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestLinesInnerWarrantyInfoInner.to_json())

# convert the object into a dict
order_create_v7_request_lines_inner_warranty_info_inner_dict = order_create_v7_request_lines_inner_warranty_info_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestLinesInnerWarrantyInfoInner from a dict
order_create_v7_request_lines_inner_warranty_info_inner_from_dict = OrderCreateV7RequestLinesInnerWarrantyInfoInner.from_dict(order_create_v7_request_lines_inner_warranty_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


