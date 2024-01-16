# OrderModifyRequestServicerequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestpreamble** | [**OrderModifyRequestServicerequestRequestpreamble**](OrderModifyRequestServicerequestRequestpreamble.md) |  | [optional] 
**ordermodifyrequest** | [**OrderModifyRequestServicerequestOrdermodifyrequest**](OrderModifyRequestServicerequestOrdermodifyrequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_modify_request_servicerequest import OrderModifyRequestServicerequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyRequestServicerequest from a JSON string
order_modify_request_servicerequest_instance = OrderModifyRequestServicerequest.from_json(json)
# print the JSON string representation of the object
print OrderModifyRequestServicerequest.to_json()

# convert the object into a dict
order_modify_request_servicerequest_dict = order_modify_request_servicerequest_instance.to_dict()
# create an instance of OrderModifyRequestServicerequest from a dict
order_modify_request_servicerequest_form_dict = order_modify_request_servicerequest.from_dict(order_modify_request_servicerequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


