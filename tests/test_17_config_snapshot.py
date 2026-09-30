from solutions.problem_17_config_snapshot import ConfigNode, deserialize, serialize


def roundtrip(tree):
    data = serialize(tree)
    assert isinstance(data, str)
    return deserialize(data)


def test_roundtrip_simple_tree():
    tree = ConfigNode("root", [
        ConfigNode("db", [ConfigNode("host=localhost"), ConfigNode("port=5432")]),
        ConfigNode("flags", [ConfigNode("dark_mode")]),
    ])
    assert roundtrip(tree) == tree


def test_roundtrip_none():
    assert roundtrip(None) is None


def test_roundtrip_single_node():
    assert roundtrip(ConfigNode("only")) == ConfigNode("only")


def test_keys_with_delimiter_characters():
    tricky = ["a,b", "[x]", "(y)", "3:abc", "|", "#", "", " ", "line\nbreak", "quote\"'", "\\", "🙂", "0"]
    tree = ConfigNode("root", [ConfigNode(k, [ConfigNode(k)]) for k in tricky])
    assert roundtrip(tree) == tree


def test_child_order_preserved():
    tree = ConfigNode("r", [ConfigNode("b"), ConfigNode("a"), ConfigNode("c")])
    result = roundtrip(tree)
    assert [c.key for c in result.children] == ["b", "a", "c"]


def test_structure_not_just_keys():
    # Same keys in pre-order, different shapes — must deserialize differently.
    t1 = ConfigNode("a", [ConfigNode("b", [ConfigNode("c")])])
    t2 = ConfigNode("a", [ConfigNode("b"), ConfigNode("c")])
    assert serialize(t1) != serialize(t2)
    assert roundtrip(t1) == t1
    assert roundtrip(t2) == t2


def test_wide_tree():
    tree = ConfigNode("root", [ConfigNode(f"k{i}") for i in range(5000)])
    assert roundtrip(tree) == tree
