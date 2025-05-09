from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        word_dict_set = set(wordDict)

        @lru_cache(None)
        def word_break(idx):
            nonlocal l
            if idx == l:
                return True
            for i in range(idx+1, l+1):
                if s[idx:i] in word_dict_set and word_break(i):
                    return True
            return False

        return word_break(0)


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))
