# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import asyncio
import logging

from typing import Any, Union, TYPE_CHECKING, List, Optional, Dict, cast

from ..exceptions import ConnectError, EventHubError
from ..amqp import AmqpAnnotatedMessage
from ._client_base_async import ClientBaseAsync
from ._producer_async import EventHubProducer
from .._constants import ALL_PARTITIONS, MAX_MESSAGE_LENGTH_BYTES
from .._common import EventDataBatch, EventData

if TYPE_CHECKING:
    from azure.core.credentials_async import AsyncTokenCredential

SendEventTypes = List[Union[EventData, AmqpAnnotatedMessage]]

_LOGGER = logging.getLogger(__name__)


class EventHubProducerClient(ClientBaseAsync):   # pylint: disable=client-accepts-api-version-keyword
    """
    The EventHubProducerClient class defines a high level interface for
    sending events to the Azure Event Hubs service.

    :param str fully_qualified_namespace: The fully qualified host name for the Event Hubs namespace.
     This is likely to be similar to <yournamespace>.servicebus.windows.net
    :param str eventhub_name: The path of the specific Event Hub to connect the client to.
    :param credential: The credential object used for authentication which
     implements a particular interface for getting tokens. It accepts
     :class:`EventHubSharedKeyCredential<azure.eventhub.aio.EventHubSharedKeyCredential>`, or credential objects
     generated by the azure-identity library and objects that implement the `get_token(self, *scopes)` method.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential or ~azure.core.credentials.AzureSasCredential
     or ~azure.core.credentials.AzureNamedKeyCredential
    :keyword bool logging_enable: Whether to output network trace logs to the logger. Default is `False`.
    :keyword float auth_timeout: The time in seconds to wait for a token to be authorized by the service.
     The default value is 60 seconds. If set to 0, no timeout will be enforced from the client.
    :keyword str user_agent: If specified, this will be added in front of the user agent string.
    :keyword int retry_total: The total number of attempts to redo a failed operation when an error occurs. Default
     value is 3.
    :keyword float retry_backoff_factor: A backoff factor to apply between attempts after the second try
     (most errors are resolved immediately by a second try without a delay).
     In fixed mode, retry policy will always sleep for {backoff factor}.
     In 'exponential' mode, retry policy will sleep for: `{backoff factor} * (2 ** ({number of total retries} - 1))`
     seconds. If the backoff_factor is 0.1, then the retry will sleep
     for [0.0s, 0.2s, 0.4s, ...] between retries. The default value is 0.8.
    :keyword float retry_backoff_max: The maximum back off time. Default value is 120 seconds (2 minutes).
    :keyword retry_mode: The delay behavior between retry attempts. Supported values are 'fixed' or 'exponential',
     where default is 'exponential'.
    :paramtype retry_mode: str
    :keyword float idle_timeout: Timeout, in seconds, after which this client will close the underlying connection
     if there is no activity. By default the value is None, meaning that the client will not shutdown due to inactivity
     unless initiated by the service.
    :keyword transport_type: The type of transport protocol that will be used for communicating with
     the Event Hubs service. Default is `TransportType.Amqp` in which case port 5671 is used.
     If the port 5671 is unavailable/blocked in the network environment, `TransportType.AmqpOverWebsocket` could
     be used instead which uses port 443 for communication.
    :paramtype transport_type: ~azure.eventhub.TransportType
    :keyword Dict http_proxy: HTTP proxy settings. This must be a dictionary with the following
     keys: `'proxy_hostname'` (str value) and `'proxy_port'` (int value).
     Additionally the following keys may also be present: `'username', 'password'`.

    .. admonition:: Example:

        .. literalinclude:: ../samples/async_samples/sample_code_eventhub_async.py
            :start-after: [START create_eventhub_producer_client_async]
            :end-before: [END create_eventhub_producer_client_async]
            :language: python
            :dedent: 4
            :caption: Create a new instance of the EventHubProducerClient.
    """

    def __init__(
        self,
        fully_qualified_namespace: str,
        eventhub_name: str,
        credential: "CredentialTypes",
        **kwargs
    ) -> None:
        super(EventHubProducerClient, self).__init__(
            fully_qualified_namespace=fully_qualified_namespace,
            eventhub_name=eventhub_name,
            credential=credential,
            network_tracing=kwargs.pop("logging_enable", False),
            **kwargs
        )
        self._producers = {
            ALL_PARTITIONS: self._create_producer()
        }  # type: Dict[str, Optional[EventHubProducer]]
        self._lock = asyncio.Lock(
            **self._internal_kwargs
        )  # sync the creation of self._producers
        self._max_message_size_on_link = 0
        self._partition_ids = None  # Optional[List[str]]

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def _get_partitions(self) -> None:
        if not self._partition_ids:
            self._partition_ids = await self.get_partition_ids()  # type: ignore
            for p_id in cast(List[str], self._partition_ids):
                self._producers[p_id] = None

    async def _get_max_mesage_size(self) -> None:
        # pylint: disable=protected-access,line-too-long
        async with self._lock:
            if not self._max_message_size_on_link:
                await cast(
                    EventHubProducer, self._producers[ALL_PARTITIONS]
                )._open_with_retry()
                self._max_message_size_on_link = (
                    cast(  # type: ignore
                        EventHubProducer, self._producers[ALL_PARTITIONS]
                    )._handler._link.remote_max_message_size
                    or MAX_MESSAGE_LENGTH_BYTES
                )

    async def _start_producer(
        self, partition_id: str, send_timeout: Optional[Union[int, float]]
    ) -> None:
        async with self._lock:
            await self._get_partitions()
            if (
                partition_id not in cast(List[str], self._partition_ids)
                and partition_id != ALL_PARTITIONS
            ):
                raise ConnectError(
                    "Invalid partition {} for the event hub {}".format(
                        partition_id, self.eventhub_name
                    )
                )

            if (
                not self._producers[partition_id]
                or cast(EventHubProducer, self._producers[partition_id]).closed
            ):
                self._producers[partition_id] = self._create_producer(
                    partition_id=(
                        None if partition_id == ALL_PARTITIONS else partition_id
                    ),
                    send_timeout=send_timeout,
                )

    def _create_producer(
        self,
        *,
        partition_id: Optional[str] = None,
        send_timeout: Optional[Union[int, float]] = None
    ) -> EventHubProducer:
        target = "amqps://{}{}".format(self._address.hostname, self._address.path)
        send_timeout = (
            self._config.send_timeout if send_timeout is None else send_timeout
        )

        handler = EventHubProducer(
            self,
            target,
            partition=partition_id,
            send_timeout=send_timeout,
            idle_timeout=self._idle_timeout,
            **self._internal_kwargs
        )
        return handler

    @classmethod
    def from_connection_string(
        cls,
        conn_str: str,
        *,
        eventhub_name: Optional[str] = None,
        logging_enable: bool = False,
        http_proxy: Optional[Dict[str, Union[str, int]]] = None,
        auth_timeout: float = 60,
        user_agent: Optional[str] = None,
        retry_total: int = 3,
        transport_type: Optional["TransportType"] = None,
        **kwargs: Any
    ) -> "EventHubProducerClient":
        """Create an EventHubProducerClient from a connection string.

        :param str conn_str: The connection string of an Event Hub.
        :keyword str eventhub_name: The path of the specific Event Hub to connect the client to.
        :keyword bool logging_enable: Whether to output network trace logs to the logger. Default is `False`.
        :keyword Dict http_proxy: HTTP proxy settings. This must be a dictionary with the following
         keys: `'proxy_hostname'` (str value) and `'proxy_port'` (int value).
         Additionally the following keys may also be present: `'username', 'password'`.
        :keyword float auth_timeout: The time in seconds to wait for a token to be authorized by the service.
         The default value is 60 seconds. If set to 0, no timeout will be enforced from the client.
        :keyword str user_agent: If specified, this will be added in front of the user agent string.
        :keyword int retry_total: The total number of attempts to redo a failed operation when an error occurs.
         Default value is 3.
        :keyword float retry_backoff_factor: A backoff factor to apply between attempts after the second try
         (most errors are resolved immediately by a second try without a delay).
         In fixed mode, retry policy will always sleep for {backoff factor}.
         In 'exponential' mode, retry policy will sleep for: `{backoff factor} * (2 ** ({number of total retries} - 1))`
         seconds. If the backoff_factor is 0.1, then the retry will sleep
         for [0.0s, 0.2s, 0.4s, ...] between retries. The default value is 0.8.
        :keyword float retry_backoff_max: The maximum back off time. Default value is 120 seconds (2 minutes).
        :keyword retry_mode: The delay behavior between retry attempts. Supported values are 'fixed' or 'exponential',
         where default is 'exponential'.
        :paramtype retry_mode: str
        :keyword float idle_timeout: Timeout, in seconds, after which this client will close the underlying connection
         if there is no activity. By default the value is None, meaning that the client will not shutdown due to
         inactivity unless initiated by the service.
        :keyword transport_type: The type of transport protocol that will be used for communicating with
         the Event Hubs service. Default is `TransportType.Amqp` in which case port 5671 is used.
         If the port 5671 is unavailable/blocked in the network environment, `TransportType.AmqpOverWebsocket` could
         be used instead which uses port 443 for communication.
        :paramtype transport_type: ~azure.eventhub.TransportType
        :rtype: ~azure.eventhub.aio.EventHubProducerClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/async_samples/sample_code_eventhub_async.py
                :start-after: [START create_eventhub_producer_client_from_conn_str_async]
                :end-before: [END create_eventhub_producer_client_from_conn_str_async]
                :language: python
                :dedent: 4
                :caption: Create a new instance of the EventHubProducerClient from connection string.
        """
        constructor_args = cls._from_connection_string(
            conn_str,
            eventhub_name=eventhub_name,
            logging_enable=logging_enable,
            http_proxy=http_proxy,
            auth_timeout=auth_timeout,
            user_agent=user_agent,
            retry_total=retry_total,
            transport_type=transport_type,
            **kwargs
        )
        return cls(**constructor_args)

    async def send_batch(
        self,
        event_data_batch: Union[EventDataBatch, SendEventTypes],
        *,
        timeout: Optional[Union[int, float]] = None,
        **kwargs
    ) -> None:
        """Sends event data and blocks until acknowledgement is received or operation times out.

        If you're sending a finite list of `EventData` or `AmqpAnnotatedMessage` and you know it's within the event hub
        frame size limit, you can send them with a `send_batch` call. Otherwise, use :meth:`create_batch`
        to create `EventDataBatch` and add either `EventData` or `AmqpAnnotatedMessage` into the batch one by one
        until the size limit, and then call this method to send out the batch.

        :param event_data_batch: The `EventDataBatch` object to be sent or a list of `EventData` to be sent
         in a batch. All `EventData` in the list or `EventDataBatch` will land on the same partition.
        :type event_data_batch: Union[~azure.eventhub.EventDataBatch, List[Union[~azure.eventhub.EventData,
            ~azure.eventhub.amqp.AmqpAnnotatedMessage]]
        :keyword float timeout: The maximum wait time to send the event data.
         If not specified, the default wait time specified when the producer was created will be used.
        :keyword str partition_id: The specific partition ID to send to. Default is None, in which case the service
         will assign to all partitions using round-robin.
         A `TypeError` will be raised if partition_id is specified and event_data_batch is an `EventDataBatch` because
         `EventDataBatch` itself has partition_id.
        :keyword str partition_key: With the given partition_key, event data will be sent to
         a particular partition of the Event Hub decided by the service.
         A `TypeError` will be raised if partition_key is specified and event_data_batch is an `EventDataBatch` because
         `EventDataBatch` itself has partition_key.
         If both partition_id and partition_key are provided, the partition_id will take precedence.
         **WARNING: Setting partition_key of non-string value on the events to be sent is discouraged
         as the partition_key will be ignored by the Event Hub service and events will be assigned
         to all partitions using round-robin. Furthermore, there are SDKs for consuming events which expect
         partition_key to only be string type, they might fail to parse the non-string value.**
        :rtype: None
        :raises: :class:`AuthenticationError<azure.eventhub.exceptions.AuthenticationError>`
         :class:`ConnectError<azure.eventhub.exceptions.ConnectError>`
         :class:`ConnectionLostError<azure.eventhub.exceptions.ConnectionLostError>`
         :class:`EventDataError<azure.eventhub.exceptions.EventDataError>`
         :class:`EventDataSendError<azure.eventhub.exceptions.EventDataSendError>`
         :class:`EventHubError<azure.eventhub.exceptions.EventHubError>`
         :class:`ValueError`
         :class:`TypeError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/async_samples/sample_code_eventhub_async.py
                :start-after: [START eventhub_producer_client_send_async]
                :end-before: [END eventhub_producer_client_send_async]
                :language: python
                :dedent: 4
                :caption: Asynchronously sends event data

        """
        partition_id = kwargs.get("partition_id")
        partition_key = kwargs.get("partition_key")

        if isinstance(event_data_batch, EventDataBatch):
            if partition_id or partition_key:
                raise TypeError(
                    "partition_id and partition_key should be None when sending an EventDataBatch "
                    "because type EventDataBatch itself may have partition_id or partition_key"
                )
            to_send_batch = event_data_batch
        else:
            to_send_batch = await self.create_batch(
                partition_id=partition_id, partition_key=partition_key
            )
            to_send_batch._load_events(  # pylint:disable=protected-access
                event_data_batch
            )

        if len(to_send_batch) == 0:
            return

        partition_id = (
            to_send_batch._partition_id  # pylint:disable=protected-access
            or ALL_PARTITIONS
        )
        try:
            await cast(EventHubProducer, self._producers[partition_id]).send(
                to_send_batch, timeout=timeout
            )
        except (KeyError, AttributeError, EventHubError):
            await self._start_producer(partition_id, timeout)
            await cast(EventHubProducer, self._producers[partition_id]).send(
                to_send_batch, timeout=timeout
            )

    async def create_batch(
        self,
        *,
        partition_id: Optional[str] = None,
        partition_key: Optional[str] = None,
        max_size_in_bytes: Optional[int] = None
    ) -> EventDataBatch:
        """Create an EventDataBatch object with the max size of all content being constrained by max_size_in_bytes.

        The max_size_in_bytes should be no greater than the max allowed message size defined by the service.

        :param str partition_id: The specific partition ID to send to. Default is None, in which case the service
         will assign to all partitions using round-robin.
        :param str partition_key: With the given partition_key, event data will be sent to
         a particular partition of the Event Hub decided by the service.
         If both partition_id and partition_key are provided, the partition_id will take precedence.
         **WARNING: Setting partition_key of non-string value on the events to be sent is discouraged
         as the partition_key will be ignored by the Event Hub service and events will be assigned
         to all partitions using round-robin. Furthermore, there are SDKs for consuming events which expect
         partition_key to only be string type, they might fail to parse the non-string value.**
        :param int max_size_in_bytes: The maximum size of bytes data that an EventDataBatch object can hold. By
         default, the value is determined by your Event Hubs tier.
        :rtype: ~azure.eventhub.EventDataBatch

        .. admonition:: Example:

            .. literalinclude:: ../samples/async_samples/sample_code_eventhub_async.py
                :start-after: [START eventhub_producer_client_create_batch_async]
                :end-before: [END eventhub_producer_client_create_batch_async]
                :language: python
                :dedent: 4
                :caption: Create EventDataBatch object within limited size

        """
        if not self._max_message_size_on_link:
            await self._get_max_mesage_size()

        if max_size_in_bytes and max_size_in_bytes > self._max_message_size_on_link:
            raise ValueError(
                "Max message size: {} is too large, acceptable max batch size is: {} bytes.".format(
                    max_size_in_bytes, self._max_message_size_on_link
                )
            )

        event_data_batch = EventDataBatch(
            max_size_in_bytes=(max_size_in_bytes or self._max_message_size_on_link),
            partition_id=partition_id,
            partition_key=partition_key,
        )

        return event_data_batch

    async def get_eventhub_properties(self) -> Dict[str, Any]:
        """Get properties of the Event Hub.

        Keys in the returned dictionary include:

            - `eventhub_name` (str)
            - `created_at` (UTC datetime.datetime)
            - `partition_ids` (list[str])

        :rtype: Dict[str, Any]
        :raises: :class:`EventHubError<azure.eventhub.exceptions.EventHubError>`
        """
        return await super(
            EventHubProducerClient, self
        )._get_eventhub_properties_async()

    async def get_partition_ids(self) -> List[str]:
        """Get partition IDs of the Event Hub.

        :rtype: list[str]
        :raises: :class:`EventHubError<azure.eventhub.exceptions.EventHubError>`
        """
        return await super(EventHubProducerClient, self)._get_partition_ids_async()

    async def get_partition_properties(self, partition_id: str) -> Dict[str, Any]:
        """Get properties of the specified partition.

        Keys in the properties dictionary include:

            - `eventhub_name` (str)
            - `id` (str)
            - `beginning_sequence_number` (int)
            - `last_enqueued_sequence_number` (int)
            - `last_enqueued_offset` (str)
            - `last_enqueued_time_utc` (UTC datetime.datetime)
            - `is_empty` (bool)

        :param partition_id: The target partition ID.
        :type partition_id: str
        :rtype: Dict[str, Any]
        :raises: :class:`EventHubError<azure.eventhub.exceptions.EventHubError>`
        """
        return await super(
            EventHubProducerClient, self
        )._get_partition_properties_async(partition_id)

    async def close(self) -> None:
        """Close the Producer client underlying AMQP connection and links.

        :rtype: None

        .. admonition:: Example:

            .. literalinclude:: ../samples/async_samples/sample_code_eventhub_async.py
                :start-after: [START eventhub_producer_client_close_async]
                :end-before: [END eventhub_producer_client_close_async]
                :language: python
                :dedent: 4
                :caption: Close down the handler.

        """
        async with self._lock:
            for pid in self._producers:
                if self._producers[pid] is not None:
                    await self._producers[pid].close()  # type: ignore
                self._producers[pid] = None

        await super(EventHubProducerClient, self)._close_async()
