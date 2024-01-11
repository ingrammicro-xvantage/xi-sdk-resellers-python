# QuoteDetailsResponseProductsInnerPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_price** | **int** | Ingram Micro quoted price specific to the reseller and quote. | [optional] 
**msrp** | **int** | Manufacturer Suggested Retail Price | [optional] 
**extended_msrp** | **int** | Extended MSRP - Manufacturer Suggested Retail Price X Quantity | [optional] 
**extended_quote_price** | **int** | Extended reseller quoted price (cost to reseller) X Quantity | [optional] 
**discount_off_list** | **float** | Discount off list percentage | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.quote_details_response_products_inner_price import QuoteDetailsResponseProductsInnerPrice

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponseProductsInnerPrice from a JSON string
quote_details_response_products_inner_price_instance = QuoteDetailsResponseProductsInnerPrice.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsResponseProductsInnerPrice.to_json()

# convert the object into a dict
quote_details_response_products_inner_price_dict = quote_details_response_products_inner_price_instance.to_dict()
# create an instance of QuoteDetailsResponseProductsInnerPrice from a dict
quote_details_response_products_inner_price_form_dict = quote_details_response_products_inner_price.from_dict(quote_details_response_products_inner_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


