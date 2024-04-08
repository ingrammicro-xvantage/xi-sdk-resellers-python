# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.async_order_create_dto_end_user_info import AsyncOrderCreateDTOEndUserInfo

class TestAsyncOrderCreateDTOEndUserInfo(unittest.TestCase):
    """AsyncOrderCreateDTOEndUserInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsyncOrderCreateDTOEndUserInfo:
        """Test AsyncOrderCreateDTOEndUserInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsyncOrderCreateDTOEndUserInfo`
        """
        model = AsyncOrderCreateDTOEndUserInfo()
        if include_optional:
            return AsyncOrderCreateDTOEndUserInfo(
                end_user_id = '',
                end_user_type = '',
                company_name = '',
                name1 = '',
                name2 = '',
                contact_id = '',
                address_line1 = '',
                address_line2 = '',
                address_line3 = '',
                contact = '',
                city = '',
                state = '',
                postal_code = '',
                address_line4 = '',
                country_code = '',
                phone_number = '',
                email = ''
            )
        else:
            return AsyncOrderCreateDTOEndUserInfo(
        )
        """

    def testAsyncOrderCreateDTOEndUserInfo(self):
        """Test AsyncOrderCreateDTOEndUserInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
