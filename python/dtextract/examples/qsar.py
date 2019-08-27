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
    runCsv(QSAR_PATH, QSAR_HAS_HEADER, QSAR_DATA_TYPES, QSAR_IS_CLASSIFY, QSAR_DELIM_WHITESPACE, QSAR_OUTPUT)
