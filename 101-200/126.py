from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        shortest_length = float('inf')
        results = []

        word_set = set(wordList)
        if endWord not in word_set:
            return []

        def distance(a, b) -> int:
            return sum(c1 != c2 for c1, c2 in zip(a, b))

        def backtrack(remaining, seq, last):
            nonlocal shortest_length
            if len(seq) > shortest_length:           # prune long path
                return
            if last == endWord:
                if len(seq) < shortest_length:       # found better
                    shortest_length = len(seq)
                    results.clear()
                results.append(seq[:])               # store copy
                return

            for word in list(remaining):             # iterate over snapshot
                if distance(word, last) == 1:
                    backtrack(remaining - {word},    # branch with new set
                              seq + [word],
                              word)

        backtrack(word_set - {beginWord}, [beginWord], beginWord)
        return [p for p in results if len(p) == shortest_length]
