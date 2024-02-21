# RenewalsDetailsResponseEndUserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | The contact name for the end user/customer. | [optional] 
**name1** | **str** | The name1 for the end user/customer. | [optional] 
**name2** | **str** | The name2 for the end user/customer. | [optional] 
**company_name** | **str** | The company name for the end user/customer. | [optional] 
**address_line1** | **str** | The address line 1 for the end user/customer. | [optional] 
**address_line2** | **str** | The address line 2 for the end user/customer. | [optional] 
**address_line3** | **str** | The address line 3 for the end user/customer. | [optional] 
**address_line4** | **str** | The address line 4 for the end user/customer. | [optional] 
**city** | **str** | The end user/customer&#39;s city. | [optional] 
**state** | **str** | The end user/customer&#39;s state. | [optional] 
**postal_code** | **str** | The end user/customer&#39;s zip or postal code. | [optional] 
**country_code** | **str** | The end user/customer&#39;s two character ISO country code. | [optional] 
**phone_number** | **str** | The end user/customer&#39;s phone number. | [optional] 
**email** | **str** | The end user/customer&#39;s email. | [optional] 

## Example

```python
from xi.sdk.resellers.models.renewals_details_response_end_user_info import RenewalsDetailsResponseEndUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsDetailsResponseEndUserInfo from a JSON string
renewals_details_response_end_user_info_instance = RenewalsDetailsResponseEndUserInfo.from_json(json)
# print the JSON string representation of the object
print RenewalsDetailsResponseEndUserInfo.to_json()

# convert the object into a dict
renewals_details_response_end_user_info_dict = renewals_details_response_end_user_info_instance.to_dict()
# create an instance of RenewalsDetailsResponseEndUserInfo from a dict
renewals_details_response_end_user_info_form_dict = renewals_details_response_end_user_info.from_dict(renewals_details_response_end_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


