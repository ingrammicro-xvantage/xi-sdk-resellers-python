# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_license_info import OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo

class TestOrderDetailB2BLinesInnerServiceContractInfoLicenseInfo(unittest.TestCase):
    """OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo:
        """Test OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo`
        """
        model = OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo()
        if include_optional:
            return OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo(
                license_number = [
                    ''
                    ],
                license_start_date = '',
                license_end_date = '',
                description = '',
                quantity = ''
            )
        else:
            return OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo(
        )
        """

    def testOrderDetailB2BLinesInnerServiceContractInfoLicenseInfo(self):
        """Test OrderDetailB2BLinesInnerServiceContractInfoLicenseInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
