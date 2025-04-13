class Solution:
    def __init__(self):
        self.memo = {}

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            self.memo[(m, n)] = 1
            return 1

        if (m, n) in self.memo:
            return self.memo[(m, n)]

        self.memo[(m-1, n)] = self.uniquePaths(m-1, n)
        self.memo[(m, n-1)] = self.uniquePaths(m, n-1)
        self.memo[(m, n)] = self.memo[(m-1, n)]+self.memo[(m, n-1)]
        return self.memo[(m, n)]


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(12, 18))
