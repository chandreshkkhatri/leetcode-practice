from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for num in nums:
            d = dictionary.get(num)
            if d:
                dictionary[num] = (d+1) % 3
            else:
                dictionary[num] = 1
            # print(dictionary)
        for k, v in dictionary.items():
            if v == 1:
                return k


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 3, 2]))
