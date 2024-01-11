# OrderDeleteRequestServicerequestRequestpreamble


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isocountrycode** | **str** | Country that Order is being place in. | 
**customer_number** | **str** | Account number order will be billed to. INGRAM MICRO ACCOUNT NUMBER REQUIRED | 

## Example

```python
from xi-sdk-resellers-python.models.order_delete_request_servicerequest_requestpreamble import OrderDeleteRequestServicerequestRequestpreamble

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDeleteRequestServicerequestRequestpreamble from a JSON string
order_delete_request_servicerequest_requestpreamble_instance = OrderDeleteRequestServicerequestRequestpreamble.from_json(json)
# print the JSON string representation of the object
print OrderDeleteRequestServicerequestRequestpreamble.to_json()

# convert the object into a dict
order_delete_request_servicerequest_requestpreamble_dict = order_delete_request_servicerequest_requestpreamble_instance.to_dict()
# create an instance of OrderDeleteRequestServicerequestRequestpreamble from a dict
order_delete_request_servicerequest_requestpreamble_form_dict = order_delete_request_servicerequest_requestpreamble.from_dict(order_delete_request_servicerequest_requestpreamble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


