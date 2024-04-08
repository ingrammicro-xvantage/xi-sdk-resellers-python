# AsyncOrderCreateDTOWarrantyInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_line_link** | **str** |  | [optional] 
**warranty_line_link** | **str** |  | [optional] 
**direct_line_link** | **str** |  | [optional] 
**serial_info** | [**List[AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner]**](AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner.md) |  | [optional] 
**vmf_additional_attributes_lines** | [**List[AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner]**](AsyncOrderCreateDTOWarrantyInfoInnerVmfAdditionalAttributesLinesInner.md) | The object containing the list of fields required at a line level by the vendor. | [optional] 

## Example

```python
from xi.sdk.resellers.models.async_order_create_dto_warranty_info_inner import AsyncOrderCreateDTOWarrantyInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOrderCreateDTOWarrantyInfoInner from a JSON string
async_order_create_dto_warranty_info_inner_instance = AsyncOrderCreateDTOWarrantyInfoInner.from_json(json)
# print the JSON string representation of the object
print(AsyncOrderCreateDTOWarrantyInfoInner.to_json())

# convert the object into a dict
async_order_create_dto_warranty_info_inner_dict = async_order_create_dto_warranty_info_inner_instance.to_dict()
# create an instance of AsyncOrderCreateDTOWarrantyInfoInner from a dict
async_order_create_dto_warranty_info_inner_form_dict = async_order_create_dto_warranty_info_inner.from_dict(async_order_create_dto_warranty_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


