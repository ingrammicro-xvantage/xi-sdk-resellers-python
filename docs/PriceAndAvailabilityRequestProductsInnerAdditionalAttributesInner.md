# PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | governmentprogramcode: Special Discount details will be provided based on the governmentprogramcode if available. shiptostatebrazil: Attribute Specific to Brazil. shipfrombranchnumber: If provided, displays only the availability of the specified branch number. | [optional] 
**attribute_value** | **str** | key value pair -key value. | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_request_products_inner_additional_attributes_inner import PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner from a JSON string
price_and_availability_request_products_inner_additional_attributes_inner_instance = PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner.to_json()

# convert the object into a dict
price_and_availability_request_products_inner_additional_attributes_inner_dict = price_and_availability_request_products_inner_additional_attributes_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner from a dict
price_and_availability_request_products_inner_additional_attributes_inner_form_dict = price_and_availability_request_products_inner_additional_attributes_inner.from_dict(price_and_availability_request_products_inner_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


