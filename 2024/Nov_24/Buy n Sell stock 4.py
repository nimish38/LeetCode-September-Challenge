class Solution:
    def maxProfit(self, k: int, prices) -> int:
        n, memo = len(prices), []
        for _ in range(n):
            x = []
            for z in range(k + 1):
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

        return solve(0, 1, k)

print(Solution().maxProfit(k = 2, prices = [3,2,6,5,0,3]))