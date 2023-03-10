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

from enum import IntFlag


class LoadOptions(IntFlag):
    """Optional flags for data source load methods."""

    None_ = 0
    """Indicates default options."""

    IgnoreNotFound = 1
    """Return None instead of an error message if the record is not found."""

    IgnoreNullKey = 2
    """
    Return None instead of error message if key=None is passed as argument.

    This option can be used to simplify the code for loading a record
    from a key stored as an optional attribute.
    """
