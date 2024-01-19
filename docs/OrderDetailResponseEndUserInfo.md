# OrderDetailResponseEndUserInfo

The contact information for the end user/customer provided by the reseller. Used to determine pricing and discounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | The contact name for the end user/customer. | [optional] 
**company_name** | **str** | The company name for the end user/customer. | [optional] 
**name1** | **str** | First name. | [optional] 
**name2** | **str** | Last name. | [optional] 
**address_line1** | **str** | The street adress and building or house number for the end user/customer. | [optional] 
**address_line2** | **str** | The apartment number for the end user/customer. | [optional] 
**address_line3** | **str** | Line 3 of the address for the end user/customer. | [optional] 
**city** | **str** | The end user/customer&#39;s city. | [optional] 
**state** | **str** | The end user/customer&#39;s state. | [optional] 
**postal_code** | **str** | The end user/customer&#39;s zip or postal code. | [optional] 
**country_code** | **str** | The end user/customer&#39;s two character ISO country code. | [optional] 
**phone_number** | **str** | The end user/customer&#39;s phone number. | [optional] 
**email** | **str** | The end user/customer&#39;s email. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_response_end_user_info import OrderDetailResponseEndUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseEndUserInfo from a JSON string
order_detail_response_end_user_info_instance = OrderDetailResponseEndUserInfo.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseEndUserInfo.to_json()

# convert the object into a dict
order_detail_response_end_user_info_dict = order_detail_response_end_user_info_instance.to_dict()
# create an instance of OrderDetailResponseEndUserInfo from a dict
order_detail_response_end_user_info_form_dict = order_detail_response_end_user_info.from_dict(order_detail_response_end_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


