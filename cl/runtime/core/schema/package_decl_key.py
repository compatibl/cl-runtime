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

from cl.runtime.core.storage.class_data import class_field
from cl.runtime.core.storage.class_record import ClassRecord


@dataclass
class PackageDeclKey(ClassRecord):
    """Key for the package declaration in schema."""

    package_id: str = class_field()
    """Unique package identifier."""

    def to_pk(self) -> str:
        """Return primary key (PK) as string."""
        return f'rt.PackageDecl;{self.package_id}'
