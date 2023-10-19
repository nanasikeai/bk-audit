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

from django.utils.translation import gettext_lazy

from apps.permission.handlers.resource_types import ResourceTypeMeta


class BusinessBKLog(ResourceTypeMeta):
    system_id = "bk_cmdb"
    id = "biz"
    name = gettext_lazy("业务")
    selection_mode = "instance"
    related_instance_selections = [{"system_id": system_id, "id": "system"}]


class SpaceBKLog(ResourceTypeMeta):
    system_id = "bk_monitorv3"
    id = "space"
    name = gettext_lazy("空间")
    selection_mode = "instance"
    related_instance_selections = [{"system_id": system_id, "id": "space_list"}]
