# QuoteDetailsRequest

Request schema for get quote details endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_products_request** | [**QuoteDetailsRequestQuoteProductsRequest**](QuoteDetailsRequestQuoteProductsRequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.quote_details_request import QuoteDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsRequest from a JSON string
quote_details_request_instance = QuoteDetailsRequest.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsRequest.to_json()

# convert the object into a dict
quote_details_request_dict = quote_details_request_instance.to_dict()
# create an instance of QuoteDetailsRequest from a dict
quote_details_request_form_dict = quote_details_request.from_dict(quote_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


