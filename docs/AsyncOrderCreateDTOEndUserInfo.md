# AsyncOrderCreateDTOEndUserInfo

The contact information for the end user/customer provided by the reseller. Used to determine pricing and discounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_user_id** | **str** | ID for the end user/customer in Ingram Micro&#39;s system. | [optional] 
**end_user_type** | **str** | End user type | [optional] 
**company_name** | **str** | The company name for the end user/customer. | [optional] 
**name1** | **str** |  | [optional] 
**name2** | **str** |  | [optional] 
**address_line1** | **str** | The address line 1 for the end user/customer. | [optional] 
**address_line2** | **str** | The address line 2 for the end user/customer. | [optional] 
**address_line3** | **str** | The address line 3 for the end user/customer. | [optional] 
**contact** | **str** | The contact name for the end user/customer. | [optional] 
**name3** | **str** |  | [optional] 
**city** | **str** | The end user/customer&#39;s city. | [optional] 
**state** | **str** | The end user/customer&#39;s state. | [optional] 
**postal_code** | **str** | The end user/customer&#39;s zip or postal code. | [optional] 
**address_line4** | **str** | The address line 4 for the end user/customer. | [optional] 
**country_code** | **str** | The end user/customer&#39;s two character ISO country code. | [optional] 
**phone_number** | **str** | The end user/customer&#39;s phone number. | [optional] 
**email** | **str** | The end user/customer&#39;s phone number. | [optional] 

## Example

```python
from xi.sdk.resellers.models.async_order_create_dto_end_user_info import AsyncOrderCreateDTOEndUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOrderCreateDTOEndUserInfo from a JSON string
async_order_create_dto_end_user_info_instance = AsyncOrderCreateDTOEndUserInfo.from_json(json)
# print the JSON string representation of the object
print(AsyncOrderCreateDTOEndUserInfo.to_json())

# convert the object into a dict
async_order_create_dto_end_user_info_dict = async_order_create_dto_end_user_info_instance.to_dict()
# create an instance of AsyncOrderCreateDTOEndUserInfo from a dict
async_order_create_dto_end_user_info_from_dict = AsyncOrderCreateDTOEndUserInfo.from_dict(async_order_create_dto_end_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


