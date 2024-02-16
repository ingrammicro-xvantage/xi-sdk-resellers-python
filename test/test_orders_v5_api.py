# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.api.orders_v5_api import OrdersV5Api


class TestOrdersV5Api(unittest.TestCase):
    """OrdersV5Api unit test stubs"""

    def setUp(self) -> None:
        self.api = OrdersV5Api()

    def tearDown(self) -> None:
        pass

    def test_delete_orders_order_number(self) -> None:
        """Test case for delete_orders_order_number

        Cancel an Existing Order
        """
        pass

    def test_get_orders_search(self) -> None:
        """Test case for get_orders_search

        Search your Orders
        """
        pass

    def test_get_v5_orders_details(self) -> None:
        """Test case for get_v5_orders_details

        Get Order Details
        """
        pass

    def test_post_v5_orders_create(self) -> None:
        """Test case for post_v5_orders_create

        Create a New Order
        """
        pass


if __name__ == '__main__':
    unittest.main()
