# DealsSearchResponseDealsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal_id** | **str** | Deal/Special bid number. | [optional] 
**version** | **str** | Most recent version number of the deal. | [optional] 
**end_user** | **str** | The end user/customer&#39;s name. | [optional] 
**vendor** | **str** | The vendor&#39;s name. | [optional] 
**deal_expiry_date** | **date** | Expiration date of the deal/Special bid. | [optional] 
**links** | [**List[RenewalsSearchResponseRenewalsInnerLinksInner]**](RenewalsSearchResponseRenewalsInnerLinksInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.deals_search_response_deals_inner import DealsSearchResponseDealsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DealsSearchResponseDealsInner from a JSON string
deals_search_response_deals_inner_instance = DealsSearchResponseDealsInner.from_json(json)
# print the JSON string representation of the object
print DealsSearchResponseDealsInner.to_json()

# convert the object into a dict
deals_search_response_deals_inner_dict = deals_search_response_deals_inner_instance.to_dict()
# create an instance of DealsSearchResponseDealsInner from a dict
deals_search_response_deals_inner_form_dict = deals_search_response_deals_inner.from_dict(deals_search_response_deals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


