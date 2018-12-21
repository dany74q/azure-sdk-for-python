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

from .proxy_resource_py3 import ProxyResource


class EventHubConnectionUpdate(ProxyResource):
    """Class representing an update to event hub connection.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param event_hub_resource_id: Required. The resource ID of the event hub
     to be used to create a data connection.
    :type event_hub_resource_id: str
    :param consumer_group: Required. The event hub consumer group.
    :type consumer_group: str
    :param table_name: The table where the data should be ingested. Optionally
     the table information can be added to each message.
    :type table_name: str
    :param mapping_rule_name: The mapping rule to be used to ingest the data.
     Optionally the mapping information can be added to each message.
    :type mapping_rule_name: str
    :param data_format: The data format of the message. Optionally the data
     format can be added to each message. Possible values include: 'MULTIJSON',
     'JSON', 'CSV'
    :type data_format: str or ~azure.mgmt.kusto.models.DataFormat
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'event_hub_resource_id': {'required': True},
        'consumer_group': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'event_hub_resource_id': {'key': 'properties.eventHubResourceId', 'type': 'str'},
        'consumer_group': {'key': 'properties.consumerGroup', 'type': 'str'},
        'table_name': {'key': 'properties.tableName', 'type': 'str'},
        'mapping_rule_name': {'key': 'properties.mappingRuleName', 'type': 'str'},
        'data_format': {'key': 'properties.dataFormat', 'type': 'str'},
    }

    def __init__(self, *, event_hub_resource_id: str, consumer_group: str, location: str=None, table_name: str=None, mapping_rule_name: str=None, data_format=None, **kwargs) -> None:
        super(EventHubConnectionUpdate, self).__init__(**kwargs)
        self.location = location
        self.event_hub_resource_id = event_hub_resource_id
        self.consumer_group = consumer_group
        self.table_name = table_name
        self.mapping_rule_name = mapping_rule_name
        self.data_format = data_format
