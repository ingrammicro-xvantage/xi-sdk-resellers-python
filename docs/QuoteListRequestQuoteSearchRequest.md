# QuoteListRequestQuoteSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_preamble** | [**QuoteListRequestQuoteSearchRequestRequestPreamble**](QuoteListRequestQuoteSearchRequestRequestPreamble.md) |  | [optional] 
**retrieve_quote_request** | [**QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest**](QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.quote_list_request_quote_search_request import QuoteListRequestQuoteSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteListRequestQuoteSearchRequest from a JSON string
quote_list_request_quote_search_request_instance = QuoteListRequestQuoteSearchRequest.from_json(json)
# print the JSON string representation of the object
print QuoteListRequestQuoteSearchRequest.to_json()

# convert the object into a dict
quote_list_request_quote_search_request_dict = quote_list_request_quote_search_request_instance.to_dict()
# create an instance of QuoteListRequestQuoteSearchRequest from a dict
quote_list_request_quote_search_request_form_dict = quote_list_request_quote_search_request.from_dict(quote_list_request_quote_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


