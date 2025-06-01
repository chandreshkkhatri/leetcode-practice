class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for _ in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    result = solution.reverseBits(43261596)
    print(result)  # Output: 964176192
