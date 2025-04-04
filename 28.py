class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l_needle = len(needle)
        l_haystack = len(haystack)

        if l_haystack < l_needle:
            return -1
        if l_haystack == l_needle:
            if haystack == needle:
                return 0
            else:
                return -1

        for i in range(l_haystack-l_needle+1):
            if haystack[i:i+l_needle] == needle:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("leetcode", "leeto"))
