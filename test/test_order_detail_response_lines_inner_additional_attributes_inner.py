# coding: utf-8

"""
    Reseller API Documentation - United States

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi-sdk-python.models.order_detail_response_lines_inner_additional_attributes_inner import OrderDetailResponseLinesInnerAdditionalAttributesInner

class TestOrderDetailResponseLinesInnerAdditionalAttributesInner(unittest.TestCase):
    """OrderDetailResponseLinesInnerAdditionalAttributesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailResponseLinesInnerAdditionalAttributesInner:
        """Test OrderDetailResponseLinesInnerAdditionalAttributesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailResponseLinesInnerAdditionalAttributesInner`
        """
        model = OrderDetailResponseLinesInnerAdditionalAttributesInner()
        if include_optional:
            return OrderDetailResponseLinesInnerAdditionalAttributesInner(
                attribute_name = '',
                attribute_value = ''
            )
        else:
            return OrderDetailResponseLinesInnerAdditionalAttributesInner(
        )
        """

    def testOrderDetailResponseLinesInnerAdditionalAttributesInner(self):
        """Test OrderDetailResponseLinesInnerAdditionalAttributesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
