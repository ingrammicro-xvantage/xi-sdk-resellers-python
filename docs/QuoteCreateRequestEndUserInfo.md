# QuoteCreateRequestEndUserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | Name of the company associated with the quote. | [optional] 
**contact** | **str** | Contact name of end user associated with the quote. | [optional] 
**address_line1** | **str** | Address line 1 for end user associated with the quote | [optional] 
**address_line2** | **str** | Address line 2 for end user associated with the quote | [optional] 
**city** | **str** | City for end user associated with the quote | [optional] 
**state** | **str** | Two letter state abbreviation for end user associated with the quote. | [optional] 
**postal_code** | **str** | Zip code of end user associated with the quote. | [optional] 
**country_code** | **str** | Two letter Country abbreviation for end user associated with the quote. | [optional] 
**email** | **str** | Email of end-user the quote associated with the quote. | [optional] 
**phone_number** | **str** | Phone number of end user associated with the quote. | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_create_request_end_user_info import QuoteCreateRequestEndUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteCreateRequestEndUserInfo from a JSON string
quote_create_request_end_user_info_instance = QuoteCreateRequestEndUserInfo.from_json(json)
# print the JSON string representation of the object
print(QuoteCreateRequestEndUserInfo.to_json())

# convert the object into a dict
quote_create_request_end_user_info_dict = quote_create_request_end_user_info_instance.to_dict()
# create an instance of QuoteCreateRequestEndUserInfo from a dict
quote_create_request_end_user_info_from_dict = QuoteCreateRequestEndUserInfo.from_dict(quote_create_request_end_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


