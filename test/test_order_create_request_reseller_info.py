# coding: utf-8

"""
    Reseller API

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi.sdk.resellers.models.order_create_request_reseller_info import OrderCreateRequestResellerInfo

class TestOrderCreateRequestResellerInfo(unittest.TestCase):
    """OrderCreateRequestResellerInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateRequestResellerInfo:
        """Test OrderCreateRequestResellerInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateRequestResellerInfo`
        """
        model = OrderCreateRequestResellerInfo()
        if include_optional:
            return OrderCreateRequestResellerInfo(
                reseller_id = '',
                company_name = '',
                contact = '',
                address_line1 = '',
                address_line2 = '',
                address_line3 = '',
                city = '',
                state = '',
                postal_code = '',
                country_code = '',
                phone_number = 56,
                email = ''
            )
        else:
            return OrderCreateRequestResellerInfo(
        )
        """

    def testOrderCreateRequestResellerInfo(self):
        """Test OrderCreateRequestResellerInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
