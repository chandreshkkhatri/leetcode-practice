class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = x
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            if n < 0:
                return 1/self.myPow(x, -1*n)
            if n % 2 == 0:
                return self.myPow(x*x, int(n/2))
            else:
                return x*self.myPow(x*x, int((n-1)/2))


if __name__ == "__main__":
    s = Solution()
    print(s.myPow(2, 10))
