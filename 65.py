class Solution:
    def isNumber(self, s: str) -> bool:
        digit_set = set('0123456789')

        def isInteger(string: str):
            if not string:
                return False
            if string[0] in ['+', '-']:
                string = string[1:]
            return string.isdigit()

        def isDecimal(string: str):
            if not string:
                return False
            if string[0] in ['+', '-']:
                string = string[1:]

            if '.' not in string:
                return False

            left, _, right = string.partition('.')
            if not left and not right:
                return False
            if left and not left.isdigit():
                return False
            if right and not right.isdigit():
                return False
            return True

        def isExponent(string: str):
            if not string:
                return False
            if string[0] not in ['e', 'E']:
                return False
            string = string[1:]
            return isInteger(string)

        i = 0
        while i < len(s) and s[i] not in ['e', 'E']:
            i += 1

        if i < len(s):
            base = s[:i]
            exponent = s[i:]
            return (isInteger(base) or isDecimal(base)) and isExponent(exponent)
        else:
            return isInteger(s) or isDecimal(s)


if __name__ == "__main__":
    s = Solution()
    print(s.isNumber("0.1"))
    print(s.isNumber("abc"))
    print(s.isNumber("1 a"))
    print(s.isNumber("2e10"))
    print(s.isNumber(" -90e3   "))
    print(s.isNumber(" 1e"))
    print(s.isNumber("e3"))
