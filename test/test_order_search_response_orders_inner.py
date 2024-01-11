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

from xi-sdk-resellers-python.models.order_search_response_orders_inner import OrderSearchResponseOrdersInner

class TestOrderSearchResponseOrdersInner(unittest.TestCase):
    """OrderSearchResponseOrdersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderSearchResponseOrdersInner:
        """Test OrderSearchResponseOrdersInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderSearchResponseOrdersInner`
        """
        model = OrderSearchResponseOrdersInner()
        if include_optional:
            return OrderSearchResponseOrdersInner(
                ingram_order_number = '',
                ingram_order_date = '',
                customer_order_number = '',
                vendor_sales_order_number = '',
                vendor_name = '',
                end_user_company_name = '',
                order_total = 1.337,
                order_status = '',
                sub_orders = [
                    xi-sdk-resellers-python.models.order_search_response_orders_inner_sub_orders_inner.OrderSearch_Response_orders_inner_subOrders_inner(
                        sub_order_number = '', 
                        sub_order_total = 1.337, 
                        sub_order_status = '', 
                        links = [
                            xi-sdk-resellers-python.models.order_search_response_orders_inner_sub_orders_inner_links_inner.OrderSearch_Response_orders_inner_subOrders_inner_links_inner(
                                topic = '', 
                                href = '', 
                                type = '', )
                            ], )
                    ],
                links = xi-sdk-resellers-python.models.order_search_response_orders_inner_links.OrderSearch_Response_orders_inner_links(
                    topic = '', 
                    href = '', 
                    type = '', )
            )
        else:
            return OrderSearchResponseOrdersInner(
        )
        """

    def testOrderSearchResponseOrdersInner(self):
        """Test OrderSearchResponseOrdersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
