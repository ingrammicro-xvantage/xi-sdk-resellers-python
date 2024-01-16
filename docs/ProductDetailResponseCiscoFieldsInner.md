# ProductDetailResponseCiscoFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_sub_group** | **str** | Cisco product sub-group | [optional] 
**service_program_name** | **str** | Cisco service program name | [optional] 
**item_catalog_category** | **str** | Cisco item catalog category | [optional] 
**configuration_indicator** | **str** | Cisco configuration indicator | [optional] 
**internal_business_entity** | **str** | Cisco internal business entity | [optional] 
**item_type** | **str** | Cisco item type | [optional] 
**global_list_price** | **str** | Cisco global list price | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.product_detail_response_cisco_fields_inner import ProductDetailResponseCiscoFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailResponseCiscoFieldsInner from a JSON string
product_detail_response_cisco_fields_inner_instance = ProductDetailResponseCiscoFieldsInner.from_json(json)
# print the JSON string representation of the object
print ProductDetailResponseCiscoFieldsInner.to_json()

# convert the object into a dict
product_detail_response_cisco_fields_inner_dict = product_detail_response_cisco_fields_inner_instance.to_dict()
# create an instance of ProductDetailResponseCiscoFieldsInner from a dict
product_detail_response_cisco_fields_inner_form_dict = product_detail_response_cisco_fields_inner.from_dict(product_detail_response_cisco_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


