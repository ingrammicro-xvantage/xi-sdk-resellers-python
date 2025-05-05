# FreightRequestShipToAddress

The shipping information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | The name of the company the order will be shipped to. | [optional] 
**address_line1** | **str** | Line 1 of the address the order will be shipped to. | [optional] 
**address_line2** | **str** | Line 2 of the address the order will be shipped to. | [optional] 
**address_line3** | **str** | Line 3 of the address the order will be shipped to. | [optional] 
**city** | **str** | The city the order will be shipped to. | [optional] 
**state** | **str** | The state the order will be shipped to. | [optional] 
**postal_code** | **str** | The zip or postal code the order will be shipped to. | [optional] 
**country_code** | **str** | The two-character ISO country code the order will be shipped to. | [optional] 

## Example

```python
from xi.sdk.resellers.models.freight_request_ship_to_address import FreightRequestShipToAddress

# TODO update the JSON string below
json = "{}"
# create an instance of FreightRequestShipToAddress from a JSON string
freight_request_ship_to_address_instance = FreightRequestShipToAddress.from_json(json)
# print the JSON string representation of the object
print(FreightRequestShipToAddress.to_json())

# convert the object into a dict
freight_request_ship_to_address_dict = freight_request_ship_to_address_instance.to_dict()
# create an instance of FreightRequestShipToAddress from a dict
freight_request_ship_to_address_from_dict = FreightRequestShipToAddress.from_dict(freight_request_ship_to_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


