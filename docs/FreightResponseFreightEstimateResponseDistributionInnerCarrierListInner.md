# FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier_code** | **str** | The code for the shipping carrier for the line item. | [optional] 
**ship_via** | **str** | The name of the shipping carrier. | [optional] 
**carrier_mode** | **str** | Mode of the carrier. | [optional] 
**estimated_freight_charge** | **float** | Estimated freight charge. | [optional] 
**days_in_transit** | **int** | Number of transit days. | [optional] 

## Example

```python
from xi.sdk.resellers.models.freight_response_freight_estimate_response_distribution_inner_carrier_list_inner import FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner

# TODO update the JSON string below
json = "{}"
# create an instance of FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner from a JSON string
freight_response_freight_estimate_response_distribution_inner_carrier_list_inner_instance = FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner.from_json(json)
# print the JSON string representation of the object
print FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner.to_json()

# convert the object into a dict
freight_response_freight_estimate_response_distribution_inner_carrier_list_inner_dict = freight_response_freight_estimate_response_distribution_inner_carrier_list_inner_instance.to_dict()
# create an instance of FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner from a dict
freight_response_freight_estimate_response_distribution_inner_carrier_list_inner_form_dict = freight_response_freight_estimate_response_distribution_inner_carrier_list_inner.from_dict(freight_response_freight_estimate_response_distribution_inner_carrier_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


