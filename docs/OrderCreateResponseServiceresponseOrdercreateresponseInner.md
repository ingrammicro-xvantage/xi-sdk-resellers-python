# OrderCreateResponseServiceresponseOrdercreateresponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numberoflineswithsuccess** | **str** | Number of line items that were successful | [optional] 
**numberoflineswitherror** | **str** | Number of line items with error | [optional] 
**numberoflineswithwarning** | **str** | Number of line items with warnings | [optional] 
**globalorderid** | **str** | Ingram sales order number | [optional] 
**ordertype** | **str** | S&#x3D;Stocked PO D&#x3D;Direct Ship PO | [optional] 
**ordertimestamp** | **str** | Time order received | [optional] 
**invoicingsystemorderid** | **str** | Ingram Micro generated order number | [optional] 
**taxamount** | **float** |  | [optional] 
**freightamount** | **float** | Freight amount customer pays for freight | [optional] 
**orderamount** | **float** | Total amount of order with freight and taxes | [optional] 
**lines** | [**List[OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner]**](OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner.md) | Collection of lines | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.order_create_response_serviceresponse_ordercreateresponse_inner import OrderCreateResponseServiceresponseOrdercreateresponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseServiceresponseOrdercreateresponseInner from a JSON string
order_create_response_serviceresponse_ordercreateresponse_inner_instance = OrderCreateResponseServiceresponseOrdercreateresponseInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateResponseServiceresponseOrdercreateresponseInner.to_json()

# convert the object into a dict
order_create_response_serviceresponse_ordercreateresponse_inner_dict = order_create_response_serviceresponse_ordercreateresponse_inner_instance.to_dict()
# create an instance of OrderCreateResponseServiceresponseOrdercreateresponseInner from a dict
order_create_response_serviceresponse_ordercreateresponse_inner_form_dict = order_create_response_serviceresponse_ordercreateresponse_inner.from_dict(order_create_response_serviceresponse_ordercreateresponse_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


