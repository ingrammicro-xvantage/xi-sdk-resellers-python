# QuoteDetailsRequestQuoteProductsRequestRequestpreamble


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_number** | **str** | Reseller Number (referred to as the account BCN) is the unique identifier for an Ingram Micro customer account. | 
**iso_country_code** | **str** | The ISO country codes are internationally recognized codes designated for each country represented by a two-letter combination (alpha-2). | 

## Example

```python
from xi.sdk.resellers.models.quote_details_request_quote_products_request_requestpreamble import QuoteDetailsRequestQuoteProductsRequestRequestpreamble

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsRequestQuoteProductsRequestRequestpreamble from a JSON string
quote_details_request_quote_products_request_requestpreamble_instance = QuoteDetailsRequestQuoteProductsRequestRequestpreamble.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsRequestQuoteProductsRequestRequestpreamble.to_json()

# convert the object into a dict
quote_details_request_quote_products_request_requestpreamble_dict = quote_details_request_quote_products_request_requestpreamble_instance.to_dict()
# create an instance of QuoteDetailsRequestQuoteProductsRequestRequestpreamble from a dict
quote_details_request_quote_products_request_requestpreamble_form_dict = quote_details_request_quote_products_request_requestpreamble.from_dict(quote_details_request_quote_products_request_requestpreamble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


