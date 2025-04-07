from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        min_jumps_i = [100000]*n
        min_jumps_i[0] = 0
        for i in range(n):
            for j in range(nums[i]):
                if (i+j+1 < n) and (min_jumps_i[i]+1 < min_jumps_i[i+j+1]):
                    min_jumps_i[i+j+1] = min_jumps_i[i] + 1
        return min_jumps_i[n-1]


if __name__ == "__main__":
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
