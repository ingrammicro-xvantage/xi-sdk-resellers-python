# coding: utf-8

"""
    Reseller API

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi.sdk.resellers.models.price_and_availability_request_products_inner_additional_attributes_inner import PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner

class TestPriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner(unittest.TestCase):
    """PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner:
        """Test PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner`
        """
        model = PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner()
        if include_optional:
            return PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner(
                attribute_name = '',
                attribute_value = ''
            )
        else:
            return PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner(
        )
        """

    def testPriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner(self):
        """Test PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
