# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.price_and_availability_response_inner_availability import PriceAndAvailabilityResponseInnerAvailability

class TestPriceAndAvailabilityResponseInnerAvailability(unittest.TestCase):
    """PriceAndAvailabilityResponseInnerAvailability unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityResponseInnerAvailability:
        """Test PriceAndAvailabilityResponseInnerAvailability
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityResponseInnerAvailability`
        """
        model = PriceAndAvailabilityResponseInnerAvailability()
        if include_optional:
            return PriceAndAvailabilityResponseInnerAvailability(
                available = True,
                total_availability = 56,
                availability_by_warehouse = [
                    xi.sdk.resellers.models.price_and_availability_response_inner_availability_availability_by_warehouse_inner.PriceAndAvailabilityResponse_inner_availability_availabilityByWarehouse_inner(
                        location = '', 
                        warehouse_id = '', 
                        quantity_available = 56, 
                        quantity_backordered = 56, 
                        quantity_backordered_eta = '', 
                        back_order_info = [
                            xi.sdk.resellers.models.price_and_availability_response_inner_availability_availability_by_warehouse_inner_back_order_info_inner.PriceAndAvailabilityResponse_inner_availability_availabilityByWarehouse_inner_backOrderInfo_inner(
                                quantity = 56, 
                                eta_date = '', )
                            ], )
                    ]
            )
        else:
            return PriceAndAvailabilityResponseInnerAvailability(
        )
        """

    def testPriceAndAvailabilityResponseInnerAvailability(self):
        """Test PriceAndAvailabilityResponseInnerAvailability"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
