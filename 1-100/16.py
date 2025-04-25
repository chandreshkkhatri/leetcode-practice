
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        min_dist = float('inf')
        triplets = []

        for idx, num in enumerate(nums):
            twins, dist = self.twoSum(nums[idx+1:], target-nums[idx])
            if dist < min_dist:
                min_dist = dist
                triplets = twins+[nums[idx]]

        return sum(triplets)

    def twoSum(self, nums, target):
        n = len(nums)
        i = 0
        j = n - 1
        ans = []
        dist = float('inf')

        while i < j:
            current_sum = nums[i] + nums[j]
            if abs(current_sum-target) < dist:
                ans = [nums[i], nums[j]]
                dist = abs(current_sum - target)
            if current_sum < target:
                i += 1
            else:
                j -= 1

        return ans, dist


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))
