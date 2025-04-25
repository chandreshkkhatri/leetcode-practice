from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def backtrack(current, open_count, close_count):
            if len(current) == 2*n:
                results.append(current)
                return

            if open_count < n:
                backtrack(current+'(', open_count+1, close_count)
            if close_count < open_count:
                backtrack(current+')', open_count, close_count+1)

        backtrack("", 0, 0)

        return results


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
