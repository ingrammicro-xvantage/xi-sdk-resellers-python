# PriceAndAvailabilityRequestProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_part_number** | **str** | Ingram Micro unique part number for the product. | [optional] 
**vendor_part_number** | **str** | Vendor’s part number for the product. | [optional] 
**customer_part_number** | **str** | Reseller/end-user’s part number for the product. | [optional] 
**upc** | **str** | The UPC code for the product. Consists of 12 numeric digits that are uniquely assigned to each trade item. | [optional] 
**quantity_requested** | **str** | Number of quantity of the Product. | [optional] 
**additional_attributes** | [**List[PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner]**](PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner.md) |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.price_and_availability_request_products_inner import PriceAndAvailabilityRequestProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityRequestProductsInner from a JSON string
price_and_availability_request_products_inner_instance = PriceAndAvailabilityRequestProductsInner.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityRequestProductsInner.to_json()

# convert the object into a dict
price_and_availability_request_products_inner_dict = price_and_availability_request_products_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityRequestProductsInner from a dict
price_and_availability_request_products_inner_form_dict = price_and_availability_request_products_inner.from_dict(price_and_availability_request_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


