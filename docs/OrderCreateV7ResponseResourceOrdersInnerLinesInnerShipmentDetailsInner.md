# OrderCreateV7ResponseResourceOrdersInnerLinesInnerShipmentDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | **str** | The code for the shipping carrier for the line item. | [optional] 
**carrier_name** | **str** | The name of the shipping carrier for the line item. | [optional] 
**ship_from_warehouse_id** | **str** | The ID of the warehouse the line item will ship from. | [optional] 
**ship_from_location** | **str** | Location from which order is shipped. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_response_resource_orders_inner_lines_inner_shipment_details_inner import OrderCreateV7ResponseResourceOrdersInnerLinesInnerShipmentDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7ResponseResourceOrdersInnerLinesInnerShipmentDetailsInner from a JSON string
order_create_v7_response_resource_orders_inner_lines_inner_shipment_details_inner_instance = OrderCreateV7ResponseResourceOrdersInnerLinesInnerShipmentDetailsInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7ResponseResourceOrdersInnerLinesInnerShipmentDetailsInner.to_json())

# convert the object into a dict
order_create_v7_response_resource_orders_inner_lines_inner_shipment_details_inner_dict = order_create_v7_response_resource_orders_inner_lines_inner_shipment_details_inner_instance.to_dict()
# create an instance of OrderCreateV7ResponseResourceOrdersInnerLinesInnerShipmentDetailsInner from a dict
order_create_v7_response_resource_orders_inner_lines_inner_shipment_details_inner_from_dict = OrderCreateV7ResponseResourceOrdersInnerLinesInnerShipmentDetailsInner.from_dict(order_create_v7_response_resource_orders_inner_lines_inner_shipment_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


