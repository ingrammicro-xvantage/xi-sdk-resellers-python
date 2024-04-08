# PriceAndAvailabilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_available_discounts** | **bool** | Boolean value that will display Discount details in the response when true. | [optional] 
**show_reserve_inventory_details** | **bool** | Boolean value that will display reserve inventory details in the response when true. | [optional] 
**special_bid_number** | **str** | Pre-approved special pricing/bid number provided to the reseller by the vendor for special pricing and discounts. Used to track the bid number where different line items have different bid numbers. | [optional] 
**availability_by_warehouse** | [**List[PriceAndAvailabilityRequestAvailabilityByWarehouseInner]**](PriceAndAvailabilityRequestAvailabilityByWarehouseInner.md) |  | [optional] 
**products** | [**List[PriceAndAvailabilityRequestProductsInner]**](PriceAndAvailabilityRequestProductsInner.md) |  | [optional] 
**additional_attributes** | [**List[PriceAndAvailabilityRequestAdditionalAttributesInner]**](PriceAndAvailabilityRequestAdditionalAttributesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_request import PriceAndAvailabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityRequest from a JSON string
price_and_availability_request_instance = PriceAndAvailabilityRequest.from_json(json)
# print the JSON string representation of the object
print(PriceAndAvailabilityRequest.to_json())

# convert the object into a dict
price_and_availability_request_dict = price_and_availability_request_instance.to_dict()
# create an instance of PriceAndAvailabilityRequest from a dict
price_and_availability_request_form_dict = price_and_availability_request.from_dict(price_and_availability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


