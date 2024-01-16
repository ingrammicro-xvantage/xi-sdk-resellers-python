# OrderSearchRequestServicerequestOrderLookupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_number** | [**OrderSearchRequestServicerequestOrderLookupRequestOrderNumber**](OrderSearchRequestServicerequestOrderLookupRequestOrderNumber.md) |  | [optional] 
**customer_order_number** | [**OrderSearchRequestServicerequestOrderLookupRequestCustomerOrderNumber**](OrderSearchRequestServicerequestOrderLookupRequestCustomerOrderNumber.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_search_request_servicerequest_order_lookup_request import OrderSearchRequestServicerequestOrderLookupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchRequestServicerequestOrderLookupRequest from a JSON string
order_search_request_servicerequest_order_lookup_request_instance = OrderSearchRequestServicerequestOrderLookupRequest.from_json(json)
# print the JSON string representation of the object
print OrderSearchRequestServicerequestOrderLookupRequest.to_json()

# convert the object into a dict
order_search_request_servicerequest_order_lookup_request_dict = order_search_request_servicerequest_order_lookup_request_instance.to_dict()
# create an instance of OrderSearchRequestServicerequestOrderLookupRequest from a dict
order_search_request_servicerequest_order_lookup_request_form_dict = order_search_request_servicerequest_order_lookup_request.from_dict(order_search_request_servicerequest_order_lookup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


