# ProductSearchResponseServiceresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsepreamble** | [**ProductSearchResponseServiceresponseResponsepreamble**](ProductSearchResponseServiceresponseResponsepreamble.md) |  | [optional] 
**productsearchresponse** | [**List[ProductSearchResponseServiceresponseProductsearchresponseInner]**](ProductSearchResponseServiceresponseProductsearchresponseInner.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.product_search_response_serviceresponse import ProductSearchResponseServiceresponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSearchResponseServiceresponse from a JSON string
product_search_response_serviceresponse_instance = ProductSearchResponseServiceresponse.from_json(json)
# print the JSON string representation of the object
print ProductSearchResponseServiceresponse.to_json()

# convert the object into a dict
product_search_response_serviceresponse_dict = product_search_response_serviceresponse_instance.to_dict()
# create an instance of ProductSearchResponseServiceresponse from a dict
product_search_response_serviceresponse_form_dict = product_search_response_serviceresponse.from_dict(product_search_response_serviceresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


