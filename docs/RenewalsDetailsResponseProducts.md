# RenewalsDetailsResponseProducts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingram_line_number** | **str** | Unique Ingram Micro line number. | [optional] 
**product_description** | **str** | The description of the product. | [optional] 
**vendor_part_number** | **str** | The vendor&#39;s part number for the line item. | [optional] 
**ingram_part_number** | **str** | Unique IngramMicro part number. | [optional] 
**manufacturer_part_number** | **str** | The manufacturer&#39;s part number for the line item. | [optional] 
**unit_price** | **float** | The unit price of the line item. | [optional] 
**quantity** | **int** | The quantity of the line item. | [optional] 
**is_consolidated** | **str** | Is the line item consolidated? Yes or No. | [optional] 

## Example

```python
from xi.sdk.resellers.models.renewals_details_response_products import RenewalsDetailsResponseProducts

# TODO update the JSON string below
json = "{}"
# create an instance of RenewalsDetailsResponseProducts from a JSON string
renewals_details_response_products_instance = RenewalsDetailsResponseProducts.from_json(json)
# print the JSON string representation of the object
print RenewalsDetailsResponseProducts.to_json()

# convert the object into a dict
renewals_details_response_products_dict = renewals_details_response_products_instance.to_dict()
# create an instance of RenewalsDetailsResponseProducts from a dict
renewals_details_response_products_form_dict = renewals_details_response_products.from_dict(renewals_details_response_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


