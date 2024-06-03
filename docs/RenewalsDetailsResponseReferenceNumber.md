# RenewalsDetailsResponseReferenceNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_id** | **str** | Notification id of the communication sent from Ingram. | [optional] 
**quote_number** | **str** | Quote number for the renewal. | [optional] 

## Example

```python
from xi.sdk.resellers.models.renewals_details_response_reference_number import RenewalsDetailsResponseReferenceNumber

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsDetailsResponseReferenceNumber from a JSON string
renewals_details_response_reference_number_instance = RenewalsDetailsResponseReferenceNumber.from_json(json)
# print the JSON string representation of the object
print(RenewalsDetailsResponseReferenceNumber.to_json())

# convert the object into a dict
renewals_details_response_reference_number_dict = renewals_details_response_reference_number_instance.to_dict()
# create an instance of RenewalsDetailsResponseReferenceNumber from a dict
renewals_details_response_reference_number_from_dict = RenewalsDetailsResponseReferenceNumber.from_dict(renewals_details_response_reference_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


