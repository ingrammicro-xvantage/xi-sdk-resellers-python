# OrderSearchResponseServiceResponseOrdersearchresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ordersfound** | **str** | Number of records found in the search result | 
**pagesize** | **str** | The submitted pagesize, default is 25 | [optional] 
**pagenumber** | **str** | The submitted pager number, default is 1 | [optional] 
**orders** | [**List[OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner]**](OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner.md) | An array of orders in the search result | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_search_response_service_response_ordersearchresponse import OrderSearchResponseServiceResponseOrdersearchresponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderSearchResponseServiceResponseOrdersearchresponse from a JSON string
order_search_response_service_response_ordersearchresponse_instance = OrderSearchResponseServiceResponseOrdersearchresponse.from_json(json)
# print the JSON string representation of the object
print OrderSearchResponseServiceResponseOrdersearchresponse.to_json()

# convert the object into a dict
order_search_response_service_response_ordersearchresponse_dict = order_search_response_service_response_ordersearchresponse_instance.to_dict()
# create an instance of OrderSearchResponseServiceResponseOrdersearchresponse from a dict
order_search_response_service_response_ordersearchresponse_form_dict = order_search_response_service_response_ordersearchresponse.from_dict(order_search_response_service_response_ordersearchresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


