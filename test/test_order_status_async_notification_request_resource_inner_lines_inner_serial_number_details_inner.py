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

from xi-sdk-resellers-python.models.order_status_async_notification_request_resource_inner_lines_inner_serial_number_details_inner import OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner

class TestOrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner(unittest.TestCase):
    """OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner:
        """Test OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner`
        """
        model = OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner()
        if include_optional:
            return OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner(
                serial_number = ''
            )
        else:
            return OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner(
        )
        """

    def testOrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner(self):
        """Test OrderStatusAsyncNotificationRequestResourceInnerLinesInnerSerialNumberDetailsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
