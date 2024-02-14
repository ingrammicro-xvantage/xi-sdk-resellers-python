# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.freight_response import FreightResponse

class TestFreightResponse(unittest.TestCase):
    """FreightResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FreightResponse:
        """Test FreightResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FreightResponse`
        """
        model = FreightResponse()
        if include_optional:
            return FreightResponse(
                freight_estimate_response = xi.sdk.resellers.models.freight_response_freight_estimate_response.freightResponse_freightEstimateResponse(
                    currency_code = '', 
                    total_freight_amount = 1.337, 
                    total_tax_amount = 1.337, 
                    total_fees = 1.337, 
                    total_net_amount = 1.337, 
                    gross_amount = 1.337, 
                    distribution = [
                        xi.sdk.resellers.models.freight_response_freight_estimate_response_distribution_inner.freightResponse_freightEstimateResponse_distribution_inner(
                            ship_from_branch_number = '', 
                            carrier_code = '', 
                            ship_via = '', 
                            freight_rate = 1.337, 
                            total_weight = 1.337, 
                            transit_days = 56, 
                            carrier_list = [
                                xi.sdk.resellers.models.freight_response_freight_estimate_response_distribution_inner_carrier_list_inner.freightResponse_freightEstimateResponse_distribution_inner_carrierList_inner(
                                    carrier_code = '', 
                                    ship_via = '', 
                                    carrier_mode = '', 
                                    estimated_freight_charge = 1.337, 
                                    days_in_transit = 56, )
                                ], )
                        ], 
                    lines = [
                        xi.sdk.resellers.models.freight_response_freight_estimate_response_lines_inner.freightResponse_freightEstimateResponse_lines_inner(
                            ingram_part_number = '', 
                            vendor_part_number = '', 
                            warehouse_id = '', 
                            quantity = 56, 
                            unit_price = 1.337, 
                            net_amount = 1.337, )
                        ], )
            )
        else:
            return FreightResponse(
        )
        """

    def testFreightResponse(self):
        """Test FreightResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
