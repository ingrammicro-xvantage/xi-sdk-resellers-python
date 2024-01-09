# OrderDeleteResponse

Response schema for order delete endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceresponse** | [**OrderCancelResponseServiceresponse**](OrderCancelResponseServiceresponse.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.order_delete_response import OrderDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDeleteResponse from a JSON string
order_delete_response_instance = OrderDeleteResponse.from_json(json)
# print the JSON string representation of the object
print OrderDeleteResponse.to_json()

# convert the object into a dict
order_delete_response_dict = order_delete_response_instance.to_dict()
# create an instance of OrderDeleteResponse from a dict
order_delete_response_form_dict = order_delete_response.from_dict(order_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


