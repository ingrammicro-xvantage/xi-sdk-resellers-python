# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_search_response_service_response_ordersearchresponse_orders_inner import OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner

class TestOrderSearchResponseServiceResponseOrdersearchresponseOrdersInner(unittest.TestCase):
    """OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner:
        """Test OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner`
        """
        model = OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner()
        if include_optional:
            return OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner(
                ordernumber = '',
                entrytimestamp = '',
                customerordernumber = '',
                suborders = [
                    xi.sdk.resellers.models.order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner.orderSearchResponse_serviceResponse_ordersearchresponse_orders_inner_suborders_inner(
                        subordernumber = '', 
                        statuscode = '', 
                        status = '', 
                        holdreasoncode = '', 
                        holdreason = '', 
                        links = [
                            xi.sdk.resellers.models.order_search_response_service_response_ordersearchresponse_orders_inner_suborders_inner_links_inner.orderSearchResponse_serviceResponse_ordersearchresponse_orders_inner_suborders_inner_links_inner(
                                topic = 'orders', 
                                href = '', 
                                type = 'GET', )
                            ], )
                    ],
                links = xi.sdk.resellers.models.order_search_response_service_response_ordersearchresponse_orders_inner_links.orderSearchResponse_serviceResponse_ordersearchresponse_orders_inner_links(
                    topic = 'orders', 
                    href = '', 
                    type = 'GET', )
            )
        else:
            return OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner(
                ordernumber = '',
                entrytimestamp = '',
        )
        """

    def testOrderSearchResponseServiceResponseOrdersearchresponseOrdersInner(self):
        """Test OrderSearchResponseServiceResponseOrdersearchresponseOrdersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
