# OrderCreateResponseOrdersInnerLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Provides the details of the orders. | [optional] 
**href** | **str** | The URL endpoint for accessing the relevant data. | [optional] 
**type** | **str** | The type of call that can be made to the href link (GET, POST, Etc.). | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_response_orders_inner_links_inner import OrderCreateResponseOrdersInnerLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseOrdersInnerLinksInner from a JSON string
order_create_response_orders_inner_links_inner_instance = OrderCreateResponseOrdersInnerLinksInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateResponseOrdersInnerLinksInner.to_json())

# convert the object into a dict
order_create_response_orders_inner_links_inner_dict = order_create_response_orders_inner_links_inner_instance.to_dict()
# create an instance of OrderCreateResponseOrdersInnerLinksInner from a dict
order_create_response_orders_inner_links_inner_from_dict = OrderCreateResponseOrdersInnerLinksInner.from_dict(order_create_response_orders_inner_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


