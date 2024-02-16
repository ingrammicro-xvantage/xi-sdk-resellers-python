# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.freight_response_freight_estimate_response_distribution_inner_carrier_list_inner import FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner

class TestFreightResponseFreightEstimateResponseDistributionInnerCarrierListInner(unittest.TestCase):
    """FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner:
        """Test FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner`
        """
        model = FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner()
        if include_optional:
            return FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner(
                carrier_code = '',
                ship_via = '',
                carrier_mode = '',
                estimated_freight_charge = 1.337,
                days_in_transit = 56
            )
        else:
            return FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner(
        )
        """

    def testFreightResponseFreightEstimateResponseDistributionInnerCarrierListInner(self):
        """Test FreightResponseFreightEstimateResponseDistributionInnerCarrierListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
