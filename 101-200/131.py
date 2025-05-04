from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        l = len(s)
        palin_len_starting_at_i = [[] for _ in range(l)]
        result = []

        def palindrome_with_centre_i(idx):
            nonlocal l
            i = 0
            while idx - i >= 0 and idx + i < l:
                if s[idx - i] != s[idx + i]:
                    break
                palin_len_starting_at_i[idx - i].append(i * 2 + 1)
                i += 1

            i = 0
            while idx - i >= 0 and idx + i + 1 < l:
                if s[idx - i] != s[idx + i + 1]:
                    break
                palin_len_starting_at_i[idx - i].append(i * 2 + 2)
                i += 1

        for i in range(l):
            palindrome_with_centre_i(i)

        def backtrack(idx, current_seq):
            if idx == l:
                result.append(current_seq)
                return

            for length in palin_len_starting_at_i[idx]:
                backtrack(idx + length, current_seq + [s[idx:idx + length]])

        backtrack(0, [])
        return result


if __name__ == "__main__":
    s = "aab"
    solution = Solution()
    print(solution.partition(s))  # Output: [["a","a","b"],["aa","b"]]
