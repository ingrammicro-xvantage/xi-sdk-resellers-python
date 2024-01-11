# OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | For orders or invoices. For orders the link provides details of the order. For invoices the link provides details of the invoice. | [optional] 
**href** | **str** | The URL endpoint for accessing the relevant data. | [optional] 
**type** | **str** | The type of call that can be made to the href link (GET, POST, Etc.). | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_search_response_orders_inner_sub_orders_inner_links_inner import OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner from a JSON string
order_search_response_orders_inner_sub_orders_inner_links_inner_instance = OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner.from_json(json)
# print the JSON string representation of the object
print OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner.to_json()

# convert the object into a dict
order_search_response_orders_inner_sub_orders_inner_links_inner_dict = order_search_response_orders_inner_sub_orders_inner_links_inner_instance.to_dict()
# create an instance of OrderSearchResponseOrdersInnerSubOrdersInnerLinksInner from a dict
order_search_response_orders_inner_sub_orders_inner_links_inner_form_dict = order_search_response_orders_inner_sub_orders_inner_links_inner.from_dict(order_search_response_orders_inner_sub_orders_inner_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


