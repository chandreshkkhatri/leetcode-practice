from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        w_counter = Counter(words)  # Count frequency of words
        word_len = len(words[0])
        l_w = len(words)
        l_s = len(s)
        ans = []

        for i in range(word_len):  # Loop over each possible start position
            j = 0
            s_counter = Counter()
            first_word_index = i

            while first_word_index + l_w * word_len <= l_s:
                new_word = s[first_word_index + j *
                             word_len:first_word_index + (j + 1) * word_len]

                if new_word in w_counter:
                    s_counter[new_word] += 1
                    j += 1

                    # If word count exceeds expected, move the window forward
                    while s_counter[new_word] > w_counter[new_word]:
                        out_word = s[first_word_index:first_word_index + word_len]
                        s_counter[out_word] -= 1
                        if s_counter[out_word] == 0:
                            del s_counter[out_word]
                        first_word_index += word_len
                        j -= 1

                    # If we have a valid window, store the index
                    if j == l_w:
                        ans.append(first_word_index)

                else:
                    # Reset the window
                    s_counter.clear()
                    j = 0
                    first_word_index += word_len

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
