# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_get_feature_value_request(
    subscription_id: str,
    location_id: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2018-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/getFeatureValue')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "locationId": _SERIALIZER.url("location_id", location_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_get_feature_value_by_factory_request(
    subscription_id: str,
    resource_group_name: str,
    factory_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2018-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getFeatureValue')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "factoryName": _SERIALIZER.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_query_feature_values_by_factory_request(
    subscription_id: str,
    resource_group_name: str,
    factory_name: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2018-06-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/queryFeaturesValue')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "factoryName": _SERIALIZER.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )

class ExposureControlOperations(object):
    """ExposureControlOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.datafactory.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_feature_value(
        self,
        location_id: str,
        exposure_control_request: "_models.ExposureControlRequest",
        **kwargs: Any
    ) -> "_models.ExposureControlResponse":
        """Get exposure control feature for specific location.

        :param location_id: The location identifier.
        :type location_id: str
        :param exposure_control_request: The exposure control request.
        :type exposure_control_request: ~azure.mgmt.datafactory.models.ExposureControlRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ExposureControlResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(exposure_control_request, 'ExposureControlRequest')

        request = build_get_feature_value_request(
            subscription_id=self._config.subscription_id,
            location_id=location_id,
            content_type=content_type,
            json=_json,
            template_url=self.get_feature_value.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ExposureControlResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_feature_value.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/getFeatureValue'}  # type: ignore


    @distributed_trace
    def get_feature_value_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_request: "_models.ExposureControlRequest",
        **kwargs: Any
    ) -> "_models.ExposureControlResponse":
        """Get exposure control feature for specific factory.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param exposure_control_request: The exposure control request.
        :type exposure_control_request: ~azure.mgmt.datafactory.models.ExposureControlRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ExposureControlResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(exposure_control_request, 'ExposureControlRequest')

        request = build_get_feature_value_by_factory_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            content_type=content_type,
            json=_json,
            template_url=self.get_feature_value_by_factory.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ExposureControlResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_feature_value_by_factory.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getFeatureValue'}  # type: ignore


    @distributed_trace
    def query_feature_values_by_factory(
        self,
        resource_group_name: str,
        factory_name: str,
        exposure_control_batch_request: "_models.ExposureControlBatchRequest",
        **kwargs: Any
    ) -> "_models.ExposureControlBatchResponse":
        """Get list of exposure control features for specific factory.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param exposure_control_batch_request: The exposure control request for list of features.
        :type exposure_control_batch_request:
         ~azure.mgmt.datafactory.models.ExposureControlBatchRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ExposureControlBatchResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ExposureControlBatchResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ExposureControlBatchResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(exposure_control_batch_request, 'ExposureControlBatchRequest')

        request = build_query_feature_values_by_factory_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            content_type=content_type,
            json=_json,
            template_url=self.query_feature_values_by_factory.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ExposureControlBatchResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    query_feature_values_by_factory.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/queryFeaturesValue'}  # type: ignore

