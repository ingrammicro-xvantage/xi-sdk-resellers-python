# FreightResponseFreightEstimateResponseLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_part_number** | **str** | The unique IngramMicro part number. | [optional] 
**vendor_part_number** | **str** | The vendor part number for the line item. | [optional] 
**warehouse_id** | **str** | The ID of the warehouse the line item will ship from. | [optional] 
**quantity** | **int** | The requested quantity of the line item. | [optional] 
**unit_price** | **float** | The unit price for the line item. | [optional] 
**net_amount** | **float** | The net amount (unit price X quantity) for the line item. | [optional] 

## Example

```python
from xi.sdk.resellers.models.freight_response_freight_estimate_response_lines_inner import FreightResponseFreightEstimateResponseLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FreightResponseFreightEstimateResponseLinesInner from a JSON string
freight_response_freight_estimate_response_lines_inner_instance = FreightResponseFreightEstimateResponseLinesInner.from_json(json)
# print the JSON string representation of the object
print FreightResponseFreightEstimateResponseLinesInner.to_json()

# convert the object into a dict
freight_response_freight_estimate_response_lines_inner_dict = freight_response_freight_estimate_response_lines_inner_instance.to_dict()
# create an instance of FreightResponseFreightEstimateResponseLinesInner from a dict
freight_response_freight_estimate_response_lines_inner_form_dict = freight_response_freight_estimate_response_lines_inner.from_dict(freight_response_freight_estimate_response_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


