# AsyncOrderCreateDTOAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The attribute name. allowDuplicateCustomerOrderNumber: Allow orders with duplicate customer PO numbers. Enables resellers to have the same PO number for multiple orders. enableCommentsAsLines:  It will enable comments as lines. | [optional] 
**attribute_value** | **str** | The attribute field data. | [optional] 

## Example

```python
from xi.sdk.resellers.models.async_order_create_dto_additional_attributes_inner import AsyncOrderCreateDTOAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOrderCreateDTOAdditionalAttributesInner from a JSON string
async_order_create_dto_additional_attributes_inner_instance = AsyncOrderCreateDTOAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print(AsyncOrderCreateDTOAdditionalAttributesInner.to_json())

# convert the object into a dict
async_order_create_dto_additional_attributes_inner_dict = async_order_create_dto_additional_attributes_inner_instance.to_dict()
# create an instance of AsyncOrderCreateDTOAdditionalAttributesInner from a dict
async_order_create_dto_additional_attributes_inner_form_dict = async_order_create_dto_additional_attributes_inner.from_dict(async_order_create_dto_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


