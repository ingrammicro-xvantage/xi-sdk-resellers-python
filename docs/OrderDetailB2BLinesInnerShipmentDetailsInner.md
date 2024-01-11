# OrderDetailB2BLinesInnerShipmentDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The quantity shipped of the line item. | [optional] 
**delivery_number** | **str** | The actual date of delivery of the line item. | [optional] 
**estimated_ship_date** | **str** | The date the line item is expected to be shipped. | [optional] 
**ship_from_warehouse_id** | **str** | The ID of the warehouse the product will ship from. | [optional] 
**ship_from_location** | **str** | The city and state the line item ships from. | [optional] 
**invoice_number** | **str** | The Ingram Micro invoice number for the line item. | [optional] 
**invoice_date** | **str** | The date the IngramMicro invoice was created for the line item. | [optional] 
**carrier_details** | [**List[OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner]**](OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner.md) | The shipment carrier details for the line item. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_detail_b2_b_lines_inner_shipment_details_inner import OrderDetailB2BLinesInnerShipmentDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerShipmentDetailsInner from a JSON string
order_detail_b2_b_lines_inner_shipment_details_inner_instance = OrderDetailB2BLinesInnerShipmentDetailsInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2BLinesInnerShipmentDetailsInner.to_json()

# convert the object into a dict
order_detail_b2_b_lines_inner_shipment_details_inner_dict = order_detail_b2_b_lines_inner_shipment_details_inner_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerShipmentDetailsInner from a dict
order_detail_b2_b_lines_inner_shipment_details_inner_form_dict = order_detail_b2_b_lines_inner_shipment_details_inner.from_dict(order_detail_b2_b_lines_inner_shipment_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


