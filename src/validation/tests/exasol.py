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

import functools
from pathlib import Path

from adbc_drivers_validation import model, quirks


class Exasol2025Quirks(model.DriverQuirks):
    name = "exasol"
    driver = "adbc_driver_exasol"
    driver_name = "exarrow-rs"
    vendor_name = "Exasol"
    vendor_version = ""
    short_version = "2025"
    features = model.DriverFeatures(
        statement_prepare=True,
        statement_rows_affected=True,
        statement_rows_affected_ddl=True,
        current_schema="ADBC_TEST",
    )
    setup = model.DriverSetup(
        database={
            "uri": model.FromEnv("EXASOL_URI"),
        },
        connection={},
        statement={},
    )

    @property
    def queries_paths(self) -> tuple[Path]:
        return (Path(__file__).parent.parent / "queries",)

    def bind_parameter(self, index: int) -> str:
        return "?"

    def is_table_not_found(self, table_name: str, error: Exception) -> bool:
        raise error

    def split_statement(self, statement: str) -> list[str]:
        return quirks.split_statement(statement, dialect="exasol")


@functools.cache
def get_quirks(version: str) -> model.DriverQuirks:
    if version == "2025":
        return Exasol2025Quirks()
    else:
        raise ValueError(f"unsupported Exasol version: {version}")
