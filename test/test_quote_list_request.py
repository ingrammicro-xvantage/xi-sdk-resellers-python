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

from xi-sdk-resellers-python.models.quote_list_request import QuoteListRequest

class TestQuoteListRequest(unittest.TestCase):
    """QuoteListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteListRequest:
        """Test QuoteListRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteListRequest`
        """
        model = QuoteListRequest()
        if include_optional:
            return QuoteListRequest(
                quote_search_request = xi-sdk-resellers-python.models.quote_list_request_quote_search_request.quoteListRequest_quoteSearchRequest(
                    request_preamble = xi-sdk-resellers-python.models.quote_list_request_quote_search_request_request_preamble.quoteListRequest_quoteSearchRequest_requestPreamble(
                        customer_number = '', 
                        customer_contact = '', 
                        iso_country_code = '', ), 
                    retrieve_quote_request = xi-sdk-resellers-python.models.quote_list_request_quote_search_request_retrieve_quote_request.quoteListRequest_quoteSearchRequest_retrieveQuoteRequest(
                        quote_number = '', 
                        bid_number = '', 
                        end_user_name = '', 
                        from_date = 'Thu Aug 01 00:00:00 UTC 2019', 
                        to_date = 'Fri Nov 01 00:00:00 UTC 2019', 
                        page_index = '', 
                        records_per_page = '', 
                        sorting = 'asc', 
                        sorting_column_name = 'toDate', 
                        third_party_source = '', ), )
            )
        else:
            return QuoteListRequest(
        )
        """

    def testQuoteListRequest(self):
        """Test QuoteListRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
