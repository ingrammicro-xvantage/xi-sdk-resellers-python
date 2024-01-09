# FreightResponseFreightEstimateResponseDistributionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ship_from_branch_number** | **str** | The ID of the warehouse the line item will ship from. | [optional] 
**carrier_code** | **str** | The code for the shipping carrier for the line item. | [optional] 
**ship_via** | **str** | The name of the shipping carrier. | [optional] 
**freight_rate** | **float** | Estimated freight charge. | [optional] 
**total_weight** | **float** | Total weight. | [optional] 
**transit_days** | **int** | Number of transit days. | [optional] 
**carrier_list** | [**List[FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner]**](FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner.md) |  | [optional] 

## Example

```python
from xi-sdk-python.models.freight_response_freight_estimate_response_distribution_inner import FreightResponseFreightEstimateResponseDistributionInner

# TODO update the JSON string below
json = "{}"
# create an instance of FreightResponseFreightEstimateResponseDistributionInner from a JSON string
freight_response_freight_estimate_response_distribution_inner_instance = FreightResponseFreightEstimateResponseDistributionInner.from_json(json)
# print the JSON string representation of the object
print FreightResponseFreightEstimateResponseDistributionInner.to_json()

# convert the object into a dict
freight_response_freight_estimate_response_distribution_inner_dict = freight_response_freight_estimate_response_distribution_inner_instance.to_dict()
# create an instance of FreightResponseFreightEstimateResponseDistributionInner from a dict
freight_response_freight_estimate_response_distribution_inner_form_dict = freight_response_freight_estimate_response_distribution_inner.from_dict(freight_response_freight_estimate_response_distribution_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


