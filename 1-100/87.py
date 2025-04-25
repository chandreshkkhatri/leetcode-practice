from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize=None)
        def dfs(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False

            for i in range(1, len(a)):
                # No swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True
                # With swap
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    return True
            return False

        return dfs(s1, s2)


if __name__ == "__main__":
    s = Solution()
    print(s.isScramble(s1="great", s2="rgeat"))
