# QuoteDetailsResponseEndUserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | End User Name | [optional] 
**company_name** | **str** | Contact name  of end user associated with the quote. | [optional] 
**address_line1** | **str** | Address line 1 for end user associated with the quote | [optional] 
**address_line2** | **str** | Address line 2 for end user associated with the quote. | [optional] 
**address_line3** | **str** | Address line 3 for end user associated with the quote. | [optional] 
**city** | **str** | City for end user associated with the quote | [optional] 
**state** | **str** | Two letter state abreviation for end user associated with the quote | [optional] 
**email** | **str** | Email of end user the quote associated with the quote. | [optional] 
**phone_number** | **str** | Phone number of end user associated with the quote. | [optional] 
**postal_code** | **str** | Zip code of end user associated with the quote. | [optional] 
**market_segment** | **str** | Market Segment of end user associated with the quote. End user market segment is included when end user is included in specific market segments like Educational, Government, Military, Medical - that may receive special pricing due to their segmentation. | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_details_response_end_user_info import QuoteDetailsResponseEndUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponseEndUserInfo from a JSON string
quote_details_response_end_user_info_instance = QuoteDetailsResponseEndUserInfo.from_json(json)
# print the JSON string representation of the object
print(QuoteDetailsResponseEndUserInfo.to_json())

# convert the object into a dict
quote_details_response_end_user_info_dict = quote_details_response_end_user_info_instance.to_dict()
# create an instance of QuoteDetailsResponseEndUserInfo from a dict
quote_details_response_end_user_info_from_dict = QuoteDetailsResponseEndUserInfo.from_dict(quote_details_response_end_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


