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
from typing import Optional, Union

import cl.runtime as rt


@dataclass
class FieldDecl(rt.ClassData):
    """Base class of type declaration in schema."""

    name: Optional[str] = None
    """Field name in code and storage."""

    label: Optional[str] = None
    """Readable field label in the front end."""

    type: Optional[Union[str, rt.TypeDeclKey]] = None
    """Field type."""

    dim: Optional[int] = None
    """List, array, or tensor dimension (defaults to scalar, i.e., the value of zero, if not specified)."""

    optional: Optional[bool] = None
    """True if field is optional (defaults to required if not specified)."""

    contains_optional: Optional[bool] = None
    """True if list, array, or tensor elements are optional (defaults to required if not specified)."""
