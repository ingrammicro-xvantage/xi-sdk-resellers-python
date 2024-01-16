# OrderSearchRequestServicerequestOrderLookupRequestOrderNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **str** |  | 
**order_branch** | **str** |  | 
**order_number** | **str** |  | [optional] 
**distribution_number** | **str** |  | [optional] 
**shipment_number** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_search_request_servicerequest_order_lookup_request_order_number import OrderSearchRequestServicerequestOrderLookupRequestOrderNumber

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchRequestServicerequestOrderLookupRequestOrderNumber from a JSON string
order_search_request_servicerequest_order_lookup_request_order_number_instance = OrderSearchRequestServicerequestOrderLookupRequestOrderNumber.from_json(json)
# print the JSON string representation of the object
print OrderSearchRequestServicerequestOrderLookupRequestOrderNumber.to_json()

# convert the object into a dict
order_search_request_servicerequest_order_lookup_request_order_number_dict = order_search_request_servicerequest_order_lookup_request_order_number_instance.to_dict()
# create an instance of OrderSearchRequestServicerequestOrderLookupRequestOrderNumber from a dict
order_search_request_servicerequest_order_lookup_request_order_number_form_dict = order_search_request_servicerequest_order_lookup_request_order_number.from_dict(order_search_request_servicerequest_order_lookup_request_order_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


