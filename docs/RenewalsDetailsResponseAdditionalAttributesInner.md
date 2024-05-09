# RenewalsDetailsResponseAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_description** | **str** | The description of the additional attribute. | [optional] 
**attribute_value** | **str** | The value of the additional attribute. | [optional] 
**start_date** | **str** | The attribute start date. | [optional] 
**expiration_date** | **str** | The attribute expiration date. | [optional] 
**is_consolidated** | **str** | Is the line item consolidated? Yes or No. | [optional] 

## Example

```python
from xi.sdk.resellers.models.renewals_details_response_additional_attributes_inner import RenewalsDetailsResponseAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsDetailsResponseAdditionalAttributesInner from a JSON string
renewals_details_response_additional_attributes_inner_instance = RenewalsDetailsResponseAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print(RenewalsDetailsResponseAdditionalAttributesInner.to_json())

# convert the object into a dict
renewals_details_response_additional_attributes_inner_dict = renewals_details_response_additional_attributes_inner_instance.to_dict()
# create an instance of RenewalsDetailsResponseAdditionalAttributesInner from a dict
renewals_details_response_additional_attributes_inner_from_dict = RenewalsDetailsResponseAdditionalAttributesInner.from_dict(renewals_details_response_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


