# ReturnsSearchResponseReturnsClaimsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_claim_id** | **str** | A unique return claim Id. | [optional] 
**case_request_number** | **str** | A unique return request number. | [optional] 
**created_on** | **date** | The date on which the return request was created.  | [optional] 
**type** | **str** | Type of request. | [optional] 
**return_reason** | **str** | The reason for the return. | [optional] 
**reference_number** | **str** | The reference number for the return. | [optional] 
**estimated_total_value** | **date** | The estimated total value of the return. | [optional] 
**credit** | **float** | The amount of credit. | [optional] 
**modified_on** | **str** | The date on which the return request was last updated. | [optional] 
**status** | **str** | The status of the request. | [optional] 
**links** | [**List[ReturnsSearchResponseReturnsClaimsInnerLinksInner]**](ReturnsSearchResponseReturnsClaimsInnerLinksInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.returns_search_response_returns_claims_inner import ReturnsSearchResponseReturnsClaimsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsSearchResponseReturnsClaimsInner from a JSON string
returns_search_response_returns_claims_inner_instance = ReturnsSearchResponseReturnsClaimsInner.from_json(json)
# print the JSON string representation of the object
print ReturnsSearchResponseReturnsClaimsInner.to_json()

# convert the object into a dict
returns_search_response_returns_claims_inner_dict = returns_search_response_returns_claims_inner_instance.to_dict()
# create an instance of ReturnsSearchResponseReturnsClaimsInner from a dict
returns_search_response_returns_claims_inner_form_dict = returns_search_response_returns_claims_inner.from_dict(returns_search_response_returns_claims_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


