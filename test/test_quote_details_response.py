# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.quote_details_response import QuoteDetailsResponse

class TestQuoteDetailsResponse(unittest.TestCase):
    """QuoteDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteDetailsResponse:
        """Test QuoteDetailsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteDetailsResponse`
        """
        model = QuoteDetailsResponse()
        if include_optional:
            return QuoteDetailsResponse(
                quote_name = '',
                quote_number = '',
                quote_guid = '',
                revision = '',
                ingram_quote_date = '',
                last_modified_date = '',
                ingram_quote_expiry_date = '',
                currency_code = '',
                special_bid_id = '',
                special_bid_effective_date = '',
                special_bid_expiration_date = '',
                vendor_quote_number = '',
                status = '',
                status_reason = '',
                closing_reason = '',
                date_closed = '',
                customer_need = '',
                proposed_solution = '',
                intro_preamble = '',
                purchase_instructions = '',
                legal_terms = '',
                quote_type = '',
                lease_info = '',
                leasing_instructions = '',
                im_warehouse = '',
                im_warehouse_gst_number = '',
                payment_terms_name = '',
                reseller_info = xi.sdk.resellers.models.quote_details_response_reseller_info.QuoteDetailsResponse_resellerInfo(
                    contact = '', 
                    company_name = '', 
                    email = '', 
                    phone_number = '', 
                    customer_number = '', ),
                end_user_info = xi.sdk.resellers.models.quote_details_response_end_user_info.QuoteDetailsResponse_endUserInfo(
                    contact = '', 
                    company_name = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    city = '', 
                    state = '', 
                    email = '', 
                    phone_number = '', 
                    postal_code = '', 
                    market_segment = '', ),
                shipping_info = xi.sdk.resellers.models.quote_details_response_shipping_info.QuoteDetailsResponse_shippingInfo(
                    company_name = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    city = '', 
                    state = '', 
                    email = '', 
                    phone_number = '', 
                    postal_code = '', 
                    shp_to_gstin_number = '', ),
                products = [
                    xi.sdk.resellers.models.quote_details_response_products_inner.QuoteDetailsResponse_products_inner(
                        quote_product_guid = '', 
                        line_number = '', 
                        quantity = 56, 
                        notes = '', 
                        ean = '', 
                        coo = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        description = '', 
                        weight = 56, 
                        weight_uom = '', 
                        is_suggestion_product = True, 
                        vpn_category = '', 
                        quote_products_supplier_part_auxiliary_id = '', 
                        vendor_name = '', 
                        terms = '', 
                        plan_description = '', 
                        is_subscription = True, 
                        reseller_margin = '', 
                        requested_start_date = '', 
                        start_date = '', 
                        end_date = '', 
                        serial_number = '', 
                        price = xi.sdk.resellers.models.quote_details_response_products_inner_price.QuoteDetailsResponse_products_inner_price(
                            quote_price = 1.337, 
                            msrp = 1.337, 
                            extended_msrp = 1.337, 
                            extended_quote_price = 1.337, 
                            discount_off_list = '', 
                            type = '', 
                            recurring_price_model = '', 
                            unit_of_measure = '', 
                            tax = '', 
                            extrafees = 1.337, 
                            extra_fees_details = [
                                xi.sdk.resellers.models.quote_details_response_products_inner_price_extra_fees_details_inner.QuoteDetailsResponse_products_inner_price_extraFeesDetails_inner(
                                    extra_fees_description = '', 
                                    extra_fees_amount = 1.337, )
                                ], 
                            discounts = [
                                xi.sdk.resellers.models.quote_details_response_products_inner_price_discounts_inner.QuoteDetailsResponse_products_inner_price_discounts_inner(
                                    type = '', 
                                    amount = 1.337, 
                                    expiration_date = '', 
                                    description = '', 
                                    avaliable_qunatity = 56, 
                                    minimum_quantity = 56, 
                                    bid_number = '', 
                                    bid_version = '', 
                                    valid_from = '', 
                                    valid_to = '', 
                                    discount_off_list = 1.337, )
                                ], ), 
                        bill_details = [
                            xi.sdk.resellers.models.quote_details_response_products_inner_bill_details_inner.QuoteDetailsResponse_products_inner_billDetails_inner(
                                type = '', 
                                unit = '', 
                                frequency = 56, 
                                unit_value = '', )
                            ], )
                    ],
                products_count = 56,
                extended_msrp_total = 1.337,
                quantity_total = 56,
                extra_fees_total = 1.337,
                extra_fees_total_details = [
                    xi.sdk.resellers.models.quote_details_response_products_inner_price_extra_fees_details_inner.QuoteDetailsResponse_products_inner_price_extraFeesDetails_inner(
                        extra_fees_description = '', 
                        extra_fees_amount = 1.337, )
                    ],
                tax_total = 1.337,
                extended_quote_price_total = 1.337,
                freight_amount = 1.337,
                total_quote_amount = '',
                additional_attributes = [
                    xi.sdk.resellers.models.quote_details_response_additional_attributes_inner.QuoteDetailsResponse_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ]
            )
        else:
            return QuoteDetailsResponse(
        )
        """

    def testQuoteDetailsResponse(self):
        """Test QuoteDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
