class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        l = s.split(' ')
        return len(l[-1])
