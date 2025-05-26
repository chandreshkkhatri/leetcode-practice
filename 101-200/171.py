class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dictionary = {chr(64 + i): i for i in range(1, 27)}
        ans = 0
        for c in columnTitle:
            ans = 26*ans + dictionary[c]

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("ZY"))  # Output: 701
    print(s.titleToNumber("A"))   # Output: 1
    print(s.titleToNumber("AB"))  # Output: 28
    print(s.titleToNumber("AAA"))  # Output: 703
