# OrderCreateResponseEndUserInfo

The contact information for the end user/customer provided by the reseller. Used to determine pricing and discounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_user_id** | **str** | The unique ID provided by the reseller for the end user/customer. | [optional] 
**contact** | **str** | The contact name for the end user/customer. | [optional] 
**company_name** | **str** | The company name for the end user/customer. | [optional] 
**name1** | **str** | name1 | [optional] 
**name2** | **str** | name2 | [optional] 
**address_line1** | **str** | The street adress and building or house number for the end user/customer. | [optional] 
**address_line2** | **str** | The apartment number for the end user/customer. | [optional] 
**address_line3** | **str** | Line 3 of the address for the end user/customer. | [optional] 
**address_line4** | **str** | Street address4 | [optional] 
**city** | **str** | The end user/customer&#39;s city. | [optional] 
**state** | **str** | The end user/customer&#39;s state. | [optional] 
**postal_code** | **str** | The end user/customer&#39;s zip or postal code. | [optional] 
**country_code** | **str** | The end user/customer&#39;s two-character ISO country code. | [optional] 
**phone_number** | **str** | The end user/customer&#39;s phone number. | [optional] 
**email** | **str** | The end user/customer&#39;s email. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_create_response_end_user_info import OrderCreateResponseEndUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateResponseEndUserInfo from a JSON string
order_create_response_end_user_info_instance = OrderCreateResponseEndUserInfo.from_json(json)
# print the JSON string representation of the object
print OrderCreateResponseEndUserInfo.to_json()

# convert the object into a dict
order_create_response_end_user_info_dict = order_create_response_end_user_info_instance.to_dict()
# create an instance of OrderCreateResponseEndUserInfo from a dict
order_create_response_end_user_info_form_dict = order_create_response_end_user_info.from_dict(order_create_response_end_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


