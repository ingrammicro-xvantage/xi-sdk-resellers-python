# OrderCreateV7Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Field for identifying whether it is a reseller or vendor event. For eg, resellers/orders | [optional] 
**event** | **str** | The event sent in the request. For eg, im::create. | [optional] 
**event_time_stamp** | **str** | The timestamp at which the event was sent. | [optional] 
**event_id** | **str** | A unique id used as identifier for the sepcific event and used for generating the x-hub signature. | [optional] 
**event_type** | **str** | The event name sent in the event request. | [optional] 
**resource** | [**OrderCreateV7ResponseResource**](OrderCreateV7ResponseResource.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_response import OrderCreateV7Response

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7Response from a JSON string
order_create_v7_response_instance = OrderCreateV7Response.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7Response.to_json())

# convert the object into a dict
order_create_v7_response_dict = order_create_v7_response_instance.to_dict()
# create an instance of OrderCreateV7Response from a dict
order_create_v7_response_from_dict = OrderCreateV7Response.from_dict(order_create_v7_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


