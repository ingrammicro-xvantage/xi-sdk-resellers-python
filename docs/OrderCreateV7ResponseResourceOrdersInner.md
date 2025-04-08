# OrderCreateV7ResponseResourceOrdersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_lines_with_success** | **int** | The number of lines in the order that were successful. | [optional] 
**number_of_lines_with_error** | **int** | The number of lines in the order that have errors. | [optional] 
**number_of_lines_with_warning** | **int** | The number of lines in the order that have a warning. | [optional] 
**ingram_order_number** | **str** | The Ingram Micro order number. | [optional] 
**ingram_order_date** | **str** | The date in UTC format that the order was created in Ingram Micro&#39;s system. | [optional] 
**notes** | **str** | Order-level notes. | [optional] 
**order_type** | **str** | The order typer. One of: S&#x3D;Stocked PO D&#x3D;Direct Ship PO | [optional] 
**order_total** | **float** | The total price for the order. | [optional] 
**freight_charges** | **float** | The total freight charges for the order. | [optional] 
**total_tax** | **float** | The total tax for the order. | [optional] 
**currency_code** | **str** | The country-specific three character ISO 4217 currency code used for the order. | [optional] 
**lines** | [**List[OrderCreateV7ResponseResourceOrdersInnerLinesInner]**](OrderCreateV7ResponseResourceOrdersInnerLinesInner.md) | The line-level details for the order. | [optional] 
**links** | [**List[OrderCreateResponseOrdersInnerLinksInner]**](OrderCreateResponseOrdersInnerLinksInner.md) | Link to Order Details for the order(s). | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_response_resource_orders_inner import OrderCreateV7ResponseResourceOrdersInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7ResponseResourceOrdersInner from a JSON string
order_create_v7_response_resource_orders_inner_instance = OrderCreateV7ResponseResourceOrdersInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7ResponseResourceOrdersInner.to_json())

# convert the object into a dict
order_create_v7_response_resource_orders_inner_dict = order_create_v7_response_resource_orders_inner_instance.to_dict()
# create an instance of OrderCreateV7ResponseResourceOrdersInner from a dict
order_create_v7_response_resource_orders_inner_from_dict = OrderCreateV7ResponseResourceOrdersInner.from_dict(order_create_v7_response_resource_orders_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


