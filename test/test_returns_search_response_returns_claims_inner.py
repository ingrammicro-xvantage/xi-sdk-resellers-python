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

from xi-sdk-resellers-python.models.returns_search_response_returns_claims_inner import ReturnsSearchResponseReturnsClaimsInner

class TestReturnsSearchResponseReturnsClaimsInner(unittest.TestCase):
    """ReturnsSearchResponseReturnsClaimsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReturnsSearchResponseReturnsClaimsInner:
        """Test ReturnsSearchResponseReturnsClaimsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReturnsSearchResponseReturnsClaimsInner`
        """
        model = ReturnsSearchResponseReturnsClaimsInner()
        if include_optional:
            return ReturnsSearchResponseReturnsClaimsInner(
                return_claim_id = '',
                case_request_number = '',
                created_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                type = '',
                return_reason = '',
                reference_number = '',
                estimated_total_value = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                credit = 1.337,
                modified_on = '',
                status = '',
                links = [
                    xi-sdk-resellers-python.models.returns_search_response_returns_claims_inner_links_inner.returnsSearchResponse_returnsClaims_inner_links_inner(
                        topic = '', 
                        href = '', 
                        type = '', )
                    ]
            )
        else:
            return ReturnsSearchResponseReturnsClaimsInner(
        )
        """

    def testReturnsSearchResponseReturnsClaimsInner(self):
        """Test ReturnsSearchResponseReturnsClaimsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
