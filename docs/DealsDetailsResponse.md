# DealsDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal_id** | **str** | Deal/Special bid number. | [optional] 
**version** | **str** | Most recent version number of the deal. | [optional] 
**end_user** | **str** | The end user/customer&#39;s name. | [optional] 
**extended_msrp** | **float** | Extended MSRP - Manufacturer Suggested Retail Price X Quantity. | [optional] 
**vendor** | **str** | The vendor&#39;s name. | [optional] 
**deal_received_on** | **date** | The date on which the deal starts. | [optional] 
**deal_expiry_date** | **date** | Expiration date of the deal/Special bid. | [optional] 
**price_protection_end_date** | **date** | The date on which the price protection will end. | [optional] 
**currency_code** | **str** | Country specific currency code. | [optional] 
**end_user_info** | [**List[RenewalsDetailsResponseEndUserInfoInner]**](RenewalsDetailsResponseEndUserInfoInner.md) |  | [optional] 
**products** | [**List[DealsDetailsResponseProductsInner]**](DealsDetailsResponseProductsInner.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.deals_details_response import DealsDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DealsDetailsResponse from a JSON string
deals_details_response_instance = DealsDetailsResponse.from_json(json)
# print the JSON string representation of the object
print DealsDetailsResponse.to_json()

# convert the object into a dict
deals_details_response_dict = deals_details_response_instance.to_dict()
# create an instance of DealsDetailsResponse from a dict
deals_details_response_form_dict = deals_details_response.from_dict(deals_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


