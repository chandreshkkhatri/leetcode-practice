from typing import List
from collections import Counter


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx1, idx2 = None, None
        nums_counter = Counter(nums)

        for it, num in enumerate(nums):
            if target - num in nums_counter:
                if target-num == num:
                    if nums_counter[num] > 1:
                        if idx1 == None:
                            idx1 = it
                        idx2 = it
                else:
                    if idx1 == None:
                        idx1 = it
                    idx2 = it

        return [idx1, idx2]


if __name__ == "__main__":
    nums_list = [2, 7, 11, 15]
    num_target = 9
    s = Solution()
    print(s.twoSum(nums_list, num_target))
