# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云 - 审计中心 (BlueKing - Audit Center) available.
Copyright (C) 2023 THL A29 Limited,
a Tencent company. All rights reserved.
Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the
specific language governing permissions and limitations under the License.
We undertake not to change the open source license (MIT license) applicable
to the current version of the project delivered to anyone in the future.
"""

from bk_resource import api, resource
from bk_resource.viewsets import ResourceRoute, ResourceViewSet


class BizsViewSet(ResourceViewSet):
    """业务接口"""

    resource_routes = [
        ResourceRoute("GET", api.bk_log.biz_topos, endpoint="biz_topos", pk_field="bk_biz_id"),
        ResourceRoute(
            "POST", api.bk_log.get_host_instance_by_node, endpoint="host_instance_by_node", pk_field="bk_biz_id"
        ),
        ResourceRoute("POST", api.bk_log.get_host_instance_by_ip, endpoint="host_instance_by_ip", pk_field="bk_biz_id"),
        ResourceRoute("POST", api.bk_log.list_agent_status, endpoint="list_agent_status", pk_field="bk_biz_id"),
        ResourceRoute("GET", api.bk_log.get_template_topos, endpoint="template_topos", pk_field="bk_biz_id"),
        ResourceRoute("GET", api.bk_log.get_nodes_by_template, endpoint="get_nodes_by_template", pk_field="bk_biz_id"),
        ResourceRoute("GET", api.bk_log.list_bcs_clusters, endpoint="list_bcs_clusters"),
    ]


class SpacesViewSet(ResourceViewSet):
    """空间接口"""

    resource_routes = [
        ResourceRoute("GET", resource.meta.get_spaces_mine),
    ]
