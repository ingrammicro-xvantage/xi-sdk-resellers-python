# OrderDetailResponseServiceresponseOrderdetailresponseLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linenumber** | **str** | Impulse line number | [optional] 
**globallinenumber** | **str** | Line of the Globel Sku / Customer Line Number | [optional] 
**ordersuffix** | **str** | Order Suffix | [optional] 
**erpordernumber** | **str** | Sales order number | [optional] 
**linestatus** | **str** | Status of the line | [optional] 
**partnumber** | **str** | Ingram part number | [optional] 
**manufacturerpartnumber** | **str** | manufacture number of the product | [optional] 
**vendorname** | **str** | name of the vendor | [optional] 
**vendorcode** | **str** | Ingram Micro assigned code for the vendor | [optional] 
**partdescription1** | **str** |  | [optional] 
**partdescription2** | **str** |  | [optional] 
**unitweight** | **str** | weight of the product unit | [optional] 
**unitprice** | **float** | Customer price of the unit | [optional] 
**extendedprice** | **float** | extended price of the order | [optional] 
**taxamount** | **float** | tax amount for the order | [optional] 
**requestedquantity** | **str** | no. of units requested | [optional] 
**confirmedquantity** | **str** | no. of units confirmed available | [optional] 
**backorderquantity** | **str** | quantity of back order | [optional] 
**serialnumberdetails** | [**List[OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerSerialnumberdetailsInner]**](OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerSerialnumberdetailsInner.md) |  | [optional] 
**trackingnumber** | **List[str]** |  | [optional] 
**shipmentdetails** | [**List[OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerShipmentdetailsInner]**](OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerShipmentdetailsInner.md) |  | [optional] 
**productextendedspecs** | [**List[InvoiceDetailResponseServiceresponseInvoicedetailresponseExtendedspecsInner]**](InvoiceDetailResponseServiceresponseInvoicedetailresponseExtendedspecsInner.md) |  | [optional] 
**backorderetadate** | **str** | estimated date of back order | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_response_serviceresponse_orderdetailresponse_lines_inner import OrderDetailResponseServiceresponseOrderdetailresponseLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseServiceresponseOrderdetailresponseLinesInner from a JSON string
order_detail_response_serviceresponse_orderdetailresponse_lines_inner_instance = OrderDetailResponseServiceresponseOrderdetailresponseLinesInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseServiceresponseOrderdetailresponseLinesInner.to_json()

# convert the object into a dict
order_detail_response_serviceresponse_orderdetailresponse_lines_inner_dict = order_detail_response_serviceresponse_orderdetailresponse_lines_inner_instance.to_dict()
# create an instance of OrderDetailResponseServiceresponseOrderdetailresponseLinesInner from a dict
order_detail_response_serviceresponse_orderdetailresponse_lines_inner_form_dict = order_detail_response_serviceresponse_orderdetailresponse_lines_inner.from_dict(order_detail_response_serviceresponse_orderdetailresponse_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


