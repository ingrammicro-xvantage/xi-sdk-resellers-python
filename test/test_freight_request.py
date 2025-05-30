# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.freight_request import FreightRequest

class TestFreightRequest(unittest.TestCase):
    """FreightRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FreightRequest:
        """Test FreightRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FreightRequest`
        """
        model = FreightRequest()
        if include_optional:
            return FreightRequest(
                bill_to_address_id = None,
                ship_to_address_id = '',
                ship_to_address = xi.sdk.resellers.models.freight_request_ship_to_address.freightRequest_shipToAddress(
                    company_name = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', ),
                lines = [
                    xi.sdk.resellers.models.freight_request_lines_inner.freightRequest_lines_inner(
                        customer_line_number = '', 
                        ingram_part_number = '', 
                        quantity = '', 
                        warehouse_id = '', 
                        carrier_code = '', )
                    ]
            )
        else:
            return FreightRequest(
        )
        """

    def testFreightRequest(self):
        """Test FreightRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
