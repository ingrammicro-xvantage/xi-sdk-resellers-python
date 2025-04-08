# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_response_orders_inner_additional_attributes_inner import OrderCreateResponseOrdersInnerAdditionalAttributesInner

class TestOrderCreateResponseOrdersInnerAdditionalAttributesInner(unittest.TestCase):
    """OrderCreateResponseOrdersInnerAdditionalAttributesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateResponseOrdersInnerAdditionalAttributesInner:
        """Test OrderCreateResponseOrdersInnerAdditionalAttributesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateResponseOrdersInnerAdditionalAttributesInner`
        """
        model = OrderCreateResponseOrdersInnerAdditionalAttributesInner()
        if include_optional:
            return OrderCreateResponseOrdersInnerAdditionalAttributesInner(
                attribute_name = '',
                attribute_value = ''
            )
        else:
            return OrderCreateResponseOrdersInnerAdditionalAttributesInner(
        )
        """

    def testOrderCreateResponseOrdersInnerAdditionalAttributesInner(self):
        """Test OrderCreateResponseOrdersInnerAdditionalAttributesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
