# AsyncOrderCreateDTOLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_line_number** | **str** | The reseller&#39;s line item number for reference in their system. | [optional] 
**ingram_part_number** | **str** | Unique IngramMicro part number. | [optional] 
**quantity** | **str** | The quantity of the line item. | [optional] 
**unit_price** | **str** | Unit Price of Item | [optional] 
**special_bid_number** | **str** |  | [optional] 
**end_user_price** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**end_user_info** | [**List[AsyncOrderCreateDTOLinesInnerEndUserInfoInner]**](AsyncOrderCreateDTOLinesInnerEndUserInfoInner.md) | The contact information for the end user/customer provided by the reseller. Used to determine pricing and discounts. | [optional] 

## Example

```python
from xi.sdk.resellers.models.async_order_create_dto_lines_inner import AsyncOrderCreateDTOLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOrderCreateDTOLinesInner from a JSON string
async_order_create_dto_lines_inner_instance = AsyncOrderCreateDTOLinesInner.from_json(json)
# print the JSON string representation of the object
print(AsyncOrderCreateDTOLinesInner.to_json())

# convert the object into a dict
async_order_create_dto_lines_inner_dict = async_order_create_dto_lines_inner_instance.to_dict()
# create an instance of AsyncOrderCreateDTOLinesInner from a dict
async_order_create_dto_lines_inner_from_dict = AsyncOrderCreateDTOLinesInner.from_dict(async_order_create_dto_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


