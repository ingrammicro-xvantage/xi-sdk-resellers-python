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

from xi.sdk.resellers.models.returns_create_request_list_inner_ship_from_info_inner import ReturnsCreateRequestListInnerShipFromInfoInner

class TestReturnsCreateRequestListInnerShipFromInfoInner(unittest.TestCase):
    """ReturnsCreateRequestListInnerShipFromInfoInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReturnsCreateRequestListInnerShipFromInfoInner:
        """Test ReturnsCreateRequestListInnerShipFromInfoInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReturnsCreateRequestListInnerShipFromInfoInner`
        """
        model = ReturnsCreateRequestListInnerShipFromInfoInner()
        if include_optional:
            return ReturnsCreateRequestListInnerShipFromInfoInner(
                company_name = '',
                contact = '',
                address_line1 = '',
                address_line2 = '',
                address_line3 = '',
                city = '',
                state = '',
                postal_code = '',
                country_code = '',
                email = '',
                phone_number = ''
            )
        else:
            return ReturnsCreateRequestListInnerShipFromInfoInner(
                company_name = '',
                contact = '',
                address_line1 = '',
                city = '',
                state = '',
                postal_code = '',
                country_code = '',
                email = '',
        )
        """

    def testReturnsCreateRequestListInnerShipFromInfoInner(self):
        """Test ReturnsCreateRequestListInnerShipFromInfoInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
