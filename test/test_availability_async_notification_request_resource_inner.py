# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.availability_async_notification_request_resource_inner import AvailabilityAsyncNotificationRequestResourceInner

class TestAvailabilityAsyncNotificationRequestResourceInner(unittest.TestCase):
    """AvailabilityAsyncNotificationRequestResourceInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AvailabilityAsyncNotificationRequestResourceInner:
        """Test AvailabilityAsyncNotificationRequestResourceInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AvailabilityAsyncNotificationRequestResourceInner`
        """
        model = AvailabilityAsyncNotificationRequestResourceInner()
        if include_optional:
            return AvailabilityAsyncNotificationRequestResourceInner(
                event_type = '',
                ingram_part_number = '',
                vendor_part_number = '',
                vendor_name = '',
                upc_code = '',
                sku_status = '',
                back_order_flag = '',
                total_availability = '',
                links = [
                    xi.sdk.resellers.models.availability_async_notification_request_resource_inner_links_inner.AvailabilityAsyncNotificationRequest_resource_inner_links_inner(
                        topic = '', 
                        href = '', 
                        type = '', )
                    ]
            )
        else:
            return AvailabilityAsyncNotificationRequestResourceInner(
        )
        """

    def testAvailabilityAsyncNotificationRequestResourceInner(self):
        """Test AvailabilityAsyncNotificationRequestResourceInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
