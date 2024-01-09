# OrderSearchResponseOrdersInnerSubOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_order_number** | **str** | The sub order number. The two-digit prefix is the warehouse code of the warehouse nearest to the reseller. The middle number is the order number. The two-digit suffix is the sub order number. | [optional] 
**sub_order_total** | **float** | The total for the suborder. | [optional] 
**sub_order_status** | **str** | The status of the suborder. One of:- Shipped, Canceled, Backordered, Processing, On Hold, Delivered | [optional] 
**links** | [**List[OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner]**](OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner.md) | Link to Order Details for the sub order(s). | [optional] 

## Example

```python
from xi-sdk-python.models.order_search_response_orders_inner_sub_orders_inner import OrderSearchResponseOrdersInnerSubOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponseOrdersInnerSubOrdersInner from a JSON string
order_search_response_orders_inner_sub_orders_inner_instance = OrderSearchResponseOrdersInnerSubOrdersInner.from_json(json)
# print the JSON string representation of the object
print OrderSearchResponseOrdersInnerSubOrdersInner.to_json()

# convert the object into a dict
order_search_response_orders_inner_sub_orders_inner_dict = order_search_response_orders_inner_sub_orders_inner_instance.to_dict()
# create an instance of OrderSearchResponseOrdersInnerSubOrdersInner from a dict
order_search_response_orders_inner_sub_orders_inner_form_dict = order_search_response_orders_inner_sub_orders_inner.from_dict(order_search_response_orders_inner_sub_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


