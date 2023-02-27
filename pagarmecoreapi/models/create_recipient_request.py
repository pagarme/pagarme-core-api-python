# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.create_bank_account_request
import pagarmecoreapi.models.create_transfer_settings_request

class CreateRecipientRequest(object):

    """Implementation of the 'CreateRecipientRequest' model.

    Request for creating a recipient

    Attributes:
        name (string): Recipient name
        email (string): Recipient email
        description (string): Recipient description
        document (string): Recipient document number
        mtype (string): Recipient type
        default_bank_account (CreateBankAccountRequest): Request for creating
            a bank account
        metadata (dict<object, string>): Metadata
        transfer_settings (CreateTransferSettingsRequest): Informações de
            transferência do recebedor
        code (string): Recipient code
        payment_mode (string): Payment mode

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "email":'email',
        "description":'description',
        "document":'document',
        "mtype":'type',
        "default_bank_account":'default_bank_account',
        "metadata":'metadata',
        "code":'code',
        "payment_mode":'payment_mode',
        "transfer_settings":'transfer_settings'
    }

    def __init__(self,
                 name=None,
                 email=None,
                 description=None,
                 document=None,
                 mtype=None,
                 default_bank_account=None,
                 metadata=None,
                 code=None,
                 payment_mode=None,
                 transfer_settings=None):
        """Constructor for the CreateRecipientRequest class"""

        # Initialize members of the class
        self.name = name
        self.email = email
        self.description = description
        self.document = document
        self.mtype = mtype
        self.default_bank_account = default_bank_account
        self.metadata = metadata
        self.transfer_settings = transfer_settings
        self.code = code
        self.payment_mode = payment_mode


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
        name = dictionary.get('name')
        email = dictionary.get('email')
        description = dictionary.get('description')
        document = dictionary.get('document')
        mtype = dictionary.get('type')
        default_bank_account = pagarmecoreapi.models.create_bank_account_request.CreateBankAccountRequest.from_dictionary(dictionary.get('default_bank_account')) if dictionary.get('default_bank_account') else None
        metadata = dictionary.get('metadata')
        code = dictionary.get('code')
        payment_mode = dictionary.get('payment_mode')
        transfer_settings = pagarmecoreapi.models.create_transfer_settings_request.CreateTransferSettingsRequest.from_dictionary(dictionary.get('transfer_settings')) if dictionary.get('transfer_settings') else None

        # Return an object of this model
        return cls(name,
                   email,
                   description,
                   document,
                   mtype,
                   default_bank_account,
                   metadata,
                   code,
                   payment_mode,
                   transfer_settings)


