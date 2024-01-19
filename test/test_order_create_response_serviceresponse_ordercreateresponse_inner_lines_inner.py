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

from xi.sdk.resellers.models.order_create_response_serviceresponse_ordercreateresponse_inner_lines_inner import OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner

class TestOrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner(unittest.TestCase):
    """OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner:
        """Test OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner`
        """
        model = OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner()
        if include_optional:
            return OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner(
                linetype = '',
                globallinenumber = '',
                partnumber = '',
                globalskuid = '',
                linenumber = '',
                carriercode = '',
                carrierdescription = '',
                requestedunitprice = 1.337,
                requestedquantity = 56,
                confirmedquantity = 56,
                backorderedquantity = 56,
                unitproductprice = 1.337,
                netamount = 1.337,
                warehouseid = '',
                ordersuffix = ''
            )
        else:
            return OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner(
        )
        """

    def testOrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner(self):
        """Test OrderCreateResponseServiceresponseOrdercreateresponseInnerLinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
