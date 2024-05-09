# OrderModifyResponseShipToInfo

The shipping information for the order provided by the reseller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **str** | Suffix used to identify shipping address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit. | [optional] 
**contact** | **str** | The company contact provided by the reseller. | [optional] 
**company_name** | **str** | The name of the company the order will be shipped to. | [optional] 
**address_line1** | **str** | The street address and building or house number the order will be shipped to. | [optional] 
**address_line2** | **str** | The apartment number the order will be shipped to. | [optional] 
**address_line3** | **str** | Line 3 of the address the order will be shipped to. | [optional] 
**city** | **str** | The city the order will be shipped to. | [optional] 
**state** | **str** | The state the order will be shipped to. | [optional] 
**postal_code** | **str** | The zip or postal code the order will be shipped to. | [optional] 
**country_code** | **str** | The two-character ISO country code the order will be shipped to. | [optional] 
**phone_number** | **str** | The company contact phone number. | [optional] 
**email** | **str** | The company contact email address. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_modify_response_ship_to_info import OrderModifyResponseShipToInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyResponseShipToInfo from a JSON string
order_modify_response_ship_to_info_instance = OrderModifyResponseShipToInfo.from_json(json)
# print the JSON string representation of the object
print(OrderModifyResponseShipToInfo.to_json())

# convert the object into a dict
order_modify_response_ship_to_info_dict = order_modify_response_ship_to_info_instance.to_dict()
# create an instance of OrderModifyResponseShipToInfo from a dict
order_modify_response_ship_to_info_from_dict = OrderModifyResponseShipToInfo.from_dict(order_modify_response_ship_to_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


