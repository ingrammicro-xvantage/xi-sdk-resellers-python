# PriceAndAvailabilityResponseServiceresponseResponsepreamble


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsestatus** | **str** | SUCCESS or FAILED, sometimes PARTIAL SUCCESS if connection to 1 of the systems fails | [optional] 
**responsemessage** | **str** | Overall status message including error message | [optional] 
**statuscode** | **str** | Statuscode Message | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.price_and_availability_response_serviceresponse_responsepreamble import PriceAndAvailabilityResponseServiceresponseResponsepreamble

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseServiceresponseResponsepreamble from a JSON string
price_and_availability_response_serviceresponse_responsepreamble_instance = PriceAndAvailabilityResponseServiceresponseResponsepreamble.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityResponseServiceresponseResponsepreamble.to_json()

# convert the object into a dict
price_and_availability_response_serviceresponse_responsepreamble_dict = price_and_availability_response_serviceresponse_responsepreamble_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseServiceresponseResponsepreamble from a dict
price_and_availability_response_serviceresponse_responsepreamble_form_dict = price_and_availability_response_serviceresponse_responsepreamble.from_dict(price_and_availability_response_serviceresponse_responsepreamble_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


