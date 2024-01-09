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

from xi-sdk-python.models.order_detail_response_miscellaneous_charges_inner import OrderDetailResponseMiscellaneousChargesInner

class TestOrderDetailResponseMiscellaneousChargesInner(unittest.TestCase):
    """OrderDetailResponseMiscellaneousChargesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailResponseMiscellaneousChargesInner:
        """Test OrderDetailResponseMiscellaneousChargesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailResponseMiscellaneousChargesInner`
        """
        model = OrderDetailResponseMiscellaneousChargesInner()
        if include_optional:
            return OrderDetailResponseMiscellaneousChargesInner(
                sub_order_number = '',
                charge_line_reference = '',
                charge_description = '',
                charge_amount = 1.337
            )
        else:
            return OrderDetailResponseMiscellaneousChargesInner(
        )
        """

    def testOrderDetailResponseMiscellaneousChargesInner(self):
        """Test OrderDetailResponseMiscellaneousChargesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
