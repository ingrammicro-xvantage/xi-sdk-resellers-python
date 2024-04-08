# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of APIs and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.returns_search_response import ReturnsSearchResponse

class TestReturnsSearchResponse(unittest.TestCase):
    """ReturnsSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReturnsSearchResponse:
        """Test ReturnsSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReturnsSearchResponse`
        """
        model = ReturnsSearchResponse()
        if include_optional:
            return ReturnsSearchResponse(
                records_found = 56,
                page_size = 56,
                page_number = 56,
                returns_claims = [
                    xi.sdk.resellers.models.returns_search_response_returns_claims_inner.returnsSearchResponse_returnsClaims_inner(
                        return_claim_id = '', 
                        case_request_number = '', 
                        created_on = '', 
                        type = '', 
                        return_reason = '', 
                        reference_number = '', 
                        estimated_total_value = 1.337, 
                        credit = 1.337, 
                        modified_on = '', 
                        status = '', 
                        links = [
                            xi.sdk.resellers.models.returns_search_response_returns_claims_inner_links_inner.returnsSearchResponse_returnsClaims_inner_links_inner(
                                topic = '', 
                                href = '', 
                                type = '', )
                            ], )
                    ],
                next_page = '',
                previous_page = ''
            )
        else:
            return ReturnsSearchResponse(
        )
        """

    def testReturnsSearchResponse(self):
        """Test ReturnsSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
