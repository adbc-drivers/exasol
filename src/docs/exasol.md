---
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
{}
---

{{ cross_reference|safe }}
# Exasol Driver {{ version }}

{{ heading|safe }}

This driver provides access to [Exasol][exasol], an in-memory analytics engine.  It is developed by Exasol Labs.  The source code can be found at [exarrow-rs](https://github.com/exasol-labs/exarrow-rs); the ADBC Driver Foundry distributes precompiled binaries of the upstream sources for Linux, macOS, and Windows.

:::{note}
This page provides some ADBC-specific documentation.  For full documentation and examples, see the upstream repository: https://github.com/exasol-labs/exarrow-rs.
:::

## Installation

The Exasol driver can be installed with [dbc](https://docs.columnar.tech/dbc):

```bash
dbc install exasol
```

## Connecting

To use the driver, provide the URI of an Exasol database as the `uri` option.

```python
from adbc_driver_manager import dbapi

conn = dbapi.connect(
  driver="exasol",
  db_kwargs={
      "uri": "exasol://user:pass@localhost:8563/?tls=true&validateservercertificate=0",
  }
)
```

Full documentation for the connection string format can be found at [exarrow-rs](https://github.com/exasol-labs/exarrow-rs/blob/main/docs/connection.md).

Note: The example above is for Python using the [adbc-driver-manager](https://pypi.org/project/adbc-driver-manager) package but the process will be similar for other driver managers.  See [adbc-quickstarts](https://github.com/columnar-tech/adbc-quickstarts).

## Feature & Type Support

{{ features|safe }}

### Types

{{ types|safe }}

## Previous Versions

To see documentation for previous versions of this driver, see the following:

- [v0.6.3](./v0.6.3.md)

{{ footnotes|safe }}

[exasol]: https://www.exasol.com/
