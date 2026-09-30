import pytest

from solutions.problem_15_org_chart_queries import OrgChart


@pytest.fixture
def org():
    return OrgChart(
        {
            "ceo": ["cto", "cfo"],
            "cto": ["eng1", "eng2"],
            "cfo": ["acct1"],
            "eng1": ["intern"],
        },
        ceo="ceo",
    )


def test_common_manager_same_branch(org):
    assert org.closest_common_manager("intern", "eng2") == "cto"


def test_common_manager_across_branches(org):
    assert org.closest_common_manager("intern", "acct1") == "ceo"


def test_common_manager_when_one_manages_other(org):
    assert org.closest_common_manager("cto", "intern") == "cto"
    assert org.closest_common_manager("intern", "cto") == "cto"


def test_common_manager_with_self(org):
    assert org.closest_common_manager("eng2", "eng2") == "eng2"


def test_chain_of_command(org):
    assert org.chain_of_command("intern") == ["ceo", "cto", "eng1", "intern"]
    assert org.chain_of_command("ceo") == ["ceo"]


def test_team_size(org):
    assert org.team_size("ceo") == 6
    assert org.team_size("cto") == 3
    assert org.team_size("eng2") == 0


def test_unknown_employee_raises(org):
    with pytest.raises(KeyError):
        org.team_size("nobody")
    with pytest.raises(KeyError):
        org.chain_of_command("nobody")
    with pytest.raises(KeyError):
        org.closest_common_manager("nobody", "ceo")


def test_deep_org_does_not_hit_recursion_limit():
    n = 5000
    reports = {f"e{i}": [f"e{i + 1}"] for i in range(n - 1)}
    reports["e2000"].append("side")
    org = OrgChart(reports, ceo="e0")
    assert org.team_size("e0") == n
    assert org.closest_common_manager(f"e{n - 1}", "side") == "e2000"
    assert len(org.chain_of_command(f"e{n - 1}")) == n
