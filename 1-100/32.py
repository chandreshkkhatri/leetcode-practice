class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        max_dp = 0
        if l < 2:
            return 0

        dp = [0]*(l+1)
        if s[:2] == '()':
            dp[1] = 2
            max_dp = 2
        else:
            dp[1] = 0

        if l != 2:
            for i in range(2, l):
                c = s[i]
                if c == '(':
                    dp[i] = 0
                else:
                    if s[i-1] == '(':
                        dp[i] = dp[i-2]+2
                    else:
                        if dp[i-1]+1 <= i and s[i - dp[i-1] - 1] == '(':
                            dp[i] = dp[i-1] + dp[i - dp[i-1] - 2]+2
                    if dp[i] > max_dp:
                        max_dp = dp[i]

        return max_dp


if __name__ == "__main__":
    sol = Solution()
    s = "(()"
    print(sol.longestValidParentheses(s))
