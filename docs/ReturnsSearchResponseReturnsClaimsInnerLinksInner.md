# ReturnsSearchResponseReturnsClaimsInnerLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Provides the details of the return. | [optional] 
**href** | **str** | The URL endpoint for accessing the relevant data. | [optional] 
**type** | **str** | The type of call that can be made to the href link (GET, POST, Etc.). | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.returns_search_response_returns_claims_inner_links_inner import ReturnsSearchResponseReturnsClaimsInnerLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsSearchResponseReturnsClaimsInnerLinksInner from a JSON string
returns_search_response_returns_claims_inner_links_inner_instance = ReturnsSearchResponseReturnsClaimsInnerLinksInner.from_json(json)
# print the JSON string representation of the object
print ReturnsSearchResponseReturnsClaimsInnerLinksInner.to_json()

# convert the object into a dict
returns_search_response_returns_claims_inner_links_inner_dict = returns_search_response_returns_claims_inner_links_inner_instance.to_dict()
# create an instance of ReturnsSearchResponseReturnsClaimsInnerLinksInner from a dict
returns_search_response_returns_claims_inner_links_inner_form_dict = returns_search_response_returns_claims_inner_links_inner.from_dict(returns_search_response_returns_claims_inner_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


