# PriceAndAvailabilityResponse

Response object model for the multi sku price and stock API endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceresponse** | [**PriceAndAvailabilityResponseServiceresponse**](PriceAndAvailabilityResponseServiceresponse.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.price_and_availability_response import PriceAndAvailabilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponse from a JSON string
price_and_availability_response_instance = PriceAndAvailabilityResponse.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityResponse.to_json()

# convert the object into a dict
price_and_availability_response_dict = price_and_availability_response_instance.to_dict()
# create an instance of PriceAndAvailabilityResponse from a dict
price_and_availability_response_form_dict = price_and_availability_response.from_dict(price_and_availability_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


