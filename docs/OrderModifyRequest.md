# OrderModifyRequest

Request schema for order modify endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servicerequest** | [**OrderModifyRequestServicerequest**](OrderModifyRequestServicerequest.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.order_modify_request import OrderModifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyRequest from a JSON string
order_modify_request_instance = OrderModifyRequest.from_json(json)
# print the JSON string representation of the object
print OrderModifyRequest.to_json()

# convert the object into a dict
order_modify_request_dict = order_modify_request_instance.to_dict()
# create an instance of OrderModifyRequest from a dict
order_modify_request_form_dict = order_modify_request.from_dict(order_modify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


