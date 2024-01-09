# OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | **str** | The code for the shipping carrier for the line item. | [optional] 
**carrier_name** | **str** | The name of the shipping carrier for the line item. | [optional] 
**ship_from_warehouse_id** | **str** | The ID of the warehouse the line item will ship from. | [optional] 
**ship_from_location** | **str** | Location from which order is shipped. | [optional] 
**freight_account_number** | **str** | The reseller&#39;s shipping account number with carrier. Used to bill the shipping carrier directly from the reseller&#39;s account with the carrier. | [optional] 
**signature_required** | **str** | Specifies whether a signature is required for delivery. Default is False. | [optional] 
**shipping_instructions** | **str** | The shipping instructions for the order. | [optional] 

## Example

```python
from xi-sdk-python.models.order_create_response_orders_inner_lines_inner_shipment_details_inner import OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner from a JSON string
order_create_response_orders_inner_lines_inner_shipment_details_inner_instance = OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner.to_json()

# convert the object into a dict
order_create_response_orders_inner_lines_inner_shipment_details_inner_dict = order_create_response_orders_inner_lines_inner_shipment_details_inner_instance.to_dict()
# create an instance of OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner from a dict
order_create_response_orders_inner_lines_inner_shipment_details_inner_form_dict = order_create_response_orders_inner_lines_inner_shipment_details_inner.from_dict(order_create_response_orders_inner_lines_inner_shipment_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


