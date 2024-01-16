# QuoteSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records_found** | **int** | Total count of quotes retrieved in the request response. | [optional] 
**page_size** | **int** | Number of records (quotes) displayed per page in the quote list. | [optional] 
**page_number** | **int** | Page index or page number for the list of quotes being returned. | [optional] 
**quotes** | [**List[QuoteSearchResponseQuotesInner]**](QuoteSearchResponseQuotesInner.md) | The quote details for the requested criteria. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.quote_search_response import QuoteSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteSearchResponse from a JSON string
quote_search_response_instance = QuoteSearchResponse.from_json(json)
# print the JSON string representation of the object
print QuoteSearchResponse.to_json()

# convert the object into a dict
quote_search_response_dict = quote_search_response_instance.to_dict()
# create an instance of QuoteSearchResponse from a dict
quote_search_response_form_dict = quote_search_response.from_dict(quote_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


