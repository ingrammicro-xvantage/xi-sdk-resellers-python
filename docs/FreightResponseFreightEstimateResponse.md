# FreightResponseFreightEstimateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | The country-specific three-character ISO 4217 currency code used for the order. | [optional] 
**total_freight_amount** | **float** | Total freight amount. | [optional] 
**total_tax_amount** | **float** | Total tax amount. | [optional] 
**total_fees** | **float** | Total fees. | [optional] 
**total_net_amount** | **float** | Total net amount. | [optional] 
**gross_amount** | **float** | Gross amount. | [optional] 
**distribution** | [**List[FreightResponseFreightEstimateResponseDistributionInner]**](FreightResponseFreightEstimateResponseDistributionInner.md) |  | [optional] 
**lines** | [**List[FreightResponseFreightEstimateResponseLinesInner]**](FreightResponseFreightEstimateResponseLinesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.freight_response_freight_estimate_response import FreightResponseFreightEstimateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FreightResponseFreightEstimateResponse from a JSON string
freight_response_freight_estimate_response_instance = FreightResponseFreightEstimateResponse.from_json(json)
# print the JSON string representation of the object
print FreightResponseFreightEstimateResponse.to_json()

# convert the object into a dict
freight_response_freight_estimate_response_dict = freight_response_freight_estimate_response_instance.to_dict()
# create an instance of FreightResponseFreightEstimateResponse from a dict
freight_response_freight_estimate_response_form_dict = freight_response_freight_estimate_response.from_dict(freight_response_freight_estimate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


