# OrderModifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_order_number** | **str** | The IngramMicro order number. | [optional] 
**change_description** | **str** | The description of the change. | [optional] 
**order_modified_date** | **str** | The date the order was modified. | [optional] 
**customer_order_number** | **str** | The reseller&#39;s order number for reference in their system. | [optional] 
**end_customer_order_number** | **str** | The end user/customer&#39;s order number for reference in their system. | [optional] 
**order_total** | **float** | The total for the order. | [optional] 
**notes** | **str** | Order-level notes. | [optional] 
**order_sub_total** | **float** | The sub total for the order. | [optional] 
**freight_charges** | **float** | The freight charges for the order. | [optional] 
**total_tax** | **float** | The total tax for the order. | [optional] 
**order_status** | **str** | The status of the order. One of the following. Backordered, In Progress, Shipped, Delivered, Canceled, On Hold | [optional] 
**bill_to_address_id** | **str** | Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit. | [optional] 
**ship_to_info** | [**OrderModifyResponseShipToInfo**](OrderModifyResponseShipToInfo.md) |  | [optional] 
**lines** | [**List[OrderModifyResponseLinesInner]**](OrderModifyResponseLinesInner.md) | The line-level details for the order. | [optional] 
**rejected_line_items** | [**List[OrderModifyResponseRejectedLineItemsInner]**](OrderModifyResponseRejectedLineItemsInner.md) | Details for failed lines in the order. | [optional] 
**additional_attributes** | [**List[OrderModifyResponseLinesInnerAdditionalAttributesInner]**](OrderModifyResponseLinesInnerAdditionalAttributesInner.md) | Header-level additional attributes. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_modify_response import OrderModifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyResponse from a JSON string
order_modify_response_instance = OrderModifyResponse.from_json(json)
# print the JSON string representation of the object
print(OrderModifyResponse.to_json())

# convert the object into a dict
order_modify_response_dict = order_modify_response_instance.to_dict()
# create an instance of OrderModifyResponse from a dict
order_modify_response_form_dict = order_modify_response.from_dict(order_modify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


