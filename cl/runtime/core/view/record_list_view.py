# Copyright (C) 2003-present CompatibL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from typing import List, final

from cl.runtime.core.storage.class_data import class_field
from cl.runtime.core.view.view import View


@final
@dataclass
class RecordListView(View):
    """View that displays a list of record specified via their primary keys."""

    view_of: List[str] = class_field()
    """Primary keys of the displayed records."""
