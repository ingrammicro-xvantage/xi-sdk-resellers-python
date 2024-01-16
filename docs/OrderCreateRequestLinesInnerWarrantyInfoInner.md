# OrderCreateRequestLinesInnerWarrantyInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_line_link** | **str** | Unique value to link hardware and warranty lines. Should be used only when products are purchased from both Ingram and/or vendor but the warranty is purchased through Ingram for them. | [optional] 
**warranty_line_link** | **str** | Customer line number of the hardware product in this request for linkage, either hardwareLineLink or warrantyLineLink can be used in a line. | [optional] 
**hardware_line_link** | **str** | Customer line number of the warranty product in this request for linkage, either hardwareLineLink or warrantyLineLink can be used in a line  | [optional] 
**serial_info** | [**List[OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner]**](OrderCreateRequestLinesInnerWarrantyInfoInnerSerialInfoInner.md) | Serial information of the hardware to be associated with the warranty, applicable on post sale orders. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_create_request_lines_inner_warranty_info_inner import OrderCreateRequestLinesInnerWarrantyInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestLinesInnerWarrantyInfoInner from a JSON string
order_create_request_lines_inner_warranty_info_inner_instance = OrderCreateRequestLinesInnerWarrantyInfoInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestLinesInnerWarrantyInfoInner.to_json()

# convert the object into a dict
order_create_request_lines_inner_warranty_info_inner_dict = order_create_request_lines_inner_warranty_info_inner_instance.to_dict()
# create an instance of OrderCreateRequestLinesInnerWarrantyInfoInner from a dict
order_create_request_lines_inner_warranty_info_inner_form_dict = order_create_request_lines_inner_warranty_info_inner.from_dict(order_create_request_lines_inner_warranty_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


