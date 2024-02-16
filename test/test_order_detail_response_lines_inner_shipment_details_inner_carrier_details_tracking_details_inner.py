# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner import OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner

class TestOrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner(unittest.TestCase):
    """OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner:
        """Test OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner`
        """
        model = OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner()
        if include_optional:
            return OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner(
                tracking_number = '',
                tracking_url = '',
                package_weight = '',
                carton_number = '',
                quantity_in_box = '',
                serial_numbers = [
                    xi.sdk.resellers.models.order_detail_response_lines_inner_shipment_details_inner_carrier_details_tracking_details_inner_serial_numbers_inner.OrderDetailResponse_lines_inner_shipmentDetails_inner_carrierDetails_trackingDetails_inner_SerialNumbers_inner(
                        serial_number = '', )
                    ]
            )
        else:
            return OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner(
        )
        """

    def testOrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner(self):
        """Test OrderDetailResponseLinesInnerShipmentDetailsInnerCarrierDetailsTrackingDetailsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
