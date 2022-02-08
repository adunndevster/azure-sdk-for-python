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
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._component_current_pricing_plan_operations import build_create_and_update_request, build_get_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ComponentCurrentPricingPlanOperations:
    """ComponentCurrentPricingPlanOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.applicationinsights.v2017_10_01.models
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
    async def get(
        self,
        resource_group_name: str,
        resource_name: str,
        **kwargs: Any
    ) -> "_models.ApplicationInsightsComponentPricingPlan":
        """Returns the current pricing plan setting for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentPricingPlan, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2017_10_01.models.ApplicationInsightsComponentPricingPlan
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationInsightsComponentPricingPlan"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationInsightsComponentPricingPlan', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/pricingPlans/current'}  # type: ignore


    @distributed_trace_async
    async def create_and_update(
        self,
        resource_group_name: str,
        resource_name: str,
        pricing_plan_properties: "_models.ApplicationInsightsComponentPricingPlan",
        **kwargs: Any
    ) -> "_models.ApplicationInsightsComponentPricingPlan":
        """Replace current pricing plan for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param pricing_plan_properties: Properties that need to be specified to update current pricing
         plan for an Application Insights component.
        :type pricing_plan_properties:
         ~azure.mgmt.applicationinsights.v2017_10_01.models.ApplicationInsightsComponentPricingPlan
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentPricingPlan, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2017_10_01.models.ApplicationInsightsComponentPricingPlan
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationInsightsComponentPricingPlan"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(pricing_plan_properties, 'ApplicationInsightsComponentPricingPlan')

        request = build_create_and_update_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            content_type=content_type,
            json=_json,
            template_url=self.create_and_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationInsightsComponentPricingPlan', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_and_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/pricingPlans/current'}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        resource_name: str,
        pricing_plan_properties: "_models.ApplicationInsightsComponentPricingPlan",
        **kwargs: Any
    ) -> "_models.ApplicationInsightsComponentPricingPlan":
        """Update current pricing plan for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource.
        :type resource_name: str
        :param pricing_plan_properties: Properties that need to be specified to update current pricing
         plan for an Application Insights component.
        :type pricing_plan_properties:
         ~azure.mgmt.applicationinsights.v2017_10_01.models.ApplicationInsightsComponentPricingPlan
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentPricingPlan, or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2017_10_01.models.ApplicationInsightsComponentPricingPlan
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ApplicationInsightsComponentPricingPlan"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(pricing_plan_properties, 'ApplicationInsightsComponentPricingPlan')

        request = build_update_request(
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            resource_name=resource_name,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApplicationInsightsComponentPricingPlan', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/pricingPlans/current'}  # type: ignore

