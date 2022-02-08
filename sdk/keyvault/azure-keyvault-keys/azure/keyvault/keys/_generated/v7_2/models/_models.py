# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Attributes(msrest.serialization.Model):
    """The object attributes managed by the KeyVault service.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar enabled: Determines whether the object is enabled.
    :vartype enabled: bool
    :ivar not_before: Not before date in UTC.
    :vartype not_before: ~datetime.datetime
    :ivar expires: Expiry date in UTC.
    :vartype expires: ~datetime.datetime
    :ivar created: Creation time in UTC.
    :vartype created: ~datetime.datetime
    :ivar updated: Last updated time in UTC.
    :vartype updated: ~datetime.datetime
    """

    _validation = {
        'created': {'readonly': True},
        'updated': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'not_before': {'key': 'nbf', 'type': 'unix-time'},
        'expires': {'key': 'exp', 'type': 'unix-time'},
        'created': {'key': 'created', 'type': 'unix-time'},
        'updated': {'key': 'updated', 'type': 'unix-time'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword enabled: Determines whether the object is enabled.
        :paramtype enabled: bool
        :keyword not_before: Not before date in UTC.
        :paramtype not_before: ~datetime.datetime
        :keyword expires: Expiry date in UTC.
        :paramtype expires: ~datetime.datetime
        """
        super(Attributes, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.not_before = kwargs.get('not_before', None)
        self.expires = kwargs.get('expires', None)
        self.created = None
        self.updated = None


class BackupKeyResult(msrest.serialization.Model):
    """The backup key result, containing the backup blob.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: The backup blob containing the backed up key.
    :vartype value: bytes
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'base64'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(BackupKeyResult, self).__init__(**kwargs)
        self.value = None


class KeyBundle(msrest.serialization.Model):
    """A KeyBundle consisting of a WebKey plus its attributes.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar key: The Json web key.
    :vartype key: ~azure.keyvault.v7_2.models.JsonWebKey
    :ivar attributes: The key management attributes.
    :vartype attributes: ~azure.keyvault.v7_2.models.KeyAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :ivar managed: True if the key's lifetime is managed by key vault. If this is a key backing a
     certificate, then managed will be true.
    :vartype managed: bool
    """

    _validation = {
        'managed': {'readonly': True},
    }

    _attribute_map = {
        'key': {'key': 'key', 'type': 'JsonWebKey'},
        'attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed': {'key': 'managed', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword key: The Json web key.
        :paramtype key: ~azure.keyvault.v7_2.models.JsonWebKey
        :keyword attributes: The key management attributes.
        :paramtype attributes: ~azure.keyvault.v7_2.models.KeyAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        """
        super(KeyBundle, self).__init__(**kwargs)
        self.key = kwargs.get('key', None)
        self.attributes = kwargs.get('attributes', None)
        self.tags = kwargs.get('tags', None)
        self.managed = None


class DeletedKeyBundle(KeyBundle):
    """A DeletedKeyBundle consisting of a WebKey plus its Attributes and deletion info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar key: The Json web key.
    :vartype key: ~azure.keyvault.v7_2.models.JsonWebKey
    :ivar attributes: The key management attributes.
    :vartype attributes: ~azure.keyvault.v7_2.models.KeyAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :ivar managed: True if the key's lifetime is managed by key vault. If this is a key backing a
     certificate, then managed will be true.
    :vartype managed: bool
    :ivar recovery_id: The url of the recovery object, used to identify and recover the deleted
     key.
    :vartype recovery_id: str
    :ivar scheduled_purge_date: The time when the key is scheduled to be purged, in UTC.
    :vartype scheduled_purge_date: ~datetime.datetime
    :ivar deleted_date: The time when the key was deleted, in UTC.
    :vartype deleted_date: ~datetime.datetime
    """

    _validation = {
        'managed': {'readonly': True},
        'scheduled_purge_date': {'readonly': True},
        'deleted_date': {'readonly': True},
    }

    _attribute_map = {
        'key': {'key': 'key', 'type': 'JsonWebKey'},
        'attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed': {'key': 'managed', 'type': 'bool'},
        'recovery_id': {'key': 'recoveryId', 'type': 'str'},
        'scheduled_purge_date': {'key': 'scheduledPurgeDate', 'type': 'unix-time'},
        'deleted_date': {'key': 'deletedDate', 'type': 'unix-time'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword key: The Json web key.
        :paramtype key: ~azure.keyvault.v7_2.models.JsonWebKey
        :keyword attributes: The key management attributes.
        :paramtype attributes: ~azure.keyvault.v7_2.models.KeyAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        :keyword recovery_id: The url of the recovery object, used to identify and recover the deleted
         key.
        :paramtype recovery_id: str
        """
        super(DeletedKeyBundle, self).__init__(**kwargs)
        self.recovery_id = kwargs.get('recovery_id', None)
        self.scheduled_purge_date = None
        self.deleted_date = None


class KeyItem(msrest.serialization.Model):
    """The key item containing key metadata.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar kid: Key identifier.
    :vartype kid: str
    :ivar attributes: The key management attributes.
    :vartype attributes: ~azure.keyvault.v7_2.models.KeyAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :ivar managed: True if the key's lifetime is managed by key vault. If this is a key backing a
     certificate, then managed will be true.
    :vartype managed: bool
    """

    _validation = {
        'managed': {'readonly': True},
    }

    _attribute_map = {
        'kid': {'key': 'kid', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed': {'key': 'managed', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword kid: Key identifier.
        :paramtype kid: str
        :keyword attributes: The key management attributes.
        :paramtype attributes: ~azure.keyvault.v7_2.models.KeyAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        """
        super(KeyItem, self).__init__(**kwargs)
        self.kid = kwargs.get('kid', None)
        self.attributes = kwargs.get('attributes', None)
        self.tags = kwargs.get('tags', None)
        self.managed = None


class DeletedKeyItem(KeyItem):
    """The deleted key item containing the deleted key metadata and information about deletion.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar kid: Key identifier.
    :vartype kid: str
    :ivar attributes: The key management attributes.
    :vartype attributes: ~azure.keyvault.v7_2.models.KeyAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :ivar managed: True if the key's lifetime is managed by key vault. If this is a key backing a
     certificate, then managed will be true.
    :vartype managed: bool
    :ivar recovery_id: The url of the recovery object, used to identify and recover the deleted
     key.
    :vartype recovery_id: str
    :ivar scheduled_purge_date: The time when the key is scheduled to be purged, in UTC.
    :vartype scheduled_purge_date: ~datetime.datetime
    :ivar deleted_date: The time when the key was deleted, in UTC.
    :vartype deleted_date: ~datetime.datetime
    """

    _validation = {
        'managed': {'readonly': True},
        'scheduled_purge_date': {'readonly': True},
        'deleted_date': {'readonly': True},
    }

    _attribute_map = {
        'kid': {'key': 'kid', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed': {'key': 'managed', 'type': 'bool'},
        'recovery_id': {'key': 'recoveryId', 'type': 'str'},
        'scheduled_purge_date': {'key': 'scheduledPurgeDate', 'type': 'unix-time'},
        'deleted_date': {'key': 'deletedDate', 'type': 'unix-time'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword kid: Key identifier.
        :paramtype kid: str
        :keyword attributes: The key management attributes.
        :paramtype attributes: ~azure.keyvault.v7_2.models.KeyAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        :keyword recovery_id: The url of the recovery object, used to identify and recover the deleted
         key.
        :paramtype recovery_id: str
        """
        super(DeletedKeyItem, self).__init__(**kwargs)
        self.recovery_id = kwargs.get('recovery_id', None)
        self.scheduled_purge_date = None
        self.deleted_date = None


class DeletedKeyListResult(msrest.serialization.Model):
    """A list of keys that have been deleted in this vault.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: A response message containing a list of deleted keys in the vault along with a
     link to the next page of deleted keys.
    :vartype value: list[~azure.keyvault.v7_2.models.DeletedKeyItem]
    :ivar next_link: The URL to get the next set of deleted keys.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DeletedKeyItem]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(DeletedKeyListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class Error(msrest.serialization.Model):
    """The key vault server error.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar inner_error: The key vault server error.
    :vartype inner_error: ~azure.keyvault.v7_2.models.Error
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'inner_error': {'key': 'innererror', 'type': 'Error'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(Error, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.inner_error = None


class JsonWebKey(msrest.serialization.Model):
    """As of http://tools.ietf.org/html/draft-ietf-jose-json-web-key-18.

    :ivar kid: Key identifier.
    :vartype kid: str
    :ivar kty: JsonWebKey Key Type (kty), as defined in
     https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-40. Possible values include:
     "EC", "EC-HSM", "RSA", "RSA-HSM", "oct", "oct-HSM".
    :vartype kty: str or ~azure.keyvault.v7_2.models.JsonWebKeyType
    :ivar key_ops:
    :vartype key_ops: list[str]
    :ivar n: RSA modulus.
    :vartype n: bytes
    :ivar e: RSA public exponent.
    :vartype e: bytes
    :ivar d: RSA private exponent, or the D component of an EC private key.
    :vartype d: bytes
    :ivar dp: RSA private key parameter.
    :vartype dp: bytes
    :ivar dq: RSA private key parameter.
    :vartype dq: bytes
    :ivar qi: RSA private key parameter.
    :vartype qi: bytes
    :ivar p: RSA secret prime.
    :vartype p: bytes
    :ivar q: RSA secret prime, with p < q.
    :vartype q: bytes
    :ivar k: Symmetric key.
    :vartype k: bytes
    :ivar t: Protected Key, used with 'Bring Your Own Key'.
    :vartype t: bytes
    :ivar crv: Elliptic curve name. For valid values, see JsonWebKeyCurveName. Possible values
     include: "P-256", "P-384", "P-521", "P-256K".
    :vartype crv: str or ~azure.keyvault.v7_2.models.JsonWebKeyCurveName
    :ivar x: X component of an EC public key.
    :vartype x: bytes
    :ivar y: Y component of an EC public key.
    :vartype y: bytes
    """

    _attribute_map = {
        'kid': {'key': 'kid', 'type': 'str'},
        'kty': {'key': 'kty', 'type': 'str'},
        'key_ops': {'key': 'key_ops', 'type': '[str]'},
        'n': {'key': 'n', 'type': 'base64'},
        'e': {'key': 'e', 'type': 'base64'},
        'd': {'key': 'd', 'type': 'base64'},
        'dp': {'key': 'dp', 'type': 'base64'},
        'dq': {'key': 'dq', 'type': 'base64'},
        'qi': {'key': 'qi', 'type': 'base64'},
        'p': {'key': 'p', 'type': 'base64'},
        'q': {'key': 'q', 'type': 'base64'},
        'k': {'key': 'k', 'type': 'base64'},
        't': {'key': 'key_hsm', 'type': 'base64'},
        'crv': {'key': 'crv', 'type': 'str'},
        'x': {'key': 'x', 'type': 'base64'},
        'y': {'key': 'y', 'type': 'base64'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword kid: Key identifier.
        :paramtype kid: str
        :keyword kty: JsonWebKey Key Type (kty), as defined in
         https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-40. Possible values include:
         "EC", "EC-HSM", "RSA", "RSA-HSM", "oct", "oct-HSM".
        :paramtype kty: str or ~azure.keyvault.v7_2.models.JsonWebKeyType
        :keyword key_ops:
        :paramtype key_ops: list[str]
        :keyword n: RSA modulus.
        :paramtype n: bytes
        :keyword e: RSA public exponent.
        :paramtype e: bytes
        :keyword d: RSA private exponent, or the D component of an EC private key.
        :paramtype d: bytes
        :keyword dp: RSA private key parameter.
        :paramtype dp: bytes
        :keyword dq: RSA private key parameter.
        :paramtype dq: bytes
        :keyword qi: RSA private key parameter.
        :paramtype qi: bytes
        :keyword p: RSA secret prime.
        :paramtype p: bytes
        :keyword q: RSA secret prime, with p < q.
        :paramtype q: bytes
        :keyword k: Symmetric key.
        :paramtype k: bytes
        :keyword t: Protected Key, used with 'Bring Your Own Key'.
        :paramtype t: bytes
        :keyword crv: Elliptic curve name. For valid values, see JsonWebKeyCurveName. Possible values
         include: "P-256", "P-384", "P-521", "P-256K".
        :paramtype crv: str or ~azure.keyvault.v7_2.models.JsonWebKeyCurveName
        :keyword x: X component of an EC public key.
        :paramtype x: bytes
        :keyword y: Y component of an EC public key.
        :paramtype y: bytes
        """
        super(JsonWebKey, self).__init__(**kwargs)
        self.kid = kwargs.get('kid', None)
        self.kty = kwargs.get('kty', None)
        self.key_ops = kwargs.get('key_ops', None)
        self.n = kwargs.get('n', None)
        self.e = kwargs.get('e', None)
        self.d = kwargs.get('d', None)
        self.dp = kwargs.get('dp', None)
        self.dq = kwargs.get('dq', None)
        self.qi = kwargs.get('qi', None)
        self.p = kwargs.get('p', None)
        self.q = kwargs.get('q', None)
        self.k = kwargs.get('k', None)
        self.t = kwargs.get('t', None)
        self.crv = kwargs.get('crv', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)


class KeyAttributes(Attributes):
    """The attributes of a key managed by the key vault service.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar enabled: Determines whether the object is enabled.
    :vartype enabled: bool
    :ivar not_before: Not before date in UTC.
    :vartype not_before: ~datetime.datetime
    :ivar expires: Expiry date in UTC.
    :vartype expires: ~datetime.datetime
    :ivar created: Creation time in UTC.
    :vartype created: ~datetime.datetime
    :ivar updated: Last updated time in UTC.
    :vartype updated: ~datetime.datetime
    :ivar recoverable_days: softDelete data retention days. Value should be >=7 and <=90 when
     softDelete enabled, otherwise 0.
    :vartype recoverable_days: int
    :ivar recovery_level: Reflects the deletion recovery level currently in effect for keys in the
     current vault. If it contains 'Purgeable' the key can be permanently deleted by a privileged
     user; otherwise, only the system can purge the key, at the end of the retention interval.
     Possible values include: "Purgeable", "Recoverable+Purgeable", "Recoverable",
     "Recoverable+ProtectedSubscription", "CustomizedRecoverable+Purgeable",
     "CustomizedRecoverable", "CustomizedRecoverable+ProtectedSubscription".
    :vartype recovery_level: str or ~azure.keyvault.v7_2.models.DeletionRecoveryLevel
    """

    _validation = {
        'created': {'readonly': True},
        'updated': {'readonly': True},
        'recoverable_days': {'readonly': True},
        'recovery_level': {'readonly': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'not_before': {'key': 'nbf', 'type': 'unix-time'},
        'expires': {'key': 'exp', 'type': 'unix-time'},
        'created': {'key': 'created', 'type': 'unix-time'},
        'updated': {'key': 'updated', 'type': 'unix-time'},
        'recoverable_days': {'key': 'recoverableDays', 'type': 'int'},
        'recovery_level': {'key': 'recoveryLevel', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword enabled: Determines whether the object is enabled.
        :paramtype enabled: bool
        :keyword not_before: Not before date in UTC.
        :paramtype not_before: ~datetime.datetime
        :keyword expires: Expiry date in UTC.
        :paramtype expires: ~datetime.datetime
        """
        super(KeyAttributes, self).__init__(**kwargs)
        self.recoverable_days = None
        self.recovery_level = None


class KeyCreateParameters(msrest.serialization.Model):
    """The key create parameters.

    All required parameters must be populated in order to send to Azure.

    :ivar kty: Required. The type of key to create. For valid values, see JsonWebKeyType. Possible
     values include: "EC", "EC-HSM", "RSA", "RSA-HSM", "oct", "oct-HSM".
    :vartype kty: str or ~azure.keyvault.v7_2.models.JsonWebKeyType
    :ivar key_size: The key size in bits. For example: 2048, 3072, or 4096 for RSA.
    :vartype key_size: int
    :ivar public_exponent: The public exponent for a RSA key.
    :vartype public_exponent: int
    :ivar key_ops:
    :vartype key_ops: list[str or ~azure.keyvault.v7_2.models.JsonWebKeyOperation]
    :ivar key_attributes: The attributes of a key managed by the key vault service.
    :vartype key_attributes: ~azure.keyvault.v7_2.models.KeyAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :ivar curve: Elliptic curve name. For valid values, see JsonWebKeyCurveName. Possible values
     include: "P-256", "P-384", "P-521", "P-256K".
    :vartype curve: str or ~azure.keyvault.v7_2.models.JsonWebKeyCurveName
    """

    _validation = {
        'kty': {'required': True},
    }

    _attribute_map = {
        'kty': {'key': 'kty', 'type': 'str'},
        'key_size': {'key': 'key_size', 'type': 'int'},
        'public_exponent': {'key': 'public_exponent', 'type': 'int'},
        'key_ops': {'key': 'key_ops', 'type': '[str]'},
        'key_attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'curve': {'key': 'crv', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword kty: Required. The type of key to create. For valid values, see JsonWebKeyType.
         Possible values include: "EC", "EC-HSM", "RSA", "RSA-HSM", "oct", "oct-HSM".
        :paramtype kty: str or ~azure.keyvault.v7_2.models.JsonWebKeyType
        :keyword key_size: The key size in bits. For example: 2048, 3072, or 4096 for RSA.
        :paramtype key_size: int
        :keyword public_exponent: The public exponent for a RSA key.
        :paramtype public_exponent: int
        :keyword key_ops:
        :paramtype key_ops: list[str or ~azure.keyvault.v7_2.models.JsonWebKeyOperation]
        :keyword key_attributes: The attributes of a key managed by the key vault service.
        :paramtype key_attributes: ~azure.keyvault.v7_2.models.KeyAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        :keyword curve: Elliptic curve name. For valid values, see JsonWebKeyCurveName. Possible values
         include: "P-256", "P-384", "P-521", "P-256K".
        :paramtype curve: str or ~azure.keyvault.v7_2.models.JsonWebKeyCurveName
        """
        super(KeyCreateParameters, self).__init__(**kwargs)
        self.kty = kwargs['kty']
        self.key_size = kwargs.get('key_size', None)
        self.public_exponent = kwargs.get('public_exponent', None)
        self.key_ops = kwargs.get('key_ops', None)
        self.key_attributes = kwargs.get('key_attributes', None)
        self.tags = kwargs.get('tags', None)
        self.curve = kwargs.get('curve', None)


class KeyImportParameters(msrest.serialization.Model):
    """The key import parameters.

    All required parameters must be populated in order to send to Azure.

    :ivar hsm: Whether to import as a hardware key (HSM) or software key.
    :vartype hsm: bool
    :ivar key: Required. The Json web key.
    :vartype key: ~azure.keyvault.v7_2.models.JsonWebKey
    :ivar key_attributes: The key management attributes.
    :vartype key_attributes: ~azure.keyvault.v7_2.models.KeyAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    """

    _validation = {
        'key': {'required': True},
    }

    _attribute_map = {
        'hsm': {'key': 'Hsm', 'type': 'bool'},
        'key': {'key': 'key', 'type': 'JsonWebKey'},
        'key_attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword hsm: Whether to import as a hardware key (HSM) or software key.
        :paramtype hsm: bool
        :keyword key: Required. The Json web key.
        :paramtype key: ~azure.keyvault.v7_2.models.JsonWebKey
        :keyword key_attributes: The key management attributes.
        :paramtype key_attributes: ~azure.keyvault.v7_2.models.KeyAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        """
        super(KeyImportParameters, self).__init__(**kwargs)
        self.hsm = kwargs.get('hsm', None)
        self.key = kwargs['key']
        self.key_attributes = kwargs.get('key_attributes', None)
        self.tags = kwargs.get('tags', None)


class KeyListResult(msrest.serialization.Model):
    """The key list result.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: A response message containing a list of keys in the key vault along with a link to
     the next page of keys.
    :vartype value: list[~azure.keyvault.v7_2.models.KeyItem]
    :ivar next_link: The URL to get the next set of keys.
    :vartype next_link: str
    """

    _validation = {
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[KeyItem]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(KeyListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = None


class KeyOperationResult(msrest.serialization.Model):
    """The key operation result.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar kid: Key identifier.
    :vartype kid: str
    :ivar result:
    :vartype result: bytes
    :ivar iv:
    :vartype iv: bytes
    :ivar authentication_tag:
    :vartype authentication_tag: bytes
    :ivar additional_authenticated_data:
    :vartype additional_authenticated_data: bytes
    """

    _validation = {
        'kid': {'readonly': True},
        'result': {'readonly': True},
        'iv': {'readonly': True},
        'authentication_tag': {'readonly': True},
        'additional_authenticated_data': {'readonly': True},
    }

    _attribute_map = {
        'kid': {'key': 'kid', 'type': 'str'},
        'result': {'key': 'value', 'type': 'base64'},
        'iv': {'key': 'iv', 'type': 'base64'},
        'authentication_tag': {'key': 'tag', 'type': 'base64'},
        'additional_authenticated_data': {'key': 'aad', 'type': 'base64'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(KeyOperationResult, self).__init__(**kwargs)
        self.kid = None
        self.result = None
        self.iv = None
        self.authentication_tag = None
        self.additional_authenticated_data = None


class KeyOperationsParameters(msrest.serialization.Model):
    """The key operations parameters.

    All required parameters must be populated in order to send to Azure.

    :ivar algorithm: Required. algorithm identifier. Possible values include: "RSA-OAEP",
     "RSA-OAEP-256", "RSA1_5", "A128GCM", "A192GCM", "A256GCM", "A128KW", "A192KW", "A256KW",
     "A128CBC", "A192CBC", "A256CBC", "A128CBCPAD", "A192CBCPAD", "A256CBCPAD".
    :vartype algorithm: str or ~azure.keyvault.v7_2.models.JsonWebKeyEncryptionAlgorithm
    :ivar value: Required.
    :vartype value: bytes
    :ivar iv: Initialization vector for symmetric algorithms.
    :vartype iv: bytes
    :ivar aad: Additional data to authenticate but not encrypt/decrypt when using authenticated
     crypto algorithms.
    :vartype aad: bytes
    :ivar tag: The tag to authenticate when performing decryption with an authenticated algorithm.
    :vartype tag: bytes
    """

    _validation = {
        'algorithm': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'algorithm': {'key': 'alg', 'type': 'str'},
        'value': {'key': 'value', 'type': 'base64'},
        'iv': {'key': 'iv', 'type': 'base64'},
        'aad': {'key': 'aad', 'type': 'base64'},
        'tag': {'key': 'tag', 'type': 'base64'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword algorithm: Required. algorithm identifier. Possible values include: "RSA-OAEP",
         "RSA-OAEP-256", "RSA1_5", "A128GCM", "A192GCM", "A256GCM", "A128KW", "A192KW", "A256KW",
         "A128CBC", "A192CBC", "A256CBC", "A128CBCPAD", "A192CBCPAD", "A256CBCPAD".
        :paramtype algorithm: str or ~azure.keyvault.v7_2.models.JsonWebKeyEncryptionAlgorithm
        :keyword value: Required.
        :paramtype value: bytes
        :keyword iv: Initialization vector for symmetric algorithms.
        :paramtype iv: bytes
        :keyword aad: Additional data to authenticate but not encrypt/decrypt when using authenticated
         crypto algorithms.
        :paramtype aad: bytes
        :keyword tag: The tag to authenticate when performing decryption with an authenticated
         algorithm.
        :paramtype tag: bytes
        """
        super(KeyOperationsParameters, self).__init__(**kwargs)
        self.algorithm = kwargs['algorithm']
        self.value = kwargs['value']
        self.iv = kwargs.get('iv', None)
        self.aad = kwargs.get('aad', None)
        self.tag = kwargs.get('tag', None)


class KeyProperties(msrest.serialization.Model):
    """Properties of the key pair backing a certificate.

    :ivar exportable: Not supported in this version. Indicates if the private key can be exported.
    :vartype exportable: bool
    :ivar key_type: The type of key pair to be used for the certificate. Possible values include:
     "EC", "EC-HSM", "RSA", "RSA-HSM", "oct", "oct-HSM".
    :vartype key_type: str or ~azure.keyvault.v7_2.models.JsonWebKeyType
    :ivar key_size: The key size in bits. For example: 2048, 3072, or 4096 for RSA.
    :vartype key_size: int
    :ivar reuse_key: Indicates if the same key pair will be used on certificate renewal.
    :vartype reuse_key: bool
    :ivar curve: Elliptic curve name. For valid values, see JsonWebKeyCurveName. Possible values
     include: "P-256", "P-384", "P-521", "P-256K".
    :vartype curve: str or ~azure.keyvault.v7_2.models.JsonWebKeyCurveName
    """

    _attribute_map = {
        'exportable': {'key': 'exportable', 'type': 'bool'},
        'key_type': {'key': 'kty', 'type': 'str'},
        'key_size': {'key': 'key_size', 'type': 'int'},
        'reuse_key': {'key': 'reuse_key', 'type': 'bool'},
        'curve': {'key': 'crv', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword exportable: Not supported in this version. Indicates if the private key can be
         exported.
        :paramtype exportable: bool
        :keyword key_type: The type of key pair to be used for the certificate. Possible values
         include: "EC", "EC-HSM", "RSA", "RSA-HSM", "oct", "oct-HSM".
        :paramtype key_type: str or ~azure.keyvault.v7_2.models.JsonWebKeyType
        :keyword key_size: The key size in bits. For example: 2048, 3072, or 4096 for RSA.
        :paramtype key_size: int
        :keyword reuse_key: Indicates if the same key pair will be used on certificate renewal.
        :paramtype reuse_key: bool
        :keyword curve: Elliptic curve name. For valid values, see JsonWebKeyCurveName. Possible values
         include: "P-256", "P-384", "P-521", "P-256K".
        :paramtype curve: str or ~azure.keyvault.v7_2.models.JsonWebKeyCurveName
        """
        super(KeyProperties, self).__init__(**kwargs)
        self.exportable = kwargs.get('exportable', None)
        self.key_type = kwargs.get('key_type', None)
        self.key_size = kwargs.get('key_size', None)
        self.reuse_key = kwargs.get('reuse_key', None)
        self.curve = kwargs.get('curve', None)


class KeyRestoreParameters(msrest.serialization.Model):
    """The key restore parameters.

    All required parameters must be populated in order to send to Azure.

    :ivar key_bundle_backup: Required. The backup blob associated with a key bundle.
    :vartype key_bundle_backup: bytes
    """

    _validation = {
        'key_bundle_backup': {'required': True},
    }

    _attribute_map = {
        'key_bundle_backup': {'key': 'value', 'type': 'base64'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword key_bundle_backup: Required. The backup blob associated with a key bundle.
        :paramtype key_bundle_backup: bytes
        """
        super(KeyRestoreParameters, self).__init__(**kwargs)
        self.key_bundle_backup = kwargs['key_bundle_backup']


class KeySignParameters(msrest.serialization.Model):
    """The key operations parameters.

    All required parameters must be populated in order to send to Azure.

    :ivar algorithm: Required. The signing/verification algorithm identifier. For more information
     on possible algorithm types, see JsonWebKeySignatureAlgorithm. Possible values include:
     "PS256", "PS384", "PS512", "RS256", "RS384", "RS512", "RSNULL", "ES256", "ES384", "ES512",
     "ES256K".
    :vartype algorithm: str or ~azure.keyvault.v7_2.models.JsonWebKeySignatureAlgorithm
    :ivar value: Required.
    :vartype value: bytes
    """

    _validation = {
        'algorithm': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'algorithm': {'key': 'alg', 'type': 'str'},
        'value': {'key': 'value', 'type': 'base64'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword algorithm: Required. The signing/verification algorithm identifier. For more
         information on possible algorithm types, see JsonWebKeySignatureAlgorithm. Possible values
         include: "PS256", "PS384", "PS512", "RS256", "RS384", "RS512", "RSNULL", "ES256", "ES384",
         "ES512", "ES256K".
        :paramtype algorithm: str or ~azure.keyvault.v7_2.models.JsonWebKeySignatureAlgorithm
        :keyword value: Required.
        :paramtype value: bytes
        """
        super(KeySignParameters, self).__init__(**kwargs)
        self.algorithm = kwargs['algorithm']
        self.value = kwargs['value']


class KeyUpdateParameters(msrest.serialization.Model):
    """The key update parameters.

    :ivar key_ops: Json web key operations. For more information on possible key operations, see
     JsonWebKeyOperation.
    :vartype key_ops: list[str or ~azure.keyvault.v7_2.models.JsonWebKeyOperation]
    :ivar key_attributes: The attributes of a key managed by the key vault service.
    :vartype key_attributes: ~azure.keyvault.v7_2.models.KeyAttributes
    :ivar tags: A set of tags. Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    """

    _attribute_map = {
        'key_ops': {'key': 'key_ops', 'type': '[str]'},
        'key_attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword key_ops: Json web key operations. For more information on possible key operations, see
         JsonWebKeyOperation.
        :paramtype key_ops: list[str or ~azure.keyvault.v7_2.models.JsonWebKeyOperation]
        :keyword key_attributes: The attributes of a key managed by the key vault service.
        :paramtype key_attributes: ~azure.keyvault.v7_2.models.KeyAttributes
        :keyword tags: A set of tags. Application specific metadata in the form of key-value pairs.
        :paramtype tags: dict[str, str]
        """
        super(KeyUpdateParameters, self).__init__(**kwargs)
        self.key_ops = kwargs.get('key_ops', None)
        self.key_attributes = kwargs.get('key_attributes', None)
        self.tags = kwargs.get('tags', None)


class KeyVaultError(msrest.serialization.Model):
    """The key vault error exception.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar error: The key vault server error.
    :vartype error: ~azure.keyvault.v7_2.models.Error
    """

    _validation = {
        'error': {'readonly': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'Error'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(KeyVaultError, self).__init__(**kwargs)
        self.error = None


class KeyVerifyParameters(msrest.serialization.Model):
    """The key verify parameters.

    All required parameters must be populated in order to send to Azure.

    :ivar algorithm: Required. The signing/verification algorithm. For more information on possible
     algorithm types, see JsonWebKeySignatureAlgorithm. Possible values include: "PS256", "PS384",
     "PS512", "RS256", "RS384", "RS512", "RSNULL", "ES256", "ES384", "ES512", "ES256K".
    :vartype algorithm: str or ~azure.keyvault.v7_2.models.JsonWebKeySignatureAlgorithm
    :ivar digest: Required. The digest used for signing.
    :vartype digest: bytes
    :ivar signature: Required. The signature to be verified.
    :vartype signature: bytes
    """

    _validation = {
        'algorithm': {'required': True},
        'digest': {'required': True},
        'signature': {'required': True},
    }

    _attribute_map = {
        'algorithm': {'key': 'alg', 'type': 'str'},
        'digest': {'key': 'digest', 'type': 'base64'},
        'signature': {'key': 'value', 'type': 'base64'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword algorithm: Required. The signing/verification algorithm. For more information on
         possible algorithm types, see JsonWebKeySignatureAlgorithm. Possible values include: "PS256",
         "PS384", "PS512", "RS256", "RS384", "RS512", "RSNULL", "ES256", "ES384", "ES512", "ES256K".
        :paramtype algorithm: str or ~azure.keyvault.v7_2.models.JsonWebKeySignatureAlgorithm
        :keyword digest: Required. The digest used for signing.
        :paramtype digest: bytes
        :keyword signature: Required. The signature to be verified.
        :paramtype signature: bytes
        """
        super(KeyVerifyParameters, self).__init__(**kwargs)
        self.algorithm = kwargs['algorithm']
        self.digest = kwargs['digest']
        self.signature = kwargs['signature']


class KeyVerifyResult(msrest.serialization.Model):
    """The key verify result.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: True if the signature is verified, otherwise false.
    :vartype value: bool
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(KeyVerifyResult, self).__init__(**kwargs)
        self.value = None
