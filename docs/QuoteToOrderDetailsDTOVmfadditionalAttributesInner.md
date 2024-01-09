# QuoteToOrderDetailsDTOVmfadditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the header level field. | [optional] 
**attribute_value** | **str** | The value of the header level field. | [optional] 
**attribute_description** | **str** | The description of the header level field. | [optional] 

## Example

```python
from xi-sdk-python.models.quote_to_order_details_dto_vmfadditional_attributes_inner import QuoteToOrderDetailsDTOVmfadditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteToOrderDetailsDTOVmfadditionalAttributesInner from a JSON string
quote_to_order_details_dto_vmfadditional_attributes_inner_instance = QuoteToOrderDetailsDTOVmfadditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print QuoteToOrderDetailsDTOVmfadditionalAttributesInner.to_json()

# convert the object into a dict
quote_to_order_details_dto_vmfadditional_attributes_inner_dict = quote_to_order_details_dto_vmfadditional_attributes_inner_instance.to_dict()
# create an instance of QuoteToOrderDetailsDTOVmfadditionalAttributesInner from a dict
quote_to_order_details_dto_vmfadditional_attributes_inner_form_dict = quote_to_order_details_dto_vmfadditional_attributes_inner.from_dict(quote_to_order_details_dto_vmfadditional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


