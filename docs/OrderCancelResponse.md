# OrderCancelResponse

Response schema for order delete endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceresponse** | [**OrderCancelResponseServiceresponse**](OrderCancelResponseServiceresponse.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_cancel_response import OrderCancelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCancelResponse from a JSON string
order_cancel_response_instance = OrderCancelResponse.from_json(json)
# print the JSON string representation of the object
print OrderCancelResponse.to_json()

# convert the object into a dict
order_cancel_response_dict = order_cancel_response_instance.to_dict()
# create an instance of OrderCancelResponse from a dict
order_cancel_response_form_dict = order_cancel_response.from_dict(order_cancel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


