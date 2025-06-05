class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        n, d = abs(numerator), abs(denominator)

        integer_part = n // d
        rem = n % d
        if rem == 0:
            return sign + str(integer_part)

        out = [sign + str(integer_part), '.']
        seen = {}

        while rem:
            if rem in seen:
                idx = seen[rem]
                out.insert(idx, '(')
                out.append(')')
                break

            seen[rem] = len(out)
            rem *= 10
            out.append(str(rem // d))
            rem %= d

        return ''.join(out)


if __name__ == "__main__":
    solution = Solution()
    numerator = 1
    denominator = 3
    print(solution.fractionToDecimal(numerator, denominator))
