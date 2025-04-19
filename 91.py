class Solution:

    def numDecodings(self, s: str) -> int:
        memo = {}

        def decoder(start):
            if start in memo:
                return memo.get(start)

            if not s[start:]:
                return 1

            if start == len(s):
                return 1

            if s[start] == '0':
                return 0

            res = decoder(start+1)

            if start < len(s) - 1 and 10 <= int(s[start:start+2]) <= 26:
                res += decoder(start+2)

            memo[start] = res
            return memo[start]

        return decoder(0)


if __name__ == "__main__":
    print(Solution().numDecodings("226"))
