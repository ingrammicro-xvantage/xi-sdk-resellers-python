# OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_date_type** | **str** | Date type. Example Single or multiple dates. | [optional] 
**delivery_date_range** | [**OrderDetailB2BLinesInnerEstimatedDatesInnerDeliveryDeliveryDateRange**](OrderDetailB2BLinesInnerEstimatedDatesInnerDeliveryDeliveryDateRange.md) |  | [optional] 
**delivery_source** | **str** | Source of the delivery. | [optional] 
**delivery_description** | **str** | Delivery description. | [optional] 
**delivered_date** | **str** | Delivery date. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_detail_b2_b_lines_inner_estimated_dates_inner_delivery import OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery from a JSON string
order_detail_b2_b_lines_inner_estimated_dates_inner_delivery_instance = OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery.to_json()

# convert the object into a dict
order_detail_b2_b_lines_inner_estimated_dates_inner_delivery_dict = order_detail_b2_b_lines_inner_estimated_dates_inner_delivery_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery from a dict
order_detail_b2_b_lines_inner_estimated_dates_inner_delivery_form_dict = order_detail_b2_b_lines_inner_estimated_dates_inner_delivery.from_dict(order_detail_b2_b_lines_inner_estimated_dates_inner_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


