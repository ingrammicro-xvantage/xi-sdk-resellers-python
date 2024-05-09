# DealsSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records_found** | **int** | Number of records found. | [optional] 
**page_size** | **int** | Number of records in a page. | [optional] 
**page_number** | **int** | Number of page. | [optional] 
**deals** | [**List[DealsSearchResponseDealsInner]**](DealsSearchResponseDealsInner.md) |  | [optional] 
**next_page** | **str** | URL for the next page. | [optional] 
**previous_page** | **str** | URL for the previous page. | [optional] 

## Example

```python
from xi.sdk.resellers.models.deals_search_response import DealsSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DealsSearchResponse from a JSON string
deals_search_response_instance = DealsSearchResponse.from_json(json)
# print the JSON string representation of the object
print(DealsSearchResponse.to_json())

# convert the object into a dict
deals_search_response_dict = deals_search_response_instance.to_dict()
# create an instance of DealsSearchResponse from a dict
deals_search_response_from_dict = DealsSearchResponse.from_dict(deals_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


