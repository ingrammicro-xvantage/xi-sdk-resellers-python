# ProductSearchRequestServicerequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requestpreamble** | [**ProductSearchRequestServicerequestRequestpreamble**](ProductSearchRequestServicerequestRequestpreamble.md) |  | [optional] 
**productsearchrequest** | [**ProductSearchRequestServicerequestProductsearchrequest**](ProductSearchRequestServicerequestProductsearchrequest.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.product_search_request_servicerequest import ProductSearchRequestServicerequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSearchRequestServicerequest from a JSON string
product_search_request_servicerequest_instance = ProductSearchRequestServicerequest.from_json(json)
# print the JSON string representation of the object
print ProductSearchRequestServicerequest.to_json()

# convert the object into a dict
product_search_request_servicerequest_dict = product_search_request_servicerequest_instance.to_dict()
# create an instance of ProductSearchRequestServicerequest from a dict
product_search_request_servicerequest_form_dict = product_search_request_servicerequest.from_dict(product_search_request_servicerequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


