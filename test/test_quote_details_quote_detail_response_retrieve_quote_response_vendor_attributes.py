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

from xi.sdk.resellers.python.models.quote_details_quote_detail_response_retrieve_quote_response_vendor_attributes import QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes

class TestQuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes(unittest.TestCase):
    """QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes:
        """Test QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes`
        """
        model = QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes()
        if include_optional:
            return QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes(
                estimate_id = '',
                deal_id = '',
                vendor_name = '',
                vendor_setting_message = ''
            )
        else:
            return QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes(
        )
        """

    def testQuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes(self):
        """Test QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseVendorAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
