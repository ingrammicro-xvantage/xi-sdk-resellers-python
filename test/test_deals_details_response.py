# coding: utf-8

"""
    Reseller API Documentation - United States

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi-sdk-python.models.deals_details_response import DealsDetailsResponse

class TestDealsDetailsResponse(unittest.TestCase):
    """DealsDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DealsDetailsResponse:
        """Test DealsDetailsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DealsDetailsResponse`
        """
        model = DealsDetailsResponse()
        if include_optional:
            return DealsDetailsResponse(
                deal_id = '',
                version = '',
                end_user = '',
                extended_msrp = 1.337,
                vendor = '',
                deal_received_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                deal_expiry_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                price_protection_end_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                currency_code = '',
                end_user_info = [
                    xi-sdk-python.models.renewals_details_response_end_user_info_inner.renewalsDetailsResponse_endUserInfo_inner(
                        contact = '', 
                        name1 = '', 
                        name2 = '', 
                        company_name = '', 
                        address_line1 = '', 
                        address_line2 = '', 
                        address_line3 = '', 
                        address_line4 = '', 
                        city = '', 
                        state = '', 
                        postal_code = '', 
                        country_code = '', 
                        phone_number = '', 
                        email = '', )
                    ],
                products = [
                    xi-sdk-python.models.deals_details_response_products_inner.dealsDetailsResponse_products_inner(
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        upc = '', 
                        product_description = '', 
                        msrp = 1.337, 
                        extended_msrp = 1.337, 
                        standard_price = 1.337, 
                        approved_quantity = 56, 
                        remaining_quantity = 56, 
                        comments = '', 
                        special_conditions = '', 
                        start_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        expiration_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        days_remaining = 56, )
                    ]
            )
        else:
            return DealsDetailsResponse(
        )
        """

    def testDealsDetailsResponse(self):
        """Test DealsDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
