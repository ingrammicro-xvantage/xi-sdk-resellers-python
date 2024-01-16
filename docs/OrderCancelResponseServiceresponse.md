# OrderCancelResponseServiceresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsepreamble** | [**OrderCancelResponseServiceresponseResponsepreamble**](OrderCancelResponseServiceresponseResponsepreamble.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_cancel_response_serviceresponse import OrderCancelResponseServiceresponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCancelResponseServiceresponse from a JSON string
order_cancel_response_serviceresponse_instance = OrderCancelResponseServiceresponse.from_json(json)
# print the JSON string representation of the object
print OrderCancelResponseServiceresponse.to_json()

# convert the object into a dict
order_cancel_response_serviceresponse_dict = order_cancel_response_serviceresponse_instance.to_dict()
# create an instance of OrderCancelResponseServiceresponse from a dict
order_cancel_response_serviceresponse_form_dict = order_cancel_response_serviceresponse.from_dict(order_cancel_response_serviceresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


