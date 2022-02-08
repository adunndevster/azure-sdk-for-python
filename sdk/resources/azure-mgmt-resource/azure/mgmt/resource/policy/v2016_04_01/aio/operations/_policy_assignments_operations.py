# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._policy_assignments_operations import build_create_by_id_request, build_create_request, build_delete_by_id_request, build_delete_request, build_get_by_id_request, build_get_request, build_list_for_resource_group_request, build_list_for_resource_request, build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PolicyAssignmentsOperations:
    """PolicyAssignmentsOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.policy.v2016_04_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def delete(
        self,
        scope: str,
        policy_assignment_name: str,
        **kwargs: Any
    ) -> "_models.PolicyAssignment":
        """Deletes a policy assignment.

        :param scope: The scope of the policy assignment.
        :type scope: str
        :param policy_assignment_name: The name of the policy assignment to delete.
        :type policy_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            scope=scope,
            policy_assignment_name=policy_assignment_name,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    delete.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyassignments/{policyAssignmentName}'}  # type: ignore


    @distributed_trace_async
    async def create(
        self,
        scope: str,
        policy_assignment_name: str,
        parameters: "_models.PolicyAssignment",
        **kwargs: Any
    ) -> "_models.PolicyAssignment":
        """Creates a policy assignment.

        Policy assignments are inherited by child resources. For example, when you apply a policy to a
        resource group that policy is assigned to all resources in the group.

        :param scope: The scope of the policy assignment.
        :type scope: str
        :param policy_assignment_name: The name of the policy assignment.
        :type policy_assignment_name: str
        :param parameters: Parameters for the policy assignment.
        :type parameters: ~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignment
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'PolicyAssignment')

        request = build_create_request(
            scope=scope,
            policy_assignment_name=policy_assignment_name,
            content_type=content_type,
            json=_json,
            template_url=self.create.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyassignments/{policyAssignmentName}'}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        scope: str,
        policy_assignment_name: str,
        **kwargs: Any
    ) -> "_models.PolicyAssignment":
        """Gets a policy assignment.

        :param scope: The scope of the policy assignment.
        :type scope: str
        :param policy_assignment_name: The name of the policy assignment to get.
        :type policy_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            scope=scope,
            policy_assignment_name=policy_assignment_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/{scope}/providers/Microsoft.Authorization/policyassignments/{policyAssignmentName}'}  # type: ignore


    @distributed_trace
    def list_for_resource_group(
        self,
        resource_group_name: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicyAssignmentListResult"]:
        """Gets policy assignments for the resource group.

        :param resource_group_name: The name of the resource group that contains policy assignments.
        :type resource_group_name: str
        :param filter: The filter to apply on the operation.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyAssignmentListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignmentListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyAssignmentListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_for_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    template_url=self.list_for_resource_group.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_for_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyAssignmentListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_for_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/policyAssignments'}  # type: ignore

    @distributed_trace
    def list_for_resource(
        self,
        resource_group_name: str,
        resource_provider_namespace: str,
        parent_resource_path: str,
        resource_type: str,
        resource_name: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicyAssignmentListResult"]:
        """Gets policy assignments for a resource.

        :param resource_group_name: The name of the resource group containing the resource. The name is
         case insensitive.
        :type resource_group_name: str
        :param resource_provider_namespace: The namespace of the resource provider.
        :type resource_provider_namespace: str
        :param parent_resource_path: The parent resource path.
        :type parent_resource_path: str
        :param resource_type: The resource type.
        :type resource_type: str
        :param resource_name: The name of the resource with policy assignments.
        :type resource_name: str
        :param filter: The filter to apply on the operation.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyAssignmentListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignmentListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyAssignmentListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_for_resource_request(
                    resource_group_name=resource_group_name,
                    resource_provider_namespace=resource_provider_namespace,
                    parent_resource_path=parent_resource_path,
                    resource_type=resource_type,
                    resource_name=resource_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    template_url=self.list_for_resource.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_for_resource_request(
                    resource_group_name=resource_group_name,
                    resource_provider_namespace=resource_provider_namespace,
                    parent_resource_path=parent_resource_path,
                    resource_type=resource_type,
                    resource_name=resource_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyAssignmentListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_for_resource.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/policyassignments'}  # type: ignore

    @distributed_trace
    def list(
        self,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PolicyAssignmentListResult"]:
        """Gets all the policy assignments for a subscription.

        :param filter: The filter to apply on the operation.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PolicyAssignmentListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignmentListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyAssignmentListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("PolicyAssignmentListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policyassignments'}  # type: ignore

    @distributed_trace_async
    async def delete_by_id(
        self,
        policy_assignment_id: str,
        **kwargs: Any
    ) -> "_models.PolicyAssignment":
        """Deletes a policy assignment by ID.

        When providing a scope for the assignment, use '/subscriptions/{subscription-id}/' for
        subscriptions, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for
        resource groups, and
        '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}'
        for resources.

        :param policy_assignment_id: The ID of the policy assignment to delete. Use the format
         '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
        :type policy_assignment_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_by_id_request(
            policy_assignment_id=policy_assignment_id,
            template_url=self.delete_by_id.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    delete_by_id.metadata = {'url': '/{policyAssignmentId}'}  # type: ignore


    @distributed_trace_async
    async def create_by_id(
        self,
        policy_assignment_id: str,
        parameters: "_models.PolicyAssignment",
        **kwargs: Any
    ) -> "_models.PolicyAssignment":
        """Creates a policy assignment by ID.

        Policy assignments are inherited by child resources. For example, when you apply a policy to a
        resource group that policy is assigned to all resources in the group. When providing a scope
        for the assignment, use '/subscriptions/{subscription-id}/' for subscriptions,
        '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for resource groups,
        and
        '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}'
        for resources.

        :param policy_assignment_id: The ID of the policy assignment to create. Use the format
         '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
        :type policy_assignment_id: str
        :param parameters: Parameters for policy assignment.
        :type parameters: ~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignment
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'PolicyAssignment')

        request = build_create_by_id_request(
            policy_assignment_id=policy_assignment_id,
            content_type=content_type,
            json=_json,
            template_url=self.create_by_id.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_by_id.metadata = {'url': '/{policyAssignmentId}'}  # type: ignore


    @distributed_trace_async
    async def get_by_id(
        self,
        policy_assignment_id: str,
        **kwargs: Any
    ) -> "_models.PolicyAssignment":
        """Gets a policy assignment by ID.

        When providing a scope for the assignment, use '/subscriptions/{subscription-id}/' for
        subscriptions, '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}' for
        resource groups, and
        '/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider-namespace}/{resource-type}/{resource-name}'
        for resources.

        :param policy_assignment_id: The ID of the policy assignment to get. Use the format
         '/{scope}/providers/Microsoft.Authorization/policyAssignments/{policy-assignment-name}'.
        :type policy_assignment_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PolicyAssignment, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2016_04_01.models.PolicyAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PolicyAssignment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_by_id_request(
            policy_assignment_id=policy_assignment_id,
            template_url=self.get_by_id.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('PolicyAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_id.metadata = {'url': '/{policyAssignmentId}'}  # type: ignore

