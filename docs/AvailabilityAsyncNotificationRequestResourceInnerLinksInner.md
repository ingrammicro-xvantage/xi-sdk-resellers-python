# AvailabilityAsyncNotificationRequestResourceInnerLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Provides the details of the orders. | [optional] 
**href** | **str** | The URL endpoint for accessing the relevant data. | [optional] 
**type** | **str** | The type of call that can be made to the href link (GET, POST, Etc.).             | [optional] 

## Example

```python
from xi.sdk.resellers.models.availability_async_notification_request_resource_inner_links_inner import AvailabilityAsyncNotificationRequestResourceInnerLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilityAsyncNotificationRequestResourceInnerLinksInner from a JSON string
availability_async_notification_request_resource_inner_links_inner_instance = AvailabilityAsyncNotificationRequestResourceInnerLinksInner.from_json(json)
# print the JSON string representation of the object
print(AvailabilityAsyncNotificationRequestResourceInnerLinksInner.to_json())

# convert the object into a dict
availability_async_notification_request_resource_inner_links_inner_dict = availability_async_notification_request_resource_inner_links_inner_instance.to_dict()
# create an instance of AvailabilityAsyncNotificationRequestResourceInnerLinksInner from a dict
availability_async_notification_request_resource_inner_links_inner_form_dict = availability_async_notification_request_resource_inner_links_inner.from_dict(availability_async_notification_request_resource_inner_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


