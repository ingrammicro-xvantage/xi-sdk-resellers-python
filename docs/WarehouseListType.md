# WarehouseListType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warehouseid** | **str** |  | [optional] 
**warehousedescription** | **str** | City of the Ingram Micro warehouse location | [optional] 
**availablequantity** | **int** | On hand available quantity | [optional] 
**onorderquantity** | **int** | On Order quantity | [optional] 
**onholdquantity** | **int** | On hold quantity | [optional] 
**etadate** | **str** |  | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.warehouse_list_type import WarehouseListType

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseListType from a JSON string
warehouse_list_type_instance = WarehouseListType.from_json(json)
# print the JSON string representation of the object
print WarehouseListType.to_json()

# convert the object into a dict
warehouse_list_type_dict = warehouse_list_type_instance.to_dict()
# create an instance of WarehouseListType from a dict
warehouse_list_type_form_dict = warehouse_list_type.from_dict(warehouse_list_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


