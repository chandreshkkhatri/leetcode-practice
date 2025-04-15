class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        ans = ''
        la = len(a)
        lb = len(b)
        idx = 0

        if la < lb:
            return self.addBinary(b, a)
        a = a[::-1]
        b = b[::-1]

        while idx < la:
            if idx >= lb:
                tmp = int(c) + int(a[idx])
                d = tmp % 2
                c = tmp//2
            else:
                tmp = int(c) + int(a[idx]) + int(b[idx])
                d = tmp % 2
                c = tmp // 2
            ans += str(d)
            idx += 1

        if c:
            ans += str(c)
        return ans[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("1010", "1011"))
