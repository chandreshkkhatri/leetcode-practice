from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        left_profits = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profits[i] = max(left_profits[i-1], prices[i] - min_price)

        right_profits = [0] * n
        max_price = prices[-1]
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profits[i] = max(right_profits[i+1], max_price - prices[i])

        max_total = 0
        for i in range(n):
            max_total = max(max_total, left_profits[i] + right_profits[i])

        return max_total


if __name__ == "__main__":
    print(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
