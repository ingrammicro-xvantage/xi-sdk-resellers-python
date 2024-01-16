# OrderStatusAsyncNotificationRequestResourceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The event name sent in the event request. | [optional] 
**order_number** | **str** | The Ingram Micro order number. | [optional] 
**customer_order_number** | **str** | The reseller&#39;s unique PO/Order number. | [optional] 
**order_entry_time_stamp** | **str** | The timestamp at which the order was created. | [optional] 
**lines** | [**List[OrderStatusAsyncNotificationRequestResourceInnerLinesInner]**](OrderStatusAsyncNotificationRequestResourceInnerLinesInner.md) | The line-level details for the order. | [optional] 
**links** | [**List[OrderStatusAsyncNotificationRequestResourceInnerLinksInner]**](OrderStatusAsyncNotificationRequestResourceInnerLinksInner.md) | Link to Order Details for the order(s). | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_status_async_notification_request_resource_inner import OrderStatusAsyncNotificationRequestResourceInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusAsyncNotificationRequestResourceInner from a JSON string
order_status_async_notification_request_resource_inner_instance = OrderStatusAsyncNotificationRequestResourceInner.from_json(json)
# print the JSON string representation of the object
print OrderStatusAsyncNotificationRequestResourceInner.to_json()

# convert the object into a dict
order_status_async_notification_request_resource_inner_dict = order_status_async_notification_request_resource_inner_instance.to_dict()
# create an instance of OrderStatusAsyncNotificationRequestResourceInner from a dict
order_status_async_notification_request_resource_inner_form_dict = order_status_async_notification_request_resource_inner.from_dict(order_status_async_notification_request_resource_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


