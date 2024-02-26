# QuoteToOrderDetailsDTOShipToInfo

The shipping information provided by the reseller for order delivery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **str** | The company contact provided by the reseller. | [optional] 
**company_name** | **str** | The name of the company the order will be shipped to. | [optional] 
**contact** | **str** | The contact name for the order will be shipped to. | [optional] 
**address_line1** | **str** | The address line 1 the order will be shipped to. | [optional] 
**address_line2** | **str** | The address line 2 the order will be shipped to. | [optional] 
**address_line3** | **str** | The address line 3 the order will be shipped to. | [optional] 
**city** | **str** | The city the order will be shipped to. | [optional] 
**state** | **str** | The state the order will be shipped to. | [optional] 
**postal_code** | **str** | The zip or postal code the order will be shipped to. | [optional] 
**country_code** | **str** | The two-character ISO country code the order will be shipped to. | [optional] 
**email** | **str** | The company contact email address. | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_to_order_details_dto_ship_to_info import QuoteToOrderDetailsDTOShipToInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteToOrderDetailsDTOShipToInfo from a JSON string
quote_to_order_details_dto_ship_to_info_instance = QuoteToOrderDetailsDTOShipToInfo.from_json(json)
# print the JSON string representation of the object
print QuoteToOrderDetailsDTOShipToInfo.to_json()

# convert the object into a dict
quote_to_order_details_dto_ship_to_info_dict = quote_to_order_details_dto_ship_to_info_instance.to_dict()
# create an instance of QuoteToOrderDetailsDTOShipToInfo from a dict
quote_to_order_details_dto_ship_to_info_form_dict = quote_to_order_details_dto_ship_to_info.from_dict(quote_to_order_details_dto_ship_to_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


