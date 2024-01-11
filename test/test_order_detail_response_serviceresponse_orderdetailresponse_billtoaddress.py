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

from xi-sdk-resellers-python.models.order_detail_response_serviceresponse_orderdetailresponse_billtoaddress import OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress

class TestOrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress(unittest.TestCase):
    """OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress:
        """Test OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress`
        """
        model = OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress()
        if include_optional:
            return OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress(
                suffix = '',
                name = '',
                attention = '',
                addressline1 = '',
                addressline2 = '',
                addressline3 = '',
                city = '',
                state = '',
                postalcode = '',
                countrycode = ''
            )
        else:
            return OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress(
        )
        """

    def testOrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress(self):
        """Test OrderDetailResponseServiceresponseOrderdetailresponseBilltoaddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
