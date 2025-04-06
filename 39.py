from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(start, current_sum, path):
            if current_sum > target:
                return
            elif current_sum == target:
                results.append(path)

            for i in range(start, len(candidates)):
                backtrack(i, current_sum+candidates[i], path + [candidates[i]])

        backtrack(0, 0, [])

        return results


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum([2, 3, 5], 8))
