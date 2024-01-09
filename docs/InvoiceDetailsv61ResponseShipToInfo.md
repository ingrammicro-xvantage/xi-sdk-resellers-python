# InvoiceDetailsv61ResponseShipToInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | Ship to Name. | [optional] 
**company_name** | **str** | Ship to company. | [optional] 
**address_line1** | **str** | Ship to Address Line1. | [optional] 
**address_line2** | **str** | Ship to Address Line2. | [optional] 
**address_line3** | **str** | Ship to Address Line3. | [optional] 
**city** | **str** | Ship to City. | [optional] 
**state** | **str** | Ship to State code | [optional] 
**postal_code** | **str** | Ship to Postalcode code. | [optional] 
**country_code** | **str** | Ship to Country code. | [optional] 
**phone_number** | **str** | Phone number of the Ship to company. | [optional] 
**email** | **str** | Email address of the Ship to company. | [optional] 

## Example

```python
from xi-sdk-python.models.invoice_detailsv61_response_ship_to_info import InvoiceDetailsv61ResponseShipToInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61ResponseShipToInfo from a JSON string
invoice_detailsv61_response_ship_to_info_instance = InvoiceDetailsv61ResponseShipToInfo.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailsv61ResponseShipToInfo.to_json()

# convert the object into a dict
invoice_detailsv61_response_ship_to_info_dict = invoice_detailsv61_response_ship_to_info_instance.to_dict()
# create an instance of InvoiceDetailsv61ResponseShipToInfo from a dict
invoice_detailsv61_response_ship_to_info_form_dict = invoice_detailsv61_response_ship_to_info.from_dict(invoice_detailsv61_response_ship_to_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


