# QuoteDetailsResponseResellerInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | Contact Name | [optional] 
**company_name** | **str** | Ingram Micro Customer&#39;s Account Name | [optional] 
**email** | **str** | Account Contact Email Address | [optional] 
**phone_number** | **str** | Account Phone Number | [optional] 
**customer_number** | **str** | Reseller account number | [optional] 

## Example

```python
from xi-sdk-python.models.quote_details_response_reseller_info import QuoteDetailsResponseResellerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponseResellerInfo from a JSON string
quote_details_response_reseller_info_instance = QuoteDetailsResponseResellerInfo.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsResponseResellerInfo.to_json()

# convert the object into a dict
quote_details_response_reseller_info_dict = quote_details_response_reseller_info_instance.to_dict()
# create an instance of QuoteDetailsResponseResellerInfo from a dict
quote_details_response_reseller_info_form_dict = quote_details_response_reseller_info.from_dict(quote_details_response_reseller_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


