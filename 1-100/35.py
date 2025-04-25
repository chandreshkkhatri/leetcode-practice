from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left = 0
        right = l-1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return l

        while left < right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if left == mid:
                left += 1
                break
            if nums[mid] < target:
                left = mid
            if nums[mid] > target:
                right = mid

        return left


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    print(sol.searchInsert(nums, target))
