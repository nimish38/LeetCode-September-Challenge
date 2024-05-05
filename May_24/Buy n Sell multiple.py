class Solution:
    def maxProfit(self, prices):
        buy, profit = float('inf'), 0
        for i in range(len(prices) - 1):
            if buy == -1 or buy > prices[i]:
                buy = prices[i]
            elif prices[i] > buy and prices[i + 1] < prices[i]:
                profit += prices[i] - buy
                buy = -1
        if buy != -1:
            profit = max(profit, prices[i + 1] - buy)
        return profit
print(Solution().maxProfit(prices = [7,6,4,3,1]))