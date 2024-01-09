# coding: utf-8

"""
    Reseller API Documentation - United States

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi-sdk-python.models.renewals_search_request_data_type import RenewalsSearchRequestDataType

class TestRenewalsSearchRequestDataType(unittest.TestCase):
    """RenewalsSearchRequestDataType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenewalsSearchRequestDataType:
        """Test RenewalsSearchRequestDataType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenewalsSearchRequestDataType`
        """
        model = RenewalsSearchRequestDataType()
        if include_optional:
            return RenewalsSearchRequestDataType(
                start_date = xi-sdk-python.models.renewals_search_request_data_type_start_date.renewalsSearchRequest_dataType_startDate(
                    custom_start_date = '', 
                    custom_end_date = '', ),
                end_date = xi-sdk-python.models.renewals_search_request_data_type_end_date.renewalsSearchRequest_dataType_endDate(
                    custom_start_date = '', 
                    custom_end_date = '', ),
                invoice_date = xi-sdk-python.models.renewals_search_request_data_type_invoice_date.renewalsSearchRequest_dataType_invoiceDate(
                    custom_start_date = '', 
                    custom_end_date = '', ),
                expiration_date = xi-sdk-python.models.renewals_search_request_data_type_expiration_date.renewalsSearchRequest_dataType_expirationDate(
                    custom_start_date = '', 
                    custom_end_date = '', )
            )
        else:
            return RenewalsSearchRequestDataType(
        )
        """

    def testRenewalsSearchRequestDataType(self):
        """Test RenewalsSearchRequestDataType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
