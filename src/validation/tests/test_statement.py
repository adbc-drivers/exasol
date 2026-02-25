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

import adbc_drivers_validation.tests.statement
import pyarrow

from . import exasol


def pytest_generate_tests(metafunc) -> None:
    quirks = [exasol.get_quirks(metafunc.config.getoption("vendor_version"))]
    return adbc_drivers_validation.tests.statement.generate_tests(quirks, metafunc)


class TestStatement(adbc_drivers_validation.tests.statement.TestStatement):
    def test_parameter_schema(self, driver, conn) -> None:
        # Override the base test since MSSQL can't infer parameter types in
        # some cases and doesn't fall back to a default
        with conn.cursor() as cursor:
            cursor.adbc_statement.set_sql_query(
                f"SELECT 1 + {driver.bind_parameter(1)}"
            )
            cursor.adbc_statement.prepare()
            handle = cursor.adbc_statement.get_parameter_schema()
            schema = pyarrow.Schema._import_from_c(handle.address)
            assert schema == pyarrow.schema(
                [
                    ("@p1", pyarrow.int32()),
                ]
            )
