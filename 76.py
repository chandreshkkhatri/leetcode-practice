from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_counter = Counter(t)
        min_length = float('inf')
        min_i1, min_i2 = 0, 0

        i1 = 0
        i2 = 0
        temp_counter = t_counter.copy()

        def window_satisfied(counter):
            return all(counter[char] <= 0 for char in t_counter)

        while i2 < len(s):
            while i2 < len(s) and not window_satisfied(temp_counter):
                temp_counter[s[i2]] -= 1
                i2 += 1

            if not window_satisfied(temp_counter):
                break

            window_counter = Counter(s[i1:i2])
            while window_counter[s[i1]] > t_counter[s[i1]]:
                window_counter[s[i1]] -= 1
                temp_counter[s[i1]] += 1
                i1 += 1

            if i2 - i1 < min_length:
                min_length = i2 - i1
                min_i1, min_i2 = i1, i2

            temp_counter[s[i1]] += 1
            i1 += 1

        return s[min_i1:min_i2] if min_length != float('inf') else ""


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    print(sol.minWindow(s, t))  # Output: "BANC"
