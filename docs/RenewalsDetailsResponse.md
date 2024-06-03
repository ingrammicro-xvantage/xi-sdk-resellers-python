# RenewalsDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**renewal_id** | **str** | Unique Ingram renewal ID. | [optional] 
**ingram_order_number** | **str** | The IngramMicro sales order number. | [optional] 
**ingram_order_date** | **str** | The IngramMicro sales order date. | [optional] 
**expiration_date** | **str** | Renewal expiration date. | [optional] 
**ingram_purchase_order_number** | **str** | Ingram purchase order number. | [optional] 
**customer_order_number** | **str** | The reseller&#39;s order number for reference in their system. | [optional] 
**end_customer_order_number** | **str** | The end customer&#39;s order number for reference in their system. | [optional] 
**renewal_value** | **str** | The value of the renewal. | [optional] 
**end_user** | **str** | The company name for the end user/customer. | [optional] 
**vendor** | **str** | The name of the vendor. | [optional] 
**status** | **str** | The status of the renewal. | [optional] 
**end_user_info** | [**RenewalsDetailsResponseEndUserInfo**](RenewalsDetailsResponseEndUserInfo.md) |  | [optional] 
**reference_number** | [**RenewalsDetailsResponseReferenceNumber**](RenewalsDetailsResponseReferenceNumber.md) |  | [optional] 
**products** | [**List[RenewalsDetailsResponseProductsInner]**](RenewalsDetailsResponseProductsInner.md) |  | [optional] 
**additional_attributes** | [**List[RenewalsDetailsResponseAdditionalAttributesInner]**](RenewalsDetailsResponseAdditionalAttributesInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.models.renewals_details_response import RenewalsDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsDetailsResponse from a JSON string
renewals_details_response_instance = RenewalsDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(RenewalsDetailsResponse.to_json())

# convert the object into a dict
renewals_details_response_dict = renewals_details_response_instance.to_dict()
# create an instance of RenewalsDetailsResponse from a dict
renewals_details_response_from_dict = RenewalsDetailsResponse.from_dict(renewals_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


