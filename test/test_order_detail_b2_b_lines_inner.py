# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b_lines_inner import OrderDetailB2BLinesInner

class TestOrderDetailB2BLinesInner(unittest.TestCase):
    """OrderDetailB2BLinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInner:
        """Test OrderDetailB2BLinesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInner`
        """
        model = OrderDetailB2BLinesInner()
        if include_optional:
            return OrderDetailB2BLinesInner(
                sub_order_number = '',
                ingram_order_line_number = '',
                vendor_sales_order_line_number = '',
                customer_line_number = '',
                line_status = '',
                ingram_part_number = '',
                vendor_part_number = '',
                vendor_name = '',
                part_description = '',
                unit_weight = 1.337,
                weight_uom = '',
                unit_price = 1.337,
                upc_code = '',
                extended_price = 1.337,
                tax_amount = 1.337,
                currency_code = '',
                quantity_ordered = 56,
                quantity_confirmed = 56,
                quantity_back_ordered = 56,
                special_bid_number = '',
                requested_deliverydate = '',
                promised_delivery_date = '',
                back_order_eta_date = '',
                line_notes = '',
                shipment_details = [
                    xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner.OrderDetailB2B_lines_inner_shipmentDetails_inner(
                        quantity = 56, 
                        delivery_number = '', 
                        estimated_ship_date = '', 
                        shipped_date = '', 
                        estimated_delivery_date = '', 
                        ship_from_warehouse_id = '', 
                        ship_from_location = '', 
                        invoice_number = '', 
                        invoice_date = '', 
                        carrier_details = [
                            xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner.OrderDetailB2B_lines_inner_shipmentDetails_inner_carrierDetails_inner(
                                carrier_code = '', 
                                carrier_name = '', 
                                quantity = 56, 
                                shipped_date = '', 
                                estimated_delivery_date = '', 
                                delivered_date = '', 
                                carrier_pickup_date = '', 
                                tracking_details = [
                                    xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner.OrderDetailB2B_lines_inner_shipmentDetails_inner_carrierDetails_inner_trackingDetails_inner(
                                        tracking_number = '', 
                                        tracking_url = '', 
                                        package_weight = '', 
                                        carton_number = '', 
                                        quantity_in_box = '', 
                                        serial_numbers = [
                                            xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner_serial_numbers_inner.OrderDetailB2B_lines_inner_shipmentDetails_inner_carrierDetails_inner_trackingDetails_inner_serialNumbers_inner(
                                                serial_number = '', )
                                            ], )
                                    ], )
                            ], )
                    ],
                service_contract_info = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info.OrderDetailB2B_lines_inner_serviceContractInfo(
                    contract_info = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_contract_info.OrderDetailB2B_lines_inner_serviceContractInfo_contractInfo(
                        contract_description = '', 
                        contract_number = '', 
                        contract_status = '', 
                        contract_start_date = '', 
                        contract_end_date = '', 
                        contract_duration = '', ), 
                    subscriptions = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_subscriptions.OrderDetailB2B_lines_inner_serviceContractInfo_subscriptions(
                        subscription_id = '', 
                        subscription_term = '', 
                        renewal_term = '', 
                        billing_model = '', 
                        subcription_start_date = '', 
                        subcription_end_date = '', ), 
                    license_info = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_license_info.OrderDetailB2B_lines_inner_serviceContractInfo_licenseInfo(
                        license_number = [
                            ''
                            ], 
                        license_start_date = '', 
                        license_end_date = '', 
                        description = '', 
                        quantity = '', ), ),
                additional_attributes = [
                    xi.sdk.resellers.models.order_detail_b2_b_lines_inner_additional_attributes_inner.OrderDetailB2B_lines_inner_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ],
                links = [
                    xi.sdk.resellers.models.order_detail_b2_b_lines_inner_links_inner.OrderDetailB2B_lines_inner_links_inner(
                        topic = '', 
                        href = '', 
                        type = '', )
                    ],
                estimated_dates = [
                    xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner.OrderDetailB2B_lines_inner_estimatedDates_inner(
                        ship = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship.OrderDetailB2B_lines_inner_estimatedDates_inner_ship(
                            ship_date_type = '', 
                            ship_date_range = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship_ship_date_range.OrderDetailB2B_lines_inner_estimatedDates_inner_ship_shipDateRange(
                                start_date = '', 
                                end_date = '', ), 
                            ship_source = '', 
                            ship_description = '', 
                            ship_date = '', ), 
                        delivery = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_delivery.OrderDetailB2B_lines_inner_estimatedDates_inner_delivery(
                            delivery_date_type = '', 
                            delivery_date_range = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_delivery_delivery_date_range.OrderDetailB2B_lines_inner_estimatedDates_inner_delivery_deliveryDateRange(
                                start_date = '', 
                                end_date = '', ), 
                            delivery_source = '', 
                            delivery_description = '', 
                            delivery_date = '', ), )
                    ],
                schedule_lines = [
                    xi.sdk.resellers.models.order_detail_b2_b_lines_inner_schedule_lines_inner.OrderDetailB2B_lines_inner_scheduleLines_inner(
                        line_number = '', 
                        schedule_line_date = '', 
                        requested_quantity = '', 
                        confirmed_quantity = '', 
                        goods_issue_date = '', )
                    ],
                multiple_shipments = [
                    xi.sdk.resellers.models.order_detail_b2_b_lines_inner_multiple_shipments_inner.OrderDetailB2B_lines_inner_multipleShipments_inner(
                        line_number = '', 
                        requested_quantity = 56, 
                        confirmed_quantity = 56, 
                        date_type = '', 
                        date_range = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship_ship_date_range.OrderDetailB2B_lines_inner_estimatedDates_inner_ship_shipDateRange(
                            start_date = '', 
                            end_date = '', ), 
                        source = '', 
                        description = '', 
                        date = '', 
                        delivery_date = '', )
                    ],
                default_carrier_name = 'FEDEX GROUND'
            )
        else:
            return OrderDetailB2BLinesInner(
        )
        """

    def testOrderDetailB2BLinesInner(self):
        """Test OrderDetailB2BLinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
