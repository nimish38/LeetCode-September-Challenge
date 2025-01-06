class Solution:
    def maxProfit(self, prices) -> int:
        n, memo = len(prices), []
        for _ in range(n):
            memo.append([-1] * 2)

        def solve(ind, buy):
            if ind >= n:
                return 0
            if memo[ind][buy] == -1:
                if buy:
                    take = solve(ind + 1, 0) - prices[ind]
                    hold = solve(ind + 1, 1)
                else:
                    take = solve(ind + 2, 1) + prices[ind]
                    hold = solve(ind + 1, 0)
                memo[ind][buy] = max(take, hold)
            return memo[ind][buy]

        return solve(0, 1)


print(Solution().maxProfit(prices = [1,2,3,0,2]))