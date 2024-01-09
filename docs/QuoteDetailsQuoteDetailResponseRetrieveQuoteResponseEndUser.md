# QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_user_name** | **str** |  | [optional] 
**end_user_address** | **str** |  | [optional] 
**end_user_address2** | **str** |  | [optional] 
**end_user_address3** | **str** |  | [optional] 
**end_user_city** | **str** |  | [optional] 
**end_user_state** | **str** |  | [optional] 
**end_user_email** | **str** |  | [optional] 
**end_user_phone** | **str** |  | [optional] 
**end_user_zip_code** | **str** |  | [optional] 
**end_user_contact_name** | **str** |  | [optional] 
**end_user_market_segment** | **str** |  | [optional] 

## Example

```python
from xi-sdk-python.models.quote_details_quote_detail_response_retrieve_quote_response_end_user import QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser from a JSON string
quote_details_quote_detail_response_retrieve_quote_response_end_user_instance = QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser.to_json()

# convert the object into a dict
quote_details_quote_detail_response_retrieve_quote_response_end_user_dict = quote_details_quote_detail_response_retrieve_quote_response_end_user_instance.to_dict()
# create an instance of QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser from a dict
quote_details_quote_detail_response_retrieve_quote_response_end_user_form_dict = quote_details_quote_detail_response_retrieve_quote_response_end_user.from_dict(quote_details_quote_detail_response_retrieve_quote_response_end_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


