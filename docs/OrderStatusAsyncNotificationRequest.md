# OrderStatusAsyncNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Field for identifying whether it is a reseller or vendor event. For eg, resellers/orders | [optional] 
**event** | **str** | The event sent in the request. For eg, im::create. | [optional] 
**event_time_stamp** | **str** | The timestamp at which the event was sent. | [optional] 
**event_id** | **str** | A unique id used as identifier for the sepcific event and used for generating the x-hub signature. | [optional] 
**resource** | [**List[OrderStatusAsyncNotificationRequestResourceInner]**](OrderStatusAsyncNotificationRequestResourceInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_status_async_notification_request import OrderStatusAsyncNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusAsyncNotificationRequest from a JSON string
order_status_async_notification_request_instance = OrderStatusAsyncNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(OrderStatusAsyncNotificationRequest.to_json())

# convert the object into a dict
order_status_async_notification_request_dict = order_status_async_notification_request_instance.to_dict()
# create an instance of OrderStatusAsyncNotificationRequest from a dict
order_status_async_notification_request_from_dict = OrderStatusAsyncNotificationRequest.from_dict(order_status_async_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


