# OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks

HATEOAS links for the main order

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | Topic being orders in this case, if it is orders then the link will provide details of the order. | [optional] 
**href** | **str** | The API endpoint for accessing the relevant data | [optional] 
**type** | **str** | The type of call that can be made to the href link | [optional] 

## Example

```python
from xi-sdk-python.models.order_search_response_service_response_ordersearchresponse_orders_inner_links import OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks from a JSON string
order_search_response_service_response_ordersearchresponse_orders_inner_links_instance = OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks.from_json(json)
# print the JSON string representation of the object
print OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks.to_json()

# convert the object into a dict
order_search_response_service_response_ordersearchresponse_orders_inner_links_dict = order_search_response_service_response_ordersearchresponse_orders_inner_links_instance.to_dict()
# create an instance of OrderSearchResponseServiceResponseOrdersearchresponseOrdersInnerLinks from a dict
order_search_response_service_response_ordersearchresponse_orders_inner_links_form_dict = order_search_response_service_response_ordersearchresponse_orders_inner_links.from_dict(order_search_response_service_response_ordersearchresponse_orders_inner_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


