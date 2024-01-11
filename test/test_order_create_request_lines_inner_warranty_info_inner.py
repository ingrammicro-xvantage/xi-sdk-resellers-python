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

from xi-sdk-resellers-python.models.order_create_request_lines_inner_warranty_info_inner import OrderCreateRequestLinesInnerWarrantyInfoInner

class TestOrderCreateRequestLinesInnerWarrantyInfoInner(unittest.TestCase):
    """OrderCreateRequestLinesInnerWarrantyInfoInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateRequestLinesInnerWarrantyInfoInner:
        """Test OrderCreateRequestLinesInnerWarrantyInfoInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateRequestLinesInnerWarrantyInfoInner`
        """
        model = OrderCreateRequestLinesInnerWarrantyInfoInner()
        if include_optional:
            return OrderCreateRequestLinesInnerWarrantyInfoInner(
                direct_line_link = '',
                warranty_line_link = '',
                hardware_line_link = '',
                serial_info = [
                    xi-sdk-resellers-python.models.order_create_request_lines_inner_warranty_info_inner_serial_info_inner.OrderCreateRequest_lines_inner_warrantyInfo_inner_serialInfo_inner(
                        dateof_purchase = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        ship_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        primary_serial_number = '', 
                        secondary_serial_number = '', )
                    ]
            )
        else:
            return OrderCreateRequestLinesInnerWarrantyInfoInner(
        )
        """

    def testOrderCreateRequestLinesInnerWarrantyInfoInner(self):
        """Test OrderCreateRequestLinesInnerWarrantyInfoInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
