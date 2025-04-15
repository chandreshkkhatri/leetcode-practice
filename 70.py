class Solution:
    def climbStairs(self, n: int) -> int:
        nums = [-1]*n
        if n == 1:
            return 1
        if n == 2:
            return 2
        nums[0] = 1
        nums[1] = 2
        for i in range(2, n):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[n-1]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))
