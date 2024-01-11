# PriceAndAvailabilityResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_status_code** | **str** | Codes signifying whether the sku is active or not. | [optional] 
**product_status_message** | **str** | Message returned saying whether sku is active. | [optional] 
**ingram_part_number** | **str** | Ingram Micro unique part number for the product. | [optional] 
**vendor_part_number** | **str** | Vendor’s part number for the product. | [optional] 
**extended_vendor_part_number** | **str** | Extended Vendor Part Number. *Currently, this feature is not available in these countries (Mexico, Turkey, New Zealand, Colombia, Chile, Brazil, Peru, Western Sahara). | [optional] 
**customer_part_number** | **str** | Reseller / end-user’s part number for the product. | [optional] 
**upc** | **str** | The UPC code for the product. Consists of 12 numeric digits that are uniquely assigned to each trade item. | [optional] 
**part_number_type** | **str** | Number type of the part. | [optional] 
**vendor_number** | **str** | Vendor number that identifies the product. | [optional] 
**vendor_name** | **str** | Vendor name for the order. | [optional] 
**description** | **str** | The description given for the product. | [optional] 
**product_class** | **str** | Indicates whether the product is directly shipped from the vendor’s warehouse or if the product ships from Ingram Micro’s warehouse. Class Codes are Ingram classifications on how skus are stocked A &#x3D; Product that is stocked usually in all IM warehouses and replenished on a regular basis. B &#x3D; Product that is stocked in limited IM warehouses and replenished on a regular basis C &#x3D; Product that is stocked in fewer IM warehouses and replenished on a regular basis. D &#x3D; Product that Ingram Micro has elected to discontinue. E &#x3D; Product that will be phased out later, according to the vendor. You may not want to replenish this product, but instead sell down what is in stock. F &#x3D; Product that we carry for a specific customer or supplier under a contractual agreement. N &#x3D; New Sku. Classification before first receipt O &#x3D; Discontinued product to be liquidated S&#x3D; Order for Specialized Demand (Order to backorder) X&#x3D; direct ship from Vendor V &#x3D; product that vendor has elected to discontinue. | [optional] 
**uom** | **str** | The description given for the product. | [optional] 
**product_status** | **str** | Status that gives whether the product is Active. | [optional] 
**accept_back_order** | **bool** | Boolean that indicates if the product accepts backorder. | [optional] 
**product_authorized** | **bool** | Boolean that indicates whether a product is authorized. | [optional] 
**returnable_product** | **bool** | Boolean that indicates if the product can be returned. | [optional] 
**end_user_info_required** | **bool** | Boolean that indicates  if end user information is required. | [optional] 
**govt_special_price_available** | **bool** | Boolean that indicates if special pricing is available for the product. | [optional] 
**govt_program_type** | **str** | Program type, “PA” for government orders, “ED” for education order. | [optional] 
**govt_end_user_type** | **str** | Type of end user of the program. F &#x3D; Federal, S &#x3D; State, E &#x3D; Local, K &#x3D; K-12 school, and H &#x3D; Higher Education. | [optional] 
**availability** | [**PriceAndAvailabilityResponseInnerAvailability**](PriceAndAvailabilityResponseInnerAvailability.md) |  | [optional] 
**reserve_inventory_details** | [**List[PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner]**](PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner.md) |  | [optional] 
**pricing** | [**PriceAndAvailabilityResponseInnerPricing**](PriceAndAvailabilityResponseInnerPricing.md) |  | [optional] 
**discounts** | [**List[PriceAndAvailabilityResponseInnerDiscountsInner]**](PriceAndAvailabilityResponseInnerDiscountsInner.md) |  | [optional] 
**bundle_part_indicator** | **bool** | True of false value to indicate whether it’s bundle part. *Currently, this feature is not available in these countries (Mexico, Turkey, New Zealand, Colombia, Chile, Brazil, Peru, Western Sahara). | [optional] 
**service_fees** | [**List[PriceAndAvailabilityResponseInnerServiceFeesInner]**](PriceAndAvailabilityResponseInnerServiceFeesInner.md) | *Currently, this feature is not available in these countries (Mexico, Turkey, New Zealand, Colombia, Chile, Brazil, Peru, Western Sahara). | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.price_and_availability_response_inner import PriceAndAvailabilityResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of PriceAndAvailabilityResponseInner from a JSON string
price_and_availability_response_inner_instance = PriceAndAvailabilityResponseInner.from_json(json)
# print the JSON string representation of the object
print PriceAndAvailabilityResponseInner.to_json()

# convert the object into a dict
price_and_availability_response_inner_dict = price_and_availability_response_inner_instance.to_dict()
# create an instance of PriceAndAvailabilityResponseInner from a dict
price_and_availability_response_inner_form_dict = price_and_availability_response_inner.from_dict(price_and_availability_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


