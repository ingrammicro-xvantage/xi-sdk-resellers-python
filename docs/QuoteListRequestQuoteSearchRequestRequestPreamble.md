# QuoteListRequestQuoteSearchRequestRequestPreamble


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_number** | **str** | Reseller Number (referred to as the account BCN) is the unique identifier for an Ingram Micro customer account. | 
**customer_contact** | **str** | Logged in User&#39;s email address. | [optional] 
**iso_country_code** | **str** | The ISO country codes are internationally recognized codes designated for each country represented by a two-letter combination (alpha-2). | 

## Example

```python
from xi.sdk.resellers.python.models.quote_list_request_quote_search_request_request_preamble import QuoteListRequestQuoteSearchRequestRequestPreamble

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteListRequestQuoteSearchRequestRequestPreamble from a JSON string
quote_list_request_quote_search_request_request_preamble_instance = QuoteListRequestQuoteSearchRequestRequestPreamble.from_json(json)
# print the JSON string representation of the object
print QuoteListRequestQuoteSearchRequestRequestPreamble.to_json()

# convert the object into a dict
quote_list_request_quote_search_request_request_preamble_dict = quote_list_request_quote_search_request_request_preamble_instance.to_dict()
# create an instance of QuoteListRequestQuoteSearchRequestRequestPreamble from a dict
quote_list_request_quote_search_request_request_preamble_form_dict = quote_list_request_quote_search_request_request_preamble.from_dict(quote_list_request_quote_search_request_request_preamble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


