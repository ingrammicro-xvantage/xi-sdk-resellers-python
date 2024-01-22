# OrderDetailResponseShipToInfo

The shipping information provided by the reseller for order delivery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | The company contact provided by the reseller. | [optional] 
**company_name** | **str** | The name of the company the order will be shipped to. | [optional] 
**name1** | **str** | First name. | [optional] 
**name2** | **str** | Last name. | [optional] 
**address_line1** | **str** | The street address the order will be shipped to. | [optional] 
**address_line2** | **str** | The building or apartment number the order will be shipped to. | [optional] 
**address_line3** | **str** | Line 3 of the address the order will be shipped to. | [optional] 
**city** | **str** | The city the order will be shipped to. | [optional] 
**state** | **str** | The state the order will be shipped to. | [optional] 
**postal_code** | **str** | The zip or postal code the order will be shipped to. | [optional] 
**country_code** | **str** | The two-character ISO country code the order will be shipped to. | [optional] 
**phone_number** | **str** | The company contact phone number. | [optional] 
**email** | **str** | The company contact email address. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_detail_response_ship_to_info import OrderDetailResponseShipToInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseShipToInfo from a JSON string
order_detail_response_ship_to_info_instance = OrderDetailResponseShipToInfo.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseShipToInfo.to_json()

# convert the object into a dict
order_detail_response_ship_to_info_dict = order_detail_response_ship_to_info_instance.to_dict()
# create an instance of OrderDetailResponseShipToInfo from a dict
order_detail_response_ship_to_info_form_dict = order_detail_response_ship_to_info.from_dict(order_detail_response_ship_to_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


