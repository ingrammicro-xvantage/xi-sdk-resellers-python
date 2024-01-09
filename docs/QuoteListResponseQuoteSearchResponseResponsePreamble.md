# QuoteListResponseQuoteSearchResponseResponsePreamble


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_status** | **str** | Status of the Request - \&quot;Passed\&quot;, \&quot;Failed\&quot; | [optional] 
**response_status_code** | **str** | responseStatusCode is the code returned in response to a request. The following Codes are returned: 200 400 500 | [optional] 
**response_message** | **str** | 200 &#x3D; Action was successfully received, understood and accepted. 400 &#x3D; The request contains bad syntax or can not be fullfilled. This means there is a problem with the request. 500 &#x3D; The server failed to fulfill an apparently valid request. This is a temporary problem, the request should be resubmitted. | [optional] 

## Example

```python
from xi-sdk-python.models.quote_list_response_quote_search_response_response_preamble import QuoteListResponseQuoteSearchResponseResponsePreamble

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteListResponseQuoteSearchResponseResponsePreamble from a JSON string
quote_list_response_quote_search_response_response_preamble_instance = QuoteListResponseQuoteSearchResponseResponsePreamble.from_json(json)
# print the JSON string representation of the object
print QuoteListResponseQuoteSearchResponseResponsePreamble.to_json()

# convert the object into a dict
quote_list_response_quote_search_response_response_preamble_dict = quote_list_response_quote_search_response_response_preamble_instance.to_dict()
# create an instance of QuoteListResponseQuoteSearchResponseResponsePreamble from a dict
quote_list_response_quote_search_response_response_preamble_form_dict = quote_list_response_quote_search_response_response_preamble.from_dict(quote_list_response_quote_search_response_response_preamble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


