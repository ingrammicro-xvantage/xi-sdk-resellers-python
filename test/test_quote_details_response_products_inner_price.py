# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.quote_details_response_products_inner_price import QuoteDetailsResponseProductsInnerPrice

class TestQuoteDetailsResponseProductsInnerPrice(unittest.TestCase):
    """QuoteDetailsResponseProductsInnerPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteDetailsResponseProductsInnerPrice:
        """Test QuoteDetailsResponseProductsInnerPrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteDetailsResponseProductsInnerPrice`
        """
        model = QuoteDetailsResponseProductsInnerPrice()
        if include_optional:
            return QuoteDetailsResponseProductsInnerPrice(
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
                    ]
            )
        else:
            return QuoteDetailsResponseProductsInnerPrice(
        )
        """

    def testQuoteDetailsResponseProductsInnerPrice(self):
        """Test QuoteDetailsResponseProductsInnerPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
