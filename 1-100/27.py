from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[k] = num
                k += 1
        return k


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(sol.removeElement(nums, val))
