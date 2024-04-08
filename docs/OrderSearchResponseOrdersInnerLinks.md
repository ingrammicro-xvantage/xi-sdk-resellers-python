# OrderSearchResponseOrdersInnerLinks

Link to Order Details for the order(s).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Provides the details of the orders. | [optional] 
**href** | **str** | The URL endpoint for accessing the relevant data. | [optional] 
**type** | **str** | The type of call that can be made to the href link (GET, POST, Etc.). | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_search_response_orders_inner_links import OrderSearchResponseOrdersInnerLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponseOrdersInnerLinks from a JSON string
order_search_response_orders_inner_links_instance = OrderSearchResponseOrdersInnerLinks.from_json(json)
# print the JSON string representation of the object
print(OrderSearchResponseOrdersInnerLinks.to_json())

# convert the object into a dict
order_search_response_orders_inner_links_dict = order_search_response_orders_inner_links_instance.to_dict()
# create an instance of OrderSearchResponseOrdersInnerLinks from a dict
order_search_response_orders_inner_links_form_dict = order_search_response_orders_inner_links.from_dict(order_search_response_orders_inner_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


