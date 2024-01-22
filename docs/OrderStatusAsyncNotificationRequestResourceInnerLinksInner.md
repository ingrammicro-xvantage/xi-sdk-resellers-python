# OrderStatusAsyncNotificationRequestResourceInnerLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Provides the details of the orders. | [optional] 
**href** | **str** | The URL endpoint for accessing the relevant data. | [optional] 
**type** | **str** | The type of call that can be made to the href link (GET, POST, Etc.).                     | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_links_inner import OrderStatusAsyncNotificationRequestResourceInnerLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinksInner from a JSON string
order_status_async_notification_request_resource_inner_links_inner_instance = OrderStatusAsyncNotificationRequestResourceInnerLinksInner.from_json(json)
# print the JSON string representation of the object
print OrderStatusAsyncNotificationRequestResourceInnerLinksInner.to_json()

# convert the object into a dict
order_status_async_notification_request_resource_inner_links_inner_dict = order_status_async_notification_request_resource_inner_links_inner_instance.to_dict()
# create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinksInner from a dict
order_status_async_notification_request_resource_inner_links_inner_form_dict = order_status_async_notification_request_resource_inner_links_inner.from_dict(order_status_async_notification_request_resource_inner_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


