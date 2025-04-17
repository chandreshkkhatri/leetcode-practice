from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        solution = []

        def backtrack(remaining_numbers, current_combination, n):
            if remaining_numbers == 0:
                solution.append(current_combination)
                return

            largest_number = current_combination[-1] if len(
                current_combination) > 0 else 0
            for i in range(largest_number+1, n+1):
                backtrack(remaining_numbers-1, current_combination+[i], n)

        backtrack(k, [], n)

        return solution


if __name__ == "__main__":
    s = Solution()
    print(s.combine(1, 1))
