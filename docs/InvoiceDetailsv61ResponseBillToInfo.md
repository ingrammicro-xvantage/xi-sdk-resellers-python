# InvoiceDetailsv61ResponseBillToInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | **str** | Bill to Name. | [optional] 
**company_name** | **str** | Bill to company. | [optional] 
**address_line1** | **str** | Bill to Address Line1. | [optional] 
**address_line2** | **str** | Bill to Address Line2. | [optional] 
**address_line3** | **str** | Bill to Address Line3. | [optional] 
**city** | **str** | Bill to City. | [optional] 
**state** | **str** | Bill to State code | [optional] 
**postal_code** | **str** | Bill to Postalcode code. | [optional] 
**country_code** | **str** | Bill to Country code. | [optional] 
**phone_number** | **str** | Phone number of the bill to company. | [optional] 
**email** | **str** | Email address of the bill to company. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.invoice_detailsv61_response_bill_to_info import InvoiceDetailsv61ResponseBillToInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61ResponseBillToInfo from a JSON string
invoice_detailsv61_response_bill_to_info_instance = InvoiceDetailsv61ResponseBillToInfo.from_json(json)
# print the JSON string representation of the object
print InvoiceDetailsv61ResponseBillToInfo.to_json()

# convert the object into a dict
invoice_detailsv61_response_bill_to_info_dict = invoice_detailsv61_response_bill_to_info_instance.to_dict()
# create an instance of InvoiceDetailsv61ResponseBillToInfo from a dict
invoice_detailsv61_response_bill_to_info_form_dict = invoice_detailsv61_response_bill_to_info.from_dict(invoice_detailsv61_response_bill_to_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


