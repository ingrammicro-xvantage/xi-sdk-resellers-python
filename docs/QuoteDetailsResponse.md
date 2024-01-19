# QuoteDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_detail_response** | [**QuoteDetailsResponseQuoteDetailResponse**](QuoteDetailsResponseQuoteDetailResponse.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_details_response import QuoteDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponse from a JSON string
quote_details_response_instance = QuoteDetailsResponse.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsResponse.to_json()

# convert the object into a dict
quote_details_response_dict = quote_details_response_instance.to_dict()
# create an instance of QuoteDetailsResponse from a dict
quote_details_response_form_dict = quote_details_response.from_dict(quote_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


