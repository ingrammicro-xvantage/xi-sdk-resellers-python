# coding: utf-8

"""
    Reseller API Documentation

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi-sdk-resellers-python.models.order_search_response_orders_inner_links import OrderSearchResponseOrdersInnerLinks

class TestOrderSearchResponseOrdersInnerLinks(unittest.TestCase):
    """OrderSearchResponseOrdersInnerLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderSearchResponseOrdersInnerLinks:
        """Test OrderSearchResponseOrdersInnerLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderSearchResponseOrdersInnerLinks`
        """
        model = OrderSearchResponseOrdersInnerLinks()
        if include_optional:
            return OrderSearchResponseOrdersInnerLinks(
                topic = '',
                href = '',
                type = ''
            )
        else:
            return OrderSearchResponseOrdersInnerLinks(
        )
        """

    def testOrderSearchResponseOrdersInnerLinks(self):
        """Test OrderSearchResponseOrdersInnerLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()