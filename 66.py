from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        i = 0
        if digits[l - 1] != 9:
            digits[l - 1] += 1
            return digits

        while i < l and digits[l - 1 - i] == 9:
            digits[l - 1 - i] = 0
            i += 1

        if i == l:
            digits[0] = 1
            digits.append(0)
            return digits
        digits[l - i - 1] += 1
        return digits


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 3]))
