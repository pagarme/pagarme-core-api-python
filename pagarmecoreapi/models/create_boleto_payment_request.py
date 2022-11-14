# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.api_helper import APIHelper
import pagarmecoreapi.models.create_address_request
import pagarmecoreapi.models.create_interest_request
import pagarmecoreapi.models.create_fine_request

class CreateBoletoPaymentRequest(object):

    """Implementation of the 'CreateBoletoPaymentRequest' model.

    Contains the settings for creating a boleto payment

    Attributes:
        retries (int): Number of retries
        bank (string): The bank code, containing three characters. The
            available codes are on the API specification
        instructions (string): The instructions field that will be printed on
            the boleto.
        due_at (datetime): Boleto due date
        billing_address (CreateAddressRequest): Card's billing address
        billing_address_id (string): The address id for the billing address
        nosso_numero (string): Customer identification number with the bank
        document_number (string): Boleto identification
        statement_descriptor (string): Soft Descriptor
        interest (CreateInterestRequest): TODO: type description here.
        fine (CreateFineRequest): TODO: type description here.
        max_days_to_pay_past_due (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "retries":'retries',
        "bank":'bank',
        "instructions":'instructions',
        "billing_address":'billing_address',
        "billing_address_id":'billing_address_id',
        "document_number":'document_number',
        "statement_descriptor":'statement_descriptor',
        "due_at":'due_at',
        "nosso_numero":'nosso_numero',
        "interest":'interest',
        "fine":'fine',
        "max_days_to_pay_past_due":'max_days_to_pay_past_due'
    }

    def __init__(self,
                 retries=None,
                 bank=None,
                 instructions=None,
                 billing_address=None,
                 billing_address_id=None,
                 document_number=None,
                 statement_descriptor=None,
                 due_at=None,
                 nosso_numero=None,
                 interest=None,
                 fine=None,
                 max_days_to_pay_past_due=None):
        """Constructor for the CreateBoletoPaymentRequest class"""

        # Initialize members of the class
        self.retries = retries
        self.bank = bank
        self.instructions = instructions
        self.due_at = APIHelper.RFC3339DateTime(due_at) if due_at else None
        self.billing_address = billing_address
        self.billing_address_id = billing_address_id
        self.nosso_numero = nosso_numero
        self.document_number = document_number
        self.statement_descriptor = statement_descriptor
        self.interest = interest
        self.fine = fine
        self.max_days_to_pay_past_due = max_days_to_pay_past_due


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        retries = dictionary.get('retries')
        bank = dictionary.get('bank')
        instructions = dictionary.get('instructions')
        billing_address = pagarmecoreapi.models.create_address_request.CreateAddressRequest.from_dictionary(dictionary.get('billing_address')) if dictionary.get('billing_address') else None
        billing_address_id = dictionary.get('billing_address_id')
        document_number = dictionary.get('document_number')
        statement_descriptor = dictionary.get('statement_descriptor')
        due_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("due_at")).datetime if dictionary.get("due_at") else None
        nosso_numero = dictionary.get('nosso_numero')
        interest = pagarmecoreapi.models.create_interest_request.CreateInterestRequest.from_dictionary(dictionary.get('interest')) if dictionary.get('interest') else None
        fine = pagarmecoreapi.models.create_fine_request.CreateFineRequest.from_dictionary(dictionary.get('fine')) if dictionary.get('fine') else None
        max_days_to_pay_past_due = dictionary.get('max_days_to_pay_past_due')

        # Return an object of this model
        return cls(retries,
                   bank,
                   instructions,
                   billing_address,
                   billing_address_id,
                   document_number,
                   statement_descriptor,
                   due_at,
                   nosso_numero,
                   interest,
                   fine,
                   max_days_to_pay_past_due)


