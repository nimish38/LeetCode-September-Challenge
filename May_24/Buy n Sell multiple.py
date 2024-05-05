class Solution:
    def maxProfit(self, prices):
        buy, profit = prices[0], 0
        for i in range(1, len(prices)):
            if buy < prices[i]:
                profit += prices[i] - buy
            buy = prices[i]
        return profit
print(Solution().maxProfit(prices = [6,1,3,2,4,7]))