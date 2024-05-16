# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_request_end_user_info import OrderCreateRequestEndUserInfo

class TestOrderCreateRequestEndUserInfo(unittest.TestCase):
    """OrderCreateRequestEndUserInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateRequestEndUserInfo:
        """Test OrderCreateRequestEndUserInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateRequestEndUserInfo`
        """
        model = OrderCreateRequestEndUserInfo()
        if include_optional:
            return OrderCreateRequestEndUserInfo(
                end_user_id = '',
                contact = '',
                company_name = '',
                name1 = '',
                name2 = '',
                address_line1 = '',
                address_line2 = '',
                address_line3 = '',
                address_line4 = '',
                city = '',
                state = '',
                postal_code = '',
                country_code = '',
                phone_number = '',
                email = ''
            )
        else:
            return OrderCreateRequestEndUserInfo(
        )
        """

    def testOrderCreateRequestEndUserInfo(self):
        """Test OrderCreateRequestEndUserInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
