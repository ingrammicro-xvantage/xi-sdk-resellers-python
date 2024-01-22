# OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner

The tracking details for the shipment containing the line item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_number** | **str** | The tracking number for the shipment containing the line item. | [optional] 
**tracking_url** | **str** | The tracking URL for the shipment containing the line item. | [optional] 
**package_weight** | **str** | The weight of the package for the line item. | [optional] 
**carton_number** | **str** | The shipment carton number that contains the line item. | [optional] 
**quantity_in_box** | **str** | The quantity of line items in the box. | [optional] 
**serial_numbers** | [**List[OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInnerSerialNumbersInner]**](OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInnerSerialNumbersInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner import OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner from a JSON string
order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner_instance = OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner.to_json()

# convert the object into a dict
order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner_dict = order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner_instance.to_dict()
# create an instance of OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner from a dict
order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner_form_dict = order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner.from_dict(order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


