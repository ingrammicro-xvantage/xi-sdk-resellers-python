# AvailabilityAsyncNotificationRequestResourceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | The event name sent in the event request. | [optional] 
**ingram_part_number** | **str** | The Unique IngramMicro part number for the product. | [optional] 
**vendor_part_number** | **str** | The vendors part number for the product. | [optional] 
**vendor_name** | **str** | The name of the vendor/manufacturer of the product. | [optional] 
**upc_code** | **str** | The UPC code for the product. Consists of 12 numeric digits that are uniquly assigned to each trade item. | [optional] 
**sku_status** | **str** | Status returned saying whether sku is active. | [optional] 
**back_order_flag** | **str** | Backordered Flag. | [optional] 
**total_availability** | **str** | totalAvailability. | [optional] 
**links** | [**List[AvailabilityAsyncNotificationRequestResourceInnerLinksInner]**](AvailabilityAsyncNotificationRequestResourceInnerLinksInner.md) | Link to Order Details for the order(s). | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.availability_async_notification_request_resource_inner import AvailabilityAsyncNotificationRequestResourceInner

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilityAsyncNotificationRequestResourceInner from a JSON string
availability_async_notification_request_resource_inner_instance = AvailabilityAsyncNotificationRequestResourceInner.from_json(json)
# print the JSON string representation of the object
print AvailabilityAsyncNotificationRequestResourceInner.to_json()

# convert the object into a dict
availability_async_notification_request_resource_inner_dict = availability_async_notification_request_resource_inner_instance.to_dict()
# create an instance of AvailabilityAsyncNotificationRequestResourceInner from a dict
availability_async_notification_request_resource_inner_form_dict = availability_async_notification_request_resource_inner.from_dict(availability_async_notification_request_resource_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


