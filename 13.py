class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            1: ['I', 'X', 'C', 'M'],
            5: ['V', 'L', 'D'],
            10: ['X', 'C', 'M']
        }

        order = 1
        it = len(s)-1
        num = 0

        while it >= 0:
            digit5 = False
            digit10 = False
            leading_ones = 0
            trailing_ones = 0

            while it >= 0 and s[it] == dic[1][order-1]:
                it -= 1
                trailing_ones += 1

            if it >= 0 and s[it] == dic[5][order-1]:
                digit5 = True
                it -= 1

            if it >= 0 and s[it] == dic[10][order-1] and not digit5:
                digit10 = True
                it -= 1

            while it >= 0 and s[it] == dic[1][order-1]:
                leading_ones += 1
                it -= 1
            if not digit5 and not digit10:
                num += (leading_ones + trailing_ones)*pow(10, order-1)
            elif digit5 and not digit10:
                num += (5-leading_ones+trailing_ones)*pow(10, order-1)
            elif not digit5 and digit10:
                num += (10-leading_ones+trailing_ones)*pow(10, order-1)
            order += 1

        return num


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MDCCCLXXXIV"))
