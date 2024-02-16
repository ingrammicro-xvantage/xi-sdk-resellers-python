# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.quote_details_response_end_user_info import QuoteDetailsResponseEndUserInfo

class TestQuoteDetailsResponseEndUserInfo(unittest.TestCase):
    """QuoteDetailsResponseEndUserInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteDetailsResponseEndUserInfo:
        """Test QuoteDetailsResponseEndUserInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteDetailsResponseEndUserInfo`
        """
        model = QuoteDetailsResponseEndUserInfo()
        if include_optional:
            return QuoteDetailsResponseEndUserInfo(
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
                market_segment = ''
            )
        else:
            return QuoteDetailsResponseEndUserInfo(
        )
        """

    def testQuoteDetailsResponseEndUserInfo(self):
        """Test QuoteDetailsResponseEndUserInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
