from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        lo = 0
        hi = l - 1
        if l == 1:
            return nums[0]
        if nums[lo] < nums[hi]:
            return nums[lo]
        while lo + 1 < hi:
            mid = int((lo + hi)/2)
            if nums[mid] >= nums[lo]:
                lo = mid
            else:
                hi = mid
        return nums[hi]


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 4, 5, 1, 2]
    ans = sol.findMin(nums)
    print(ans)
