from solutions.problem_02_lru_cache import LRUCache


def test_basic_get_put():
    cache = LRUCache(2)
    cache.put(1, "a")
    cache.put(2, "b")
    assert cache.get(1) == "a"


def test_eviction_order():
    cache = LRUCache(2)
    cache.put(1, "a")
    cache.put(2, "b")
    cache.get(1)          # 1 is now most-recently-used
    cache.put(3, "c")     # evicts 2
    assert cache.get(2) == -1
    assert cache.get(1) == "a"
    assert cache.get(3) == "c"


def test_full_eviction_sequence():
    cache = LRUCache(2)
    cache.put(1, "a")
    cache.put(2, "b")
    cache.get(1)
    cache.put(3, "c")     # evicts 2
    cache.put(4, "d")     # evicts 1
    assert cache.get(1) == -1
    assert cache.get(3) == "c"
    assert cache.get(4) == "d"


def test_update_existing_key():
    cache = LRUCache(2)
    cache.put(1, "a")
    cache.put(1, "z")
    assert cache.get(1) == "z"
