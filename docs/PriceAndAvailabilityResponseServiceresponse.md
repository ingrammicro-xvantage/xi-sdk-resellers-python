# PriceAndAvailabilityResponseServiceresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsepreamble** | [**PriceAndAvailabilityResponseServiceresponseResponsepreamble**](PriceAndAvailabilityResponseServiceresponseResponsepreamble.md) |  | [optional] 
**priceandstockresponse** | [**PriceAndAvailabilityResponseServiceresponsePriceandstockresponse**](PriceAndAvailabilityResponseServiceresponsePriceandstockresponse.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.price_and_availability_response_serviceresponse import PriceAndAvailabilityResponseServiceresponse

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseServiceresponse from a JSON string
price_and_availability_response_serviceresponse_instance = PriceAndAvailabilityResponseServiceresponse.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityResponseServiceresponse.to_json()

# convert the object into a dict
price_and_availability_response_serviceresponse_dict = price_and_availability_response_serviceresponse_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseServiceresponse from a dict
price_and_availability_response_serviceresponse_form_dict = price_and_availability_response_serviceresponse.from_dict(price_and_availability_response_serviceresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


