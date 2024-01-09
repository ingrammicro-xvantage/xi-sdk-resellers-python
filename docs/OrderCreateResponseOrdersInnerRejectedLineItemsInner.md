# OrderCreateResponseOrdersInnerRejectedLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_linenumber** | **str** | The reseller&#39;s line item number of the rejected item for their reference. Number | [optional] 
**ingram_part_number** | **str** | The Ingram Micro part number for the rejected line item. | [optional] 
**vendor_part_number** | **str** | The vendor part number for the rejected line item. | [optional] 
**quantity_ordered** | **int** | The quantity ordered of the rejected line item. | [optional] 
**reject_code** | **str** | The rejection code for the rejected line item. Ex: &#39;EN&#39;  | [optional] 
**reject_reason** | **str** | The rejection reason for the rejected line item. Ex: &#39;SKU-NOTFOUND    DF41281&#39;  | [optional] 

## Example

```python
from xi-sdk-python.models.order_create_response_orders_inner_rejected_line_items_inner import OrderCreateResponseOrdersInnerRejectedLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseOrdersInnerRejectedLineItemsInner from a JSON string
order_create_response_orders_inner_rejected_line_items_inner_instance = OrderCreateResponseOrdersInnerRejectedLineItemsInner.from_json(json)
# print the JSON string representation of the object
print OrderCreateResponseOrdersInnerRejectedLineItemsInner.to_json()

# convert the object into a dict
order_create_response_orders_inner_rejected_line_items_inner_dict = order_create_response_orders_inner_rejected_line_items_inner_instance.to_dict()
# create an instance of OrderCreateResponseOrdersInnerRejectedLineItemsInner from a dict
order_create_response_orders_inner_rejected_line_items_inner_form_dict = order_create_response_orders_inner_rejected_line_items_inner.from_dict(order_create_response_orders_inner_rejected_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


