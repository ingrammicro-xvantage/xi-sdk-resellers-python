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

from xi-sdk-python.models.order_delete_response import OrderDeleteResponse

class TestOrderDeleteResponse(unittest.TestCase):
    """OrderDeleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDeleteResponse:
        """Test OrderDeleteResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDeleteResponse`
        """
        model = OrderDeleteResponse()
        if include_optional:
            return OrderDeleteResponse(
                serviceresponse = xi-sdk-python.models.order_cancel_response_serviceresponse.orderCancelResponse_serviceresponse(
                    responsepreamble = xi-sdk-python.models.order_cancel_response_serviceresponse_responsepreamble.orderCancelResponse_serviceresponse_responsepreamble(
                        request_status = '', 
                        return_code = '', 
                        return_message = '', ), )
            )
        else:
            return OrderDeleteResponse(
        )
        """

    def testOrderDeleteResponse(self):
        """Test OrderDeleteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
