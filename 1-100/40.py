from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        results = []
        candidates.sort()

        def backtrack(start, path, current_sum):
            if current_sum == target:
                if path not in results:
                    results.append(path)
                return
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i+1, path + [candidates[i]],
                          current_sum+candidates[i])

        backtrack(0, [], 0)

        return results


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
