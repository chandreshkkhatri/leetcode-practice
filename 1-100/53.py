from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMin = 0
        l = len(nums)
        currentSum = 0

        for i, num in enumerate(nums):
            currentSum += num
            nums[i] = currentSum
        currentDiff = -1000000000

        for i, num in enumerate(nums):
            diff = num - currentMin
            if diff > currentDiff:
                currentDiff = diff
            if num < currentMin:
                currentMin = num

        return currentDiff


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(s.maxSubArray([1]))
    print(s.maxSubArray([5, 4, -1, 7, 8]))
