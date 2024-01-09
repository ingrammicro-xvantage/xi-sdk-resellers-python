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

from xi-sdk-python.models.quote_list_response_quote_search_response_quote_list_inner import QuoteListResponseQuoteSearchResponseQuoteListInner

class TestQuoteListResponseQuoteSearchResponseQuoteListInner(unittest.TestCase):
    """QuoteListResponseQuoteSearchResponseQuoteListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteListResponseQuoteSearchResponseQuoteListInner:
        """Test QuoteListResponseQuoteSearchResponseQuoteListInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteListResponseQuoteSearchResponseQuoteListInner`
        """
        model = QuoteListResponseQuoteSearchResponseQuoteListInner()
        if include_optional:
            return QuoteListResponseQuoteSearchResponseQuoteListInner(
                quote_name = '',
                quote_number = '',
                revision_number = 56,
                end_user_name = '',
                bid_number = '',
                total_amount = '',
                quote_status = '',
                created_date = 'Tue Oct 08 00:00:00 UTC 2019',
                last_modified_date = 'Tue Oct 08 00:00:00 UTC 2019',
                quote_expiry_date = 'Tue Oct 08 00:00:00 UTC 2019'
            )
        else:
            return QuoteListResponseQuoteSearchResponseQuoteListInner(
        )
        """

    def testQuoteListResponseQuoteSearchResponseQuoteListInner(self):
        """Test QuoteListResponseQuoteSearchResponseQuoteListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
