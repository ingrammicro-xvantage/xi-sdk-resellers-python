# QuoteDetailsRequestQuoteProductsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestpreamble** | [**QuoteDetailsRequestQuoteProductsRequestRequestpreamble**](QuoteDetailsRequestQuoteProductsRequestRequestpreamble.md) |  | [optional] 
**retrieve_quote_products_request** | [**QuoteDetailsRequestQuoteProductsRequestRetrieveQuoteProductsRequest**](QuoteDetailsRequestQuoteProductsRequestRetrieveQuoteProductsRequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.quote_details_request_quote_products_request import QuoteDetailsRequestQuoteProductsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsRequestQuoteProductsRequest from a JSON string
quote_details_request_quote_products_request_instance = QuoteDetailsRequestQuoteProductsRequest.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsRequestQuoteProductsRequest.to_json()

# convert the object into a dict
quote_details_request_quote_products_request_dict = quote_details_request_quote_products_request_instance.to_dict()
# create an instance of QuoteDetailsRequestQuoteProductsRequest from a dict
quote_details_request_quote_products_request_form_dict = quote_details_request_quote_products_request.from_dict(quote_details_request_quote_products_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


