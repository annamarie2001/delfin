# Copyright 2020 The SODA Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import copy

from delfin.common import constants


def build_storages(storages):
    # Build list of storages
    views = [build_storage(storage)
             for storage in storages]
    return dict(storages=views)


def build_storage(storage):
    view = copy.deepcopy(storage)
    if view['sync_status'] == constants.SyncStatus.SYNCED:
        view['sync_status'] = 'SYNCED'
    else:
        view['sync_status'] = 'SYNCING'
    return dict(view)


def build_capabilities(storage_info, capabilities):
    """build capability API response"""
    # build metadata
    metadata = dict()
    metadata['vendor'] = storage_info['vendor']
    metadata['model'] = storage_info['model']

    # create final view
    view = dict()
    view['metadata'] = metadata
    view['spec'] = capabilities
    return view
