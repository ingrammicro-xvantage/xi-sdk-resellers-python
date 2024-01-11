# OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_number** | **str** | The tracking number for the shipment containing the line item. | [optional] 
**tracking_url** | **str** | The tracking URL for the shipment containing the line item. | [optional] 
**package_weight** | **str** | The weight of the package for the line item. | [optional] 
**carton_number** | **str** | The shipment carton number that contains the line item. | [optional] 
**quantity_in_box** | **str** | The quantity of line items in the box. | [optional] 
**serial_numbers** | [**List[OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInnerSerialNumbersInner]**](OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInnerSerialNumbersInner.md) | A list of serial numbers of the line items contained in the shipment. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner import OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner from a JSON string
order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner_instance = OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner.to_json()

# convert the object into a dict
order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner_dict = order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner_instance.to_dict()
# create an instance of OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner from a dict
order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner_form_dict = order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner.from_dict(order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


