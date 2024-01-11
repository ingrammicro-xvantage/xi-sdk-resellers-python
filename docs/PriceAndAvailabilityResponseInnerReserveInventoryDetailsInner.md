# PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity_reserved** | **int** | The quantity of the product reserved for the customer. | [optional] 
**quantity_available** | **int** | The availability of the product reserved. | [optional] 
**effectivedate** | **str** | The reservation date for the product in UTC format. | [optional] 
**expirydate** | **str** | The expiration date for the reservation of the product in UTC format. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.price_and_availability_response_inner_reserve_inventory_details_inner import PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner from a JSON string
price_and_availability_response_inner_reserve_inventory_details_inner_instance = PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner.to_json()

# convert the object into a dict
price_and_availability_response_inner_reserve_inventory_details_inner_dict = price_and_availability_response_inner_reserve_inventory_details_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner from a dict
price_and_availability_response_inner_reserve_inventory_details_inner_form_dict = price_and_availability_response_inner_reserve_inventory_details_inner.from_dict(price_and_availability_response_inner_reserve_inventory_details_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


