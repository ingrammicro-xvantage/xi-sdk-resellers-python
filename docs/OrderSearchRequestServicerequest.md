# OrderSearchRequestServicerequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestpreamble** | [**OrderSearchRequestServicerequestRequestpreamble**](OrderSearchRequestServicerequestRequestpreamble.md) |  | 
**order_lookup_request** | [**OrderSearchRequestServicerequestOrderLookupRequest**](OrderSearchRequestServicerequestOrderLookupRequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_search_request_servicerequest import OrderSearchRequestServicerequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchRequestServicerequest from a JSON string
order_search_request_servicerequest_instance = OrderSearchRequestServicerequest.from_json(json)
# print the JSON string representation of the object
print OrderSearchRequestServicerequest.to_json()

# convert the object into a dict
order_search_request_servicerequest_dict = order_search_request_servicerequest_instance.to_dict()
# create an instance of OrderSearchRequestServicerequest from a dict
order_search_request_servicerequest_form_dict = order_search_request_servicerequest.from_dict(order_search_request_servicerequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


