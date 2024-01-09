# PriceAndAvailabilityResponseInnerAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | Boolean that indicates if the product ordered is available | [optional] 
**total_availability** | **int** | The total amount of available products | [optional] 
**availability_by_warehouse** | [**List[PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner]**](PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.price_and_availability_response_inner_availability import PriceAndAvailabilityResponseInnerAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerAvailability from a JSON string
price_and_availability_response_inner_availability_instance = PriceAndAvailabilityResponseInnerAvailability.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityResponseInnerAvailability.to_json()

# convert the object into a dict
price_and_availability_response_inner_availability_dict = price_and_availability_response_inner_availability_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerAvailability from a dict
price_and_availability_response_inner_availability_form_dict = price_and_availability_response_inner_availability.from_dict(price_and_availability_response_inner_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


