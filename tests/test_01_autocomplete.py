from solutions.problem_01_autocomplete import AutocompleteSystem


def make_system():
    ac = AutocompleteSystem()
    ac.insert("cat", 5)
    ac.insert("car", 5)
    ac.insert("care", 3)
    ac.insert("dog", 10)
    return ac


def test_search_ranks_by_freq_then_lex():
    ac = make_system()
    assert ac.search("ca", 2) == ["car", "cat"]


def test_search_exact_match():
    ac = make_system()
    assert ac.search("care", 5) == ["care"]


def test_search_no_match():
    ac = make_system()
    assert ac.search("z", 5) == []


def test_type_char_live_typing():
    ac = make_system()
    ac.type_char("c")
    results = ac.type_char("a")
    assert set(results) >= {"car", "cat", "care"}


def test_reset_query():
    ac = make_system()
    ac.type_char("c")
    ac.reset_query()
    results = ac.type_char("d")
    assert results == ["dog"]
