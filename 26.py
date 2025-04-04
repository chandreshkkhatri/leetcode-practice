from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        j = 0

        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[j+1] = nums[i+1]
                j += 1

        return j+1


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().removeDuplicates(nums))
