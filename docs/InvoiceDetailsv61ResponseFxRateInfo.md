# InvoiceDetailsv61ResponseFxRateInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | Currency code. | [optional] 
**company_currency** | **str** | Company currency code. | [optional] 
**invoice_currency** | **str** | Invoice currency. | [optional] 
**currency_fx_rate** | **float** | Currency FX rate. | [optional] 

## Example

```python
from xi.sdk.resellers.models.invoice_detailsv61_response_fx_rate_info import InvoiceDetailsv61ResponseFxRateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsv61ResponseFxRateInfo from a JSON string
invoice_detailsv61_response_fx_rate_info_instance = InvoiceDetailsv61ResponseFxRateInfo.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailsv61ResponseFxRateInfo.to_json())

# convert the object into a dict
invoice_detailsv61_response_fx_rate_info_dict = invoice_detailsv61_response_fx_rate_info_instance.to_dict()
# create an instance of InvoiceDetailsv61ResponseFxRateInfo from a dict
invoice_detailsv61_response_fx_rate_info_form_dict = invoice_detailsv61_response_fx_rate_info.from_dict(invoice_detailsv61_response_fx_rate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


