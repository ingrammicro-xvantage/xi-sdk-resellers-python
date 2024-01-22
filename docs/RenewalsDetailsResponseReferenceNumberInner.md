# RenewalsDetailsResponseReferenceNumberInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_id** | **str** | Notification id of the communication sent from Ingram. | [optional] 
**quote_number** | **str** | Quote number for the renewal. | [optional] 

## Example

```python
from xi.sdk.resellers.models.renewals_details_response_reference_number_inner import RenewalsDetailsResponseReferenceNumberInner

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsDetailsResponseReferenceNumberInner from a JSON string
renewals_details_response_reference_number_inner_instance = RenewalsDetailsResponseReferenceNumberInner.from_json(json)
# print the JSON string representation of the object
print RenewalsDetailsResponseReferenceNumberInner.to_json()

# convert the object into a dict
renewals_details_response_reference_number_inner_dict = renewals_details_response_reference_number_inner_instance.to_dict()
# create an instance of RenewalsDetailsResponseReferenceNumberInner from a dict
renewals_details_response_reference_number_inner_form_dict = renewals_details_response_reference_number_inner.from_dict(renewals_details_response_reference_number_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


