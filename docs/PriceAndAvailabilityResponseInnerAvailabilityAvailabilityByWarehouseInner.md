# PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Indicates where (location) the product is available. | [optional] 
**warehouse_id** | **str** | Indicates where (Ingram Warehouse Id) the product is available. | [optional] 
**quantity_available** | **int** | The quantity of the product available in a given warehouse. | [optional] 
**quantity_backordered** | **int** | The quantity of a product backordered in a given warehouse. | [optional] 
**quantity_backordered_eta** | **str** | The estimated time of arrival of a product that has been backordered in a given warehouse. | [optional] 
**quantity_on_order** | **int** | The quantity of the product on order. | [optional] 
**back_order_info** | [**List[PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInnerBackOrderInfoInner]**](PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInnerBackOrderInfoInner.md) | *Currently, this feature is not available in these countries (Mexico, Turkey, New Zealand, Colombia, Chile, Brazil, Peru, Western Sahara). | [optional] 

## Example

```python
from xi.sdk.resellers.models.price_and_availability_response_inner_availability_availability_by_warehouse_inner import PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner from a JSON string
price_and_availability_response_inner_availability_availability_by_warehouse_inner_instance = PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner.from_json(json)
# print the JSON string representation of the object
print(PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner.to_json())

# convert the object into a dict
price_and_availability_response_inner_availability_availability_by_warehouse_inner_dict = price_and_availability_response_inner_availability_availability_by_warehouse_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner from a dict
price_and_availability_response_inner_availability_availability_by_warehouse_inner_form_dict = price_and_availability_response_inner_availability_availability_by_warehouse_inner.from_dict(price_and_availability_response_inner_availability_availability_by_warehouse_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


