from solutions.problem_13_service_cluster_finder import deploy_order, service_clusters

CALLS = {
    "api": ["auth", "orders"],
    "auth": ["users"],
    "users": ["auth"],
    "orders": ["billing"],
    "billing": ["ledger"],
    "ledger": ["orders"],
}


def as_frozensets(clusters):
    return sorted((frozenset(c) for c in clusters), key=sorted)


def assert_valid_deploy_order(order, calls):
    index = {}
    for i, cluster in enumerate(order):
        for svc in cluster:
            assert svc not in index, f"{svc} appears in more than one cluster"
            index[svc] = i
    for caller, callees in calls.items():
        for callee in callees:
            assert index[callee] <= index[caller], f"{callee} must deploy before {caller}"


def test_service_clusters():
    assert as_frozensets(service_clusters(CALLS)) == as_frozensets(
        [{"api"}, {"auth", "users"}, {"orders", "billing", "ledger"}]
    )


def test_target_only_and_acyclic_services_are_singletons():
    calls = {"a": ["b"], "b": ["c"]}
    assert as_frozensets(service_clusters(calls)) == as_frozensets([{"a"}, {"b"}, {"c"}])


def test_self_loop_is_single_cluster():
    assert as_frozensets(service_clusters({"a": ["a"]})) == [frozenset({"a"})]


def test_two_cycles_joined_one_way_stay_separate():
    calls = {"a": ["b"], "b": ["a", "c"], "c": ["d"], "d": ["c"]}
    assert as_frozensets(service_clusters(calls)) == as_frozensets([{"a", "b"}, {"c", "d"}])


def test_deploy_order():
    order = deploy_order(CALLS)
    assert as_frozensets(order) == as_frozensets(service_clusters(CALLS))
    assert_valid_deploy_order(order, CALLS)
    assert order[-1] == {"api"}


def test_deploy_order_chain():
    calls = {"web": ["cache"], "cache": ["db"], "db": []}
    assert deploy_order(calls) == [{"db"}, {"cache"}, {"web"}]


def test_long_cycle_does_not_hit_recursion_limit():
    n = 3000
    calls = {f"s{i}": [f"s{(i + 1) % n}"] for i in range(n)}
    clusters = service_clusters(calls)
    assert len(clusters) == 1
    assert len(clusters[0]) == n
