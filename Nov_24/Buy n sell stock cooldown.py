class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)

        def solve(ind, buy):
            if ind >= n:
                return 0
            if buy:
                take = solve(ind + 1, 0) - prices[ind]
                hold = solve(ind + 1, 1)
            else:
                take = solve(ind + 2, 1) + prices[ind]
                hold = solve(ind + 1, 0)
            return max(take, hold)
        
        return solve(0, 1)
