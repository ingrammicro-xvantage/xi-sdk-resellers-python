# QuoteDetailsResponseQuoteDetailResponseRetrieveQuoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_guid** | **str** |  | [optional] 
**quote_name** | **str** |  | [optional] 
**quote_number** | **str** |  | [optional] 
**quote_expiry_date** | **str** |  | [optional] 
**revision_number** | **str** |  | [optional] 
**intro_preamble** | **str** |  | [optional] 
**purchase_instructions** | **str** |  | [optional] 
**legal_terms** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**price_deviation_id** | **str** |  | [optional] 
**price_deviation_start_date** | **str** |  | [optional] 
**price_deviation_expiry_date** | **str** |  | [optional] 
**customer_need** | **str** |  | [optional] 
**solution_proposed** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**modified** | **str** |  | [optional] 
**leasing_calculations** | **str** |  | [optional] 
**leasing_instructions** | **str** |  | [optional] 
**account_info** | [**QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseAccountInfo**](QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseAccountInfo.md) |  | [optional] 
**contact_info** | [**QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseContactInfo**](QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseContactInfo.md) |  | [optional] 
**vendor_attributes** | [**QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes**](QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes.md) |  | [optional] 
**end_user** | [**QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser**](QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser.md) |  | [optional] 
**quote_product_list** | [**List[QuoteProductList]**](QuoteProductList.md) |  | [optional] 
**total_quote_product_count** | **str** |  | [optional] 
**total_extended_msrp** | **str** |  | [optional] 
**total_quantity** | **str** |  | [optional] 
**total_extended_quote_price** | **str** |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.quote_details_response_quote_detail_response_retrieve_quote_response import QuoteDetailsResponseQuoteDetailResponseRetrieveQuoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponseQuoteDetailResponseRetrieveQuoteResponse from a JSON string
quote_details_response_quote_detail_response_retrieve_quote_response_instance = QuoteDetailsResponseQuoteDetailResponseRetrieveQuoteResponse.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsResponseQuoteDetailResponseRetrieveQuoteResponse.to_json()

# convert the object into a dict
quote_details_response_quote_detail_response_retrieve_quote_response_dict = quote_details_response_quote_detail_response_retrieve_quote_response_instance.to_dict()
# create an instance of QuoteDetailsResponseQuoteDetailResponseRetrieveQuoteResponse from a dict
quote_details_response_quote_detail_response_retrieve_quote_response_form_dict = quote_details_response_quote_detail_response_retrieve_quote_response.from_dict(quote_details_response_quote_detail_response_retrieve_quote_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


