# OrderDetailResponseLinesInnerShipmentDetailsInner

Shipping details for the line item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The quantity shipped of the line item. | [optional] 
**estimated_ship_date** | **date** | The estimated ship date for the line item. | [optional] 
**shipped_date** | **date** | The date the line item was shipped. | [optional] 
**estimated_delivery_date** | **date** | The date the line item is expected to be delivered. | [optional] 
**delivered_date** | **date** | The actual date of delivery of the line item. | [optional] 
**ship_from_warehouse_id** | **str** | The ID of the warehouse the product will ship from. | [optional] 
**ship_from_location** | **str** | The city and state the line item ships from. | [optional] 
**invoice_number** | **str** | The Ingram Micro invoice number for the line item. | [optional] 
**invoice_date** | **date** | The date the IngramMicro invoice was created for the line item. | [optional] 
**carrier_details** | [**OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails**](OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_response_lines_inner_shipment_details_inner import OrderDetailResponseLinesInnerShipmentDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseLinesInnerShipmentDetailsInner from a JSON string
order_detail_response_lines_inner_shipment_details_inner_instance = OrderDetailResponseLinesInnerShipmentDetailsInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseLinesInnerShipmentDetailsInner.to_json()

# convert the object into a dict
order_detail_response_lines_inner_shipment_details_inner_dict = order_detail_response_lines_inner_shipment_details_inner_instance.to_dict()
# create an instance of OrderDetailResponseLinesInnerShipmentDetailsInner from a dict
order_detail_response_lines_inner_shipment_details_inner_form_dict = order_detail_response_lines_inner_shipment_details_inner.from_dict(order_detail_response_lines_inner_shipment_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


