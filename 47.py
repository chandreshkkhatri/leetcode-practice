from typing import Counter, List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums_counter = Counter(nums)
        nums_len = len(nums)
        results = []

        def backtrack(remaining_nums, current_perm, nums_counter):
            if remaining_nums == 0:
                results.append(current_perm)

            for idx, num in enumerate(nums_counter):
                if nums_counter[num] > 0:
                    nums_counter[num] -= 1
                    backtrack(remaining_nums-1, current_perm +
                              [num], nums_counter.copy())
                    nums_counter[num] += 1

        backtrack(nums_len, [], nums_counter)
        return results


if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))
    print(s.permuteUnique([1, 2, 3]))
    print(s.permuteUnique([1, 2, 3, 4]))
