# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.quote_list_request_quote_search_request_retrieve_quote_request import QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest

class TestQuoteListRequestQuoteSearchRequestRetrieveQuoteRequest(unittest.TestCase):
    """QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest:
        """Test QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest`
        """
        model = QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest()
        if include_optional:
            return QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest(
                quote_number = '',
                bid_number = '',
                end_user_name = '',
                from_date = 'Thu Aug 01 00:00:00 UTC 2019',
                to_date = 'Fri Nov 01 00:00:00 UTC 2019',
                page_index = '',
                records_per_page = '',
                sorting = 'asc',
                sorting_column_name = 'toDate',
                third_party_source = ''
            )
        else:
            return QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest(
        )
        """

    def testQuoteListRequestQuoteSearchRequestRetrieveQuoteRequest(self):
        """Test QuoteListRequestQuoteSearchRequestRetrieveQuoteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
