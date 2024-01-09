# OrderDeleteRequestServicerequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestpreamble** | [**OrderDeleteRequestServicerequestRequestpreamble**](OrderDeleteRequestServicerequestRequestpreamble.md) |  | 
**order_delete_request_details** | [**OrderDeleteRequestServicerequestOrderDeleteRequestDetails**](OrderDeleteRequestServicerequestOrderDeleteRequestDetails.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.order_delete_request_servicerequest import OrderDeleteRequestServicerequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDeleteRequestServicerequest from a JSON string
order_delete_request_servicerequest_instance = OrderDeleteRequestServicerequest.from_json(json)
# print the JSON string representation of the object
print OrderDeleteRequestServicerequest.to_json()

# convert the object into a dict
order_delete_request_servicerequest_dict = order_delete_request_servicerequest_instance.to_dict()
# create an instance of OrderDeleteRequestServicerequest from a dict
order_delete_request_servicerequest_form_dict = order_delete_request_servicerequest.from_dict(order_delete_request_servicerequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


