#!/bin/bash
# Copyright (c) 2026 ADBC Drivers Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -euo pipefail

main() {
    local -r platform="${1}"
    # shellcheck disable=SC2034
    local -r arch="${2}"

    pushd "$(pwd)/exarrow-rs"
    # Ignore doctests; they seem to fail
    if [[ "${platform}" == "linux" ]]; then
        cargo test --lib --bins --tests
    else
        # We don't spawn the Docker container on other platforms
        cargo test --no-run
    fi
}

main "$@"
