# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.api_helper import APIHelper
import pagarmecoreapi.models.get_subscription_response
import pagarmecoreapi.models.get_subscription_item_response

class GetIncrementResponse(object):

    """Implementation of the 'GetIncrementResponse' model.

    Response object for getting a increment

    Attributes:
        id (string): TODO: type description here.
        value (float): TODO: type description here.
        increment_type (string): TODO: type description here.
        status (string): TODO: type description here.
        created_at (datetime): TODO: type description here.
        cycles (int): TODO: type description here.
        deleted_at (datetime): TODO: type description here.
        description (string): TODO: type description here.
        subscription (GetSubscriptionResponse): TODO: type description here.
        subscription_item (GetSubscriptionItemResponse): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id":'id',
        "value":'value',
        "increment_type":'increment_type',
        "status":'status',
        "created_at":'created_at',
        "cycles":'cycles',
        "deleted_at":'deleted_at',
        "description":'description',
        "subscription":'subscription',
        "subscription_item":'subscription_item'
    }

    def __init__(self,
                 id=None,
                 value=None,
                 increment_type=None,
                 status=None,
                 created_at=None,
                 cycles=None,
                 deleted_at=None,
                 description=None,
                 subscription=None,
                 subscription_item=None):
        """Constructor for the GetIncrementResponse class"""

        # Initialize members of the class
        self.id = id
        self.value = value
        self.increment_type = increment_type
        self.status = status
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.cycles = cycles
        self.deleted_at = APIHelper.RFC3339DateTime(deleted_at) if deleted_at else None
        self.description = description
        self.subscription = subscription
        self.subscription_item = subscription_item


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
        id = dictionary.get('id')
        value = dictionary.get('value')
        increment_type = dictionary.get('increment_type')
        status = dictionary.get('status')
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else None
        cycles = dictionary.get('cycles')
        deleted_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("deleted_at")).datetime if dictionary.get("deleted_at") else None
        description = dictionary.get('description')
        subscription = pagarmecoreapi.models.get_subscription_response.GetSubscriptionResponse.from_dictionary(dictionary.get('subscription')) if dictionary.get('subscription') else None
        subscription_item = pagarmecoreapi.models.get_subscription_item_response.GetSubscriptionItemResponse.from_dictionary(dictionary.get('subscription_item')) if dictionary.get('subscription_item') else None

        # Return an object of this model
        return cls(id,
                   value,
                   increment_type,
                   status,
                   created_at,
                   cycles,
                   deleted_at,
                   description,
                   subscription,
                   subscription_item)


