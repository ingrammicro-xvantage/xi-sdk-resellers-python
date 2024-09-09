# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.quote_details_response_products_inner import QuoteDetailsResponseProductsInner

class TestQuoteDetailsResponseProductsInner(unittest.TestCase):
    """QuoteDetailsResponseProductsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteDetailsResponseProductsInner:
        """Test QuoteDetailsResponseProductsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteDetailsResponseProductsInner`
        """
        model = QuoteDetailsResponseProductsInner()
        if include_optional:
            return QuoteDetailsResponseProductsInner(
                quote_product_guid = '',
                line_number = '',
                quantity = 56,
                remaining_quote_qty = 56,
                minimum_order_allowed_qty = 56,
                notes = '',
                ean = '',
                coo = '',
                ingram_part_number = '',
                vendor_part_number = '',
                description = '',
                weight = 1.337,
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
                    remaining_quantity_extended_msrp = 1.337, 
                    remaining_quantity_extended_quote_price = 1.337, 
                    discount_off_list = '', 
                    type = '', 
                    recurring_price_model = '', 
                    unit_of_measure = '', 
                    tax = 1.337, 
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
                    ]
            )
        else:
            return QuoteDetailsResponseProductsInner(
        )
        """

    def testQuoteDetailsResponseProductsInner(self):
        """Test QuoteDetailsResponseProductsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
