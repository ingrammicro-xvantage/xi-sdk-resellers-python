# ReturnsCreateRequestListInnerShipFromInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** | Name of the company from where the product will be shipped. | 
**contact** | **str** | Contact name of the person from where the product will be shipped. | 
**address_line1** | **str** | Ship from Address Line1. | 
**address_line2** | **str** | Ship from Address Line2. | [optional] 
**address_line3** | **str** | Ship from Address Line3. | [optional] 
**city** | **str** | Ship from City. | 
**state** | **str** | Ship from state. | 
**postal_code** | **str** | Ship from postal code. | 
**country_code** | **str** | ship from country code. | 
**email** | **str** | Ship from email. | 
**phone_number** | **str** | Ship from phone number. | [optional] 

## Example

```python
from xi.sdk.resellers.models.returns_create_request_list_inner_ship_from_info_inner import ReturnsCreateRequestListInnerShipFromInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnsCreateRequestListInnerShipFromInfoInner from a JSON string
returns_create_request_list_inner_ship_from_info_inner_instance = ReturnsCreateRequestListInnerShipFromInfoInner.from_json(json)
# print the JSON string representation of the object
print(ReturnsCreateRequestListInnerShipFromInfoInner.to_json())

# convert the object into a dict
returns_create_request_list_inner_ship_from_info_inner_dict = returns_create_request_list_inner_ship_from_info_inner_instance.to_dict()
# create an instance of ReturnsCreateRequestListInnerShipFromInfoInner from a dict
returns_create_request_list_inner_ship_from_info_inner_from_dict = ReturnsCreateRequestListInnerShipFromInfoInner.from_dict(returns_create_request_list_inner_ship_from_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


