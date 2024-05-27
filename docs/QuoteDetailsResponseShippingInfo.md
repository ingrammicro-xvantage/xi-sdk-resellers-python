# QuoteDetailsResponseShippingInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | Contact name  of shipping info associated with the quote. | [optional] 
**address_line1** | **str** | Address line 1 for shipping info associated with the quote | [optional] 
**address_line2** | **str** | Address line 2 for shipping info associated with the quote. | [optional] 
**address_line3** | **str** | Address line 3 for shipping info associated with the quote. | [optional] 
**city** | **str** | City for shipping info associated with the quote | [optional] 
**state** | **str** | Two letter state abreviation for shipping info associated with the quote | [optional] 
**email** | **str** | Email of shipping info the quote associated with the quote. | [optional] 
**phone_number** | **str** | Phone number of shipping info associated with the quote. | [optional] 
**postal_code** | **str** | Zip code of shipping info associated with the quote. | [optional] 
**shp_to_gstin_number** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_details_response_shipping_info import QuoteDetailsResponseShippingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponseShippingInfo from a JSON string
quote_details_response_shipping_info_instance = QuoteDetailsResponseShippingInfo.from_json(json)
# print the JSON string representation of the object
print(QuoteDetailsResponseShippingInfo.to_json())

# convert the object into a dict
quote_details_response_shipping_info_dict = quote_details_response_shipping_info_instance.to_dict()
# create an instance of QuoteDetailsResponseShippingInfo from a dict
quote_details_response_shipping_info_from_dict = QuoteDetailsResponseShippingInfo.from_dict(quote_details_response_shipping_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


