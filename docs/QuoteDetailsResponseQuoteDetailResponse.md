# QuoteDetailsResponseQuoteDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_preamble** | [**QuoteDetailsQuoteDetailResponseResponsePreamble**](QuoteDetailsQuoteDetailResponseResponsePreamble.md) |  | [optional] 
**retrieve_quote_response** | [**QuoteDetailsResponseQuoteDetailResponseRetrieveQuoteResponse**](QuoteDetailsResponseQuoteDetailResponseRetrieveQuoteResponse.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.quote_details_response_quote_detail_response import QuoteDetailsResponseQuoteDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponseQuoteDetailResponse from a JSON string
quote_details_response_quote_detail_response_instance = QuoteDetailsResponseQuoteDetailResponse.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsResponseQuoteDetailResponse.to_json()

# convert the object into a dict
quote_details_response_quote_detail_response_dict = quote_details_response_quote_detail_response_instance.to_dict()
# create an instance of QuoteDetailsResponseQuoteDetailResponse from a dict
quote_details_response_quote_detail_response_form_dict = quote_details_response_quote_detail_response.from_dict(quote_details_response_quote_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


