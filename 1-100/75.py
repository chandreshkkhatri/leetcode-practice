from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_objects = [0, 0, 0]
        for num in nums:
            if num == 0:
                count_objects[0] += 1
            elif num == 1:
                count_objects[1] += 1
            else:
                count_objects[2] += 1

        nums[:count_objects[0]] = [0]*count_objects[0]
        nums[count_objects[0]:count_objects[0] +
             count_objects[1]] = [1]*count_objects[1]
        nums[count_objects[0]+count_objects[1]             : sum(count_objects)] = [2]*count_objects[2]

        return nums


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(nums)
