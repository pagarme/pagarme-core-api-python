# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.api_helper import APIHelper
import pagarmecoreapi.models.create_customer_request
import pagarmecoreapi.models.create_card_request
import pagarmecoreapi.models.create_pricing_scheme_request
import pagarmecoreapi.models.create_subscription_item_request
import pagarmecoreapi.models.create_shipping_request
import pagarmecoreapi.models.create_discount_request
import pagarmecoreapi.models.create_setup_request
import pagarmecoreapi.models.create_increment_request
import pagarmecoreapi.models.create_period_request
import pagarmecoreapi.models.create_sub_merchant_request
import pagarmecoreapi.models.create_subscription_split_request

class CreateSubscriptionRequest(object):

    """Implementation of the 'CreateSubscriptionRequest' model.

    Request for creating a subcription

    Attributes:
        customer (CreateCustomerRequest): Customer
        card (CreateCardRequest): Card
        code (string): Subscription code
        payment_method (string): Payment method
        billing_type (string): Billing type
        statement_descriptor (string): Statement descriptor for credit card
            subscriptions
        description (string): Subscription description
        currency (string): Currency
        interval (string): Interval
        interval_count (int): Interval count
        pricing_scheme (CreatePricingSchemeRequest): Subscription pricing
            scheme
        items (list of CreateSubscriptionItemRequest): Subscription items
        shipping (CreateShippingRequest): Shipping
        discounts (list of CreateDiscountRequest): Discounts
        metadata (dict<object, string>): Metadata
        setup (CreateSetupRequest): Setup data
        plan_id (string): Plan id
        customer_id (string): Customer id
        card_id (string): Card id
        billing_day (int): Billing day
        installments (int): Number of installments
        start_at (datetime): Subscription start date
        minimum_price (int): Subscription minimum price
        cycles (int): Number of cycles
        card_token (string): Card token
        gateway_affiliation_id (string): Gateway Affiliation code
        quantity (int): Quantity
        boleto_due_days (int): Days until boleto expires
        increments (list of CreateIncrementRequest): Increments
        period (CreatePeriodRequest): TODO: type description here.
        submerchant (CreateSubMerchantRequest): SubMerchant
        split (CreateSubscriptionSplitRequest): Split

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer":'customer',
        "card":'card',
        "code":'code',
        "payment_method":'payment_method',
        "billing_type":'billing_type',
        "statement_descriptor":'statement_descriptor',
        "description":'description',
        "currency":'currency',
        "interval":'interval',
        "interval_count":'interval_count',
        "pricing_scheme":'pricing_scheme',
        "items":'items',
        "shipping":'shipping',
        "discounts":'discounts',
        "metadata":'metadata',
        "setup":'setup',
        "increments":'increments',
        "plan_id":'plan_id',
        "customer_id":'customer_id',
        "card_id":'card_id',
        "billing_day":'billing_day',
        "installments":'installments',
        "start_at":'start_at',
        "minimum_price":'minimum_price',
        "cycles":'cycles',
        "card_token":'card_token',
        "gateway_affiliation_id":'gateway_affiliation_id',
        "quantity":'quantity',
        "boleto_due_days":'boleto_due_days',
        "period":'period',
        "submerchant":'submerchant',
        "split":'split'
    }

    def __init__(self,
                 customer=None,
                 card=None,
                 code=None,
                 payment_method=None,
                 billing_type=None,
                 statement_descriptor=None,
                 description=None,
                 currency=None,
                 interval=None,
                 interval_count=None,
                 pricing_scheme=None,
                 items=None,
                 shipping=None,
                 discounts=None,
                 metadata=None,
                 setup=None,
                 increments=None,
                 plan_id=None,
                 customer_id=None,
                 card_id=None,
                 billing_day=None,
                 installments=None,
                 start_at=None,
                 minimum_price=None,
                 cycles=None,
                 card_token=None,
                 gateway_affiliation_id=None,
                 quantity=None,
                 boleto_due_days=None,
                 period=None,
                 submerchant=None,
                 split=None):
        """Constructor for the CreateSubscriptionRequest class"""

        # Initialize members of the class
        self.customer = customer
        self.card = card
        self.code = code
        self.payment_method = payment_method
        self.billing_type = billing_type
        self.statement_descriptor = statement_descriptor
        self.description = description
        self.currency = currency
        self.interval = interval
        self.interval_count = interval_count
        self.pricing_scheme = pricing_scheme
        self.items = items
        self.shipping = shipping
        self.discounts = discounts
        self.metadata = metadata
        self.setup = setup
        self.plan_id = plan_id
        self.customer_id = customer_id
        self.card_id = card_id
        self.billing_day = billing_day
        self.installments = installments
        self.start_at = APIHelper.RFC3339DateTime(start_at) if start_at else None
        self.minimum_price = minimum_price
        self.cycles = cycles
        self.card_token = card_token
        self.gateway_affiliation_id = gateway_affiliation_id
        self.quantity = quantity
        self.boleto_due_days = boleto_due_days
        self.increments = increments
        self.period = period
        self.submerchant = submerchant
        self.split = split


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
        customer = pagarmecoreapi.models.create_customer_request.CreateCustomerRequest.from_dictionary(dictionary.get('customer')) if dictionary.get('customer') else None
        card = pagarmecoreapi.models.create_card_request.CreateCardRequest.from_dictionary(dictionary.get('card')) if dictionary.get('card') else None
        code = dictionary.get('code')
        payment_method = dictionary.get('payment_method')
        billing_type = dictionary.get('billing_type')
        statement_descriptor = dictionary.get('statement_descriptor')
        description = dictionary.get('description')
        currency = dictionary.get('currency')
        interval = dictionary.get('interval')
        interval_count = dictionary.get('interval_count')
        pricing_scheme = pagarmecoreapi.models.create_pricing_scheme_request.CreatePricingSchemeRequest.from_dictionary(dictionary.get('pricing_scheme')) if dictionary.get('pricing_scheme') else None
        items = None
        if dictionary.get('items') != None:
            items = list()
            for structure in dictionary.get('items'):
                items.append(pagarmecoreapi.models.create_subscription_item_request.CreateSubscriptionItemRequest.from_dictionary(structure))
        shipping = pagarmecoreapi.models.create_shipping_request.CreateShippingRequest.from_dictionary(dictionary.get('shipping')) if dictionary.get('shipping') else None
        discounts = None
        if dictionary.get('discounts') != None:
            discounts = list()
            for structure in dictionary.get('discounts'):
                discounts.append(pagarmecoreapi.models.create_discount_request.CreateDiscountRequest.from_dictionary(structure))
        metadata = dictionary.get('metadata')
        setup = pagarmecoreapi.models.create_setup_request.CreateSetupRequest.from_dictionary(dictionary.get('setup')) if dictionary.get('setup') else None
        increments = None
        if dictionary.get('increments') != None:
            increments = list()
            for structure in dictionary.get('increments'):
                increments.append(pagarmecoreapi.models.create_increment_request.CreateIncrementRequest.from_dictionary(structure))
        plan_id = dictionary.get('plan_id')
        customer_id = dictionary.get('customer_id')
        card_id = dictionary.get('card_id')
        billing_day = dictionary.get('billing_day')
        installments = dictionary.get('installments')
        start_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_at")).datetime if dictionary.get("start_at") else None
        minimum_price = dictionary.get('minimum_price')
        cycles = dictionary.get('cycles')
        card_token = dictionary.get('card_token')
        gateway_affiliation_id = dictionary.get('gateway_affiliation_id')
        quantity = dictionary.get('quantity')
        boleto_due_days = dictionary.get('boleto_due_days')
        period = pagarmecoreapi.models.create_period_request.CreatePeriodRequest.from_dictionary(dictionary.get('period')) if dictionary.get('period') else None
        submerchant = pagarmecoreapi.models.create_sub_merchant_request.CreateSubMerchantRequest.from_dictionary(dictionary.get('submerchant')) if dictionary.get('submerchant') else None
        split = pagarmecoreapi.models.create_subscription_split_request.CreateSubscriptionSplitRequest.from_dictionary(dictionary.get('split')) if dictionary.get('split') else None

        # Return an object of this model
        return cls(customer,
                   card,
                   code,
                   payment_method,
                   billing_type,
                   statement_descriptor,
                   description,
                   currency,
                   interval,
                   interval_count,
                   pricing_scheme,
                   items,
                   shipping,
                   discounts,
                   metadata,
                   setup,
                   increments,
                   plan_id,
                   customer_id,
                   card_id,
                   billing_day,
                   installments,
                   start_at,
                   minimum_price,
                   cycles,
                   card_token,
                   gateway_affiliation_id,
                   quantity,
                   boleto_due_days,
                   period,
                   submerchant,
                   split)


