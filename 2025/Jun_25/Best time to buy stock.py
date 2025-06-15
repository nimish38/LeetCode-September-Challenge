class Solution(object):
    def maxProfit(self, prices):
        buy, best = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] - buy > best:
                best = prices[i] - buy
            if prices[i] < buy:
                buy = prices[i]
        return best