# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
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

def build_create_or_update_request(
    subscription_id: str,
    resource_group_name: str,
    template_spec_name: str,
    template_spec_version: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-05-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "templateSpecName": _SERIALIZER.url("template_spec_name", template_spec_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "templateSpecVersion": _SERIALIZER.url("template_spec_version", template_spec_version, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
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
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_update_request(
    subscription_id: str,
    resource_group_name: str,
    template_spec_name: str,
    template_spec_version: str,
    *,
    json: JSONType = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-05-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "templateSpecName": _SERIALIZER.url("template_spec_name", template_spec_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "templateSpecVersion": _SERIALIZER.url("template_spec_version", template_spec_version, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
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
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        json=json,
        content=content,
        **kwargs
    )


def build_get_request(
    subscription_id: str,
    resource_group_name: str,
    template_spec_name: str,
    template_spec_version: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-05-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "templateSpecName": _SERIALIZER.url("template_spec_name", template_spec_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "templateSpecVersion": _SERIALIZER.url("template_spec_version", template_spec_version, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_request(
    subscription_id: str,
    resource_group_name: str,
    template_spec_name: str,
    template_spec_version: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-05-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "templateSpecName": _SERIALIZER.url("template_spec_name", template_spec_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "templateSpecVersion": _SERIALIZER.url("template_spec_version", template_spec_version, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    subscription_id: str,
    resource_group_name: str,
    template_spec_name: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2021-05-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions')
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
        "templateSpecName": _SERIALIZER.url("template_spec_name", template_spec_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class TemplateSpecVersionsOperations(object):
    """TemplateSpecVersionsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.templatespecs.v2021_05_01.models
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
    def create_or_update(
        self,
        resource_group_name: str,
        template_spec_name: str,
        template_spec_version: str,
        template_spec_version_model: "_models.TemplateSpecVersion",
        **kwargs: Any
    ) -> "_models.TemplateSpecVersion":
        """Creates or updates a Template Spec version.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param template_spec_version: The version of the Template Spec.
        :type template_spec_version: str
        :param template_spec_version_model: Template Spec Version supplied to the operation.
        :type template_spec_version_model:
         ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersion
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TemplateSpecVersion, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersion
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpecVersion"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(template_spec_version_model, 'TemplateSpecVersion')

        request = build_create_or_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            template_spec_version=template_spec_version,
            content_type=content_type,
            json=_json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('TemplateSpecVersion', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('TemplateSpecVersion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}'}  # type: ignore


    @distributed_trace
    def update(
        self,
        resource_group_name: str,
        template_spec_name: str,
        template_spec_version: str,
        template_spec_version_update_model: Optional["_models.TemplateSpecVersionUpdateModel"] = None,
        **kwargs: Any
    ) -> "_models.TemplateSpecVersion":
        """Updates Template Spec Version tags with specified values.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param template_spec_version: The version of the Template Spec.
        :type template_spec_version: str
        :param template_spec_version_update_model: Template Spec Version resource with the tags to be
         updated.
        :type template_spec_version_update_model:
         ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersionUpdateModel
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TemplateSpecVersion, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersion
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpecVersion"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if template_spec_version_update_model is not None:
            _json = self._serialize.body(template_spec_version_update_model, 'TemplateSpecVersionUpdateModel')
        else:
            _json = None

        request = build_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            template_spec_version=template_spec_version,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TemplateSpecVersion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}'}  # type: ignore


    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        template_spec_name: str,
        template_spec_version: str,
        **kwargs: Any
    ) -> "_models.TemplateSpecVersion":
        """Gets a Template Spec version from a specific Template Spec.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param template_spec_version: The version of the Template Spec.
        :type template_spec_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TemplateSpecVersion, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersion
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpecVersion"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            template_spec_version=template_spec_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TemplateSpecVersion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        resource_group_name: str,
        template_spec_name: str,
        template_spec_version: str,
        **kwargs: Any
    ) -> None:
        """Deletes a specific version from a Template Spec. When operation completes, status code 200
        returned without content.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :param template_spec_version: The version of the Template Spec.
        :type template_spec_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            template_spec_name=template_spec_name,
            template_spec_version=template_spec_version,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions/{templateSpecVersion}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        template_spec_name: str,
        **kwargs: Any
    ) -> Iterable["_models.TemplateSpecVersionsListResult"]:
        """Lists all the Template Spec versions in the specified Template Spec.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param template_spec_name: Name of the Template Spec.
        :type template_spec_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TemplateSpecVersionsListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.resource.templatespecs.v2021_05_01.models.TemplateSpecVersionsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TemplateSpecVersionsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    template_spec_name=template_spec_name,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    template_spec_name=template_spec_name,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("TemplateSpecVersionsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.TemplateSpecsError, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Resources/templateSpecs/{templateSpecName}/versions'}  # type: ignore
