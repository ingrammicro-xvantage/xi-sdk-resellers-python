# ProductDetailResponseAdditionalInformation

Additional Information related to the product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_weight** | [**List[ProductDetailResponseAdditionalInformationProductWeightInner]**](ProductDetailResponseAdditionalInformationProductWeightInner.md) | Weight information related to the product. | [optional] 
**is_bulk_freight** | **bool** | Example : true or false | [optional] 
**height** | **str** | Example : &#39;5.2 Inches&#39; | [optional] 
**width** | **str** | Example : &#39;13 inches&#39; | [optional] 
**length** | **str** | Example : &#39;20.4 inches&#39; | [optional] 
**net_weight** | **str** | Example : &#39;10 lb&#39; | [optional] 
**dimension_unit** | **str** | Example : &#39;Unit value&#39; | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_detail_response_additional_information import ProductDetailResponseAdditionalInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailResponseAdditionalInformation from a JSON string
product_detail_response_additional_information_instance = ProductDetailResponseAdditionalInformation.from_json(json)
# print the JSON string representation of the object
print(ProductDetailResponseAdditionalInformation.to_json())

# convert the object into a dict
product_detail_response_additional_information_dict = product_detail_response_additional_information_instance.to_dict()
# create an instance of ProductDetailResponseAdditionalInformation from a dict
product_detail_response_additional_information_from_dict = ProductDetailResponseAdditionalInformation.from_dict(product_detail_response_additional_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


