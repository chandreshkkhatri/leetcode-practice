class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        if l1 > l2:
            return self.multiply(num2, num1)
        num1 = num1[::-1]
        num2 = num2[::-1]

        i = 0
        subMultiples = []

        for num in num2:
            subMultiples.append(self.multiply_with_digit(num1, num))
        multiple = self.sum_submultiples(subMultiples)

        return str(multiple)

    def multiply_with_digit(self, num: str, d: str) -> str:
        digits = ''
        carry = 0

        for digit in num:
            currentProduct = int(digit)*int(d) + carry
            currentDigit = currentProduct % 10
            carry = currentProduct//10
            digits += str(currentDigit)
        digits += str(carry)

        return digits

    def sum_submultiples(self, subMultiples):
        total = 0
        print(subMultiples)
        for i, m in enumerate(subMultiples):
            total += int(m[::-1])*pow(10, i)

        return total


if __name__ == "__main__":
    s = Solution()
    print(s.multiply("123", "456"))
