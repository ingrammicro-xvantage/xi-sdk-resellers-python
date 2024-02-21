# ProductDetailResponseIndicators

Indicators of the Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_warranty** | **bool** | Boolean that indicates whether product has a warranty. | [optional] 
**is_new_product** | **bool** | Boolean that indicates whether it’s a new product.  | [optional] 
**has_return_limits** | **bool** | Boolean that indicates whether there is any limit to return the product. | [optional] 
**is_back_order_allowed** | **bool** | Boolean that indicates whether back order is allowed for the product. | [optional] 
**is_shipped_from_partner** | **bool** | Boolean that indicates whether product is shipped from the partner. | [optional] 
**is_replacement_product** | **bool** | Boolean that indicates whether product is a replacement product. | [optional] 
**replacement_type** | **str** |  | [optional] 
**is_directship** | **bool** | Boolean that indicates whether it’s a direct ship product. | [optional] 
**is_downloadable** | **bool** | Boolean that indicates whether product is downloadable. | [optional] 
**is_digital_type** | **bool** | Boolean that indicates whether it’s a digital product.  | [optional] 
**sku_type** | **str** | skutype | [optional] 
**has_std_special_price** | **bool** | Boolean that indicates whether product has any standard special price. | [optional] 
**has_acop_special_price** | **bool** | Boolean that indicates whether product has any ACOP special price. | [optional] 
**has_acop_quantity_break** | **bool** | Boolean that indicates whether product has any ACOP quantity break. | [optional] 
**has_std_web_discount** | **bool** | Boolean that indicates whether product has any standard web discount. | [optional] 
**has_special_bid** | **bool** | Boolean that indicates whether product has any special bid. | [optional] 
**is_exportable_to_country** | **bool** | Boolean that indicates whether product is exportable. | [optional] 
**is_discontinued_product** | **bool** | Boolean that indicates whether it’s a discontinued product. | [optional] 
**is_refurbished_product** | **bool** | Boolean that indicates whether product is refurbished. | [optional] 
**is_returnable_product** | **bool** | Boolean that indicates if the product can be returned. | [optional] 
**is_ingram_ship** | **bool** | Boolean that indicates whether it’s a Ingram shipped product. | [optional] 
**is_enduser_required** | **bool** | Do vendor requires Enduser name required to create an order. | [optional] 
**is_heavy_weight** | **bool** | Boolean that indicates whether it’s  heavy weight product. | [optional] 
**has_ltl** | **bool** | Boolean that indicates whether it hasLtl or not. | [optional] 
**is_clearance_product** | **bool** | Boolean that indicates whether it’s clearnce product. | [optional] 
**has_bundle** | **bool** | Boolean that indicates whether it’s a bundled product. | [optional] 
**is_oversize_product** | **bool** | Boolean that indicates whether it’s oversized product. | [optional] 
**is_preorder_product** | **bool** | Boolean that indicates whether it’s a preorder product. | [optional] 
**is_license_product** | **bool** | Boolean that indicates whether it’s a licened product. | [optional] 
**is_directship_orderable** | **bool** | Boolean that indicates whether product is directship orderable. | [optional] 
**is_service_sku** | **bool** | Boolean that indicates whether product is service SKU. | [optional] 
**is_configurable** | **bool** | Boolean that indicates whether product is configurable. | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_detail_response_indicators import ProductDetailResponseIndicators

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailResponseIndicators from a JSON string
product_detail_response_indicators_instance = ProductDetailResponseIndicators.from_json(json)
# print the JSON string representation of the object
print ProductDetailResponseIndicators.to_json()

# convert the object into a dict
product_detail_response_indicators_dict = product_detail_response_indicators_instance.to_dict()
# create an instance of ProductDetailResponseIndicators from a dict
product_detail_response_indicators_form_dict = product_detail_response_indicators.from_dict(product_detail_response_indicators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


