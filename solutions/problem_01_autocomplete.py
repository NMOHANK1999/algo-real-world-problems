"""01. Autocomplete Engine — see problems/01_autocomplete_engine.md"""

from __future__ import annotations

class Node:
    def __init__(self):
        self.fullNode = [None] * 26
        self.end = False
        self.score = 0


class AutocompleteSystem:
    def __repr__(self):
        raise NotImplementedError
    
    def __init__(self) -> None:
        self.char_reg = ""
        self.root = Node()

    def insert(self, word: str, freq: int) -> None:
        start = self.root
        for let in word:
            ind = ord(let) - ord("a")
            if not start.fullNode[ind]:
                start.fullNode[ind] = Node()
            start = start.fullNode[ind]
        start.end = True
        start.score = freq

    def search(self, prefix: str, k: int) -> list[str]:
        start = self.root
        for let in prefix:
            ind = ord(let) - ord("a")
            if not start.fullNode[ind]:
                return []
            start = start.fullNode[ind]
        ans = []
        def dfs(letter, rest):
            if letter.end:
                ans.append([letter.score, prefix + rest])
            for index, child in enumerate(letter.fullNode):
                if child:
                    dfs(child, rest + chr(ord('a') + index))

        dfs(start, "")

        ans.sort(key = lambda x: -x[0])
        return [word for score, word in ans[:k]]


    def type_char(self, c: str) -> list[str]:
        self.char_reg += c
        return self.search(self.char_reg, 5)
        

    def reset_query(self) -> None:
        self.char_reg = ""

ac = AutocompleteSystem()
ac.insert("cat", 5)
ac.insert("car", 5)
ac.insert("care", 3)
ac.insert("dog", 10)

print(ac.search("ca", 2))   # -> ["car", "cat"]   (freq tie -> lexicographic)
print(ac.search("care", 5)) # -> ["care"]
print(ac.search("z", 5))    # -> []

print(ac.type_char("c"))    # -> results for "c"
print(ac.type_char("a"))    # -> results for "ca"
ac.reset_query()
print(ac.type_char("d"))    # -> results for "d" -> ["dog"]
