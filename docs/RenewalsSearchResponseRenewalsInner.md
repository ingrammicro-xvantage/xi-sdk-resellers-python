# RenewalsSearchResponseRenewalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**renewal_id** | **str** | Unique renewal ID. | [optional] 
**customer_order_number** | **str** | The reseller&#39;s order number for reference in their system. | [optional] 
**reference_number** | **str** | Renewal reference number. It could be notification id or quote number. | [optional] 
**end_user** | **str** | The company name for the end user/customer. | [optional] 
**vendor** | **str** | The name of the vendor. | [optional] 
**expiration_date** | **str** | Renewal expiration date. | [optional] 
**renewal_value** | **str** | The value of the renewal. | [optional] 
**status** | **str** | The status of the renewal. | [optional] 
**links** | [**List[RenewalsSearchResponseRenewalsInnerLinksInner]**](RenewalsSearchResponseRenewalsInnerLinksInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.renewals_search_response_renewals_inner import RenewalsSearchResponseRenewalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsSearchResponseRenewalsInner from a JSON string
renewals_search_response_renewals_inner_instance = RenewalsSearchResponseRenewalsInner.from_json(json)
# print the JSON string representation of the object
print RenewalsSearchResponseRenewalsInner.to_json()

# convert the object into a dict
renewals_search_response_renewals_inner_dict = renewals_search_response_renewals_inner_instance.to_dict()
# create an instance of RenewalsSearchResponseRenewalsInner from a dict
renewals_search_response_renewals_inner_form_dict = renewals_search_response_renewals_inner.from_dict(renewals_search_response_renewals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


