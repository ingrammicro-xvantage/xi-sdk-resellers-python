# OrderDetailB2B


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_order_number** | **str** | The IngramMicro sales order number. | [optional] 
**ingram_order_date** | **datetime** | The IngramMicro sales order date. | [optional] 
**order_type** | **str** | The IngramMicro sales order type. | [optional] 
**customer_order_number** | **str** | The reseller&#39;s order number for reference in their system. | [optional] 
**end_customer_order_number** | **str** | The end customer&#39;s order number for reference in their system. | [optional] 
**web_order_id** | **str** | The web order id of the order. | [optional] 
**vendor_sales_order_number** | **str** | The vendor&#39;s order number for reference in their system | [optional] 
**ingram_purchase_order_number** | **str** | Ingram purchase order number. | [optional] 
**order_status** | **str** | The header-level status of the order. One of- Shipped, Canceled, Backordered, Processing, On Hold, Delivered. | [optional] 
**order_total** | **float** | The total cost for the order, includes subtotal, freight charges, and tax. | [optional] 
**order_sub_total** | **float** | The sub total cost for the order, not including tax and freight. | [optional] 
**freight_charges** | **float** | The freight charges for the order. | [optional] 
**currency_code** | **str** | The country-specific three digit ISO 4217 currency code for the order. | [optional] 
**total_weight** | **float** | Total order weight. unit -- North america - Pounds , other countries will be KG. | [optional] 
**total_tax** | **float** | Total tax on the orders placed. | [optional] 
**payment_terms** | **str** | The payment terms of the order. (Ex- Net 30 days). | [optional] 
**notes** | **str** | The header-level notes for the order. | [optional] 
**bill_to_info** | [**OrderDetailB2BBillToInfo**](OrderDetailB2BBillToInfo.md) |  | [optional] 
**ship_to_info** | [**OrderDetailB2BShipToInfo**](OrderDetailB2BShipToInfo.md) |  | [optional] 
**end_user_info** | [**OrderDetailB2BEndUserInfo**](OrderDetailB2BEndUserInfo.md) |  | [optional] 
**lines** | [**List[OrderDetailB2BLinesInner]**](OrderDetailB2BLinesInner.md) |  | [optional] 
**miscellaneous_charges** | [**List[OrderDetailB2BMiscellaneousChargesInner]**](OrderDetailB2BMiscellaneousChargesInner.md) |  | [optional] 
**additional_attributes** | [**List[OrderDetailB2BAdditionalAttributesInner]**](OrderDetailB2BAdditionalAttributesInner.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_detail_b2_b import OrderDetailB2B

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2B from a JSON string
order_detail_b2_b_instance = OrderDetailB2B.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2B.to_json()

# convert the object into a dict
order_detail_b2_b_dict = order_detail_b2_b_instance.to_dict()
# create an instance of OrderDetailB2B from a dict
order_detail_b2_b_form_dict = order_detail_b2_b.from_dict(order_detail_b2_b_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


