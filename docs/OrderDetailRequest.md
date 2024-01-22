# OrderDetailRequest

Request schema for order details endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servicerequest** | [**OrderDetailRequestServicerequest**](OrderDetailRequestServicerequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_request import OrderDetailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailRequest from a JSON string
order_detail_request_instance = OrderDetailRequest.from_json(json)
# print the JSON string representation of the object
print OrderDetailRequest.to_json()

# convert the object into a dict
order_detail_request_dict = order_detail_request_instance.to_dict()
# create an instance of OrderDetailRequest from a dict
order_detail_request_form_dict = order_detail_request.from_dict(order_detail_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


