# OrderDetailResponseMiscellaneousChargesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_order_number** | **str** | The sub order number. The two-digit prefix is the warehouse code of the warehouse nearest the reseller. The middle number is the order number. The two-digit suffix is the sub order number. | [optional] 
**charge_line_reference** | **str** | Impulse line number for the miscellaneous charge. | [optional] 
**charge_description** | **str** | Description of the miscellaneous charges. | [optional] 
**charge_amount** | **float** | The amount of miscellaneous charges. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_detail_response_miscellaneous_charges_inner import OrderDetailResponseMiscellaneousChargesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseMiscellaneousChargesInner from a JSON string
order_detail_response_miscellaneous_charges_inner_instance = OrderDetailResponseMiscellaneousChargesInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseMiscellaneousChargesInner.to_json()

# convert the object into a dict
order_detail_response_miscellaneous_charges_inner_dict = order_detail_response_miscellaneous_charges_inner_instance.to_dict()
# create an instance of OrderDetailResponseMiscellaneousChargesInner from a dict
order_detail_response_miscellaneous_charges_inner_form_dict = order_detail_response_miscellaneous_charges_inner.from_dict(order_detail_response_miscellaneous_charges_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


