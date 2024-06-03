# ReturnsDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_of_details** | **str** | The type of the details. Return or Claim. | [optional] 
**rma_claim_id** | **str** | The rmaClaimId claim id. | [optional] 
**case_request_number** | **str** | A unique return request number. | [optional] 
**created_on** | **str** | The date on which the return request was created. | [optional] 
**return_reason** | **str** | The reason for the return. | [optional] 
**reference_number** | **str** | The reference number for the return. | [optional] 
**status** | **str** | The status of the request. | [optional] 
**return_warehouse_address** | **str** | The address of the return warehouse. | [optional] 
**products** | [**List[ReturnsDetailsResponseProductsInner]**](ReturnsDetailsResponseProductsInner.md) |  | [optional] 
**sub_total** | **float** | Sub total amount of the return request. | [optional] 
**tax** | **float** | The tax amount of the return request. | [optional] 
**additional_fees** | **float** | The additional fees for the return request. | [optional] 
**estimated_total** | **float** | The total estimated amount for the return request. | [optional] 

## Example

```python
from xi.sdk.resellers.models.returns_details_response import ReturnsDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsDetailsResponse from a JSON string
returns_details_response_instance = ReturnsDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ReturnsDetailsResponse.to_json())

# convert the object into a dict
returns_details_response_dict = returns_details_response_instance.to_dict()
# create an instance of ReturnsDetailsResponse from a dict
returns_details_response_from_dict = ReturnsDetailsResponse.from_dict(returns_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


