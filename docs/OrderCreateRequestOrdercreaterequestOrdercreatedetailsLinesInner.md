# OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linetype** | **str** | Values are “P” for product or “C” for comments. This can be left blank when ordering product and a “P” will be assumed.  If you are adding a COMMENT, then this value must be “C”.  Extended spec for comments:   Attribute Name: “commenttext” Attribute Value: “thank you for the order”  To make the comment invisible to the packing slip place “///” in front of the comment in the Attribute Value field.  This will allow the Ingram sales rep to see the comment on the order but will not forward on to shipping documents. | [optional] 
**linenumber** | **str** | This is used when a partner wants to use their own line number. Can be left blank. | [optional] 
**ingrampartnumber** | **str** | This is the Ingram sku number to be used for placing an order. | [optional] 
**quantity** | **str** | The quantity that is to be ordered. | 
**vendorpartnumber** | **str** | The Manufacturer part number. Can be used to place an order instead of the Ingram sku.  If there are multiple Ingram part numbers to one vendor part number.  The order will be rejected. | [optional] 
**customerpartnumber** | **str** | This is the Customers unique part numbers that must be crossed referenced to the Ingram Micro Sku before it can be used.  Please contact your sales rep for additional information on how to set this up. | [optional] 
**upc_code** | **str** |  | [optional] 
**warehouseid** | **str** |  | [optional] 
**unitprice** | **str** | This is a requested price from the customer. Pre-approval is necessary before using this feature.  A methodology called price variance to manage requested pricing needs to be setup in advance by your sales rep.  If unit price is provided without this advanced setup the unit price will be ignored and standard Ingram Micro pricing will apply. | [optional] 
**enduser** | [**OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInnerEnduser**](OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInnerEnduser.md) |  | [optional] 
**productextendedspecs** | [**List[OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInnerProductextendedspecsInner]**](OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInnerProductextendedspecsInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_request_ordercreaterequest_ordercreatedetails_lines_inner import OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner from a JSON string
order_create_request_ordercreaterequest_ordercreatedetails_lines_inner_instance = OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner.to_json()

# convert the object into a dict
order_create_request_ordercreaterequest_ordercreatedetails_lines_inner_dict = order_create_request_ordercreaterequest_ordercreatedetails_lines_inner_instance.to_dict()
# create an instance of OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner from a dict
order_create_request_ordercreaterequest_ordercreatedetails_lines_inner_form_dict = order_create_request_ordercreaterequest_ordercreatedetails_lines_inner.from_dict(order_create_request_ordercreaterequest_ordercreatedetails_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


