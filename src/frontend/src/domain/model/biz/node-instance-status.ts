/*
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
*/
export default class NodeInstanceStatus {
  agent_error_count: number;
  bk_inst_id: number;
  bk_inst_name: string;
  bk_obj_id: string;
  count: number;
  labels: string[];
  node_path: string;

  constructor(payload = {} as NodeInstanceStatus) {
    this.agent_error_count = payload.agent_error_count;
    this.bk_inst_id = payload.bk_inst_id;
    this.bk_inst_name = payload.bk_inst_name;
    this.bk_obj_id = payload.bk_obj_id;
    this.count = payload.count;
    this.labels = payload.labels;
    this.node_path = payload.node_path;
  }
}
