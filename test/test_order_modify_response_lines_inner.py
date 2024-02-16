# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_modify_response_lines_inner import OrderModifyResponseLinesInner

class TestOrderModifyResponseLinesInner(unittest.TestCase):
    """OrderModifyResponseLinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderModifyResponseLinesInner:
        """Test OrderModifyResponseLinesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderModifyResponseLinesInner`
        """
        model = OrderModifyResponseLinesInner()
        if include_optional:
            return OrderModifyResponseLinesInner(
                sub_order_number = '',
                ingram_line_number = '',
                customer_line_number = '',
                ingram_part_number = '',
                vendor_part_number = '',
                quantity_ordered = 56,
                quantity_confirmed = 56,
                quantity_back_ordered = 56,
                shipment_details = xi.sdk.resellers.models.order_modify_response_lines_inner_shipment_details.OrderModifyResponse_lines_inner_shipmentDetails(
                    carrier_code = '', 
                    carrier_name = '', 
                    freight_account_number = '', ),
                additional_attributes = [
                    xi.sdk.resellers.models.order_modify_response_lines_inner_additional_attributes_inner.OrderModifyResponse_lines_inner_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ],
                notes = ''
            )
        else:
            return OrderModifyResponseLinesInner(
        )
        """

    def testOrderModifyResponseLinesInner(self):
        """Test OrderModifyResponseLinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
