# OrderDetailRequestServicerequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestpreamble** | [**InvoiceDetailRequestServicerequestRequestpreamble**](InvoiceDetailRequestServicerequestRequestpreamble.md) |  | 
**orderdetailrequest** | [**OrderDetailRequestServicerequestOrderdetailrequest**](OrderDetailRequestServicerequestOrderdetailrequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_request_servicerequest import OrderDetailRequestServicerequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailRequestServicerequest from a JSON string
order_detail_request_servicerequest_instance = OrderDetailRequestServicerequest.from_json(json)
# print the JSON string representation of the object
print OrderDetailRequestServicerequest.to_json()

# convert the object into a dict
order_detail_request_servicerequest_dict = order_detail_request_servicerequest_instance.to_dict()
# create an instance of OrderDetailRequestServicerequest from a dict
order_detail_request_servicerequest_form_dict = order_detail_request_servicerequest.from_dict(order_detail_request_servicerequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


