# OrderDeleteRequestServicerequestOrderDeleteRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_date** | **str** | Date order entered | 
**order_branch** | **str** | Ingram Micro&#39;s first 2 numbers of the order number | 
**order_number** | **str** | Ingram Micro&#39;s middle 6 numbers of the order# | 
**rejection_code** | **str** |  | [optional] 
**distribution_number** | **str** | Ingram Micro&#39;s suffix number of the order# | [optional] 
**shipment_number** | **str** | Ingram Micro&#39;s last number of the order# | [optional] 
**operator_id** | **str** | Ingram ID(not required) | [optional] 

## Example

```python
from xi-sdk-python.models.order_delete_request_servicerequest_order_delete_request_details import OrderDeleteRequestServicerequestOrderDeleteRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDeleteRequestServicerequestOrderDeleteRequestDetails from a JSON string
order_delete_request_servicerequest_order_delete_request_details_instance = OrderDeleteRequestServicerequestOrderDeleteRequestDetails.from_json(json)
# print the JSON string representation of the object
print OrderDeleteRequestServicerequestOrderDeleteRequestDetails.to_json()

# convert the object into a dict
order_delete_request_servicerequest_order_delete_request_details_dict = order_delete_request_servicerequest_order_delete_request_details_instance.to_dict()
# create an instance of OrderDeleteRequestServicerequestOrderDeleteRequestDetails from a dict
order_delete_request_servicerequest_order_delete_request_details_form_dict = order_delete_request_servicerequest_order_delete_request_details.from_dict(order_delete_request_servicerequest_order_delete_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


