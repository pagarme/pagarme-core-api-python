# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.create_apple_pay_request
import pagarmecoreapi.models.create_google_pay_request
import pagarmecoreapi.models.create_emv_decrypt_request

class CreateCardPaymentContactlessRequest(object):

    """Implementation of the 'CreateCardPaymentContactlessRequest' model.

    The card payment contactless request

    Attributes:
        mtype (string): The authentication type
        apple_pay (CreateApplePayRequest): The ApplePay Token Payment Request
        google_pay (CreateGooglePayRequest): The GooglePay Token Payment
            Request
        emv (CreateEmvDecryptRequest): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type',
        "apple_pay":'apple_pay',
        "google_pay":'google_pay',
        "emv":'emv'
    }

    def __init__(self,
                 mtype=None,
                 apple_pay=None,
                 google_pay=None,
                 emv=None):
        """Constructor for the CreateCardPaymentContactlessRequest class"""

        # Initialize members of the class
        self.mtype = mtype
        self.apple_pay = apple_pay
        self.google_pay = google_pay
        self.emv = emv


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
        mtype = dictionary.get('type')
        apple_pay = pagarmecoreapi.models.create_apple_pay_request.CreateApplePayRequest.from_dictionary(dictionary.get('apple_pay')) if dictionary.get('apple_pay') else None
        google_pay = pagarmecoreapi.models.create_google_pay_request.CreateGooglePayRequest.from_dictionary(dictionary.get('google_pay')) if dictionary.get('google_pay') else None
        emv = pagarmecoreapi.models.create_emv_decrypt_request.CreateEmvDecryptRequest.from_dictionary(dictionary.get('emv')) if dictionary.get('emv') else None

        # Return an object of this model
        return cls(mtype,
                   apple_pay,
                   google_pay,
                   emv)


