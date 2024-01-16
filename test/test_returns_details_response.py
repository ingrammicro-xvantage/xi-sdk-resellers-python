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

from xi.sdk.resellers.python.models.returns_details_response import ReturnsDetailsResponse

class TestReturnsDetailsResponse(unittest.TestCase):
    """ReturnsDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReturnsDetailsResponse:
        """Test ReturnsDetailsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReturnsDetailsResponse`
        """
        model = ReturnsDetailsResponse()
        if include_optional:
            return ReturnsDetailsResponse(
                type_of_details = '',
                rma_claim_id = '',
                case_request_number = '',
                created_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                return_reason = '',
                reference_number = '',
                status = '',
                return_warehouse_address = '',
                products = [
                    xi.sdk.resellers.python.models.returns_details_response_products_inner.returnsDetailsResponse_products_inner(
                        ingram_line_number = '', 
                        description = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        upc = '', 
                        invoice_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        invoice_number = '', 
                        customer_order_number = 56, 
                        request_details = 56, 
                        quantity = 56, 
                        unit_price = 1.337, 
                        extended_price = 1.337, 
                        status = '', 
                        return_branch = 56, 
                        ship_from_branch = 56, )
                    ],
                sub_total = 1.337,
                tax = 1.337,
                additional_fees = 1.337,
                estimated_total = 1.337
            )
        else:
            return ReturnsDetailsResponse(
        )
        """

    def testReturnsDetailsResponse(self):
        """Test ReturnsDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
