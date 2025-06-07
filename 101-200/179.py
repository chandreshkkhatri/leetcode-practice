from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))

        def cmp(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        strs.sort(key=cmp_to_key(cmp))

        ans = ''.join(strs)

        return '0' if ans[0] == '0' else ans


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 30, 34, 5, 9]
    print(solution.largestNumber(nums))  # Output: "9534330"
