# QuoteToOrderDetailsDTOAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The attribute name. allowDuplicateCustomerOrderNumber: Allow orders with duplicate customer PO numbers. Enables resellers to have the same PO number for multiple orders. enableCommentsAsLines:  It will enable comments as lines. | [optional] 
**attribute_value** | **str** | The attribute field data. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.quote_to_order_details_dto_additional_attributes_inner import QuoteToOrderDetailsDTOAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteToOrderDetailsDTOAdditionalAttributesInner from a JSON string
quote_to_order_details_dto_additional_attributes_inner_instance = QuoteToOrderDetailsDTOAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print QuoteToOrderDetailsDTOAdditionalAttributesInner.to_json()

# convert the object into a dict
quote_to_order_details_dto_additional_attributes_inner_dict = quote_to_order_details_dto_additional_attributes_inner_instance.to_dict()
# create an instance of QuoteToOrderDetailsDTOAdditionalAttributesInner from a dict
quote_to_order_details_dto_additional_attributes_inner_form_dict = quote_to_order_details_dto_additional_attributes_inner.from_dict(quote_to_order_details_dto_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


