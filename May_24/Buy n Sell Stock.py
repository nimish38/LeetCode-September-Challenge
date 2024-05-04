class Solution:
    def maxProfit(self, prices):
        buy, profit = float('inf'), 0
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit

print(Solution().maxProfit(prices = [7,6,4,3,1]))