# OrderDetailB2BLinesInnerEstimatedDatesInnerShip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ship_date_type** | **str** | Date type. Example Single or multiple dates. | [optional] 
**ship_date_range** | [**OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange**](OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange.md) |  | [optional] 
**ship_source** | **str** | Source of the shipment. | [optional] 
**ship_description** | **str** | Shipment description. | [optional] 
**ship_date** | **str** | Ship date. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship import OrderDetailB2BLinesInnerEstimatedDatesInnerShip

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerEstimatedDatesInnerShip from a JSON string
order_detail_b2_b_lines_inner_estimated_dates_inner_ship_instance = OrderDetailB2BLinesInnerEstimatedDatesInnerShip.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2BLinesInnerEstimatedDatesInnerShip.to_json()

# convert the object into a dict
order_detail_b2_b_lines_inner_estimated_dates_inner_ship_dict = order_detail_b2_b_lines_inner_estimated_dates_inner_ship_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerEstimatedDatesInnerShip from a dict
order_detail_b2_b_lines_inner_estimated_dates_inner_ship_form_dict = order_detail_b2_b_lines_inner_estimated_dates_inner_ship.from_dict(order_detail_b2_b_lines_inner_estimated_dates_inner_ship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


