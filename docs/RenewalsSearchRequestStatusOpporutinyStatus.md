# RenewalsSearchRequestStatusOpporutinyStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of opportunity status, it can be either Open or Closed. | [optional] 
**sub_status** | **str** | The sub-status of Opportunity status. Possible sub-status values for Open opportunity status are Ready to order, Quote pending, Notification sent, Future, and Quote requested. Possible sub-status values for Closed opportunity status are All, Ordered, Quote closed-contract sales desk, Expired, Transition to new/upsell, Lost to competitior, Consolidated, Transitioned to cloud, Renewal went direct, EOL, End user out of business, Void, Other, and Cancelled. | [optional] 

## Example

```python
from xi-sdk-python.models.renewals_search_request_status_opporutiny_status import RenewalsSearchRequestStatusOpporutinyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsSearchRequestStatusOpporutinyStatus from a JSON string
renewals_search_request_status_opporutiny_status_instance = RenewalsSearchRequestStatusOpporutinyStatus.from_json(json)
# print the JSON string representation of the object
print RenewalsSearchRequestStatusOpporutinyStatus.to_json()

# convert the object into a dict
renewals_search_request_status_opporutiny_status_dict = renewals_search_request_status_opporutiny_status_instance.to_dict()
# create an instance of RenewalsSearchRequestStatusOpporutinyStatus from a dict
renewals_search_request_status_opporutiny_status_form_dict = renewals_search_request_status_opporutiny_status.from_dict(renewals_search_request_status_opporutiny_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


