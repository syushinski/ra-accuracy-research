# Copyright 2015-2016 Stanford University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Main code

from runCsv import *
from ..data.consts import *

if __name__ == "__main__":
    runCsv(OZONE_8_PATH, OZONE_8_HAS_HEADER, OZONE_8_DATA_TYPES, OZONE_8_IS_CLASSIFY, OZONE_8_DELIM_WHITESPACE, OZONE_8_OUTPUT)
    runCsv(OZONE_1_PATH, OZONE_1_HAS_HEADER, OZONE_1_DATA_TYPES, OZONE_1_IS_CLASSIFY, OZONE_1_DELIM_WHITESPACE, OZONE_1_OUTPUT)
