class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = self.preProcessString(s)
        l = len(string)
        for i in range(l//2):
            if string[i] != string[l-1-i]:
                return False
        return True

    def preProcessString(self, s: str) -> str:
        string = ''
        for c in s:
            if c.isalnum():
                string += c.lower()
        return string


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
