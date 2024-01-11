# coding: utf-8

"""
    Reseller API Documentation

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi-sdk-resellers-python.api.orders_api import OrdersApi


class TestOrdersApi(unittest.TestCase):
    """OrdersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrdersApi()

    def tearDown(self) -> None:
        pass

    def test_delete_ordercancel(self) -> None:
        """Test case for delete_ordercancel

        Cancel your Order
        """
        pass

    def test_get_orderdetails_v6_1(self) -> None:
        """Test case for get_orderdetails_v6_1

        Get Order Details v6.1
        """
        pass

    def test_get_resellers_v6_ordersearch(self) -> None:
        """Test case for get_resellers_v6_ordersearch

        Search your Orders
        """
        pass

    def test_post_createorder_v6(self) -> None:
        """Test case for post_createorder_v6

        Create your Order
        """
        pass

    def test_put_ordermodify(self) -> None:
        """Test case for put_ordermodify

        Modify your Order
        """
        pass


if __name__ == '__main__':
    unittest.main()
