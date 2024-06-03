# OrderDetailB2BLinesInnerScheduleLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **str** | Line number. | [optional] 
**schedule_line_date** | **str** | schedule Line Date. | [optional] 
**requested_quantity** | **str** | Requested quantity. | [optional] 
**confirmed_quantity** | **str** | Confirmed quantity. | [optional] 
**goods_issue_date** | **str** | Date when good issued. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_schedule_lines_inner import OrderDetailB2BLinesInnerScheduleLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerScheduleLinesInner from a JSON string
order_detail_b2_b_lines_inner_schedule_lines_inner_instance = OrderDetailB2BLinesInnerScheduleLinesInner.from_json(json)
# print the JSON string representation of the object
print(OrderDetailB2BLinesInnerScheduleLinesInner.to_json())

# convert the object into a dict
order_detail_b2_b_lines_inner_schedule_lines_inner_dict = order_detail_b2_b_lines_inner_schedule_lines_inner_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerScheduleLinesInner from a dict
order_detail_b2_b_lines_inner_schedule_lines_inner_from_dict = OrderDetailB2BLinesInnerScheduleLinesInner.from_dict(order_detail_b2_b_lines_inner_schedule_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


