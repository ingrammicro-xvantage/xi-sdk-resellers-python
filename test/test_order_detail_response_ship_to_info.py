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

from xi.sdk.resellers.python.models.order_detail_response_ship_to_info import OrderDetailResponseShipToInfo

class TestOrderDetailResponseShipToInfo(unittest.TestCase):
    """OrderDetailResponseShipToInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailResponseShipToInfo:
        """Test OrderDetailResponseShipToInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailResponseShipToInfo`
        """
        model = OrderDetailResponseShipToInfo()
        if include_optional:
            return OrderDetailResponseShipToInfo(
                contact = '',
                company_name = '',
                name1 = '',
                name2 = '',
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
            return OrderDetailResponseShipToInfo(
        )
        """

    def testOrderDetailResponseShipToInfo(self):
        """Test OrderDetailResponseShipToInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
