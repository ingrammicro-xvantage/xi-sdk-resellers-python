# OrderCreateRequestResellerInfo

The address and contact information provided by the reseller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reseller_id** | **str** | The reseller&#39;s Id. | [optional] 
**company_name** | **str** | The reseller&#39;s company name. | [optional] 
**contact** | **str** | The reseller&#39;s contact name. | [optional] 
**address_line1** | **str** | The reseller&#39;s street address. | [optional] 
**address_line2** | **str** | The reseller&#39;s building or apartment number. | [optional] 
**address_line3** | **str** | The reseller&#39;s address line 3. | [optional] 
**city** | **str** | The reseller&#39;s city. | [optional] 
**state** | **str** | The reseller&#39;s state. | [optional] 
**postal_code** | **str** | The reseller&#39;s zip or postal code. | [optional] 
**country_code** | **str** | The reseller&#39;s two-character ISO country code. | [optional] 
**phone_number** | **int** | The reseller&#39;s phone number. | [optional] 
**email** | **str** | The reseller&#39;s email address. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_request_reseller_info import OrderCreateRequestResellerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestResellerInfo from a JSON string
order_create_request_reseller_info_instance = OrderCreateRequestResellerInfo.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestResellerInfo.to_json()

# convert the object into a dict
order_create_request_reseller_info_dict = order_create_request_reseller_info_instance.to_dict()
# create an instance of OrderCreateRequestResellerInfo from a dict
order_create_request_reseller_info_form_dict = order_create_request_reseller_info.from_dict(order_create_request_reseller_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


