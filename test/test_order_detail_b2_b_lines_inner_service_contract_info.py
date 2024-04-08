# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info import OrderDetailB2BLinesInnerServiceContractInfo

class TestOrderDetailB2BLinesInnerServiceContractInfo(unittest.TestCase):
    """OrderDetailB2BLinesInnerServiceContractInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInnerServiceContractInfo:
        """Test OrderDetailB2BLinesInnerServiceContractInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInnerServiceContractInfo`
        """
        model = OrderDetailB2BLinesInnerServiceContractInfo()
        if include_optional:
            return OrderDetailB2BLinesInnerServiceContractInfo(
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
                    quantity = '', )
            )
        else:
            return OrderDetailB2BLinesInnerServiceContractInfo(
        )
        """

    def testOrderDetailB2BLinesInnerServiceContractInfo(self):
        """Test OrderDetailB2BLinesInnerServiceContractInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
