# OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addlineorupdateline** | **str** |  | [optional] 
**linenumber** | **str** |  | [optional] 
**customerlinenumber** | **str** |  | [optional] 
**ingrampartnumber** | **str** |  | [optional] 
**quantityordered** | **int** |  | [optional] 
**customerpartnumber** | **str** |  | [optional] 
**linetype** | **str** |  | [optional] 

## Example

```python
from xi-sdk-python.models.order_modify_request_servicerequest_ordermodifyrequest_linedata_inner import OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner from a JSON string
order_modify_request_servicerequest_ordermodifyrequest_linedata_inner_instance = OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner.from_json(json)
# print the JSON string representation of the object
print OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner.to_json()

# convert the object into a dict
order_modify_request_servicerequest_ordermodifyrequest_linedata_inner_dict = order_modify_request_servicerequest_ordermodifyrequest_linedata_inner_instance.to_dict()
# create an instance of OrderModifyRequestServicerequestOrdermodifyrequestLinedataInner from a dict
order_modify_request_servicerequest_ordermodifyrequest_linedata_inner_form_dict = order_modify_request_servicerequest_ordermodifyrequest_linedata_inner.from_dict(order_modify_request_servicerequest_ordermodifyrequest_linedata_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


