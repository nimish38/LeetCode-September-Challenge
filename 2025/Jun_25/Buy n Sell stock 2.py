class Solution:
    def maxProfit(self, prices):
        buy, profit = prices[0], 0
        for i in range(1, len(prices)):
            if buy < prices[i]:
                profit += prices[i] - buy
            buy = prices[i]
        return profit

print(Solution().maxProfit(prices = [7,1,5,3,6,4]))