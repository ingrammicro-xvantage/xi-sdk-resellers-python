# FreightResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**freight_estimate_response** | [**FreightResponseFreightEstimateResponse**](FreightResponseFreightEstimateResponse.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.freight_response import FreightResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FreightResponse from a JSON string
freight_response_instance = FreightResponse.from_json(json)
# print the JSON string representation of the object
print FreightResponse.to_json()

# convert the object into a dict
freight_response_dict = freight_response_instance.to_dict()
# create an instance of FreightResponse from a dict
freight_response_form_dict = freight_response.from_dict(freight_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


