# OrderDetailB2BAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Header level custom field names. | [optional] 
**attribute_value** | **str** | Value of the custom fields. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_b2_b_additional_attributes_inner import OrderDetailB2BAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailB2BAdditionalAttributesInner from a JSON string
order_detail_b2_b_additional_attributes_inner_instance = OrderDetailB2BAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailB2BAdditionalAttributesInner.to_json()

# convert the object into a dict
order_detail_b2_b_additional_attributes_inner_dict = order_detail_b2_b_additional_attributes_inner_instance.to_dict()
# create an instance of OrderDetailB2BAdditionalAttributesInner from a dict
order_detail_b2_b_additional_attributes_inner_form_dict = order_detail_b2_b_additional_attributes_inner.from_dict(order_detail_b2_b_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


