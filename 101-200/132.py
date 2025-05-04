class Solution:
    def minCut(self, s: str) -> int:
        l = len(s)
        # Step 1: Precompute palindromes using a DP table
        dp_palindrome = [[False] * l for _ in range(l)]

        # Every single character is a palindrome
        for i in range(l):
            dp_palindrome[i][i] = True

        # Check for palindromes of length 2 and greater
        for length in range(2, l + 1):  # length of the substring
            for i in range(l - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or dp_palindrome[i + 1][j - 1]):
                    dp_palindrome[i][j] = True

        # Step 2: Use DP to compute minimum cuts
        dp_min_cuts = [float('inf')] * l
        for i in range(l):
            if dp_palindrome[0][i]:
                # no cuts needed if the substring s[0:i+1] is a palindrome
                dp_min_cuts[i] = 0
            else:
                for j in range(i):
                    if dp_palindrome[j + 1][i]:
                        dp_min_cuts[i] = min(
                            dp_min_cuts[i], dp_min_cuts[j] + 1)

        return dp_min_cuts[l - 1]


if __name__ == "__main__":
    s = "aab"
    solution = Solution()
    print(solution.minCut(s))  # Output: 1
