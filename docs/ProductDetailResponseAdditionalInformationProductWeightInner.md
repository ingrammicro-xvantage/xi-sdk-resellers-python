# ProductDetailResponseAdditionalInformationProductWeightInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plant_id** | **str** | ID of the plant.  Example : &#39;US01&#39; | [optional] 
**weight** | **float** | Weight of the product.   Example : 2 | [optional] 
**weight_unit** | **str** | Weight unit of the product.   Example : &#39;LB&#39; | [optional] 

## Example

```python
from xi-sdk-python.models.product_detail_response_additional_information_product_weight_inner import ProductDetailResponseAdditionalInformationProductWeightInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailResponseAdditionalInformationProductWeightInner from a JSON string
product_detail_response_additional_information_product_weight_inner_instance = ProductDetailResponseAdditionalInformationProductWeightInner.from_json(json)
# print the JSON string representation of the object
print ProductDetailResponseAdditionalInformationProductWeightInner.to_json()

# convert the object into a dict
product_detail_response_additional_information_product_weight_inner_dict = product_detail_response_additional_information_product_weight_inner_instance.to_dict()
# create an instance of ProductDetailResponseAdditionalInformationProductWeightInner from a dict
product_detail_response_additional_information_product_weight_inner_form_dict = product_detail_response_additional_information_product_weight_inner.from_dict(product_detail_response_additional_information_product_weight_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


