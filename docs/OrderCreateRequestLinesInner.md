# OrderCreateRequestLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_line_number** | **str** | The reseller&#39;s line item number for reference in their system. The customer line number needs to be a unique numeric value between 1 and 884. In the event we receive duplicate values or alphanumeric values in the customer line number, we will re-sequence the customer line number. To prevent re-sequencing, please use a unique numeric value between 1 and 884 in the customer line number. | [optional] 
**ingram_part_number** | **str** | The unique IngramMicro part number. | [optional] 
**quantity** | **int** | The requested quantity of the line item. | [optional] 
**special_bid_number** | **str** | The line-level bid number provided to the reseller by the vendor for special pricing and discounts. Used to track the bid number in the case of split orders or where different line items have different bid numbers. Line-level bid number take precedence over header-level bid numbers. | [optional] 
**notes** | **str** | Line-level notes. | [optional] 
**unit_price** | **float** | The reseller-requested unit price for the line item. The unit price is not guaranteed. | [optional] 
**end_user_price** | **float** | The end user price. | [optional] 
**additional_attributes** | [**List[OrderCreateRequestLinesInnerAdditionalAttributesInner]**](OrderCreateRequestLinesInnerAdditionalAttributesInner.md) |  | [optional] 
**warranty_info** | [**List[OrderCreateRequestLinesInnerWarrantyInfoInner]**](OrderCreateRequestLinesInnerWarrantyInfoInner.md) | Warranty details for the line. This is required in case of warranty orders. | [optional] 
**end_user_info** | [**List[OrderCreateRequestLinesInnerEndUserInfoInner]**](OrderCreateRequestLinesInnerEndUserInfoInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_request_lines_inner import OrderCreateRequestLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestLinesInner from a JSON string
order_create_request_lines_inner_instance = OrderCreateRequestLinesInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateRequestLinesInner.to_json())

# convert the object into a dict
order_create_request_lines_inner_dict = order_create_request_lines_inner_instance.to_dict()
# create an instance of OrderCreateRequestLinesInner from a dict
order_create_request_lines_inner_form_dict = order_create_request_lines_inner.from_dict(order_create_request_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


