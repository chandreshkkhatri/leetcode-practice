class Solution:
    def reverse(self, x: int) -> int:
        sign_x = 1 if x >= 0 else -1
        str_x = str(x*sign_x)[::-1]

        reverse_x = int(str_x)*sign_x
        if (reverse_x > pow(2, 31) - 1) or (reverse_x < - pow(2, 31)):
            return 0
        else:
            return reverse_x


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))
