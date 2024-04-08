# AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_of_purchase** | **str** |  | [optional] 
**ship_date** | **str** |  | [optional] 
**primary_serial_number** | **str** |  | [optional] 
**secondary_serial_number** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.async_order_create_dto_warranty_info_inner_serial_info_inner import AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner from a JSON string
async_order_create_dto_warranty_info_inner_serial_info_inner_instance = AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner.from_json(json)
# print the JSON string representation of the object
print(AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner.to_json())

# convert the object into a dict
async_order_create_dto_warranty_info_inner_serial_info_inner_dict = async_order_create_dto_warranty_info_inner_serial_info_inner_instance.to_dict()
# create an instance of AsyncOrderCreateDTOWarrantyInfoInnerSerialInfoInner from a dict
async_order_create_dto_warranty_info_inner_serial_info_inner_form_dict = async_order_create_dto_warranty_info_inner_serial_info_inner.from_dict(async_order_create_dto_warranty_info_inner_serial_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


