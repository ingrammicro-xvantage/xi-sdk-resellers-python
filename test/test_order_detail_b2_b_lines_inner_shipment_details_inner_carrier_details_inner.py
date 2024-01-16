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

from xi.sdk.resellers.python.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner import OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner

class TestOrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner(unittest.TestCase):
    """OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner:
        """Test OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner`
        """
        model = OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner()
        if include_optional:
            return OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner(
                carrier_code = '',
                carrier_name = '',
                quantity = 56,
                shipped_date = '',
                estimated_delivery_date = '',
                delivered_date = '',
                carrier_pickup_date = '',
                tracking_details = [
                    xi.sdk.resellers.python.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner.OrderDetailB2B_lines_inner_shipmentDetails_inner_carrierDetails_inner_trackingDetails_inner(
                        tracking_number = '', 
                        tracking_url = '', 
                        package_weight = '', 
                        carton_number = '', 
                        quantity_in_box = '', 
                        serial_numbers = [
                            xi.sdk.resellers.python.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner_serial_numbers_inner.OrderDetailB2B_lines_inner_shipmentDetails_inner_carrierDetails_inner_trackingDetails_inner_serialNumbers_inner(
                                serial_number = '', )
                            ], )
                    ]
            )
        else:
            return OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner(
        )
        """

    def testOrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner(self):
        """Test OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
