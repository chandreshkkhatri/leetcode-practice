from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(None)
        def is_interleave(p1, p2, p3):
            if p3 == len(s3):
                return p1 == len(s1) and p2 == len(s2)

            valid = False
            if p1 < len(s1) and s1[p1] == s3[p3]:
                valid |= is_interleave(p1 + 1, p2, p3 + 1)
            if p2 < len(s2) and s2[p2] == s3[p3]:
                valid |= is_interleave(p1, p2 + 1, p3 + 1)

            return valid

        return is_interleave(0, 0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave(s1="a", s2="b", s3="ab"))
