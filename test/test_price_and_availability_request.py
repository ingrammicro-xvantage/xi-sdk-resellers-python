# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.price_and_availability_request import PriceAndAvailabilityRequest

class TestPriceAndAvailabilityRequest(unittest.TestCase):
    """PriceAndAvailabilityRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityRequest:
        """Test PriceAndAvailabilityRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityRequest`
        """
        model = PriceAndAvailabilityRequest()
        if include_optional:
            return PriceAndAvailabilityRequest(
                show_available_discounts = True,
                show_reserve_inventory_details = True,
                special_bid_number = '',
                availability_by_warehouse = [
                    xi.sdk.resellers.models.price_and_availability_request_availability_by_warehouse_inner.PriceAndAvailabilityRequest_availabilityByWarehouse_inner(
                        availability_by_warehouse_id = '', 
                        availability_for_all_location = True, )
                    ],
                products = [
                    xi.sdk.resellers.models.price_and_availability_request_products_inner.PriceAndAvailabilityRequest_products_inner(
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        customer_part_number = '', 
                        upc = '', 
                        quantity_requested = '', 
                        plan_id = '', 
                        additional_attributes = [
                            xi.sdk.resellers.models.price_and_availability_request_products_inner_additional_attributes_inner.PriceAndAvailabilityRequest_products_inner_additionalAttributes_inner(
                                attribute_name = '', 
                                attribute_value = '', )
                            ], )
                    ],
                additional_attributes = [
                    xi.sdk.resellers.models.price_and_availability_request_additional_attributes_inner.PriceAndAvailabilityRequest_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ]
            )
        else:
            return PriceAndAvailabilityRequest(
        )
        """

    def testPriceAndAvailabilityRequest(self):
        """Test PriceAndAvailabilityRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
