# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateWithdrawRequest(object):

    """Implementation of the 'CreateWithdrawRequest' model.

    TODO: type model description here.

    Attributes:
        amount (int): TODO: type description here.
        metadata (dict<object, string>): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount":'amount',
        "metadata":'metadata'
    }

    def __init__(self,
                 amount=None,
                 metadata=None):
        """Constructor for the CreateWithdrawRequest class"""

        # Initialize members of the class
        self.amount = amount
        self.metadata = metadata


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
        amount = dictionary.get('amount')
        metadata = dictionary.get('metadata')

        # Return an object of this model
        return cls(amount,
                   metadata)


