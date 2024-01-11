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

from xi-sdk-resellers-python.models.quote_to_order_details_dto import QuoteToOrderDetailsDTO

class TestQuoteToOrderDetailsDTO(unittest.TestCase):
    """QuoteToOrderDetailsDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteToOrderDetailsDTO:
        """Test QuoteToOrderDetailsDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteToOrderDetailsDTO`
        """
        model = QuoteToOrderDetailsDTO()
        if include_optional:
            return QuoteToOrderDetailsDTO(
                quote_number = '',
                customer_order_number = '',
                enduser_order_number = '',
                bill_to_address_id = '',
                end_user_info = [
                    xi-sdk-resellers-python.models.quote_to_order_details_dto_end_user_info_inner.QuoteToOrderDetailsDTO_endUserInfo_inner(
                        company_name = '', 
                        contact = '', 
                        address_line1 = '', 
                        address_line2 = '', 
                        address_line3 = '', 
                        city = '', 
                        state = '', 
                        postal_code = '', 
                        country_code = '', 
                        email = '', 
                        phone_number = '', )
                    ],
                ship_to_info = [
                    xi-sdk-resellers-python.models.quote_to_order_details_dto_ship_to_info_inner.QuoteToOrderDetailsDTO_shipToInfo_inner(
                        address_id = '', 
                        company_name = '', 
                        contact = '', 
                        address_line1 = '', 
                        address_line2 = '', 
                        address_line3 = '', 
                        city = '', 
                        state = '', 
                        postal_code = '', 
                        country_code = '', 
                        email = '', )
                    ],
                additional_attributes = [
                    xi-sdk-resellers-python.models.quote_to_order_details_dto_additional_attributes_inner.QuoteToOrderDetailsDTO_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ],
                vmfadditional_attributes = [
                    xi-sdk-resellers-python.models.quote_to_order_details_dto_vmfadditional_attributes_inner.QuoteToOrderDetailsDTO_vmfadditionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', 
                        attribute_description = '', )
                    ],
                lines = [
                    xi-sdk-resellers-python.models.quote_to_order_details_dto_lines_inner.QuoteToOrderDetailsDTO_lines_inner(
                        customer_line_number = '', 
                        ingram_part_number = '', 
                        quantity = '', 
                        vmf_additional_attributes_lines = [
                            xi-sdk-resellers-python.models.validate_quote_response_lines_inner_vmf_additional_attributes_lines_inner.ValidateQuoteResponse_lines_inner_vmfAdditionalAttributesLines_inner(
                                attribute_name = '', 
                                attribute_value = '', 
                                attribute_description = '', )
                            ], )
                    ]
            )
        else:
            return QuoteToOrderDetailsDTO(
        )
        """

    def testQuoteToOrderDetailsDTO(self):
        """Test QuoteToOrderDetailsDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
