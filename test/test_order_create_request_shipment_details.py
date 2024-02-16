# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_request_shipment_details import OrderCreateRequestShipmentDetails

class TestOrderCreateRequestShipmentDetails(unittest.TestCase):
    """OrderCreateRequestShipmentDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateRequestShipmentDetails:
        """Test OrderCreateRequestShipmentDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateRequestShipmentDetails`
        """
        model = OrderCreateRequestShipmentDetails()
        if include_optional:
            return OrderCreateRequestShipmentDetails(
                carrier_code = '',
                freight_account_number = '',
                ship_complete = '',
                requested_delivery_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                signature_required = True,
                shipping_instructions = ''
            )
        else:
            return OrderCreateRequestShipmentDetails(
        )
        """

    def testOrderCreateRequestShipmentDetails(self):
        """Test OrderCreateRequestShipmentDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
