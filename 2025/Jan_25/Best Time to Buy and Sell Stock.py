class Solution:
    def maxProfit(self, prices):
        margin, lowest = 0, float('inf')
        for val in prices:
            margin = max(margin, val - lowest)
            lowest = min(lowest, val)
        return margin


print(Solution().maxProfit(prices = [7,6,4,3,1]))