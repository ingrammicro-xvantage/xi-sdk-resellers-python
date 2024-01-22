# coding: utf-8

"""
    Reseller API

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi.sdk.resellers.models.order_create_response import OrderCreateResponse

class TestOrderCreateResponse(unittest.TestCase):
    """OrderCreateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateResponse:
        """Test OrderCreateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateResponse`
        """
        model = OrderCreateResponse()
        if include_optional:
            return OrderCreateResponse(
                serviceresponse = xi.sdk.resellers.models.order_create_response_serviceresponse.orderCreateResponse_serviceresponse(
                    responsepreamble = xi.sdk.resellers.models.invoice_detail_response_serviceresponse_responsepreamble.InvoiceDetailResponse_serviceresponse_responsepreamble(
                        responsestatus = '', 
                        statuscode = '', 
                        responsemessage = '', ), 
                    ordersummary = xi.sdk.resellers.models.order_create_response_serviceresponse_ordersummary.orderCreateResponse_serviceresponse_ordersummary(
                        customerponumber = '', 
                        totalorderamount = '', 
                        totalordercreated = '', 
                        shiptoaddress = xi.sdk.resellers.models.order_create_response_serviceresponse_ordersummary_shiptoaddress.orderCreateResponse_serviceresponse_ordersummary_shiptoaddress(
                            attention = '', 
                            name = '', 
                            addressline1 = '', 
                            addressline2 = '', 
                            addressline3 = '', 
                            city = '', 
                            state = '', 
                            postalcode = '', 
                            countrycode = '', ), ), 
                    ordercreateresponse = [
                        xi.sdk.resellers.models.order_create_response_serviceresponse_ordercreateresponse_inner.orderCreateResponse_serviceresponse_ordercreateresponse_inner(
                            numberoflineswithsuccess = '', 
                            numberoflineswitherror = '', 
                            numberoflineswithwarning = '', 
                            globalorderid = '', 
                            ordertype = 'S', 
                            ordertimestamp = '', 
                            invoicingsystemorderid = '', 
                            taxamount = 1.337, 
                            freightamount = 1.337, 
                            orderamount = 1.337, 
                            lines = [
                                xi.sdk.resellers.models.order_create_response_serviceresponse_ordercreateresponse_inner_lines_inner.orderCreateResponse_serviceresponse_ordercreateresponse_inner_Lines_inner(
                                    linetype = '', 
                                    globallinenumber = '', 
                                    partnumber = '', 
                                    globalskuid = '', 
                                    linenumber = '', 
                                    carriercode = '', 
                                    carrierdescription = '', 
                                    requestedunitprice = 1.337, 
                                    requestedquantity = 56, 
                                    confirmedquantity = 56, 
                                    backorderedquantity = 56, 
                                    unitproductprice = 1.337, 
                                    netamount = 1.337, 
                                    warehouseid = '', 
                                    ordersuffix = '', )
                                ], )
                        ], )
            )
        else:
            return OrderCreateResponse(
        )
        """

    def testOrderCreateResponse(self):
        """Test OrderCreateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
