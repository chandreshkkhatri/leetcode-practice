from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)

        if l % 2 == 0:
            return (nums[l//2 - 1] + nums[l//2])/2.0
        else:
            return nums[l//2]


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
