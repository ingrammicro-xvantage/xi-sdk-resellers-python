# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.renewals_search_response import RenewalsSearchResponse

class TestRenewalsSearchResponse(unittest.TestCase):
    """RenewalsSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenewalsSearchResponse:
        """Test RenewalsSearchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenewalsSearchResponse`
        """
        model = RenewalsSearchResponse()
        if include_optional:
            return RenewalsSearchResponse(
                records_found = 56,
                page_size = 56,
                page_number = 56,
                renewals = [
                    xi.sdk.resellers.models.renewals_search_response_renewals_inner.renewalsSearchResponse_renewals_inner(
                        renewal_id = 56, 
                        customer_order_number = '', 
                        reference_number = '', 
                        end_user = '', 
                        vendor = '', 
                        expiration_date = '', 
                        renewal_value = 1.337, 
                        status = '', 
                        links = [
                            xi.sdk.resellers.models.renewals_search_response_renewals_inner_links_inner.renewalsSearchResponse_renewals_inner_links_inner(
                                topic = '', 
                                href = '', 
                                type = '', )
                            ], )
                    ],
                next_page = '',
                previous_page = ''
            )
        else:
            return RenewalsSearchResponse(
        )
        """

    def testRenewalsSearchResponse(self):
        """Test RenewalsSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
