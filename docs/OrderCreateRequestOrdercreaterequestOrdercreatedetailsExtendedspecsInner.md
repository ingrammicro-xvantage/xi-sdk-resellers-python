# OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner

Attribute Name and Value: This field identifies if your order is a DIRECT SHIP order (license / warranty) or how you want your Backorders managed as well as other process options like placing your order on hold or adding a comment. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributename** | **str** |  | [optional] 
**attributevalue** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_create_request_ordercreaterequest_ordercreatedetails_extendedspecs_inner import OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner from a JSON string
order_create_request_ordercreaterequest_ordercreatedetails_extendedspecs_inner_instance = OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner.to_json()

# convert the object into a dict
order_create_request_ordercreaterequest_ordercreatedetails_extendedspecs_inner_dict = order_create_request_ordercreaterequest_ordercreatedetails_extendedspecs_inner_instance.to_dict()
# create an instance of OrderCreateRequestOrdercreaterequestOrdercreatedetailsExtendedspecsInner from a dict
order_create_request_ordercreaterequest_ordercreatedetails_extendedspecs_inner_form_dict = order_create_request_ordercreaterequest_ordercreatedetails_extendedspecs_inner.from_dict(order_create_request_ordercreaterequest_ordercreatedetails_extendedspecs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


