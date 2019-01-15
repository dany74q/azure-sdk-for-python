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

from msrest.serialization import Model


class IntegrationRuntimeComputeProperties(Model):
    """The compute resource properties for managed integration runtime.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param location: The location for managed integration runtime. The
     supported regions could be found on
     https://docs.microsoft.com/en-us/azure/data-factory/data-factory-data-movement-activities
    :type location: str
    :param node_size: The node size requirement to managed integration
     runtime.
    :type node_size: str
    :param number_of_nodes: The required number of nodes for managed
     integration runtime.
    :type number_of_nodes: int
    :param max_parallel_executions_per_node: Maximum parallel executions count
     per node for managed integration runtime.
    :type max_parallel_executions_per_node: int
    :param v_net_properties: VNet properties for managed integration runtime.
    :type v_net_properties:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeVNetProperties
    :param virtual_network: VNet properties for managed integration runtime.
    :type virtual_network:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeVirtualNetworkProperties
    """

    _validation = {
        'number_of_nodes': {'minimum': 1},
        'max_parallel_executions_per_node': {'minimum': 1},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'location': {'key': 'location', 'type': 'str'},
        'node_size': {'key': 'nodeSize', 'type': 'str'},
        'number_of_nodes': {'key': 'numberOfNodes', 'type': 'int'},
        'max_parallel_executions_per_node': {'key': 'maxParallelExecutionsPerNode', 'type': 'int'},
        'v_net_properties': {'key': 'vNetProperties', 'type': 'IntegrationRuntimeVNetProperties'},
        'virtual_network': {'key': 'virtualNetwork', 'type': 'IntegrationRuntimeVirtualNetworkProperties'},
    }

    def __init__(self, **kwargs):
        super(IntegrationRuntimeComputeProperties, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.location = kwargs.get('location', None)
        self.node_size = kwargs.get('node_size', None)
        self.number_of_nodes = kwargs.get('number_of_nodes', None)
        self.max_parallel_executions_per_node = kwargs.get('max_parallel_executions_per_node', None)
        self.v_net_properties = kwargs.get('v_net_properties', None)
        self.virtual_network = kwargs.get('virtual_network', None)
