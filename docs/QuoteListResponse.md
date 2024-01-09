# QuoteListResponse

Response schema for get quote list endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_search_response** | [**QuoteListResponseQuoteSearchResponse**](QuoteListResponseQuoteSearchResponse.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.quote_list_response import QuoteListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteListResponse from a JSON string
quote_list_response_instance = QuoteListResponse.from_json(json)
# print the JSON string representation of the object
print QuoteListResponse.to_json()

# convert the object into a dict
quote_list_response_dict = quote_list_response_instance.to_dict()
# create an instance of QuoteListResponse from a dict
quote_list_response_form_dict = quote_list_response.from_dict(quote_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


