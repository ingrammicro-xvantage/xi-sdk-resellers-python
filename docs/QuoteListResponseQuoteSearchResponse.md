# QuoteListResponseQuoteSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_preamble** | [**QuoteListResponseQuoteSearchResponseResponsePreamble**](QuoteListResponseQuoteSearchResponseResponsePreamble.md) |  | [optional] 
**quote_list** | [**List[QuoteListResponseQuoteSearchResponseQuoteListInner]**](QuoteListResponseQuoteSearchResponseQuoteListInner.md) |  | [optional] 
**total_count** | **int** | Total count of quotes retrieved in the request response. | [optional] 

## Example

```python
from xi-sdk-python.models.quote_list_response_quote_search_response import QuoteListResponseQuoteSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteListResponseQuoteSearchResponse from a JSON string
quote_list_response_quote_search_response_instance = QuoteListResponseQuoteSearchResponse.from_json(json)
# print the JSON string representation of the object
print QuoteListResponseQuoteSearchResponse.to_json()

# convert the object into a dict
quote_list_response_quote_search_response_dict = quote_list_response_quote_search_response_instance.to_dict()
# create an instance of QuoteListResponseQuoteSearchResponse from a dict
quote_list_response_quote_search_response_form_dict = quote_list_response_quote_search_response.from_dict(quote_list_response_quote_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


