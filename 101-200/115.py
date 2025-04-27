class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if s[i] == t[j]:
                return dp(i+1, j) + dp(i+1, j+1)
            else:
                return dp(i+1, j)

        return dp(0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.numDistinct("rabbbit", "rabbit"))
