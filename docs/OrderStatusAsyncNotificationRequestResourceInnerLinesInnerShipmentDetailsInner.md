# OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_date** | **str** | The date the line item was shipped. | [optional] 
**ship_from_warehouse_id** | **str** | The ID of the warehouse the product will ship from. | [optional] 
**warehouse_name** | **str** | \&quot;\&quot; | [optional] 
**carrier_code** | **str** | The carrier code for the shipment containing the  line item. | [optional] 
**carrier_name** | **str** | The name of the carrier of the shipment containing   the line item. | [optional] 
**package_details** | [**List[OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner]**](OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner import OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner from a JSON string
order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_instance = OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner.from_json(json)
# print the JSON string representation of the object
print OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner.to_json()

# convert the object into a dict
order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_dict = order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_instance.to_dict()
# create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner from a dict
order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_form_dict = order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner.from_dict(order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


