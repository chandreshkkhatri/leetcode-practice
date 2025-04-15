class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i*i <= x:
            i += 1
        return i-1


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(4))
