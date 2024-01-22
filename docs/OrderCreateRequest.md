# OrderCreateRequest

Request schema for order create endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ordercreaterequest** | [**OrderCreateRequestOrdercreaterequest**](OrderCreateRequestOrdercreaterequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_request import OrderCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequest from a JSON string
order_create_request_instance = OrderCreateRequest.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequest.to_json()

# convert the object into a dict
order_create_request_dict = order_create_request_instance.to_dict()
# create an instance of OrderCreateRequest from a dict
order_create_request_form_dict = order_create_request.from_dict(order_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


