# Copyright 2022 The DLRover Authors. All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dlrover.python.common.constants import EngineType
from dlrover.python.master.scaler.elasticjob_scaler import ElasticJobScaler
from dlrover.python.master.scaler.pod_scaler import PodScaler


def new_job_scaler(engine, job_name, namespace):
    if engine == EngineType.ELASTICJOB:
        return ElasticJobScaler(job_name, namespace)
    elif engine == EngineType.PY_ELASTICJOB:
        return PodScaler(job_name, namespace)