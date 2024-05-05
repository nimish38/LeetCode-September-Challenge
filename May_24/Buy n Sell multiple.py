class Solution:
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        buy, profit = float('inf'), 0
        for i in range(len(prices) - 1):
            if buy == -1 or buy > prices[i]:
                buy = prices[i]
            elif prices[i] > buy and prices[i + 1] < prices[i]:
                profit += prices[i] - buy
                buy = -1
        if buy != -1:
            profit = max(profit, profit + prices[i + 1] - buy)
        return profit
print(Solution().maxProfit(prices = [6,1,3,2,4,7]))