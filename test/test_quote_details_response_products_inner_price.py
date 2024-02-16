# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

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
                quote_price = 56,
                msrp = 56,
                extended_msrp = 56,
                extended_quote_price = 56,
                discount_off_list = 1.337
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
