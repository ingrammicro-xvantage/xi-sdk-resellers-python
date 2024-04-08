# OrderModifyResponseLinesInnerShipmentDetails

Shipping details for the order provided by the reseller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | **str** | The carrier code for the shipment containing the line item. | [optional] 
**carrier_name** | **str** | The name of the carrier of the shipment containing the line item. | [optional] 
**freight_account_number** | **str** | The reseller&#39;s shipping account number with carrier. Used to bill the shipping carrier directly from the reseller&#39;s account with the carrier. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_modify_response_lines_inner_shipment_details import OrderModifyResponseLinesInnerShipmentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyResponseLinesInnerShipmentDetails from a JSON string
order_modify_response_lines_inner_shipment_details_instance = OrderModifyResponseLinesInnerShipmentDetails.from_json(json)
# print the JSON string representation of the object
print(OrderModifyResponseLinesInnerShipmentDetails.to_json())

# convert the object into a dict
order_modify_response_lines_inner_shipment_details_dict = order_modify_response_lines_inner_shipment_details_instance.to_dict()
# create an instance of OrderModifyResponseLinesInnerShipmentDetails from a dict
order_modify_response_lines_inner_shipment_details_form_dict = order_modify_response_lines_inner_shipment_details.from_dict(order_modify_response_lines_inner_shipment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


