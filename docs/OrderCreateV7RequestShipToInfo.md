# OrderCreateV7RequestShipToInfo

The shipping information provided by the reseller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **str** | The ID references the resellers address in Ingram Micro&#39;s system for shipping. Provided to resellers during the onboarding process. | [optional] 
**contact** | **str** | The company contact provided by the reseller. | [optional] 
**company_name** | **str** | The reseller&#39;s company name or the End-User&#39;s Name | [optional] 
**address_line1** | **str** | The street address and building or house number the order will be shipped to. | [optional] 
**address_line2** | **str** | The apartment number the order will be shipped to. | [optional] 
**city** | **str** | The city the order will be shipped to. | [optional] 
**state** | **str** | The state the order will be shipped to. | [optional] 
**postal_code** | **str** | End User Name | [optional] 
**country_code** | **str** | The zip or postal code the order will be shipped to. | [optional] 
**email** | **str** | The company contact email address. | [optional] 
**shipping_notes** | **str** |  | [optional] 
**phone_number** | **str** | The company contact phone number. | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_v7_request_ship_to_info import OrderCreateV7RequestShipToInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateV7RequestShipToInfo from a JSON string
order_create_v7_request_ship_to_info_instance = OrderCreateV7RequestShipToInfo.from_json(json)
# print the JSON string representation of the object
print(OrderCreateV7RequestShipToInfo.to_json())

# convert the object into a dict
order_create_v7_request_ship_to_info_dict = order_create_v7_request_ship_to_info_instance.to_dict()
# create an instance of OrderCreateV7RequestShipToInfo from a dict
order_create_v7_request_ship_to_info_from_dict = OrderCreateV7RequestShipToInfo.from_dict(order_create_v7_request_ship_to_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


