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

from xi.sdk.resellers.python.models.order_detail_response_lines_inner_shipment_details_inner import OrderDetailResponseLinesInnerShipmentDetailsInner

class TestOrderDetailResponseLinesInnerShipmentDetailsInner(unittest.TestCase):
    """OrderDetailResponseLinesInnerShipmentDetailsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailResponseLinesInnerShipmentDetailsInner:
        """Test OrderDetailResponseLinesInnerShipmentDetailsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailResponseLinesInnerShipmentDetailsInner`
        """
        model = OrderDetailResponseLinesInnerShipmentDetailsInner()
        if include_optional:
            return OrderDetailResponseLinesInnerShipmentDetailsInner(
                quantity = 56,
                estimated_ship_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                shipped_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                estimated_delivery_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                delivered_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                ship_from_warehouse_id = '',
                ship_from_location = '',
                invoice_number = '',
                invoice_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                carrier_details = xi.sdk.resellers.python.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details.OrderDetailResponse_lines_inner_shipmentDetails_inner_carrierDetails(
                    carrier_code = '', 
                    carrier_name = '', 
                    tracking_details = [
                        xi.sdk.resellers.python.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner.OrderDetailResponse_lines_inner_shipmentDetails_inner_carrierDetails_trackingDetails_inner(
                            tracking_number = '', 
                            tracking_url = '', 
                            package_weight = '', 
                            carton_number = '', 
                            quantity_in_box = '', 
                            serial_numbers = [
                                xi.sdk.resellers.python.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner_serial_numbers_inner.OrderDetailResponse_lines_inner_shipmentDetails_inner_carrierDetails_trackingDetails_inner_SerialNumbers_inner(
                                    serial_number = '', )
                                ], )
                        ], )
            )
        else:
            return OrderDetailResponseLinesInnerShipmentDetailsInner(
        )
        """

    def testOrderDetailResponseLinesInnerShipmentDetailsInner(self):
        """Test OrderDetailResponseLinesInnerShipmentDetailsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
