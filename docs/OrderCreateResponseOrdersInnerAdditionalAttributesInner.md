# OrderCreateResponseOrdersInnerAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** |  allowPartialOrder: Allow orders with failed lines. (SAP) Depends on backorder settings.   dpasRating: DX rating by Department of Defense is the highest rating by the highest offices and meant to be top priority. DO any other gov offices at the federal level to priotize.   dpasProgramId: Identifies the actual agency that signed off on the DPAS priority.   storageLocation: Determine the location of the product stock in SAP for Marketplaces.  soldTo: To be used in cases when Sold-To is different than Customer ID.  Z101: Used for end customer details such as name, address, phone, etc. This information flows to SAP and is used by warehouse.  euDepId: DEP ID would be the &#39;End User DEP/ABM Organization ID&#39; up to 32 characters and is assigned by Apple.  depOrderNbr: depordernbr is &#39;End User PO to reseller&#39; Can appear in message lines or dedicated end user po#.   | [optional] 
**attribute_value** | **str** | Attribute value | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_create_response_orders_inner_additional_attributes_inner import OrderCreateResponseOrdersInnerAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseOrdersInnerAdditionalAttributesInner from a JSON string
order_create_response_orders_inner_additional_attributes_inner_instance = OrderCreateResponseOrdersInnerAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateResponseOrdersInnerAdditionalAttributesInner.to_json()

# convert the object into a dict
order_create_response_orders_inner_additional_attributes_inner_dict = order_create_response_orders_inner_additional_attributes_inner_instance.to_dict()
# create an instance of OrderCreateResponseOrdersInnerAdditionalAttributesInner from a dict
order_create_response_orders_inner_additional_attributes_inner_form_dict = order_create_response_orders_inner_additional_attributes_inner.from_dict(order_create_response_orders_inner_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


