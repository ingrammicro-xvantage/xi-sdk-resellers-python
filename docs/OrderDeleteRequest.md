# OrderDeleteRequest

Request schema for order delete endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servicerequest** | [**OrderDeleteRequestServicerequest**](OrderDeleteRequestServicerequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_delete_request import OrderDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDeleteRequest from a JSON string
order_delete_request_instance = OrderDeleteRequest.from_json(json)
# print the JSON string representation of the object
print OrderDeleteRequest.to_json()

# convert the object into a dict
order_delete_request_dict = order_delete_request_instance.to_dict()
# create an instance of OrderDeleteRequest from a dict
order_delete_request_form_dict = order_delete_request.from_dict(order_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


