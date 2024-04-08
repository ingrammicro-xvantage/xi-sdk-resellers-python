# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b_miscellaneous_charges_inner import OrderDetailB2BMiscellaneousChargesInner

class TestOrderDetailB2BMiscellaneousChargesInner(unittest.TestCase):
    """OrderDetailB2BMiscellaneousChargesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BMiscellaneousChargesInner:
        """Test OrderDetailB2BMiscellaneousChargesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BMiscellaneousChargesInner`
        """
        model = OrderDetailB2BMiscellaneousChargesInner()
        if include_optional:
            return OrderDetailB2BMiscellaneousChargesInner(
                sub_order_number = '',
                charge_line_reference = '',
                charge_description = '',
                charge_amount = ''
            )
        else:
            return OrderDetailB2BMiscellaneousChargesInner(
        )
        """

    def testOrderDetailB2BMiscellaneousChargesInner(self):
        """Test OrderDetailB2BMiscellaneousChargesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
