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

from xi.sdk.resellers.python.models.order_status_async_notification_request import OrderStatusAsyncNotificationRequest

class TestOrderStatusAsyncNotificationRequest(unittest.TestCase):
    """OrderStatusAsyncNotificationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderStatusAsyncNotificationRequest:
        """Test OrderStatusAsyncNotificationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderStatusAsyncNotificationRequest`
        """
        model = OrderStatusAsyncNotificationRequest()
        if include_optional:
            return OrderStatusAsyncNotificationRequest(
                topic = '',
                event = '',
                event_time_stamp = '',
                event_id = '',
                resource = [
                    xi.sdk.resellers.python.models.order_status_async_notification_request_resource_inner.OrderStatusAsyncNotificationRequest_resource_inner(
                        event_type = '', 
                        order_number = '', 
                        customer_order_number = '', 
                        order_entry_time_stamp = '', 
                        lines = [
                            xi.sdk.resellers.python.models.order_status_async_notification_request_resource_inner_lines_inner.OrderStatusAsyncNotificationRequest_resource_inner_lines_inner(
                                line_number = '', 
                                sub_order_number = '', 
                                line_status = '', 
                                ingram_part_number = '', 
                                vendor_part_number = '', 
                                requested_quantity = '', 
                                shipped_quantity = '', 
                                backordered_quantity = '', 
                                shipment_details = [
                                    xi.sdk.resellers.python.models.order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner.OrderStatusAsyncNotificationRequest_resource_inner_lines_inner_shipmentDetails_inner(
                                        shipment_date = '', 
                                        ship_from_warehouse_id = '', 
                                        warehouse_name = '', 
                                        carrier_code = '', 
                                        carrier_name = '', 
                                        package_details = [
                                            xi.sdk.resellers.python.models.order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_package_details_inner.OrderStatusAsyncNotificationRequest_resource_inner_lines_inner_shipmentDetails_inner_packageDetails_inner(
                                                carton_number = '', 
                                                quantity_inbox = '', 
                                                tracking_number = '', )
                                            ], )
                                    ], 
                                serial_number_details = [
                                    xi.sdk.resellers.python.models.order_status_async_notification_request_resource_inner_lines_inner_serial_number_details_inner.OrderStatusAsyncNotificationRequest_resource_inner_lines_inner_serialNumberDetails_inner(
                                        serial_number = '', )
                                    ], )
                            ], 
                        links = [
                            xi.sdk.resellers.python.models.order_status_async_notification_request_resource_inner_links_inner.OrderStatusAsyncNotificationRequest_resource_inner_links_inner(
                                topic = '', 
                                href = '', 
                                type = '', )
                            ], )
                    ]
            )
        else:
            return OrderStatusAsyncNotificationRequest(
        )
        """

    def testOrderStatusAsyncNotificationRequest(self):
        """Test OrderStatusAsyncNotificationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
