# ProductSearchRequestServicerequestProductsearchrequestSearchcriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **str** | Name of the vendor or manufacturer or brand of the product | [optional] 
**vendorpartnumber** | **str** | Vendor provided part number | [optional] 
**partdescription** | **str** | This field seraches the decriptioon of the product. | [optional] 
**upc** | **str** | Universal Product Code | [optional] 
**customerpartnumber** | **str** | Customer’s designated part number  | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_search_request_servicerequest_productsearchrequest_searchcriteria import ProductSearchRequestServicerequestProductsearchrequestSearchcriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSearchRequestServicerequestProductsearchrequestSearchcriteria from a JSON string
product_search_request_servicerequest_productsearchrequest_searchcriteria_instance = ProductSearchRequestServicerequestProductsearchrequestSearchcriteria.from_json(json)
# print the JSON string representation of the object
print ProductSearchRequestServicerequestProductsearchrequestSearchcriteria.to_json()

# convert the object into a dict
product_search_request_servicerequest_productsearchrequest_searchcriteria_dict = product_search_request_servicerequest_productsearchrequest_searchcriteria_instance.to_dict()
# create an instance of ProductSearchRequestServicerequestProductsearchrequestSearchcriteria from a dict
product_search_request_servicerequest_productsearchrequest_searchcriteria_form_dict = product_search_request_servicerequest_productsearchrequest_searchcriteria.from_dict(product_search_request_servicerequest_productsearchrequest_searchcriteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


