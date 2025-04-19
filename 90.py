from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        self.generate_subsets(nums, 0, [], results)
        return results

    def generate_subsets(self, nums: List[int], start: int, current_set: List[int], results: List[List[int]]) -> None:
        results.append(current_set[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            current_set.append(nums[i])
            self.generate_subsets(nums, i + 1, current_set, results)
            current_set.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2, 3, 3, 3, 3, 4, 4, 4]))
