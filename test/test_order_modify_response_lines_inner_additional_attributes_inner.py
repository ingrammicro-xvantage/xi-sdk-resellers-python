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

from xi-sdk-python.models.order_modify_response_lines_inner_additional_attributes_inner import OrderModifyResponseLinesInnerAdditionalAttributesInner

class TestOrderModifyResponseLinesInnerAdditionalAttributesInner(unittest.TestCase):
    """OrderModifyResponseLinesInnerAdditionalAttributesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderModifyResponseLinesInnerAdditionalAttributesInner:
        """Test OrderModifyResponseLinesInnerAdditionalAttributesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderModifyResponseLinesInnerAdditionalAttributesInner`
        """
        model = OrderModifyResponseLinesInnerAdditionalAttributesInner()
        if include_optional:
            return OrderModifyResponseLinesInnerAdditionalAttributesInner(
                attribute_name = '',
                attribute_value = ''
            )
        else:
            return OrderModifyResponseLinesInnerAdditionalAttributesInner(
        )
        """

    def testOrderModifyResponseLinesInnerAdditionalAttributesInner(self):
        """Test OrderModifyResponseLinesInnerAdditionalAttributesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
