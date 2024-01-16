# OrderModifyRequestServicerequestOrdermodifyrequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingramorderbranch** | **str** |  | [optional] 
**ingramordernumber** | **str** |  | [optional] 
**ingramorderdist** | **str** |  | [optional] 
**ingramordership** | **str** |  | [optional] 
**customerponumber** | **str** |  | [optional] 
**shipto** | [**OrderModifyRequestServicerequestOrdermodifyrequestShipto**](OrderModifyRequestServicerequestOrdermodifyrequestShipto.md) |  | [optional] 
**headerdata** | [**OrderModifyRequestServicerequestOrdermodifyrequestHeaderdata**](OrderModifyRequestServicerequestOrdermodifyrequestHeaderdata.md) |  | [optional] 
**linedata** | [**List[OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner]**](OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_modify_request_servicerequest_ordermodifyrequest import OrderModifyRequestServicerequestOrdermodifyrequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyRequestServicerequestOrdermodifyrequest from a JSON string
order_modify_request_servicerequest_ordermodifyrequest_instance = OrderModifyRequestServicerequestOrdermodifyrequest.from_json(json)
# print the JSON string representation of the object
print OrderModifyRequestServicerequestOrdermodifyrequest.to_json()

# convert the object into a dict
order_modify_request_servicerequest_ordermodifyrequest_dict = order_modify_request_servicerequest_ordermodifyrequest_instance.to_dict()
# create an instance of OrderModifyRequestServicerequestOrdermodifyrequest from a dict
order_modify_request_servicerequest_ordermodifyrequest_form_dict = order_modify_request_servicerequest_ordermodifyrequest.from_dict(order_modify_request_servicerequest_ordermodifyrequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


