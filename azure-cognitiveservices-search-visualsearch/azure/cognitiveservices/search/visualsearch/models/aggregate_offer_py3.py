# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .offer_py3 import Offer


class AggregateOffer(Offer):
    """Defines a list of offers from merchants that are related to the image.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    :ivar id: A String identifier.
    :vartype id: str
    :ivar read_link: The URL that returns this resource. To use the URL,
     append query parameters as appropriate and include the
     Ocp-Apim-Subscription-Key header.
    :vartype read_link: str
    :ivar web_search_url: The URL to Bing's search result for this item.
    :vartype web_search_url: str
    :ivar name: The name of the thing represented by this object.
    :vartype name: str
    :ivar url: The URL to get more information about the thing represented by
     this object.
    :vartype url: str
    :ivar image: An image of the item.
    :vartype image:
     ~azure.cognitiveservices.search.visualsearch.models.ImageObject
    :ivar description: A short description of the item.
    :vartype description: str
    :ivar alternate_name: An alias for the item.
    :vartype alternate_name: str
    :ivar bing_id: An ID that uniquely identifies this item.
    :vartype bing_id: str
    :ivar seller: Seller for this offer.
    :vartype seller:
     ~azure.cognitiveservices.search.visualsearch.models.Organization
    :ivar price: The item's price.
    :vartype price: float
    :ivar price_currency: The monetary currency. For example, USD. Possible
     values include: 'USD', 'CAD', 'GBP', 'EUR', 'COP', 'JPY', 'CNY', 'AUD',
     'INR', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AWG', 'AZN',
     'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BOV',
     'BRL', 'BSD', 'BTN', 'BWP', 'BYR', 'BZD', 'CDF', 'CHE', 'CHF', 'CHW',
     'CLF', 'CLP', 'COU', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK',
     'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'FJD', 'FKP', 'GEL', 'GHS', 'GIP',
     'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR',
     'ILS', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'KES', 'KGS', 'KHR', 'KMF',
     'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL',
     'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR',
     'MVR', 'MWK', 'MXN', 'MXV', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK',
     'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG',
     'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK',
     'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STD', 'SYP', 'SZL', 'THB',
     'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX',
     'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XOF', 'XPF',
     'YER', 'ZAR', 'ZMW'. Default value: "USD" .
    :vartype price_currency: str or
     ~azure.cognitiveservices.search.visualsearch.models.Currency
    :ivar availability: The item's availability. The following are the
     possible values: Discontinued, InStock, InStoreOnly, LimitedAvailability,
     OnlineOnly, OutOfStock, PreOrder, SoldOut. Possible values include:
     'Discontinued', 'InStock', 'InStoreOnly', 'LimitedAvailability',
     'OnlineOnly', 'OutOfStock', 'PreOrder', 'SoldOut'
    :vartype availability: str or
     ~azure.cognitiveservices.search.visualsearch.models.ItemAvailability
    :ivar aggregate_rating: An aggregated rating that indicates how well the
     product has been rated by others.
    :vartype aggregate_rating:
     ~azure.cognitiveservices.search.visualsearch.models.AggregateRating
    :ivar last_updated: The last date that the offer was updated. The date is
     in the form YYYY-MM-DD.
    :vartype last_updated: str
    :ivar offers: A list of offers from merchants that have offerings related
     to the image.
    :vartype offers:
     list[~azure.cognitiveservices.search.visualsearch.models.Offer]
    """

    _validation = {
        '_type': {'required': True},
        'id': {'readonly': True},
        'read_link': {'readonly': True},
        'web_search_url': {'readonly': True},
        'name': {'readonly': True},
        'url': {'readonly': True},
        'image': {'readonly': True},
        'description': {'readonly': True},
        'alternate_name': {'readonly': True},
        'bing_id': {'readonly': True},
        'seller': {'readonly': True},
        'price': {'readonly': True},
        'price_currency': {'readonly': True},
        'availability': {'readonly': True},
        'aggregate_rating': {'readonly': True},
        'last_updated': {'readonly': True},
        'offers': {'readonly': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'read_link': {'key': 'readLink', 'type': 'str'},
        'web_search_url': {'key': 'webSearchUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'image': {'key': 'image', 'type': 'ImageObject'},
        'description': {'key': 'description', 'type': 'str'},
        'alternate_name': {'key': 'alternateName', 'type': 'str'},
        'bing_id': {'key': 'bingId', 'type': 'str'},
        'seller': {'key': 'seller', 'type': 'Organization'},
        'price': {'key': 'price', 'type': 'float'},
        'price_currency': {'key': 'priceCurrency', 'type': 'str'},
        'availability': {'key': 'availability', 'type': 'str'},
        'aggregate_rating': {'key': 'aggregateRating', 'type': 'AggregateRating'},
        'last_updated': {'key': 'lastUpdated', 'type': 'str'},
        'offers': {'key': 'offers', 'type': '[Offer]'},
    }

    def __init__(self, **kwargs) -> None:
        super(AggregateOffer, self).__init__(**kwargs)
        self.offers = None
        self._type = 'AggregateOffer'
