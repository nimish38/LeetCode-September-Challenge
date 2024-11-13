class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)

        def solve(ind, buy, cap):
            if ind == n or cap == 0:
                return 0
            if buy:
                take = solve(ind + 1, False, cap) - prices[ind]
                hold = solve(ind + 1, True, cap)
            else:
                take = solve(ind + 1, True, cap - 1) + prices[ind]
                hold = solve(ind + 1, False, cap)
            return max(take, hold)

        return solve(0, True, 2)

print(Solution().maxProfit(prices = [1,2,3,4,5]))
