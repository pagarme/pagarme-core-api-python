# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.api_helper import APIHelper

class CreateCheckoutBoletoPaymentRequest(object):

    """Implementation of the 'CreateCheckoutBoletoPaymentRequest' model.

    TODO: type model description here.

    Attributes:
        bank (string): Bank identifier
        instructions (string): Instructions
        due_at (datetime): Due date

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bank":'bank',
        "instructions":'instructions',
        "due_at":'due_at'
    }

    def __init__(self,
                 bank=None,
                 instructions=None,
                 due_at=None):
        """Constructor for the CreateCheckoutBoletoPaymentRequest class"""

        # Initialize members of the class
        self.bank = bank
        self.instructions = instructions
        self.due_at = APIHelper.RFC3339DateTime(due_at) if due_at else None


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
        bank = dictionary.get('bank')
        instructions = dictionary.get('instructions')
        due_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("due_at")).datetime if dictionary.get("due_at") else None

        # Return an object of this model
        return cls(bank,
                   instructions,
                   due_at)


