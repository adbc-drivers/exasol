<!--
  Copyright (c) 2026 ADBC Drivers Contributors

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->

# How to Contribute

All contributors are expected to follow the [Code of
Conduct](https://github.com/adbc-drivers/exasol?tab=coc-ov-file#readme).

## Reporting Issues and Making Feature Requests

Please file issues and feature requests on the GitHub issue tracker:
https://github.com/adbc-drivers/exasol/issues

Potential security vulnerabilities should be reported to
[security@adbc-drivers.org](mailto:security@adbc-drivers.org) instead.  See
the [Security
Policy](https://github.com/adbc-drivers/exasol?tab=security-ov-file#readme).

## Build and Test

Most likely, you want to contribute to the upstream driver at
https://github.com/exasol-labs/exarrow-rs.  This repository only holds
build and test scripts for the ADBC Driver Foundry.

You can invoke the build script used by CI:

```shell
$ cd src/
# ./ci/scripts/build.sh <test|release> <linux|macos|windows> <amd64|arm64>
# For example, this makes a debug build:
$ ./ci/scripts/build.sh test linux amd64
```

This will produce a shared library in `src/build`.

To run the validation suite, you will first need to build the shared library.
You will also need to set up a Exasol instance (see [the validation
README](./src/validation/README.md)).  Finally, from the `src/` subdirectory:

```shell
$ pixi run validate
```

This will produce a test report, which can be rendered into a documentation
page (using MyST Markdown):

```shell
$ pixi run gendocs --output generated/
```

Then look at `./generated/exasol.md`.

## Opening a Pull Request

Before opening a pull request:

- Review your changes and make sure no stray files, etc. are included.
- Ensure the Apache license header is at the top of all files.
- Check if there is an existing issue.  If not, please file one, unless the
  change is trivial.
- Assign the issue to yourself by commenting just the word `take`.
- Run the static checks by installing [pre-commit](https://pre-commit.com/),
  then running `pre-commit run --all-files` from inside the repository.  Make
  sure all your changes are staged/committed (unstaged changes will be
  ignored).

When writing the pull request description:

- Ensure the title follows [Conventional
  Commits](https://www.conventionalcommits.org/en/v1.0.0/) format.  The
  component generally be omitted.  Example titles:

  - `feat: support GEOGRAPHY data type`
  - `chore: update action versions`
  - `fix!: return us instead of ms`

  Ensure that breaking changes are appropriately flagged with a `!` as seen
  in the last example above.
- Make sure the description ends with `Closes #NNN`, `Fixes #NNN`, or
  similar, so that the issue will be linked to your pull request.
