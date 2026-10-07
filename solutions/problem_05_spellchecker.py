"""05. Typeahead Spell-Checker — see problems/05_typeahead_spellchecker.md"""

from __future__ import annotations

"""
After much trial and error, 
I found that:
if it's not equal to, it has to be the minimum of all adjacent elements + 1
If it's equal to it has to be the diagonal value
"""

def edit_dist(test_word, static_word) -> int:
    mat = [[0] * (len(static_word) + 1) for _ in range(len(test_word) + 1)]
    for i in range(len(static_word) + 1):
        mat[0][i] = i
    for i in range(len(test_word) + 1):
        mat[i][0] = i
    mat[0][0] = 0

    for i in range(len(test_word)):
        for j in range(len(static_word)):
            if test_word[i] == static_word[j]:
                mat[i +1][j +1] = mat[i][j]
            else:
                mat[i +1][j +1] = min(mat[i][j], mat[i][j+1], mat[i+1][j]) +  1
    # print("static dist btw {} and {} is {}".format(test_word, static_word, mat[i +1][j +1]))
    return mat[i +1][j +1]

def suggest(word: str, dictionary: list[str], max_dist: int) -> list[str]:
    ans = []
    for test_word in dictionary:
        if edit_dist(test_word, word) <= max_dist:
            ans.append(test_word)
    return ans
    
dictionary = ["cat", "cot", "cost", "dog", "cats"]

assert suggest("cat", dictionary, 1) == ["cat", "cot", "cats"]
assert suggest("cat", dictionary, 0) == ["cat"]
assert suggest("xyz", dictionary, 1) == []