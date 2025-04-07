from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        check = [False]*100001
        for num in nums:
            if num > 0 and num < 100001:
                check[num] = True

        i = 1

        while i < 100001 and check[i] == True:
            i += 1

        return i


if __name__ == "__main__":
    nums = [1, 2, 0]
    s = Solution()
    print(s.firstMissingPositive(nums))
