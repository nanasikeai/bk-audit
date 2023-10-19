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

from bk_resource import Resource
from django.utils.translation import gettext_lazy

from apps.feature.handlers import FeatureHandler
from apps.feature.serializers import FeatureToggleRequestSerializer


class FeatureToggle(Resource):
    name = gettext_lazy("特性开关")
    tags = ["Feature"]
    RequestSerializer = FeatureToggleRequestSerializer

    def perform_request(self, validated_request_data):
        handler = FeatureHandler(validated_request_data["feature_id"])
        return {"enabled": handler.feature.is_enable_view if handler.check() else False}
