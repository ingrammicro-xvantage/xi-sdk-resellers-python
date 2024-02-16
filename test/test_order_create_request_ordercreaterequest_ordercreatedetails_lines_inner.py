# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_request_ordercreaterequest_ordercreatedetails_lines_inner import OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner

class TestOrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner(unittest.TestCase):
    """OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner:
        """Test OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner`
        """
        model = OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner()
        if include_optional:
            return OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner(
                linetype = 'P',
                linenumber = '',
                ingrampartnumber = '',
                quantity = '',
                vendorpartnumber = '',
                customerpartnumber = '',
                upc_code = '',
                warehouseid = '',
                unitprice = '',
                enduser = xi.sdk.resellers.models.order_create_request_ordercreaterequest_ordercreatedetails_lines_inner_enduser.orderCreateRequest_ordercreaterequest_ordercreatedetails_lines_inner_enduser(
                    id = '', 
                    addressline1 = '', 
                    addressline2 = '', 
                    addressline3 = '', 
                    city = '', 
                    state = '', 
                    postalcode = '', 
                    countrycode = '', 
                    phonenumber = '', 
                    extensionnumber = '', 
                    faxnumber = '', 
                    email = '', ),
                productextendedspecs = [
                    xi.sdk.resellers.models.order_create_request_ordercreaterequest_ordercreatedetails_lines_inner_productextendedspecs_inner.orderCreateRequest_ordercreaterequest_ordercreatedetails_lines_inner_productextendedspecs_inner(
                        attributename = 'shipfrom', 
                        attributevalue = '', )
                    ]
            )
        else:
            return OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner(
                quantity = '',
        )
        """

    def testOrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner(self):
        """Test OrderCreateRequestOrdercreaterequestOrdercreatedetailsLinesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
