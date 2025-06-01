class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n:
            ans += n % 2
            n = n//2

        return ans


if __name__ == "__main__":
    solution = Solution()
    result = solution.hammingWeight(11)
    print(result)  # Output: 3
