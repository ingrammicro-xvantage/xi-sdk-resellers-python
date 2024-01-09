# QuoteDetailsResponseAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | estimateId - is the identification number for an estimate provided by Cisco for a quote.  dealId - is the identification number for the specific deal pricing related to a Cisco quote  vendorName - Name of Vendor associated with the quote.  vendorMessage - Vendor Message is associated with primary vendor in the quote.  In cases where a vendor requires a message be presented in the quote, the vendor name and message will be retreived and must be included in the quote vendor message fields. | [optional] 
**attribute_value** | **str** | The attribute field data. | [optional] 

## Example

```python
from xi-sdk-python.models.quote_details_response_additional_attributes_inner import QuoteDetailsResponseAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteDetailsResponseAdditionalAttributesInner from a JSON string
quote_details_response_additional_attributes_inner_instance = QuoteDetailsResponseAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print QuoteDetailsResponseAdditionalAttributesInner.to_json()

# convert the object into a dict
quote_details_response_additional_attributes_inner_dict = quote_details_response_additional_attributes_inner_instance.to_dict()
# create an instance of QuoteDetailsResponseAdditionalAttributesInner from a dict
quote_details_response_additional_attributes_inner_form_dict = quote_details_response_additional_attributes_inner.from_dict(quote_details_response_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


