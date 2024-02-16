# QuoteToOrderDetailsDTOLinesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_line_number** | **str** | The reseller&#39;s line item number for reference in their system. | [optional] 
**ingram_part_number** | **str** | Unique IngramMicro part number. | [optional] 
**quantity** | **str** | The quantity of the line item. | [optional] 
**vmf_additional_attributes_lines** | [**List[QuoteToOrderDetailsDTOLinesInnerVmfAdditionalAttributesLinesInner]**](QuoteToOrderDetailsDTOLinesInnerVmfAdditionalAttributesLinesInner.md) | The object containing the list of fields required at a line level by the vendor. | [optional] 

## Example

```python
from xi.sdk.resellers.models.quote_to_order_details_dto_lines_inner import QuoteToOrderDetailsDTOLinesInner

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteToOrderDetailsDTOLinesInner from a JSON string
quote_to_order_details_dto_lines_inner_instance = QuoteToOrderDetailsDTOLinesInner.from_json(json)
# print the JSON string representation of the object
print QuoteToOrderDetailsDTOLinesInner.to_json()

# convert the object into a dict
quote_to_order_details_dto_lines_inner_dict = quote_to_order_details_dto_lines_inner_instance.to_dict()
# create an instance of QuoteToOrderDetailsDTOLinesInner from a dict
quote_to_order_details_dto_lines_inner_form_dict = quote_to_order_details_dto_lines_inner.from_dict(quote_to_order_details_dto_lines_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


