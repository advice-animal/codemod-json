"""Check caller-facing annotations as well as runtime behavior."""

from pathlib import Path

from codemod_json import parse, parse_str
from codemod_json.base import JsonStream
from codemod_json.parser import ContainerJsonStream


def test_readme_example(tmp_path: Path) -> None:
    somepath = tmp_path / "example.json"
    somepath.write_bytes(b'{"version": ["2.7"]}')

    # Keep this block in step with the README's Python example.
    stream = parse(somepath.read_bytes())
    if stream["version"] == ["2.7"]:
        stream["version"][:] = ["3.6", "3.13"]
    somepath.write_bytes(stream.text)

    assert somepath.read_bytes() == b'{"version": ["3.6", "3.13"]}'


def test_parser_return_types() -> None:
    binary_stream: ContainerJsonStream = parse(b'{"version": 1}')
    string_stream: ContainerJsonStream = parse_str('{"version": 1}')
    binary_text: bytes = binary_stream.text
    string_text: bytes = string_stream.text
    assert binary_text == string_text == b'{"version": 1}'


def test_stream_interface() -> None:
    stream: JsonStream = parse_str('{"version": 1}')
    stream["version"] = 2
    text: bytes = stream.text
    assert text == b'{"version": 2}'
