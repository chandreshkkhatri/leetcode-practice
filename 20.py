class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []

        for c in s:
            if self.is_closing(c):
                if len(bracket_stack) == 0 or not self.is_complement(bracket_stack.pop(), c):
                    return False
            else:
                bracket_stack.append(c)
        if len(bracket_stack) > 0:
            return False
        return True

    def is_closing(self, c):
        if c == ')' or c == "}" or c == "]":
            return True
        else:
            return False

    def is_complement(self, a, b):
        if (a == '(' and b == ')') or (a == '{' and b == '}') or (a == '[' and b == ']'):
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))
