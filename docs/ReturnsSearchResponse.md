# ReturnsSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records_found** | **int** | Number of records found. | [optional] 
**page_size** | **int** | Number of records in a page. | [optional] 
**page_number** | **int** | Number of page. | [optional] 
**returns_claims** | [**List[ReturnsSearchResponseReturnsClaimsInner]**](ReturnsSearchResponseReturnsClaimsInner.md) |  | [optional] 
**next_page** | **str** | URL for the next page. | [optional] 
**previous_page** | **str** | URL for the previous page. | [optional] 

## Example

```python
from xi.sdk.resellers.models.returns_search_response import ReturnsSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsSearchResponse from a JSON string
returns_search_response_instance = ReturnsSearchResponse.from_json(json)
# print the JSON string representation of the object
print ReturnsSearchResponse.to_json()

# convert the object into a dict
returns_search_response_dict = returns_search_response_instance.to_dict()
# create an instance of ReturnsSearchResponse from a dict
returns_search_response_form_dict = returns_search_response.from_dict(returns_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


