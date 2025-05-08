from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for num in nums:
            if dictionary.get(num):
                dictionary[num] = False
            else:
                dictionary[num] = True
        for k, v in dictionary.items():
            if v:
                return k


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
    print(s.singleNumber([2, 2, 1]))  # Output: 1
    print(s.singleNumber([1]))  # Output: 1
    print(s.singleNumber([1, 0, 0]))  # Output: 1
    print(s.singleNumber([0, 0, 0, 1]))  # Output: 1
