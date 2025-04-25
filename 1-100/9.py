class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        for i in range(int(n/2)):
            if s[i] != s[n-i-1]:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))
