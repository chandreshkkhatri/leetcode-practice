from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == "__main__":
    sol = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    ans = sol.evalRPN(tokens)
    print(ans)  # Output: 9
