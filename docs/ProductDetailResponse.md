# ProductDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_part_number** | **str** | Ingram Micro unique part number for the product. | [optional] 
**vendor_part_number** | **str** | Vendor’s part number for the product. | [optional] 
**customer_part_number** | **str** | Reseller / end-user’s part number for the product. | [optional] 
**product_authorized** | **str** | Boolean that indicates whether a product is authorized. | [optional] 
**description** | **str** | The description given for the product. | [optional] 
**product_detail_description** | **str** | The detailed description given for the product. | [optional] 
**upc** | **str** | The UPC code for the product. Consists of 12 numeric digits that are uniquely assigned to each trade item. | [optional] 
**product_category** | **str** | The category of the product. | [optional] 
**product_subcategory** | **str** | The sub-category of the product. | [optional] 
**vendor_name** | **str** | Vendor name for the order. | [optional] 
**vendor_number** | **str** | Vendor number that identifies the product. | [optional] 
**product_status_code** | **str** | Status code of the product. | [optional] 
**product_class** | **str** | Indicates whether the product is directly shipped from the vendor’s warehouse or if the product ships from Ingram Micro’s warehouse. Class Codes are Ingram classifications on how skus are stocked A &#x3D; Product that is stocked usually in all IM warehouses and replenished on a regular basis. B &#x3D; Product that is stocked in limited IM warehouses and replenished on a regular basis C &#x3D; Product that is stocked in fewer IM warehouses and replenished on a regular basis. D &#x3D; Product that Ingram Micro has elected to discontinue. E &#x3D; Product that will be phased out later, according to the vendor. You may not want to replenish this product, but instead sell down what is in stock. F &#x3D; Product that we carry for a specific customer or supplier under a contractual agreement. N &#x3D; New Sku. Classification before first receipt O &#x3D; Discontinued product to be liquidated S&#x3D; Order for Specialized Demand (Order to backorder) X&#x3D; direct ship from Vendor V &#x3D; product that vendor has elected to discontinue. | [optional] 
**indicators** | [**ProductDetailResponseIndicators**](ProductDetailResponseIndicators.md) |  | [optional] 
**cisco_fields** | [**ProductDetailResponseCiscoFields**](ProductDetailResponseCiscoFields.md) |  | [optional] 
**technical_specifications** | [**List[ProductDetailResponseTechnicalSpecificationsInner]**](ProductDetailResponseTechnicalSpecificationsInner.md) | Technical specifications of the product. | [optional] 
**warranty_information** | **List[object]** | Warranty information related to the product. | [optional] 
**additional_information** | [**ProductDetailResponseAdditionalInformation**](ProductDetailResponseAdditionalInformation.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_detail_response import ProductDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailResponse from a JSON string
product_detail_response_instance = ProductDetailResponse.from_json(json)
# print the JSON string representation of the object
print ProductDetailResponse.to_json()

# convert the object into a dict
product_detail_response_dict = product_detail_response_instance.to_dict()
# create an instance of ProductDetailResponse from a dict
product_detail_response_form_dict = product_detail_response.from_dict(product_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


