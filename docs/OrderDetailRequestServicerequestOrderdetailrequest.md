# OrderDetailRequestServicerequestOrderdetailrequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ordernumber** | **str** | Ingram Micro Order Number | 
**customerponumber** | **str** |  | [optional] 
**orderdate** | **str** |  | [optional] 
**systemid** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_request_servicerequest_orderdetailrequest import OrderDetailRequestServicerequestOrderdetailrequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailRequestServicerequestOrderdetailrequest from a JSON string
order_detail_request_servicerequest_orderdetailrequest_instance = OrderDetailRequestServicerequestOrderdetailrequest.from_json(json)
# print the JSON string representation of the object
print OrderDetailRequestServicerequestOrderdetailrequest.to_json()

# convert the object into a dict
order_detail_request_servicerequest_orderdetailrequest_dict = order_detail_request_servicerequest_orderdetailrequest_instance.to_dict()
# create an instance of OrderDetailRequestServicerequestOrderdetailrequest from a dict
order_detail_request_servicerequest_orderdetailrequest_form_dict = order_detail_request_servicerequest_orderdetailrequest.from_dict(order_detail_request_servicerequest_orderdetailrequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


