# OrderDetailResponseLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_order_number** | **str** | The sub order number. The two-digit prefix is the warehouse code of the warehouse nearest the reseller. The middle number is the order number. The two-digit suffix is the sub order number. | [optional] 
**ingram_order_line_number** | **str** | Unique Ingram Micro line number. Starts with 001. | [optional] 
**vendor_sales_order_line_number** | **str** | The vendor&#39;s sales order line number. | [optional] 
**customer_linenumber** | **str** | The reseller&#39;s line item number for reference in their system. | [optional] 
**line_status** | **str** | The status for the line item in the order. One of- Backordered, In Progress, Shipped, Delivered, Canceled, On Hold | [optional] 
**ingram_part_number** | **str** | Unique IngramMicro part number. | [optional] 
**vendor_part_number** | **str** | The vendor&#39;s part number for the line item. | [optional] 
**vendor_name** | **str** | The vendor&#39;s name for the part in their system. | [optional] 
**part_description** | **str** | The vendor&#39;s description of the part in their system. | [optional] 
**unit_weight** | **float** | The unit weight of the line item. | [optional] 
**weight_uom** | **str** | The unit of measure for the line item. | [optional] 
**unit_price** | **int** | The unit price of the line item. | [optional] 
**upc_code** | **str** | The UPC code of a product. | [optional] 
**extended_price** | **float** | Unit price X quantity for the line item. | [optional] 
**tax_amount** | **float** | The tax amount for the line item. | [optional] 
**currency_code** | **str** | The country-specific three character ISO 4217 currency code for the line item. | [optional] 
**quantity_ordered** | **int** | The quantity ordered of the line item. | [optional] 
**quantity_confirmed** | **int** | The quantity confirmed for the line item. | [optional] 
**quantity_back_ordered** | **int** | The quantity backordered for the line item. | [optional] 
**special_bid_number** | **str** | The line-level bid number provided to the reseller by the vendor for special pricing and discounts. Used to track the bid number in the case of split orders or where different line items have different bid numbers. Line-level bid numbers take precedence over header-level bid numbers. | [optional] 
**requested_delivery_date** | **date** | Reseller-requested delivery date. Delivery date is not guaranteed. | [optional] 
**promised_delivery_date** | **date** | The delivery date promised by IngramMicro. | [optional] 
**line_notes** | **str** | Line-level notes for the order. | [optional] 
**shipment_details** | [**List[OrderDetailResponseLinesInnerShipmentDetailsInner]**](OrderDetailResponseLinesInnerShipmentDetailsInner.md) |  | [optional] 
**additional_attributes** | [**List[OrderDetailResponseLinesInnerAdditionalAttributesInner]**](OrderDetailResponseLinesInnerAdditionalAttributesInner.md) |  | [optional] 
**links** | [**List[OrderDetailResponseLinesInnerLinksInner]**](OrderDetailResponseLinesInnerLinksInner.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_detail_response_lines_inner import OrderDetailResponseLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseLinesInner from a JSON string
order_detail_response_lines_inner_instance = OrderDetailResponseLinesInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseLinesInner.to_json()

# convert the object into a dict
order_detail_response_lines_inner_dict = order_detail_response_lines_inner_instance.to_dict()
# create an instance of OrderDetailResponseLinesInner from a dict
order_detail_response_lines_inner_form_dict = order_detail_response_lines_inner.from_dict(order_detail_response_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


