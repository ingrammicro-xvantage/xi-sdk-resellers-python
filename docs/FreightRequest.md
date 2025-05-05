# FreightRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bill_to_address_id** | **object** | Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit. | [optional] 
**ship_to_address_id** | **str** | The ID references the reseller&#39;s address in Ingram Micro&#39;s system for shipping. Provided to resellers during the onboarding process. | [optional] 
**ship_to_address** | [**FreightRequestShipToAddress**](FreightRequestShipToAddress.md) |  | [optional] 
**lines** | [**List[FreightRequestLinesInner]**](FreightRequestLinesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.freight_request import FreightRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FreightRequest from a JSON string
freight_request_instance = FreightRequest.from_json(json)
# print the JSON string representation of the object
print(FreightRequest.to_json())

# convert the object into a dict
freight_request_dict = freight_request_instance.to_dict()
# create an instance of FreightRequest from a dict
freight_request_from_dict = FreightRequest.from_dict(freight_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


