# codemod-json

This library makes surgical edits to JSON documents, based on tree-sitter and
inspired by tomlkit and pyupgrade.  Preserves _all_ whitespace and formatting
on lines that don't require changes, and generally within a line as well, so
you can make minimal diffs in your codemod tools.

# Basic Usage

```json
{
    // some comment
    "version": ["foo"],
    "commands": [], // another comment
}
```

```py
from codemod_json import parse
stream = parse(somepath.read_bytes())
if stream["version"] == ["2.7"]:
    stream["version"][:] = ["3.6", "3.13"]
somepath.write_bytes(stream.text)
```

```json
{
    // some comment
    "version": ["3.6", "3.13"],
    "commands": [], // another comment
}
```

# Type Checking

`parse(bytes)` and `parse_str(str)` return a `ContainerJsonStream`. Its `.text`
property returns UTF-8 `bytes` with pending edits applied, ready to pass to
`Path.write_bytes`. The `JsonStream` base interface also declares `.text`.

Run `make lint` after installing `.[dev,test]` to check the package with strict
mypy and ty. Both also check `tests/test_typing.py`, which exercises the README
example as caller code: checking only the implementation would not catch a
missing attribute on a parser's declared return type.

# Version Compat

Usage of this library should work back to 3.9 (because of the tree-sitter dep),
but development (and mypy compatibility) only on 3.10-3.12.  Linting requires
3.12+ for full fidelity.

# Versioning

This library follows [meanver](https://meanver.org/) which basically means
[semver](https://semver.org/) along with a promise to rename when the major
version changes.

# License

codemod-json is copyright [Tim Hatch](https://timhatch.com/), and licensed under
the MIT license.  See the `LICENSE` file for details.
