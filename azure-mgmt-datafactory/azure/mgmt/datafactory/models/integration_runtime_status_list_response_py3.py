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


class IntegrationRuntimeStatusListResponse(Model):
    """A list of integration runtime status.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. List of integration runtime status.
    :type value:
     list[~azure.mgmt.datafactory.models.IntegrationRuntimeStatusResponse]
    :param next_link: The link to the next page of results, if any remaining
     results exist.
    :type next_link: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[IntegrationRuntimeStatusResponse]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, value, next_link: str=None, **kwargs) -> None:
        super(IntegrationRuntimeStatusListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
