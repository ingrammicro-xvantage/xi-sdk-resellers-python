# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_modify_response_ship_to_info import OrderModifyResponseShipToInfo

class TestOrderModifyResponseShipToInfo(unittest.TestCase):
    """OrderModifyResponseShipToInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderModifyResponseShipToInfo:
        """Test OrderModifyResponseShipToInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderModifyResponseShipToInfo`
        """
        model = OrderModifyResponseShipToInfo()
        if include_optional:
            return OrderModifyResponseShipToInfo(
                address_id = '',
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
            return OrderModifyResponseShipToInfo(
        )
        """

    def testOrderModifyResponseShipToInfo(self):
        """Test OrderModifyResponseShipToInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
