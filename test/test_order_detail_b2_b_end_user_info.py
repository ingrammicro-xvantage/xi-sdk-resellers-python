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

from xi.sdk.resellers.python.models.order_detail_b2_b_end_user_info import OrderDetailB2BEndUserInfo

class TestOrderDetailB2BEndUserInfo(unittest.TestCase):
    """OrderDetailB2BEndUserInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BEndUserInfo:
        """Test OrderDetailB2BEndUserInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BEndUserInfo`
        """
        model = OrderDetailB2BEndUserInfo()
        if include_optional:
            return OrderDetailB2BEndUserInfo(
                contact = '',
                company_name = '',
                address_line1 = '',
                address_line2 = '',
                address_line3 = '',
                city = '',
                state = '',
                postal_code = '',
                country_code = '',
                phone_number = '',
                email = ''
            )
        else:
            return OrderDetailB2BEndUserInfo(
        )
        """

    def testOrderDetailB2BEndUserInfo(self):
        """Test OrderDetailB2BEndUserInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
