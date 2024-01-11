# OrderModifyRequestLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_part_number** | **str** | The unique IngramMicro part number. | [optional] 
**ingram_line_number** | **str** | The IngramMicro line number. | [optional] 
**customer_line_number** | **str** | The reseller&#39;s line number for reference in their system. | [optional] 
**add_update_delete_line** | **str** | The line number that was added, updated, or deleted. | [optional] 
**quantity** | **int** | The quantity of the line item. | [optional] 
**notes** | **str** | The line-level notes. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_modify_request_lines_inner import OrderModifyRequestLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderModifyRequestLinesInner from a JSON string
order_modify_request_lines_inner_instance = OrderModifyRequestLinesInner.from_json(json)
# print the JSON string representation of the object
print OrderModifyRequestLinesInner.to_json()

# convert the object into a dict
order_modify_request_lines_inner_dict = order_modify_request_lines_inner_instance.to_dict()
# create an instance of OrderModifyRequestLinesInner from a dict
order_modify_request_lines_inner_form_dict = order_modify_request_lines_inner.from_dict(order_modify_request_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


