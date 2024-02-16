# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.returns_create_response_returns_claims_inner import ReturnsCreateResponseReturnsClaimsInner

class TestReturnsCreateResponseReturnsClaimsInner(unittest.TestCase):
    """ReturnsCreateResponseReturnsClaimsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReturnsCreateResponseReturnsClaimsInner:
        """Test ReturnsCreateResponseReturnsClaimsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReturnsCreateResponseReturnsClaimsInner`
        """
        model = ReturnsCreateResponseReturnsClaimsInner()
        if include_optional:
            return ReturnsCreateResponseReturnsClaimsInner(
                rma_claim_id = '',
                case_request_number = '',
                reference_number = '',
                created_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                type = '',
                return_reason = '',
                ingram_part_number = '',
                vendor_part_number = '',
                quantity = 56,
                notes = '',
                estimated_total_value = 1.337,
                credit = 1.337,
                status = '',
                links = [
                    xi.sdk.resellers.models.returns_search_response_returns_claims_inner_links_inner.returnsSearchResponse_returnsClaims_inner_links_inner(
                        topic = '', 
                        href = '', 
                        type = '', )
                    ]
            )
        else:
            return ReturnsCreateResponseReturnsClaimsInner(
        )
        """

    def testReturnsCreateResponseReturnsClaimsInner(self):
        """Test ReturnsCreateResponseReturnsClaimsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
