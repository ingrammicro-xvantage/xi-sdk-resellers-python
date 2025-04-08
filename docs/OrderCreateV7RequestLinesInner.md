# OrderCreateV7RequestLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_line_number** | **str** | The reseller&#39;s line item number for reference in their system. The customer line number needs to be a unique numeric value between 1 and 884. In the event we receive duplicate values or alphanumeric values in the customer line number, we will re-sequence the customer line number. To prevent re-sequencing, please use a unique numeric value between 1 and 884 in the customer line number. | [optional] 
**ingram_part_number** | **str** | The unique IngramMicro part number. | [optional] 
**vendor_part_number** | **str** | The vendor&#39;s part number for the line item. | [optional] 
**quantity** | **int** | The requested quantity of the line item. | [optional] 
**unit_price** | **float** | The reseller-requested unit price for the line item. The unit price is not guaranteed. | [optional] 
**special_bid_number** | **str** | The line-level bid number provided to the reseller by the vendor for special pricing and discounts. Used to track the bid number in the case of split orders or where different line items have different bid numbers. Line-level bid number take precedence over header-level bid numbers. | [optional] 
**end_user_price** | **float** | The end-user price. Required for Export Orders. | [optional] 
**notes** | **str** | The attribute field data. | [optional] 
**end_user_info** | [**List[OrderCreateV7RequestLinesInnerEndUserInfoInner]**](OrderCreateV7RequestLinesInnerEndUserInfoInner.md) |  | [optional] 
**additional_attributes** | [**List[OrderCreateV7RequestLinesInnerAdditionalAttributesInner]**](OrderCreateV7RequestLinesInnerAdditionalAttributesInner.md) |  | [optional] 
**vmf_additional_attributes_lines** | [**List[OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner]**](OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_lines_inner import OrderCreateV7RequestLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestLinesInner from a JSON string
order_create_v7_request_lines_inner_instance = OrderCreateV7RequestLinesInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestLinesInner.to_json())

# convert the object into a dict
order_create_v7_request_lines_inner_dict = order_create_v7_request_lines_inner_instance.to_dict()
# create an instance of OrderCreateV7RequestLinesInner from a dict
order_create_v7_request_lines_inner_from_dict = OrderCreateV7RequestLinesInner.from_dict(order_create_v7_request_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


