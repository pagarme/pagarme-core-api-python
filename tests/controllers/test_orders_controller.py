# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from pagarmecoreapi.api_helper import APIHelper


class OrdersControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(OrdersControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.orders

    # Gets all orders
    def test_test_get_orders(self):
        # Parameters for the API call
        page = None
        size = None
        code = None
        status = None
        created_since = None
        created_until = None
        customer_id = None

        # Perform the API call through the SDK function
        result = self.controller.get_orders(page, size, code, status, created_since, created_until, customer_id)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


