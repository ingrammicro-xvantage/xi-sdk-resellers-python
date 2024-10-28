# PriceAndAvailabilityRequestAvailabilityByWarehouseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_by_warehouse_id** | [**PriceAndAvailabilityRequestAvailabilityByWarehouseInnerAvailabilityByWarehouseId**](PriceAndAvailabilityRequestAvailabilityByWarehouseInnerAvailabilityByWarehouseId.md) |  | [optional] 
**availability_for_all_location** | **bool** | Pass boolean value as input, if true the response will contain warehouse location details, if false the response will not hold warehouse location details. By default value is true. | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_request_availability_by_warehouse_inner import PriceAndAvailabilityRequestAvailabilityByWarehouseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityRequestAvailabilityByWarehouseInner from a JSON string
price_and_availability_request_availability_by_warehouse_inner_instance = PriceAndAvailabilityRequestAvailabilityByWarehouseInner.from_json(json)
# print the JSON string representation of the object
print(PriceAndAvailabilityRequestAvailabilityByWarehouseInner.to_json())

# convert the object into a dict
price_and_availability_request_availability_by_warehouse_inner_dict = price_and_availability_request_availability_by_warehouse_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityRequestAvailabilityByWarehouseInner from a dict
price_and_availability_request_availability_by_warehouse_inner_from_dict = PriceAndAvailabilityRequestAvailabilityByWarehouseInner.from_dict(price_and_availability_request_availability_by_warehouse_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


