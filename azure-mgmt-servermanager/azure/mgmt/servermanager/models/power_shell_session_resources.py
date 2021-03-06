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


class PowerShellSessionResources(Model):
    """A collection of PowerShell session resources.

    :param value: Collection of PowerShell session resources.
    :type value:
     list[~azure.mgmt.servermanager.models.PowerShellSessionResource]
    :param next_link: The URL to the next set of resources.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PowerShellSessionResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PowerShellSessionResources, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)
