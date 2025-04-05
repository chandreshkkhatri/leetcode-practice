from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if l == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]

        left = 0
        right = l-1

        while left < right:
            mid = int((left+right)//2)
            if nums[mid] == target:
                left = mid
                break
            if left == mid:
                left += 1
                break
            if nums[mid] < target:
                left = mid
            if nums[mid] > target:
                right = mid

        if nums[left] != target:
            return [-1, -1]
        right = left
        while left-1 >= 0 and nums[left-1] == target:
            left -= 1
        while right+1 < l and nums[right+1] == target:
            right += 1

        return [left, right]


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(sol.searchRange(nums, target))
