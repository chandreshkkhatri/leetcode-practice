from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()

        max_diff = 0
        for i in range(len(nums)-1):
            max_diff = max(nums[i+1]-nums[i], max_diff)
        return max_diff


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 6, 9, 1]
    ans = sol.maximumGap(nums)
    print(ans)
