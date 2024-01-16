# OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carton_number** | **str** | The shipment carton number that contains the line item. | [optional] 
**quantity_inbox** | **str** | The quantity of line items in the box. | [optional] 
**tracking_number** | **str** | The tracking number for the shipment containing the line item. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_package_details_inner import OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner from a JSON string
order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_package_details_inner_instance = OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner.from_json(json)
# print the JSON string representation of the object
print OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner.to_json()

# convert the object into a dict
order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_package_details_inner_dict = order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_package_details_inner_instance.to_dict()
# create an instance of OrderStatusAsyncNotificationRequestResourceInnerLinesInnerShipmentDetailsInnerPackageDetailsInner from a dict
order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_package_details_inner_form_dict = order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_package_details_inner.from_dict(order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_package_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


