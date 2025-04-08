# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.price_and_availability_request_products_inner import PriceAndAvailabilityRequestProductsInner

class TestPriceAndAvailabilityRequestProductsInner(unittest.TestCase):
    """PriceAndAvailabilityRequestProductsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityRequestProductsInner:
        """Test PriceAndAvailabilityRequestProductsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityRequestProductsInner`
        """
        model = PriceAndAvailabilityRequestProductsInner()
        if include_optional:
            return PriceAndAvailabilityRequestProductsInner(
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
                    ]
            )
        else:
            return PriceAndAvailabilityRequestProductsInner(
        )
        """

    def testPriceAndAvailabilityRequestProductsInner(self):
        """Test PriceAndAvailabilityRequestProductsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
