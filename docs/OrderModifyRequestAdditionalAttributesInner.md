# OrderModifyRequestAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | Example values are &#39;entryMethod&#39;, &#39;enableCommentsAsLines&#39;, &#39;regionCode&#39; | [optional] 
**attribute_value** | **str** | Attribute Value | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_modify_request_additional_attributes_inner import OrderModifyRequestAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyRequestAdditionalAttributesInner from a JSON string
order_modify_request_additional_attributes_inner_instance = OrderModifyRequestAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print OrderModifyRequestAdditionalAttributesInner.to_json()

# convert the object into a dict
order_modify_request_additional_attributes_inner_dict = order_modify_request_additional_attributes_inner_instance.to_dict()
# create an instance of OrderModifyRequestAdditionalAttributesInner from a dict
order_modify_request_additional_attributes_inner_form_dict = order_modify_request_additional_attributes_inner.from_dict(order_modify_request_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


