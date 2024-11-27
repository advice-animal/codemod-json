from codemod_json import parse_str

def test_inplace_modification():
    doc = parse_str('''{
"a": "b", // c1
"c": "d" // c2
} // c3''')
    doc["c"] = "foo"
    assert doc.text.decode("utf-8") == '''{
"a": "b", // c1
"c": "foo" // c2
} // c3'''

def test_anneal_append():
    doc = parse_str('''{
"a": "b", // c1
"c": "d" // c2
} // c3''')
    doc["x"] = "foo"
    assert doc.text.decode("utf-8") == '''{
"a": "b",
"c": "d",
"x": "foo"
} // c3'''

def test_nested_object():
    doc = parse_str("{}")
    doc["x"] = "foo"
    doc["y"] = {"a": "b"}
    assert doc.text.decode("utf-8") == '''{"x": "foo","y": {"a": "b"}}'''

def test_delete_object():
    doc = parse_str('{"a": "b", "c": "d"}')
    del doc["c"]
    # TODO space after comma should go away
    assert doc.text.decode("utf-8") == '''{"a": "b" }'''
