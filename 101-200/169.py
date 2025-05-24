from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


if __name__ == "__main__":
    nums = [3, 3, 4]
    s = Solution()
    print(s.majorityElement(nums))
