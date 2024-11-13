class Solution:
    def maxProfit(self, prices) -> int:
        n, memo = len(prices), []
        for _ in range(n):
            x = []
            for z in range(3):
                x.append([-1] * 2)
            memo.append(x)

        def solve(ind, buy, cap):
            if ind == n or cap == 0:
                return 0
            if memo[ind][cap][buy] == -1:
                if buy:
                    take = solve(ind + 1, 0, cap) - prices[ind]
                    hold = solve(ind + 1, 1, cap)
                else:
                    take = solve(ind + 1, 1, cap - 1) + prices[ind]
                    hold = solve(ind + 1, 0, cap)
                memo[ind][cap][buy] = max(take, hold)
            return memo[ind][cap][buy]

        return solve(0, 1, 2)

print(Solution().maxProfit(prices = [1,2,3,4,5]))
