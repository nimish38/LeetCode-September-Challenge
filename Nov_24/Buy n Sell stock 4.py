class Solution:
    def maxProfit(self, k: int, prices) -> int:
        n = len(prices)

        def solve(ind, buy, cap):
            if ind == n or cap == 0:
                return 0
            if buy:
                take = solve(ind + 1, 0, cap) - prices[ind]
                hold = solve(ind + 1, 1, cap)
            else:
                take = solve(ind + 1, 1, cap - 1) + prices[ind]
                hold = solve(ind + 1, 0, cap)
            return max(take, hold)

        return solve(0, 1, k)
