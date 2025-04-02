from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        if not common_prefix:
            return ''
        for str_i in strs:
            common_prefix = self.commonPrefix(str_i, common_prefix)

        return common_prefix

    def commonPrefix(self, s1: str, s2: str) -> str:
        s = ''
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                s = s + s1[i]
            else:
                return s
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "flow", "flight"]))
