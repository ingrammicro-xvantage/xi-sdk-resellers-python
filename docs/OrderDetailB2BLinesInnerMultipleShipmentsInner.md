# OrderDetailB2BLinesInnerMultipleShipmentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **str** | Line number. | [optional] 
**requested_quantity** | **str** | Requested quantity. | [optional] 
**confirmed_quantity** | **str** | Confirmed quantity. | [optional] 
**data_type** | **str** | Date type. Example Single or multiple dates. | [optional] 
**date_range** | [**OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange**](OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange.md) |  | [optional] 
**source** | **str** | Source. | [optional] 
**description** | **str** | Description. | [optional] 
**var_date** | **str** | Date. | [optional] 
**delivery_date** | **str** | Delivery date. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_multiple_shipments_inner import OrderDetailB2BLinesInnerMultipleShipmentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerMultipleShipmentsInner from a JSON string
order_detail_b2_b_lines_inner_multiple_shipments_inner_instance = OrderDetailB2BLinesInnerMultipleShipmentsInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2BLinesInnerMultipleShipmentsInner.to_json()

# convert the object into a dict
order_detail_b2_b_lines_inner_multiple_shipments_inner_dict = order_detail_b2_b_lines_inner_multiple_shipments_inner_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerMultipleShipmentsInner from a dict
order_detail_b2_b_lines_inner_multiple_shipments_inner_form_dict = order_detail_b2_b_lines_inner_multiple_shipments_inner.from_dict(order_detail_b2_b_lines_inner_multiple_shipments_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


