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

from xi.sdk.resellers.python.models.post_quote_to_order_v6400_response_fields_inner import PostQuoteToOrderV6400ResponseFieldsInner

class TestPostQuoteToOrderV6400ResponseFieldsInner(unittest.TestCase):
    """PostQuoteToOrderV6400ResponseFieldsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostQuoteToOrderV6400ResponseFieldsInner:
        """Test PostQuoteToOrderV6400ResponseFieldsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostQuoteToOrderV6400ResponseFieldsInner`
        """
        model = PostQuoteToOrderV6400ResponseFieldsInner()
        if include_optional:
            return PostQuoteToOrderV6400ResponseFieldsInner(
                field = '',
                message = '',
                value = ''
            )
        else:
            return PostQuoteToOrderV6400ResponseFieldsInner(
        )
        """

    def testPostQuoteToOrderV6400ResponseFieldsInner(self):
        """Test PostQuoteToOrderV6400ResponseFieldsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
