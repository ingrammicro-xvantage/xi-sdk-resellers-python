# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_modify_request_servicerequest_ordermodifyrequest import OrderModifyRequestServicerequestOrdermodifyrequest

class TestOrderModifyRequestServicerequestOrdermodifyrequest(unittest.TestCase):
    """OrderModifyRequestServicerequestOrdermodifyrequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderModifyRequestServicerequestOrdermodifyrequest:
        """Test OrderModifyRequestServicerequestOrdermodifyrequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderModifyRequestServicerequestOrdermodifyrequest`
        """
        model = OrderModifyRequestServicerequestOrdermodifyrequest()
        if include_optional:
            return OrderModifyRequestServicerequestOrdermodifyrequest(
                ingramorderbranch = '',
                ingramordernumber = '',
                ingramorderdist = '',
                ingramordership = '',
                customerponumber = '',
                shipto = xi.sdk.resellers.models.order_modify_request_servicerequest_ordermodifyrequest_shipto.orderModifyRequest_servicerequest_ordermodifyrequest_shipto(
                    id = '', 
                    name = '', 
                    addressline = '', 
                    city = '', 
                    state = '', 
                    postalcode = '', 
                    countrycode = '', ),
                headerdata = xi.sdk.resellers.models.order_modify_request_servicerequest_ordermodifyrequest_headerdata.orderModifyRequest_servicerequest_ordermodifyrequest_headerdata(
                    actioncode = '', 
                    shipviacode = '', ),
                linedata = [
                    xi.sdk.resellers.models.order_modify_request_servicerequest_ordermodifyrequest_linedata_inner.orderModifyRequest_servicerequest_ordermodifyrequest_linedata_inner(
                        addlineorupdateline = '', 
                        linenumber = '', 
                        customerlinenumber = '', 
                        ingrampartnumber = '', 
                        quantityordered = 56, 
                        customerpartnumber = '', 
                        linetype = '', )
                    ]
            )
        else:
            return OrderModifyRequestServicerequestOrdermodifyrequest(
        )
        """

    def testOrderModifyRequestServicerequestOrdermodifyrequest(self):
        """Test OrderModifyRequestServicerequestOrdermodifyrequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
