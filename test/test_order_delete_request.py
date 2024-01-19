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

from xi.sdk.resellers.models.order_delete_request import OrderDeleteRequest

class TestOrderDeleteRequest(unittest.TestCase):
    """OrderDeleteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDeleteRequest:
        """Test OrderDeleteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDeleteRequest`
        """
        model = OrderDeleteRequest()
        if include_optional:
            return OrderDeleteRequest(
                servicerequest = xi.sdk.resellers.models.order_delete_request_servicerequest.orderDeleteRequest_servicerequest(
                    requestpreamble = xi.sdk.resellers.models.order_delete_request_servicerequest_requestpreamble.orderDeleteRequest_servicerequest_requestpreamble(
                        isocountrycode = '', 
                        customer_number = '', ), 
                    order_delete_request_details = xi.sdk.resellers.models.order_delete_request_servicerequest_order_delete_request_details.orderDeleteRequest_servicerequest_OrderDeleteRequestDetails(
                        entry_date = '8/25/2018', 
                        order_branch = '', 
                        order_number = '', 
                        rejection_code = '', 
                        distribution_number = '', 
                        shipment_number = '', 
                        operator_id = '', ), )
            )
        else:
            return OrderDeleteRequest(
        )
        """

    def testOrderDeleteRequest(self):
        """Test OrderDeleteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
