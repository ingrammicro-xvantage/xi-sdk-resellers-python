# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_v7_request_reseller_info import OrderCreateV7RequestResellerInfo

class TestOrderCreateV7RequestResellerInfo(unittest.TestCase):
    """OrderCreateV7RequestResellerInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateV7RequestResellerInfo:
        """Test OrderCreateV7RequestResellerInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateV7RequestResellerInfo`
        """
        model = OrderCreateV7RequestResellerInfo()
        if include_optional:
            return OrderCreateV7RequestResellerInfo(
                reseller_id = '',
                company_name = '',
                contact = '',
                address_line1 = '',
                address_line2 = '',
                city = '',
                state = '',
                postal_code = '',
                country_code = '',
                phone_number = '',
                email = ''
            )
        else:
            return OrderCreateV7RequestResellerInfo(
        )
        """

    def testOrderCreateV7RequestResellerInfo(self):
        """Test OrderCreateV7RequestResellerInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
