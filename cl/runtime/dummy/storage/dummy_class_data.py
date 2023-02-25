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

from __future__ import annotations

from dataclasses import dataclass

import cl.runtime as rt


@dataclass
class DummyClassData(rt.ClassData):
    """Dataclass-based serializable data sample used in tests."""

    base_record_field_str: str = rt.class_field()
    """String attribute of base class."""

    base_record_field_float: float = rt.class_field()
    """Float attribute of base class."""

    @staticmethod
    def create() -> DummyClassData:
        """Return an instance of this class populated with sample data."""

        obj = DummyClassData()
        obj.base_record_field_str = 'def'
        obj.base_record_field_float = 4.56
        return obj