# OrderModifyResponseRejectedLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_line_number** | **str** | The IngramMicro line number for the failed line item. | [optional] 
**customer_line_number** | **str** | The reseller&#39;s line number of the failed line item for reference in their system. | [optional] 
**ingram_part_number** | **str** | The IngramMicro part number for the failed line item. | [optional] 
**vendor_part_number** | **str** | The vendor&#39;s part number for the failed line item. | [optional] 
**quantity_ordered** | **int** | The quantity ordered of the failed line item. | [optional] 
**reject_code** | **str** | The rejection code for the failed line item. | [optional] 
**reject_reason** | **str** | The rejection reason for the failed line item. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_modify_response_rejected_line_items_inner import OrderModifyResponseRejectedLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyResponseRejectedLineItemsInner from a JSON string
order_modify_response_rejected_line_items_inner_instance = OrderModifyResponseRejectedLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(OrderModifyResponseRejectedLineItemsInner.to_json())

# convert the object into a dict
order_modify_response_rejected_line_items_inner_dict = order_modify_response_rejected_line_items_inner_instance.to_dict()
# create an instance of OrderModifyResponseRejectedLineItemsInner from a dict
order_modify_response_rejected_line_items_inner_form_dict = order_modify_response_rejected_line_items_inner.from_dict(order_modify_response_rejected_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


