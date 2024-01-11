# PriceAndAvailabilityResponseInnerServiceFeesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_type** | **str** | Condition Type of the service fees. | [optional] 
**description** | **str** | Description of the service fees. | [optional] 
**amount** | **float** | Amount of the service fees. | [optional] 
**end_date** | **str** | End Date of the service fees. | [optional] 
**currency_code** | **str** | Currency Code of the service fees. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.price_and_availability_response_inner_service_fees_inner import PriceAndAvailabilityResponseInnerServiceFeesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerServiceFeesInner from a JSON string
price_and_availability_response_inner_service_fees_inner_instance = PriceAndAvailabilityResponseInnerServiceFeesInner.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityResponseInnerServiceFeesInner.to_json()

# convert the object into a dict
price_and_availability_response_inner_service_fees_inner_dict = price_and_availability_response_inner_service_fees_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerServiceFeesInner from a dict
price_and_availability_response_inner_service_fees_inner_form_dict = price_and_availability_response_inner_service_fees_inner.from_dict(price_and_availability_response_inner_service_fees_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


