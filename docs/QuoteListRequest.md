# QuoteListRequest

Request schema for get quote list endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_search_request** | [**QuoteListRequestQuoteSearchRequest**](QuoteListRequestQuoteSearchRequest.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.quote_list_request import QuoteListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteListRequest from a JSON string
quote_list_request_instance = QuoteListRequest.from_json(json)
# print the JSON string representation of the object
print QuoteListRequest.to_json()

# convert the object into a dict
quote_list_request_dict = quote_list_request_instance.to_dict()
# create an instance of QuoteListRequest from a dict
quote_list_request_form_dict = quote_list_request.from_dict(quote_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


