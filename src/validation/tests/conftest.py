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

import sys
import typing
from pathlib import Path

import adbc_driver_manager.dbapi
import adbc_drivers_validation.model
import adbc_drivers_validation.tests.conftest
import pytest
from adbc_drivers_validation.tests.conftest import (  # noqa: F401
    conn,
    conn_factory,
    manual_test,
    pytest_collection_modifyitems,
)

from . import exasol


def pytest_addoption(parser):
    adbc_drivers_validation.tests.conftest.pytest_addoption(parser)
    parser.addoption("--vendor-version", action="store", default="2025")


@pytest.fixture(scope="session")
def driver(request, pytestconfig) -> adbc_drivers_validation.model.DriverQuirks:
    driver = request.param
    assert driver.startswith("exasol")
    return exasol.get_quirks(pytestconfig.getoption("vendor_version"))


@pytest.fixture(scope="session")
def driver_path(driver: adbc_drivers_validation.model.DriverQuirks) -> str:
    ext = {
        "win32": "dll",
        "darwin": "dylib",
    }.get(sys.platform, "so")
    return str(
        Path(__file__).parent.parent.parent
        / f"build/libadbc_driver_{driver.name}.{ext}"
    )


@pytest.fixture(scope="session", autouse=True)
def _setup_resources(
    driver: adbc_drivers_validation.model.DriverQuirks,
    conn_factory: typing.Callable[[], adbc_driver_manager.dbapi.Connection],  # noqa: F811
) -> None:
    with conn_factory() as conn:  # noqa:F811
        with conn.cursor() as cursor:
            statements = [
                # f"CREATE SCHEMA {driver.features.secondary_schema}",
                # f"CREATE DATABASE {driver.features.secondary_catalog}",
                # f"USE {driver.features.secondary_catalog}",
                # f"CREATE SCHEMA {driver.features.secondary_catalog_schema}",
            ]

            for statement in statements:
                try:
                    cursor.adbc_statement.set_sql_query(statement)
                    cursor.adbc_statement.execute_update()
                except adbc_driver_manager.dbapi.ProgrammingError as e:
                    if "There is already an object named" in str(
                        e
                    ) or "already exists" in str(e):
                        continue
                    raise RuntimeError(statement) from e
