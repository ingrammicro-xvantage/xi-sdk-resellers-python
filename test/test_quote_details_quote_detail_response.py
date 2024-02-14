# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.quote_details_quote_detail_response import QuoteDetailsQuoteDetailResponse

class TestQuoteDetailsQuoteDetailResponse(unittest.TestCase):
    """QuoteDetailsQuoteDetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteDetailsQuoteDetailResponse:
        """Test QuoteDetailsQuoteDetailResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteDetailsQuoteDetailResponse`
        """
        model = QuoteDetailsQuoteDetailResponse()
        if include_optional:
            return QuoteDetailsQuoteDetailResponse(
                response_preamble = xi.sdk.resellers.models.quote_details_quote_detail_response_response_preamble.quoteDetails_quoteDetailResponse_responsePreamble(
                    response_status = '', 
                    status_code = '', 
                    response_message = '', ),
                retrieve_quote_response = xi.sdk.resellers.models.quote_details_quote_detail_response_retrieve_quote_response.quoteDetails_quoteDetailResponse_retrieveQuoteResponse(
                    quote_guid = '', 
                    quote_name = '', 
                    quote_number = '', 
                    quote_expiry_date = 'Wed Jan 01 00:00:00 UTC 2020', 
                    revision_number = '', 
                    intro_preamble = '', 
                    purchase_instructions = '', 
                    legal_terms = '', 
                    currency_code = '', 
                    price_deviation_id = '', 
                    price_deviation_start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    price_deviation_expiry_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    customer_need = '', 
                    solution_proposed = '', 
                    status = '', 
                    created = 'Fri Oct 04 00:00:00 UTC 2019', 
                    modified = 'Fri Oct 04 00:00:00 UTC 2019', 
                    leasing_calculations = '', 
                    leasing_instructions = '', 
                    account_info = xi.sdk.resellers.models.quote_details_quote_detail_response_retrieve_quote_response_account_info.quoteDetails_quoteDetailResponse_retrieveQuoteResponse_accountInfo(
                        account_name = '', 
                        bcn = '', 
                        phone = '', ), 
                    contact_info = xi.sdk.resellers.models.quote_details_quote_detail_response_retrieve_quote_response_contact_info.quoteDetails_quoteDetailResponse_retrieveQuoteResponse_contactInfo(
                        contact_email = '', 
                        contact_name = '', ), 
                    vendor_attributes = xi.sdk.resellers.models.quote_details_quote_detail_response_retrieve_quote_response_vendor_attributes.quoteDetails_quoteDetailResponse_retrieveQuoteResponse_vendorAttributes(
                        estimate_id = '', 
                        deal_id = '', 
                        vendor_name = '', 
                        vendor_setting_message = '', ), 
                    end_user = xi.sdk.resellers.models.quote_details_quote_detail_response_retrieve_quote_response_end_user.quoteDetails_quoteDetailResponse_retrieveQuoteResponse_endUser(
                        end_user_name = '', 
                        end_user_address = '', 
                        end_user_address2 = '', 
                        end_user_address3 = '', 
                        end_user_city = '', 
                        end_user_state = '', 
                        end_user_email = '', 
                        end_user_phone = '', 
                        end_user_zip_code = '', 
                        end_user_contact_name = '', 
                        end_user_market_segment = '', ), ),
                quote_product_list = [
                    xi.sdk.resellers.models.quote_details/quote_product_list/response.quoteDetails.quoteProductList.Response(
                        quote_product_guid = '', 
                        quantity = '', 
                        comments = '', 
                        bid_start_date = '', 
                        bid_expiry_date = '', 
                        sku = '', 
                        line_number = '', 
                        description = '', 
                        vendor_part_number = '', 
                        weight = '', 
                        is_suggestion_product = '', 
                        vpn_category = '', 
                        quote_products_supplier_part_auxiliary_id = '', 
                        quote_products_vendor = '', 
                        price = xi.sdk.resellers.models.quote_product_list_price.quoteProductList_price(
                            quote_price = 1.337, 
                            msrp = 1.337, 
                            extended_msrp = 1.337, 
                            extended_quote_price = 1.337, ), )
                    ],
                total_quote_product_count = '',
                total_extended_msrp = '',
                total_quantity = 56,
                total_extended_quote_price = ''
            )
        else:
            return QuoteDetailsQuoteDetailResponse(
        )
        """

    def testQuoteDetailsQuoteDetailResponse(self):
        """Test QuoteDetailsQuoteDetailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
