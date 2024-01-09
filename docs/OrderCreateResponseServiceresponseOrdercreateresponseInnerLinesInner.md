# OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linetype** | **str** | “P”-Line or SKU Number “C”-Comment Line | [optional] 
**globallinenumber** | **str** | Ingram generated line number | [optional] 
**partnumber** | **str** | Ingram Micro Sku Number | [optional] 
**globalskuid** | **str** |  | [optional] 
**linenumber** | **str** |  | [optional] 
**carriercode** | **str** | Transportation 2 digit codes | [optional] 
**carrierdescription** | **str** | Transportation Carrier Name | [optional] 
**requestedunitprice** | **float** | Price requested by reseller. Price Variance can be set up by Ingram Micro Sales Rep | [optional] 
**requestedquantity** | **int** | Quanity Requested | [optional] 
**confirmedquantity** | **int** | Quanity Shipped | [optional] 
**backorderedquantity** | **int** | Quanity of units that didn’t ship | [optional] 
**unitproductprice** | **float** | Price Per Unit | [optional] 
**netamount** | **float** | Total amount. Quantity X Unit Price | [optional] 
**warehouseid** | **str** |  | [optional] 
**ordersuffix** | **str** | Use order suffix with the globalorderid for this line item. | [optional] 

## Example

```python
from xi-sdk-python.models.order_create_response_serviceresponse_ordercreateresponse_inner_lines_inner import OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner from a JSON string
order_create_response_serviceresponse_ordercreateresponse_inner_lines_inner_instance = OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner.to_json()

# convert the object into a dict
order_create_response_serviceresponse_ordercreateresponse_inner_lines_inner_dict = order_create_response_serviceresponse_ordercreateresponse_inner_lines_inner_instance.to_dict()
# create an instance of OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner from a dict
order_create_response_serviceresponse_ordercreateresponse_inner_lines_inner_form_dict = order_create_response_serviceresponse_ordercreateresponse_inner_lines_inner.from_dict(order_create_response_serviceresponse_ordercreateresponse_inner_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


