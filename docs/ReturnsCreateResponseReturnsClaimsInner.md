# ReturnsCreateResponseReturnsClaimsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_claim_id** | **str** | The rmaClaimId claim id. | [optional] 
**case_request_number** | **str** | A unique return request number. | [optional] 
**reference_number** | **str** | The reference number for the return. | [optional] 
**created_on** | **date** | The date on which the return request was created.  | [optional] 
**type** | **str** | Type of request. | [optional] 
**return_reason** | **str** | The reason for the return. | [optional] 
**ingram_part_number** | **str** | Unique line number from Ingram. | [optional] 
**vendor_part_number** | **str** | Vendor Part Number. | [optional] 
**quantity** | **int** | Return quantity of the product. | [optional] 
**notes** | **str** | Return notes. | [optional] 
**estimated_total_value** | **float** | The estimated total value of the return. | [optional] 
**credit** | **float** | The amount of credit. | [optional] 
**status** | **str** | The status of the request. | [optional] 
**links** | [**List[ReturnsSearchResponseReturnsClaimsInnerLinksInner]**](ReturnsSearchResponseReturnsClaimsInnerLinksInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.returns_create_response_returns_claims_inner import ReturnsCreateResponseReturnsClaimsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsCreateResponseReturnsClaimsInner from a JSON string
returns_create_response_returns_claims_inner_instance = ReturnsCreateResponseReturnsClaimsInner.from_json(json)
# print the JSON string representation of the object
print ReturnsCreateResponseReturnsClaimsInner.to_json()

# convert the object into a dict
returns_create_response_returns_claims_inner_dict = returns_create_response_returns_claims_inner_instance.to_dict()
# create an instance of ReturnsCreateResponseReturnsClaimsInner from a dict
returns_create_response_returns_claims_inner_form_dict = returns_create_response_returns_claims_inner.from_dict(returns_create_response_returns_claims_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


