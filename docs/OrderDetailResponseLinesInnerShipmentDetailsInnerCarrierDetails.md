# OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails

The shipment carrier details for the line item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | **str** | The carrier code for the shipment containing the line item. | [optional] 
**carrier_name** | **str** | The name of the carrier of the shipment containing the line item. | [optional] 
**tracking_details** | [**List[OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner]**](OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details import OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails from a JSON string
order_detail_response_lines_inner_shipment_details_inner_carrier_details_instance = OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails.to_json()

# convert the object into a dict
order_detail_response_lines_inner_shipment_details_inner_carrier_details_dict = order_detail_response_lines_inner_shipment_details_inner_carrier_details_instance.to_dict()
# create an instance of OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetails from a dict
order_detail_response_lines_inner_shipment_details_inner_carrier_details_form_dict = order_detail_response_lines_inner_shipment_details_inner_carrier_details.from_dict(order_detail_response_lines_inner_shipment_details_inner_carrier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


