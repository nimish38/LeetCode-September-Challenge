class Solution:
    def maxProfit(self, prices):
        buy, bestbuy, bestsell, profit = -1, float('inf'), -1, 0
        for price in prices:
            if buy == -1 or buy > price:
                buy = price
                bestbuy = min(buy, bestbuy)
            elif price - buy > 0:
                profit += price - buy
                buy = -1
                bestsell = max(bestsell, price)
        return max(profit, bestsell - bestbuy)

print(Solution().maxProfit(prices = [7,1,5,6,9,4]))