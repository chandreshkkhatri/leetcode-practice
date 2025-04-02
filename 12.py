class Solution:
    def intToRoman(self, num: int) -> str:
        digit = num % 10
        it = 1
        string = ""

        while num:
            digit = num % 10
            string = self.get_roman_literal(it, digit)+string
            it += 1
            num = num//10
        return string

    def get_roman_literal(self, order, digit):
        dictionary = {
            1: {
                1: 'I',
                5: 'V',
                10: 'X'
            },
            2: {
                1: 'X',
                5: 'L',
                10: 'C'
            },
            3: {
                1: 'C',
                5: 'D',
                10: 'M'
            },
            4: {
                1: 'M'
            }
        }
        if digit == 4:
            return f"{dictionary[order][1]}{dictionary[order][5]}"
        elif digit == 9:
            return f"{dictionary[order][1]}{dictionary[order][10]}"
        elif digit < 5:
            return "".join([dictionary[order][1] for _ in range(digit)])
        else:
            return "".join([dictionary[order][5]]+[dictionary[order][1] for _ in range(digit-5)])


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3749))
