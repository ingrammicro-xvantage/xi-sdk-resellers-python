# OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerShipmentdetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | quantity shipped | [optional] 
**shipmentdate** | **str** | date of shipment | [optional] 
**shipfromwarehouseid** | **str** | Warehouse product was shipped from | [optional] 
**warehousename** | **str** | name of the warehouse | [optional] 
**invoicenumber** | **str** | Invoice Number | [optional] 
**invoicedate** | **str** | date on the invoice generated | [optional] 
**status** | **str** | code for current Status of the order | [optional] 
**statusdescription** | **str** | Description of status | [optional] 
**shippeddate** | **str** | date of shipment | [optional] 
**holdreasoncodedescription** | **str** | Description of the code if the order is on hold | [optional] 
**ponumber** | **str** | Ingram PO Number to vendors for direct ship orders | [optional] 
**carriertype** | **str** | Helps to determine shipment type. for e.g. LTL is used for heavy shipment. SML is used for light shipment | [optional] 
**carriercode** | **str** |  | [optional] 
**carriername** | **str** | Name of the carrier. If carriername is LTL then the tracking info is in the \&quot;pronumber\&quot; data field | [optional] 
**pronumber** | **str** |  | [optional] 
**packagedetails** | [**OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerShipmentdetailsInnerPackagedetails**](OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerShipmentdetailsInnerPackagedetails.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.order_detail_response_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner import OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerShipmentdetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerShipmentdetailsInner from a JSON string
order_detail_response_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner_instance = OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerShipmentdetailsInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerShipmentdetailsInner.to_json()

# convert the object into a dict
order_detail_response_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner_dict = order_detail_response_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner_instance.to_dict()
# create an instance of OrderDetailResponseServiceresponseOrderdetailresponseLinesInnerShipmentdetailsInner from a dict
order_detail_response_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner_form_dict = order_detail_response_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner.from_dict(order_detail_response_serviceresponse_orderdetailresponse_lines_inner_shipmentdetails_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


