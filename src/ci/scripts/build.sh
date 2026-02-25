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
    # "test" or "release"
    local -r config="${1}"
    local -r platform="${2}"
    # shellcheck disable=SC2034
    local -r arch="${3}"

    mkdir -p build

    case "${platform}" in
        linux)
            prefix="lib"
            ext="so"

            # bzip2-rs leaks symbols
            # https://github.com/trifectatechfoundation/bzip2-rs/issues/81
            mkdir -p "$(pwd)/exarrow-rs/.cargo/"
            cp ./cargo-config.toml "$(pwd)/exarrow-rs/.cargo/config.toml"
            cp ./intercept-version-script.sh "$(pwd)/exarrow-rs/"
            ;;
        macos)
            prefix="lib"
            ext="dylib"
            ;;
        windows)
            prefix=""
            ext="dll"
            ;;
    esac

    pushd "$(pwd)/exarrow-rs"
    if [[ "${config}" == "release" ]]; then
        cargo build --locked --release -Fffi
        cp "target/release/${prefix}exarrow_rs.${ext}" "../build/libadbc_driver_exasol.${ext}"
    else
        cargo build --locked -Fffi
        cp "target/debug/${prefix}exarrow_rs.${ext}" "../build/libadbc_driver_exasol.${ext}"
    fi
}

main "$@"
