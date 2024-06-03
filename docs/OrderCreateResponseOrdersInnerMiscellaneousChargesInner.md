# OrderCreateResponseOrdersInnerMiscellaneousChargesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_order_number** | **str** | The sub order number. The two-digit prefix is the warehouse code of the warehouse nearest the reseller. The middle number is the order number. The two-digit suffix is the sub order number. | [optional] 
**charge_line_reference** | **str** | Impulse line number for the miscellaneous charge. | [optional] 
**charge_description** | **str** | Description of the miscellaneous charges for the order. | [optional] 
**charge_amount** | **float** | The total amount of miscellaneous charges for the order. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_response_orders_inner_miscellaneous_charges_inner import OrderCreateResponseOrdersInnerMiscellaneousChargesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseOrdersInnerMiscellaneousChargesInner from a JSON string
order_create_response_orders_inner_miscellaneous_charges_inner_instance = OrderCreateResponseOrdersInnerMiscellaneousChargesInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateResponseOrdersInnerMiscellaneousChargesInner.to_json())

# convert the object into a dict
order_create_response_orders_inner_miscellaneous_charges_inner_dict = order_create_response_orders_inner_miscellaneous_charges_inner_instance.to_dict()
# create an instance of OrderCreateResponseOrdersInnerMiscellaneousChargesInner from a dict
order_create_response_orders_inner_miscellaneous_charges_inner_from_dict = OrderCreateResponseOrdersInnerMiscellaneousChargesInner.from_dict(order_create_response_orders_inner_miscellaneous_charges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


