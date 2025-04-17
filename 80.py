from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        j = 2
        count = 0
        l = len(nums)
        if l < 2:
            return l
        if nums[1] == nums[0]:
            count = 1
        else:
            count = 0
        while j < l:
            if nums[j] == nums[j-1]:
                count += 1
            else:
                count = 0
            if count < 2:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
