# ProductLineType

Product line items object under each invoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linenumber** | **str** |  | [optional] 
**linetype** | **str** |  | [optional] 
**partnumber** | **str** |  | [optional] 
**vendorpartnumber** | **str** |  | [optional] 
**partdescription** | **str** |  | [optional] 
**shipfrombranch** | **str** |  | [optional] 
**shippedquantity** | **str** |  | [optional] 
**orderedquantity** | **str** |  | [optional] 
**marginpercent** | **str** |  | [optional] 
**backorderquantity** | **str** |  | [optional] 
**backorderetadate** | **date** |  | [optional] 
**extendedprice** | **str** |  | [optional] 
**specialbidnumber** | **str** |  | [optional] 
**ordersuffix** | **str** |  | [optional] 
**isacopapplied** | **str** |  | [optional] 
**unitprice** | **str** |  | [optional] 
**unitofmeasure** | **str** |  | [optional] 
**serialnumberdetails** | [**List[ProductLineTypeSerialnumberdetailsInner]**](ProductLineTypeSerialnumberdetailsInner.md) |  | [optional] 
**trackingnumberdetails** | [**List[ProductLineTypeTrackingnumberdetailsInner]**](ProductLineTypeTrackingnumberdetailsInner.md) |  | [optional] 
**productextendedspecs** | [**List[InvoiceDetailResponseServiceresponseInvoicedetailresponseExtendedspecsInner]**](InvoiceDetailResponseServiceresponseInvoicedetailresponseExtendedspecsInner.md) |  | [optional] 

## Example

```python
from xi.sdk.resellers.python.models.product_line_type import ProductLineType

# TODO update the JSON string below
json = "{}"
# create an instance of ProductLineType from a JSON string
product_line_type_instance = ProductLineType.from_json(json)
# print the JSON string representation of the object
print ProductLineType.to_json()

# convert the object into a dict
product_line_type_dict = product_line_type_instance.to_dict()
# create an instance of ProductLineType from a dict
product_line_type_form_dict = product_line_type.from_dict(product_line_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


