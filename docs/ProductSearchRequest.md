# ProductSearchRequest

Request object model for the product search endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servicerequest** | [**ProductSearchRequestServicerequest**](ProductSearchRequestServicerequest.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_search_request import ProductSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSearchRequest from a JSON string
product_search_request_instance = ProductSearchRequest.from_json(json)
# print the JSON string representation of the object
print ProductSearchRequest.to_json()

# convert the object into a dict
product_search_request_dict = product_search_request_instance.to_dict()
# create an instance of ProductSearchRequest from a dict
product_search_request_form_dict = product_search_request.from_dict(product_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


