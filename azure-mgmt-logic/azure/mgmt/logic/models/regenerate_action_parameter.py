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


class RegenerateActionParameter(Model):
    """The access key regenerate action content.

    :param key_type: The key type. Possible values include: 'NotSpecified',
     'Primary', 'Secondary'
    :type key_type: str or ~azure.mgmt.logic.models.KeyType
    """

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RegenerateActionParameter, self).__init__(**kwargs)
        self.key_type = kwargs.get('key_type', None)
