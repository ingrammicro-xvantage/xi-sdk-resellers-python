# PriceAndAvailabilityRequestServicerequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestpreamble** | [**PriceAndAvailabilityRequestServicerequestRequestpreamble**](PriceAndAvailabilityRequestServicerequestRequestpreamble.md) |  | [optional] 
**priceandstockrequest** | [**PriceAndAvailabilityRequestServicerequestPriceandstockrequest**](PriceAndAvailabilityRequestServicerequestPriceandstockrequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_request_servicerequest import PriceAndAvailabilityRequestServicerequest

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityRequestServicerequest from a JSON string
price_and_availability_request_servicerequest_instance = PriceAndAvailabilityRequestServicerequest.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityRequestServicerequest.to_json()

# convert the object into a dict
price_and_availability_request_servicerequest_dict = price_and_availability_request_servicerequest_instance.to_dict()
# create an instance of PriceAndAvailabilityRequestServicerequest from a dict
price_and_availability_request_servicerequest_form_dict = price_and_availability_request_servicerequest.from_dict(price_and_availability_request_servicerequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


