# FreightRequestLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_line_number** | **str** | The ID references the reseller&#39;s address in Ingram Micro&#39;s system for shipping. Provided to resellers during the onboarding process. | [optional] 
**ingram_part_number** | **str** | The unique IngramMicro part number. | [optional] 
**quantity** | **str** | The requested quantity of the line item. | [optional] 
**warehouse_id** | **str** | The ID of the warehouse the line item will ship from. | [optional] 
**carrier_code** | **str** | The code for the shipping carrier for the line item. | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.freight_request_lines_inner import FreightRequestLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FreightRequestLinesInner from a JSON string
freight_request_lines_inner_instance = FreightRequestLinesInner.from_json(json)
# print the JSON string representation of the object
print FreightRequestLinesInner.to_json()

# convert the object into a dict
freight_request_lines_inner_dict = freight_request_lines_inner_instance.to_dict()
# create an instance of FreightRequestLinesInner from a dict
freight_request_lines_inner_form_dict = freight_request_lines_inner.from_dict(freight_request_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


