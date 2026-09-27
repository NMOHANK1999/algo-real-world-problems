"""02. LRU Cache Layer — see problems/02_lru_cache_layer.md"""

from __future__ import annotations

class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.next, self.prev = None, None
    def __repr__(self):
        return self.val

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.MRU = Node(None, None)
        self.LRU = Node(None, None)
        self.MRU.next = self.LRU

    def print_tree(self):
        start = self.MRU.next
        while start.next:
            print("{}({})-->".format(start.key, start.val))
            start = start.next
        print("DONE")

    def remove(self, key):
        # print("removing", key, " with value: ", self.cache[key])
        prev, next = self.cache[key].prev , self.cache[key].next
        prev.next = next
        next.prev = prev


    def insert(self, key):
        prev, next = self.MRU, self.MRU.next
        prev.next = next.prev = self.cache[key]
        self.cache[key].prev, self.cache[key].next = prev, next

    def get(self, key):
        if key in self.cache:
            self.remove(key)
            self.insert(key)
            return self.cache[key].val
        else:
            return -1

    def put(self, key, value) -> None:
        if key in self.cache:
            self.remove(key)
        self.cache[key] = Node(key, value)
        self.insert(key)
        if len(self.cache) > self.capacity:
            key_to_evict = self.LRU.prev.key
            print("evict ", key_to_evict) 
            self.remove(key_to_evict)
            del self.cache[key_to_evict]
            self.print_tree()


cache = LRUCache(2)
cache.put(1, "a")
cache.print_tree()
cache.put(2, "b")
cache.print_tree()
assert cache.get(1) == "a"        # -> "a"   (1 is now most-recently-used)
cache.put(3, "c")   # evicts 2 (least-recently-used)
cache.print_tree()
assert cache.get(2) == -1       # -> -1
cache.put(4, "d")   # evicts 1
cache.print_tree()
assert cache.get(1) == -1       # -> -1
assert cache.get(3) == "c"       # -> "c"
assert cache.get(4) == "d"       # -> "d"