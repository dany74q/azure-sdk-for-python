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


class DataDisksGroups(Model):
    """The data disks groups for the role.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param disks_per_node: The number of disks per node.
    :type disks_per_node: int
    :ivar storage_account_type: ReadOnly. The storage account type. Do not set
     this value.
    :vartype storage_account_type: str
    :ivar disk_size_gb: ReadOnly. The DiskSize in GB. Do not set this value.
    :vartype disk_size_gb: int
    """

    _validation = {
        'storage_account_type': {'readonly': True},
        'disk_size_gb': {'readonly': True},
    }

    _attribute_map = {
        'disks_per_node': {'key': 'disksPerNode', 'type': 'int'},
        'storage_account_type': {'key': 'storageAccountType', 'type': 'str'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
    }

    def __init__(self, *, disks_per_node: int=None, **kwargs) -> None:
        super(DataDisksGroups, self).__init__(**kwargs)
        self.disks_per_node = disks_per_node
        self.storage_account_type = None
        self.disk_size_gb = None
