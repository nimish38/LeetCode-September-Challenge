class Solution(object):
    def maxProfit(self, prices):
        lowest, best = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                best = max(best, prices[i] - lowest)
        return best