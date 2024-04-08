# OrderCreateResponseOrdersInnerLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_order_number** | **str** | The sub order number. The two-digit prefix is the warehouse code of the warehouse nearest the reseller. The middle number is the order number. The two-digit suffix is the sub order number. | [optional] 
**ingram_line_number** | **str** | The Ingram Micro line number for the product. | [optional] 
**customer_line_number** | **str** | The reseller&#39;s line number for reference in their system. | [optional] 
**line_status** | **str** | The status for the line item in the order. One of: Backordered, Open | [optional] 
**ingram_part_number** | **str** | The Ingram Micro part number for the line item. | [optional] 
**vendor_part_number** | **str** | The vendor part number for the line item. | [optional] 
**unit_price** | **float** | The unit price for the line item. | [optional] 
**extended_unit_price** | **float** | The extended list price (unit price X quantity) for the line item. | [optional] 
**quantity_ordered** | **int** | The quantity of the line item ordered. | [optional] 
**quantity_confirmed** | **int** | The quantity of the line item that has been confirmed. | [optional] 
**quantity_back_ordered** | **int** | The quantity of the line item that is backordered. | [optional] 
**special_bid_number** | **str** | The bid number for the line item provided to the reseller by the vendor for special pricing and discounts. Line-level bid numbers take precedence over header-level bid numbers. | [optional] 
**notes** | **str** | Line-level notes. | [optional] 
**shipment_details** | [**List[OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner]**](OrderCreateResponseOrdersInnerLinesInnerShipmentDetailsInner.md) | The shipment details for the line item. | [optional] 
**additional_attributes** | [**List[OrderCreateResponseOrdersInnerLinesInnerAdditionalAttributesInner]**](OrderCreateResponseOrdersInnerLinesInnerAdditionalAttributesInner.md) | SAP requested and country-specific line level details. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_response_orders_inner_lines_inner import OrderCreateResponseOrdersInnerLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseOrdersInnerLinesInner from a JSON string
order_create_response_orders_inner_lines_inner_instance = OrderCreateResponseOrdersInnerLinesInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateResponseOrdersInnerLinesInner.to_json())

# convert the object into a dict
order_create_response_orders_inner_lines_inner_dict = order_create_response_orders_inner_lines_inner_instance.to_dict()
# create an instance of OrderCreateResponseOrdersInnerLinesInner from a dict
order_create_response_orders_inner_lines_inner_form_dict = order_create_response_orders_inner_lines_inner.from_dict(order_create_response_orders_inner_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


