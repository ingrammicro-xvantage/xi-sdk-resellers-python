# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_links_inner import OrderStatusAsyncNotificationRequestResourceInnerLinksInner

class TestOrderStatusAsyncNotificationRequestResourceInnerLinksInner(unittest.TestCase):
    """OrderStatusAsyncNotificationRequestResourceInnerLinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderStatusAsyncNotificationRequestResourceInnerLinksInner:
        """Test OrderStatusAsyncNotificationRequestResourceInnerLinksInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderStatusAsyncNotificationRequestResourceInnerLinksInner`
        """
        model = OrderStatusAsyncNotificationRequestResourceInnerLinksInner()
        if include_optional:
            return OrderStatusAsyncNotificationRequestResourceInnerLinksInner(
                topic = '',
                href = '',
                type = ''
            )
        else:
            return OrderStatusAsyncNotificationRequestResourceInnerLinksInner(
        )
        """

    def testOrderStatusAsyncNotificationRequestResourceInnerLinksInner(self):
        """Test OrderStatusAsyncNotificationRequestResourceInnerLinksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
