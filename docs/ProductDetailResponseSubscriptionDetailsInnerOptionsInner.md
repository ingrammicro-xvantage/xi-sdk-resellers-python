# ProductDetailResponseSubscriptionDetailsInnerOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | ID of the subscription resource | [optional] 
**resource_name** | **str** | Name of the subscription resource | [optional] 
**vendor_part_number** | **str** | Vendor’s part number for the product. | [optional] 
**min_units** | **int** | Minimum units must be purchased. | [optional] 
**max_units** | **int** | Maximum units are available for purchase. | [optional] 
**depends_on** | **str** | The name of the product must be purchased to purchase this product. | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_detail_response_subscription_details_inner_options_inner import ProductDetailResponseSubscriptionDetailsInnerOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailResponseSubscriptionDetailsInnerOptionsInner from a JSON string
product_detail_response_subscription_details_inner_options_inner_instance = ProductDetailResponseSubscriptionDetailsInnerOptionsInner.from_json(json)
# print the JSON string representation of the object
print(ProductDetailResponseSubscriptionDetailsInnerOptionsInner.to_json())

# convert the object into a dict
product_detail_response_subscription_details_inner_options_inner_dict = product_detail_response_subscription_details_inner_options_inner_instance.to_dict()
# create an instance of ProductDetailResponseSubscriptionDetailsInnerOptionsInner from a dict
product_detail_response_subscription_details_inner_options_inner_from_dict = ProductDetailResponseSubscriptionDetailsInnerOptionsInner.from_dict(product_detail_response_subscription_details_inner_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


