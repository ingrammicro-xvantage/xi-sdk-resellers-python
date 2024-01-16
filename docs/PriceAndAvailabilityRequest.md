# PriceAndAvailabilityRequest

Request object model for the multi sku price and stock API endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servicerequest** | [**PriceAndAvailabilityRequestServicerequest**](PriceAndAvailabilityRequestServicerequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.price_and_availability_request import PriceAndAvailabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityRequest from a JSON string
price_and_availability_request_instance = PriceAndAvailabilityRequest.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityRequest.to_json()

# convert the object into a dict
price_and_availability_request_dict = price_and_availability_request_instance.to_dict()
# create an instance of PriceAndAvailabilityRequest from a dict
price_and_availability_request_form_dict = price_and_availability_request.from_dict(price_and_availability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


