
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        n = len(s)

        @lru_cache(None)
        def dfs(start):
            if start == n:
                return [""]  # return list with empty string as base case

            results = []
            for end in range(start + 1, n + 1):
                word = s[start:end]
                if word in word_set:
                    for subsentence in dfs(end):
                        if subsentence:
                            results.append(word + " " + subsentence)
                        else:
                            results.append(word)
            return results

        return dfs(0)


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    # Output: ["cats and dog", "cat sand dog"]
    print(s.wordBreak("pineapplepenapple", [
          "apple", "pen", "applepen", "pine", "pineapple"]))
    # Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # Output: []
