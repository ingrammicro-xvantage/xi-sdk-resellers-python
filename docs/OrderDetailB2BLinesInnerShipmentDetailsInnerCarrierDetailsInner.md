# OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | **str** | The carrier code for the shipment containing the line item. | [optional] 
**carrier_name** | **str** | The name of the carrier of the shipment containing the line item. | [optional] 
**quantity** | **int** | The quantity shipped of the line item. | [optional] 
**shipped_date** | **str** | The actual date when line item shipped. | [optional] 
**estimated_delivery_date** | **str** | The date the line item is expected to be delivered. | [optional] 
**delivered_date** | **str** | The actual date of delivery of the line item. | [optional] 
**carrier_pickup_date** | **str** | The actual date when carrier picked up line item. | [optional] 
**tracking_details** | [**List[OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner]**](OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner.md) | The tracking details for the shipment containing the line item. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner import OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner from a JSON string
order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_instance = OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner.to_json()

# convert the object into a dict
order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_dict = order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner from a dict
order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_form_dict = order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner.from_dict(order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


