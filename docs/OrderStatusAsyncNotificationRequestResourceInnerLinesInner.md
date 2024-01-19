# OrderStatusAsyncNotificationRequestResourceInnerLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **str** | The Ingram Micro line number for the product | [optional] 
**sub_order_number** | **str** | The sub order number. The two-digit prefix is the warehouse code of the warehouse nearest the reseller. The middle number is the order number. The two-digit suffix is the sub order number. | [optional] 
**line_status** | **str** | The status for the line item in the order. One of: Backordered, Open, Shipped | [optional] 
**ingram_part_number** | **str** | The Ingram Micro part number for the line item. | [optional] 
**vendor_part_number** | **str** | The vendor part number for the line item. | [optional] 
**requested_quantity** | **str** | The quantity of the line item requested. | [optional] 
**shipped_quantity** | **str** | The quantity of the line item that has been shipped. | [optional] 
**backordered_quantity** | **str** | The quantity of the line item that is backordered. | [optional] 
**shipment_details** | [**List[OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner]**](OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInner.md) |  | [optional] 
**serial_number_details** | [**List[OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner]**](OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_lines_inner import OrderStatusAsyncNotificationRequestResourceInnerLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinesInner from a JSON string
order_status_async_notification_request_resource_inner_lines_inner_instance = OrderStatusAsyncNotificationRequestResourceInnerLinesInner.from_json(json)
# print the JSON string representation of the object
print OrderStatusAsyncNotificationRequestResourceInnerLinesInner.to_json()

# convert the object into a dict
order_status_async_notification_request_resource_inner_lines_inner_dict = order_status_async_notification_request_resource_inner_lines_inner_instance.to_dict()
# create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinesInner from a dict
order_status_async_notification_request_resource_inner_lines_inner_form_dict = order_status_async_notification_request_resource_inner_lines_inner.from_dict(order_status_async_notification_request_resource_inner_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


