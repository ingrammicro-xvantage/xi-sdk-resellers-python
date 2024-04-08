# ProductSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records_found** | **int** | The number of recourds found for the search. | [optional] 
**page_size** | **int** | The number of results per page. Default is 25. | [optional] 
**page_number** | **int** | current page number default is 1 | [optional] 
**catalog** | [**List[ProductSearchResponseCatalogInner]**](ProductSearchResponseCatalogInner.md) |  | [optional] 
**next_page** | **str** | link/URL for accessing next page. | [optional] 
**previous_page** | **str** | link/URL for accessing previous page. | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_search_response import ProductSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSearchResponse from a JSON string
product_search_response_instance = ProductSearchResponse.from_json(json)
# print the JSON string representation of the object
print(ProductSearchResponse.to_json())

# convert the object into a dict
product_search_response_dict = product_search_response_instance.to_dict()
# create an instance of ProductSearchResponse from a dict
product_search_response_form_dict = product_search_response.from_dict(product_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


