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

from bk_audit.log.models import AuditInstance
from django.db import models
from django.utils.translation import gettext_lazy

from core.models import SoftDeleteModel


class VisionPanel(SoftDeleteModel):
    """
    仪表盘
    """

    id = models.CharField(gettext_lazy("ID"), primary_key=True, max_length=255)
    name = models.CharField(gettext_lazy("Name"), max_length=255)
    priority_index = models.IntegerField(gettext_lazy("优先指数"), default=0)

    class Meta:
        verbose_name = gettext_lazy("仪表盘")
        verbose_name_plural = verbose_name
        ordering = ["-priority_index", "name"]


class VisionPanelInstance:
    def __init__(self, panel: VisionPanel):
        self.instance_id = panel.id
        self.instance_name = panel.name

    @property
    def instance(self):
        return AuditInstance(self)
