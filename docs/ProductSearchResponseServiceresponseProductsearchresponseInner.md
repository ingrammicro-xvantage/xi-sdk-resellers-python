# ProductSearchResponseServiceresponseProductsearchresponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responseflag** | **str** | Number of records in the search result. | [optional] 
**partnumbers** | [**List[ProductSearchResponseServiceresponseProductsearchresponseInnerPartnumbersInner]**](ProductSearchResponseServiceresponseProductsearchresponseInnerPartnumbersInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_search_response_serviceresponse_productsearchresponse_inner import ProductSearchResponseServiceresponseProductsearchresponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSearchResponseServiceresponseProductsearchresponseInner from a JSON string
product_search_response_serviceresponse_productsearchresponse_inner_instance = ProductSearchResponseServiceresponseProductsearchresponseInner.from_json(json)
# print the JSON string representation of the object
print ProductSearchResponseServiceresponseProductsearchresponseInner.to_json()

# convert the object into a dict
product_search_response_serviceresponse_productsearchresponse_inner_dict = product_search_response_serviceresponse_productsearchresponse_inner_instance.to_dict()
# create an instance of ProductSearchResponseServiceresponseProductsearchresponseInner from a dict
product_search_response_serviceresponse_productsearchresponse_inner_form_dict = product_search_response_serviceresponse_productsearchresponse_inner.from_dict(product_search_response_serviceresponse_productsearchresponse_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


