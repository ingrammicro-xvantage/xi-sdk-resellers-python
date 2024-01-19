# OrderModifyResponseLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_order_number** | **str** | The sub order number. The two-digit prefix is the warehouse code of the warehouse nearest the reseller. The middle number is the order number. The two-digit suffix is the sub order number. | [optional] 
**ingram_line_number** | **str** | The IngramMicro line number. | [optional] 
**customer_line_number** | **str** | The reseller&#39;s line number for reference in their system. | [optional] 
**ingram_part_number** | **str** | The unique IngramMicro part number for the line item. | [optional] 
**vendor_part_number** | **str** | The vendor&#39;s part number for the line item. | [optional] 
**quantity_ordered** | **int** | The quantity ordered of the line item. | [optional] 
**quantity_confirmed** | **int** | The quantity confirmed of the line item. | [optional] 
**quantity_back_ordered** | **int** | The quantity backordered of the line item. | [optional] 
**shipment_details** | [**OrderModifyResponseLinesInnerShipmentDetails**](OrderModifyResponseLinesInnerShipmentDetails.md) |  | [optional] 
**additional_attributes** | [**List[OrderModifyResponseLinesInnerAdditionalAttributesInner]**](OrderModifyResponseLinesInnerAdditionalAttributesInner.md) | SAP requested and country-specific line level details. | [optional] 
**notes** | **str** | Line-level notes for the order. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_modify_response_lines_inner import OrderModifyResponseLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyResponseLinesInner from a JSON string
order_modify_response_lines_inner_instance = OrderModifyResponseLinesInner.from_json(json)
# print the JSON string representation of the object
print OrderModifyResponseLinesInner.to_json()

# convert the object into a dict
order_modify_response_lines_inner_dict = order_modify_response_lines_inner_instance.to_dict()
# create an instance of OrderModifyResponseLinesInner from a dict
order_modify_response_lines_inner_form_dict = order_modify_response_lines_inner.from_dict(order_modify_response_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


