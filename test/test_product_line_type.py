# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.product_line_type import ProductLineType

class TestProductLineType(unittest.TestCase):
    """ProductLineType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductLineType:
        """Test ProductLineType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductLineType`
        """
        model = ProductLineType()
        if include_optional:
            return ProductLineType(
                linenumber = '',
                linetype = '',
                partnumber = '',
                vendorpartnumber = '',
                partdescription = '',
                shipfrombranch = '',
                shippedquantity = '',
                orderedquantity = '',
                marginpercent = '',
                backorderquantity = '',
                backorderetadate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                extendedprice = '',
                specialbidnumber = '',
                ordersuffix = '',
                isacopapplied = '',
                unitprice = '',
                unitofmeasure = '',
                serialnumberdetails = [
                    xi.sdk.resellers.models.product_line_type_serialnumberdetails_inner.productLineType_serialnumberdetails_inner(
                        serialnumber = '', 
                        deliverynumber = '', )
                    ],
                trackingnumberdetails = [
                    xi.sdk.resellers.models.product_line_type_trackingnumberdetails_inner.productLineType_trackingnumberdetails_inner(
                        trackingnumber = '', )
                    ],
                productextendedspecs = [
                    xi.sdk.resellers.models.invoice_detail_response_serviceresponse_invoicedetailresponse_extendedspecs_inner.InvoiceDetailResponse_serviceresponse_invoicedetailresponse_extendedspecs_inner(
                        attributename = '', 
                        attributevalue = '', )
                    ]
            )
        else:
            return ProductLineType(
        )
        """

    def testProductLineType(self):
        """Test ProductLineType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
