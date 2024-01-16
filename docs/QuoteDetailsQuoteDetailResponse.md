# QuoteDetailsQuoteDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_preamble** | [**QuoteDetailsQuoteDetailResponseResponsePreamble**](QuoteDetailsQuoteDetailResponseResponsePreamble.md) |  | [optional] 
**retrieve_quote_response** | [**QuoteDetailsQuoteDetailResponseRetrieveQuoteResponse**](QuoteDetailsQuoteDetailResponseRetrieveQuoteResponse.md) |  | [optional] 
**quote_product_list** | [**List[QuoteProductList]**](QuoteProductList.md) |  | [optional] 
**total_quote_product_count** | **str** |  | [optional] 
**total_extended_msrp** | **str** |  | [optional] 
**total_quantity** | **int** |  | [optional] 
**total_extended_quote_price** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.quote_details_quote_detail_response import QuoteDetailsQuoteDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsQuoteDetailResponse from a JSON string
quote_details_quote_detail_response_instance = QuoteDetailsQuoteDetailResponse.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsQuoteDetailResponse.to_json()

# convert the object into a dict
quote_details_quote_detail_response_dict = quote_details_quote_detail_response_instance.to_dict()
# create an instance of QuoteDetailsQuoteDetailResponse from a dict
quote_details_quote_detail_response_form_dict = quote_details_quote_detail_response.from_dict(quote_details_quote_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


