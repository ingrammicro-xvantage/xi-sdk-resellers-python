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

from xi.sdk.resellers.models.order_detail_response_serviceresponse_orderdetailresponse_commentlines_inner import OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner

class TestOrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner(unittest.TestCase):
    """OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner:
        """Test OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner`
        """
        model = OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner()
        if include_optional:
            return OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner(
                commenttext1 = '',
                commenttext2 = ''
            )
        else:
            return OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner(
        )
        """

    def testOrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner(self):
        """Test OrderDetailResponseServiceresponseOrderdetailresponseCommentlinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
