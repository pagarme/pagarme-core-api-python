# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.api_helper import APIHelper
from pagarmecoreapi.configuration import Configuration
from pagarmecoreapi.controllers.base_controller import BaseController
from pagarmecoreapi.http.auth.basic_auth import BasicAuth
from pagarmecoreapi.models.get_plan_response import GetPlanResponse
from pagarmecoreapi.models.get_plan_item_response import GetPlanItemResponse
from pagarmecoreapi.models.list_plans_response import ListPlansResponse
from pagarmecoreapi.exceptions.error_exception import ErrorException

class PlansController(BaseController):

    """A Controller to access Endpoints in the pagarmecoreapi API."""


    def get_plan(self,
                 plan_id):
        """Does a GET request to /plans/{plan_id}.

        Gets a plan

        Args:
            plan_id (string): Plan id

        Returns:
            GetPlanResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'plan_id': plan_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetPlanResponse.from_dictionary)

    def update_plan(self,
                    plan_id,
                    body,
                    idempotency_key=None):
        """Does a PUT request to /plans/{plan_id}.

        Updates a plan

        Args:
            plan_id (string): Plan id
            body (UpdatePlanRequest): Request for updating a plan
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetPlanResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'plan_id': plan_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetPlanResponse.from_dictionary)

    def delete_plan(self,
                    plan_id,
                    idempotency_key=None):
        """Does a DELETE request to /plans/{plan_id}.

        Deletes a plan

        Args:
            plan_id (string): Plan id
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetPlanResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'plan_id': plan_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetPlanResponse.from_dictionary)

    def update_plan_metadata(self,
                             plan_id,
                             body,
                             idempotency_key=None):
        """Does a PATCH request to /Plans/{plan_id}/metadata.

        Updates the metadata from a plan

        Args:
            plan_id (string): The plan id
            body (UpdateMetadataRequest): Request for updating the plan
                metadata
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetPlanResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/Plans/{plan_id}/metadata'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'plan_id': plan_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.patch(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetPlanResponse.from_dictionary)

    def update_plan_item(self,
                         plan_id,
                         plan_item_id,
                         body,
                         idempotency_key=None):
        """Does a PUT request to /plans/{plan_id}/items/{plan_item_id}.

        Updates a plan item

        Args:
            plan_id (string): Plan id
            plan_item_id (string): Plan item id
            body (UpdatePlanItemRequest): Request for updating the plan item
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetPlanItemResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}/items/{plan_item_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'plan_id': plan_id,
            'plan_item_id': plan_item_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetPlanItemResponse.from_dictionary)

    def get_plan_item(self,
                      plan_id,
                      plan_item_id):
        """Does a GET request to /plans/{plan_id}/items/{plan_item_id}.

        Gets a plan item

        Args:
            plan_id (string): Plan id
            plan_item_id (string): Plan item id

        Returns:
            GetPlanItemResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}/items/{plan_item_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'plan_id': plan_id,
            'plan_item_id': plan_item_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetPlanItemResponse.from_dictionary)

    def delete_plan_item(self,
                         plan_id,
                         plan_item_id,
                         idempotency_key=None):
        """Does a DELETE request to /plans/{plan_id}/items/{plan_item_id}.

        Removes an item from a plan

        Args:
            plan_id (string): Plan id
            plan_item_id (string): Plan item id
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetPlanItemResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}/items/{plan_item_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'plan_id': plan_id,
            'plan_item_id': plan_item_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetPlanItemResponse.from_dictionary)

    def create_plan_item(self,
                         plan_id,
                         body,
                         idempotency_key=None):
        """Does a POST request to /plans/{plan_id}/items.

        Adds a new item to a plan

        Args:
            plan_id (string): Plan id
            body (CreatePlanItemRequest): Request for creating a plan item
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetPlanItemResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans/{plan_id}/items'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, { 
            'plan_id': plan_id
        })
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetPlanItemResponse.from_dictionary)

    def create_plan(self,
                    body,
                    idempotency_key=None):
        """Does a POST request to /plans.

        Creates a new plan

        Args:
            body (CreatePlanRequest): Request for creating a plan
            idempotency_key (string, optional): TODO: type description here.
                Example: 

        Returns:
            GetPlanResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'idempotency-key': idempotency_key
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, GetPlanResponse.from_dictionary)

    def get_plans(self,
                  page=None,
                  size=None,
                  name=None,
                  status=None,
                  billing_type=None,
                  created_since=None,
                  created_until=None):
        """Does a GET request to /plans.

        Gets all plans

        Args:
            page (int, optional): Page number
            size (int, optional): Page size
            name (string, optional): Filter for Plan's name
            status (string, optional): Filter for Plan's status
            billing_type (string, optional): Filter for plan's billing type
            created_since (datetime, optional): Filter for plan's creation
                date start range
            created_until (datetime, optional): Filter for plan's creation
                date end range

        Returns:
            ListPlansResponse: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/plans'
        _query_builder = Configuration.base_uri
        _query_builder += _url_path
        _query_parameters = {
            'page': page,
            'size': size,
            'name': name,
            'status': status,
            'billing_type': billing_type,
            'created_since': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_since),
            'created_until': APIHelper.when_defined(APIHelper.RFC3339DateTime, created_until)
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise ErrorException('Invalid request', _context)
        elif _context.response.status_code == 401:
            raise ErrorException('Invalid API key', _context)
        elif _context.response.status_code == 404:
            raise ErrorException('An informed resource was not found', _context)
        elif _context.response.status_code == 412:
            raise ErrorException('Business validation error', _context)
        elif _context.response.status_code == 422:
            raise ErrorException('Contract validation error', _context)
        elif _context.response.status_code == 500:
            raise ErrorException('Internal server error', _context)
        self.validate_response(_context)

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, ListPlansResponse.from_dictionary)
