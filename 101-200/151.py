class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.lstrip().rstrip().split(' ')
        slist = slist[::-1]
        nlist = []
        for c in slist:
            if c:
                nlist.append(c)
        return ' '.join(nlist)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("the sky is blue"))
