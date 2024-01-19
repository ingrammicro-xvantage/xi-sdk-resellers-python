# OrderDetailResponseServiceresponseOrderdetailresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ordernumber** | **str** |  | [optional] 
**ordertype** | **str** | Order Type   B - BRANCH TRANSFER C - CASH ORDER D - DIRECT ORDER F - FUTURE ORDER P - SPECIAL ORDER Q - QUOTE ORDER S - STOCK ORDER M - MEMO ORDER | [optional] 
**customerordernumber** | **str** | Customer PO number | [optional] 
**enduserponumber** | **str** | End User PO number | [optional] 
**orderstatus** | **str** | Status of order within Ingram system S - SALES HOLD H - TAG HOLD I - INVOICED P - PENDING E - BILLING ERROR F - FORCE BILLING V - VOIDED T - TRANSFERRED D - HOLD SHIPMENT R - RELEASED O - IM ONLINE HOLD U - BILL FOR HISTORY ONLY W - ORDER NOT PRINTED A - DROP SHIP HOLD B - INTERNET CUST ORIG HOLD 1 - PICKED 2 - INSPECTED 3 - PACKED 4 - SHIPPED C - CREDIT HOLD 9 - CISCO 3A6 Q - RMA HOLD G - CREDIT HOLD N - CREDIT HOLD | [optional] 
**entrytimestamp** | **str** | Time stamp of the order placed | [optional] 
**entrymethoddescription** | **str** | Description of the entry method  | [optional] 
**ordertotalvalue** | **float** | Total order value | [optional] 
**ordersubtotal** | **float** | Subtotal order value | [optional] 
**freightamount** | **str** | Freight charges | [optional] 
**currencycode** | **str** | Country specific currency code | [optional] 
**totalweight** | **str** | Total order weight. unit -- North america - Pounds , other countries will be KG | [optional] 
**totaltax** | **str** | total tax on the orders placed | [optional] 
**billtoaddress** | [**OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress**](OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress.md) |  | [optional] 
**shiptoaddress** | [**OrderDetailResponseServiceresponseOrderdetailresponseShiptoaddress**](OrderDetailResponseServiceresponseOrderdetailresponseShiptoaddress.md) |  | [optional] 
**enduserinfo** | [**OrderDetailResponseServiceresponseOrderdetailresponseEnduserinfo**](OrderDetailResponseServiceresponseOrderdetailresponseEnduserinfo.md) |  | [optional] 
**lines** | [**List[OrderDetailResponseServiceresponseOrderdetailresponseLinesInner]**](OrderDetailResponseServiceresponseOrderdetailresponseLinesInner.md) |  | [optional] 
**commentlines** | [**List[OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner]**](OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner.md) |  | [optional] 
**miscfeeline** | [**List[OrderDetailResponseServiceresponseOrderdetailresponseMiscfeelineInner]**](OrderDetailResponseServiceresponseOrderdetailresponseMiscfeelineInner.md) |  | [optional] 
**extendedspecs** | [**List[OrderDetailResponseServiceresponseOrderdetailresponseExtendedspecsInner]**](OrderDetailResponseServiceresponseOrderdetailresponseExtendedspecsInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_response_serviceresponse_orderdetailresponse import OrderDetailResponseServiceresponseOrderdetailresponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseServiceresponseOrderdetailresponse from a JSON string
order_detail_response_serviceresponse_orderdetailresponse_instance = OrderDetailResponseServiceresponseOrderdetailresponse.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseServiceresponseOrderdetailresponse.to_json()

# convert the object into a dict
order_detail_response_serviceresponse_orderdetailresponse_dict = order_detail_response_serviceresponse_orderdetailresponse_instance.to_dict()
# create an instance of OrderDetailResponseServiceresponseOrderdetailresponse from a dict
order_detail_response_serviceresponse_orderdetailresponse_form_dict = order_detail_response_serviceresponse_orderdetailresponse.from_dict(order_detail_response_serviceresponse_orderdetailresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


