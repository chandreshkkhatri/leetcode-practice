class Solution:
    def myAtoi(self, s: str) -> int:
        it = 0
        l = len(s)

        while it < l and s[it] == ' ':
            it += 1

        is_neg = False

        if it < l and s[it] == '-':
            is_neg = True
            it += 1
        elif it < l and s[it] == '+':
            it += 1

        while it < l and s[it] == '0':
            it += 1

        num = 0
        digit_count = 0
        while it < l and self.is_digit(s[it]) and digit_count < 11:
            num *= 10
            num += int(s[it])
            it += 1
            digit_count += 1

        if num == 0:
            return 0
        elif is_neg:
            if num > 2**31:
                return -2**31
            else:
                return -num
        else:
            if num > 2**31-1:
                return 2**31-1
            else:
                return num

    def is_digit(self, c):
        digit_set = set([str(i) for i in range(10)])

        if c in digit_set:
            return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("-042"))
