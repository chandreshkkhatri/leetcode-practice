from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrices = []
        sellPrices = []
        l = len(prices)
        currentMin = 10001
        currentMax = 0

        for i in range(l):

            if prices[i] < currentMin:
                currentMin = prices[i]
            buyPrices.append(currentMin)

            if prices[l - i - 1] > currentMax:
                currentMax = prices[l - i - 1]
            sellPrices.append(currentMax)

        profits = []
        sellPrices.reverse()

        for i in range(l):
            profits.append(sellPrices[i] - buyPrices[i])

        return max(profits)


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
