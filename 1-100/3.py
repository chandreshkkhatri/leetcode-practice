class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        longest_substring_length = 0
        last_non_repeating_char = 0

        for i, c in enumerate(s):
            if last_index.get(c) != None:
                substring_length = 0
                if last_non_repeating_char <= last_index.get(c):
                    last_non_repeating_char = last_index.get(c) + 1
                    substring_length = i - last_index.get(c)
                else:
                    substring_length = i - last_non_repeating_char+1
                if substring_length > longest_substring_length:
                    longest_substring_length = substring_length

            else:
                substring = i - last_non_repeating_char+1
                if substring > longest_substring_length:
                    longest_substring_length = substring
            last_index[c] = i

        return longest_substring_length


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"

    print(sol.lengthOfLongestSubstring(s))
