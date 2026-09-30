from solutions.problem_19_account_merger import merge_accounts


def test_example():
    accounts = [
        ("John", ["john@work.com", "john_home@mail.com"]),
        ("John", ["john@work.com", "j.smith@corp.com"]),
        ("Mary", ["mary@mail.com"]),
        ("John", ["johnny@other.com"]),
    ]
    assert merge_accounts(accounts) == [
        ("John", ["j.smith@corp.com", "john@work.com", "john_home@mail.com"]),
        ("John", ["johnny@other.com"]),
        ("Mary", ["mary@mail.com"]),
    ]


def test_transitive_merge_through_chain():
    accounts = [
        ("Ann", ["a@x.com", "b@x.com"]),
        ("Ann", ["c@x.com", "d@x.com"]),
        ("Ann", ["b@x.com", "c@x.com"]),
    ]
    assert merge_accounts(accounts) == [
        ("Ann", ["a@x.com", "b@x.com", "c@x.com", "d@x.com"]),
    ]


def test_same_name_different_people():
    accounts = [("Sam", ["s1@x.com"]), ("Sam", ["s2@x.com"])]
    assert merge_accounts(accounts) == [("Sam", ["s1@x.com"]), ("Sam", ["s2@x.com"])]


def test_duplicate_email_within_account():
    assert merge_accounts([("Bo", ["b@x.com", "b@x.com"])]) == [("Bo", ["b@x.com"])]


def test_empty():
    assert merge_accounts([]) == []


def test_large_chain():
    n = 20_000
    accounts = [("Z", [f"e{i}@x.com", f"e{i + 1}@x.com"]) for i in range(n)]
    result = merge_accounts(accounts)
    assert len(result) == 1
    assert len(result[0][1]) == n + 1
