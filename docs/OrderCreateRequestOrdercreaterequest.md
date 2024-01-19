# OrderCreateRequestOrdercreaterequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestpreamble** | [**OrderCreateRequestOrdercreaterequestRequestpreamble**](OrderCreateRequestOrdercreaterequestRequestpreamble.md) |  | 
**ordercreatedetails** | [**OrderCreateRequestOrdercreaterequestOrdercreatedetails**](OrderCreateRequestOrdercreaterequestOrdercreatedetails.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_request_ordercreaterequest import OrderCreateRequestOrdercreaterequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestOrdercreaterequest from a JSON string
order_create_request_ordercreaterequest_instance = OrderCreateRequestOrdercreaterequest.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestOrdercreaterequest.to_json()

# convert the object into a dict
order_create_request_ordercreaterequest_dict = order_create_request_ordercreaterequest_instance.to_dict()
# create an instance of OrderCreateRequestOrdercreaterequest from a dict
order_create_request_ordercreaterequest_form_dict = order_create_request_ordercreaterequest.from_dict(order_create_request_ordercreaterequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


