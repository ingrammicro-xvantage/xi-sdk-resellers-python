# AsyncOrderCreateDTOResellerInfo

The address and contact information provided by the reseller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reseller_id** | **str** | The reseller&#39;s Id. | [optional] 
**company_name** | **str** | The reseller&#39;s company name. | [optional] 
**contact** | **str** | The reseller&#39;s contact name. | [optional] 
**address_line1** | **str** | The reseller&#39;s address line 1. | [optional] 
**address_line2** | **str** | The reseller&#39;s address line 2. | [optional] 
**address_line3** | **str** | The reseller&#39;s address line 3. | [optional] 
**address_line4** | **str** | The reseller&#39;s address line 4. | [optional] 
**city** | **str** | The reseller&#39;s city. | [optional] 
**state** | **str** | The reseller&#39;s state. | [optional] 
**postal_code** | **str** | The reseller&#39;s zip or postal code. | [optional] 
**country_code** | **str** | The reseller&#39;s two-character ISO country code. | [optional] 
**phone_number** | **str** | The reseller&#39;s phone number. | [optional] 
**email** | **str** | The reseller&#39;s Email Address. | [optional] 

## Example

```python
from xi.sdk.resellers.models.async_order_create_dto_reseller_info import AsyncOrderCreateDTOResellerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOrderCreateDTOResellerInfo from a JSON string
async_order_create_dto_reseller_info_instance = AsyncOrderCreateDTOResellerInfo.from_json(json)
# print the JSON string representation of the object
print(AsyncOrderCreateDTOResellerInfo.to_json())

# convert the object into a dict
async_order_create_dto_reseller_info_dict = async_order_create_dto_reseller_info_instance.to_dict()
# create an instance of AsyncOrderCreateDTOResellerInfo from a dict
async_order_create_dto_reseller_info_form_dict = async_order_create_dto_reseller_info.from_dict(async_order_create_dto_reseller_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


