# QuoteDetails

Response schema for quote details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_detail_response** | [**QuoteDetailsQuoteDetailResponse**](QuoteDetailsQuoteDetailResponse.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.quote_details import QuoteDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetails from a JSON string
quote_details_instance = QuoteDetails.from_json(json)
# print the JSON string representation of the object
print QuoteDetails.to_json()

# convert the object into a dict
quote_details_dict = quote_details_instance.to_dict()
# create an instance of QuoteDetails from a dict
quote_details_form_dict = quote_details.from_dict(quote_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


