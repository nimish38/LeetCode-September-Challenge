class Solution:
    def maxProfit(self, prices):
        buy, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

print(Solution().maxProfit(prices = [7,6,4,3,1]))