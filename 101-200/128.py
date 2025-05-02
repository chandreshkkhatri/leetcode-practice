from typing import Counter, List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_counter = Counter(nums)
        l = len(nums)

        if l == 0:
            return 0

        n = len(nums_counter)
        if n == 1:
            return 1

        i = 0
        longest = 0
        last = 0
        current_len_counter = 0
        element_counter = 0

        while i < l:
            if i in nums_set:
                current_len_counter += 1
                element_counter += 1
                nums_set.remove(i)
            else:
                longest = max(longest, current_len_counter)
                current_len_counter = 0
                last = i
            if element_counter == n:
                longest = max(longest, current_len_counter)
                current_len_counter = 0
                element_counter = 0
                break
            i += 1

        return max(longest, current_len_counter)
