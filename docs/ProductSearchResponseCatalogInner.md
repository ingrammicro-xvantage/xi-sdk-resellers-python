# ProductSearchResponseCatalogInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the product. | [optional] 
**category** | **str** | The category of the product. Example: Displays. | [optional] 
**sub_category** | **str** | The sub category for the product. Example: ComputernMonitors. | [optional] 
**product_type** | **str** | The product type of the product. Example: LCD Monitors. | [optional] 
**ingram_part_number** | **str** | The Unique IngramMicro part number for the product. | [optional] 
**vendor_part_number** | **str** | The vendor part number for the product. | [optional] 
**upc_code** | **str** | The UPC code for the product. Consists of 12 numeric digits that are uniquly assigned to each trade item. | [optional] 
**vendor_name** | **str** | The name of the vendor/manufacturer of the product. | [optional] 
**end_user_required** | **str** | Indicates whether the contact information for the end user/customer is required, which determines pricing and discounts. | [optional] 
**has_discounts** | **str** | Specifies if there are discounts available for the product. | [optional] 
**type** | **str** | The SKU type of product. One of Physical, Digital, or Any. | [optional] 
**discontinued** | **str** | Indicates if the product has been discontinued. | [optional] 
**new_product** | **str** | Indicates if the product is new. For digital products, newer than 10 days. For physical products, newer than 150 days. | [optional] 
**direct_ship** | **str** | Indicates if the product will be shipped directly to the reseller or end user from the vendor/manufacturer. | [optional] 
**has_warranty** | **str** | Indicates if the product has a warranty. | [optional] 
**links** | [**List[ProductSearchResponseCatalogInnerLinksInner]**](ProductSearchResponseCatalogInnerLinksInner.md) |  | [optional] 
**extra_description** | **str** | The extended description of the product. | [optional] 
**replacement_sku** | **str** | Identifies a SKU that is a comparable subsititution of the current SKU if available. | [optional] 
**authorized_to_purchase** | **str** | It is true when it exists in matched queries field of ealstic search API. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.product_search_response_catalog_inner import ProductSearchResponseCatalogInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSearchResponseCatalogInner from a JSON string
product_search_response_catalog_inner_instance = ProductSearchResponseCatalogInner.from_json(json)
# print the JSON string representation of the object
print ProductSearchResponseCatalogInner.to_json()

# convert the object into a dict
product_search_response_catalog_inner_dict = product_search_response_catalog_inner_instance.to_dict()
# create an instance of ProductSearchResponseCatalogInner from a dict
product_search_response_catalog_inner_form_dict = product_search_response_catalog_inner.from_dict(product_search_response_catalog_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


