from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        i = 0
        is_bought = False
        profit = 0

        while i < l - 1:
            if not is_bought and prices[i] < prices[i+1]:
                is_bought = True
                buy_price = prices[i]
            elif is_bought and prices[i] > prices[i+1]:
                is_bought = False
                sell_price = prices[i]
                profit += sell_price - buy_price
            i += 1  # always increment

        # Handle if we are holding a stock at the end
        if is_bought:
            profit += prices[-1] - buy_price

        return profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
