from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index_in_reach = 0
        it = 0

        while it < len(nums)-1:
            if (it + nums[it]) > max_index_in_reach:
                max_index_in_reach = it + nums[it]

            if max_index_in_reach <= it:
                return False

            it += 1

        return True


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    print(s.canJump(nums))
