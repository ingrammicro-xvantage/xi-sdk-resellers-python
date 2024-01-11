# OrderCreateRequestShipToInfo

The shipping information provided by the reseller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **str** | The ID references the resellers address in Ingram Micro&#39;s system for shipping. Provided to resellers during the onboarding process. | [optional] 
**contact** | **str** | The company contact provided by the reseller. | [optional] 
**company_name** | **str** | The name of the company the order will be shipped to. | [optional] 
**name1** | **str** | name1 | [optional] 
**name2** | **str** | name2 | [optional] 
**address_line1** | **str** | The street address and building or house number the order will be shipped to. | [optional] 
**address_line2** | **str** | The apartment number the order will be shipped to. | [optional] 
**address_line3** | **str** | Line 3 of the address the order will be shipped to. | [optional] 
**address_line4** | **str** | Street address4 | [optional] 
**city** | **str** | The city the order will be shipped to. | [optional] 
**state** | **str** | The state the order will be shipped to. | [optional] 
**postal_code** | **str** | The zip or postal code the order will be shipped to. | [optional] 
**country_code** | **str** | The two-character ISO country code the order will be shipped to. | [optional] 
**phone_number** | **str** | The company contact phone number. | [optional] 
**email** | **str** | The company contact email address. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_create_request_ship_to_info import OrderCreateRequestShipToInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestShipToInfo from a JSON string
order_create_request_ship_to_info_instance = OrderCreateRequestShipToInfo.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestShipToInfo.to_json()

# convert the object into a dict
order_create_request_ship_to_info_dict = order_create_request_ship_to_info_instance.to_dict()
# create an instance of OrderCreateRequestShipToInfo from a dict
order_create_request_ship_to_info_form_dict = order_create_request_ship_to_info.from_dict(order_create_request_ship_to_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


