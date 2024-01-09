# OrderDetailResponseLinesInnerLinksInner

Link to Order Details for the line item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Provides the details of the line item. | [optional] 
**href** | **str** | The API endpoint for accessing the relevant data. | [optional] 
**type** | **str** | The type of call that can be made to the href link(GET,POST etc). | [optional] 

## Example

```python
from xi-sdk-python.models.order_detail_response_lines_inner_links_inner import OrderDetailResponseLinesInnerLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderDetailResponseLinesInnerLinksInner from a JSON string
order_detail_response_lines_inner_links_inner_instance = OrderDetailResponseLinesInnerLinksInner.from_json(json)
# print the JSON string representation of the object
print OrderDetailResponseLinesInnerLinksInner.to_json()

# convert the object into a dict
order_detail_response_lines_inner_links_inner_dict = order_detail_response_lines_inner_links_inner_instance.to_dict()
# create an instance of OrderDetailResponseLinesInnerLinksInner from a dict
order_detail_response_lines_inner_links_inner_form_dict = order_detail_response_lines_inner_links_inner.from_dict(order_detail_response_lines_inner_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


