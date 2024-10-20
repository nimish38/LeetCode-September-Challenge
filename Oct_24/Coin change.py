class Solution:
    def coinChange(self, coins, amount: int) -> int:
        def solve(change):
            if change in coins:
                return 1
            res = float('inf')
            for coin in coins:
                if change - coin > 0:
                    temp = 1 + solve(change - coin)
                    res = min(temp, res)
            if res == float('inf'):
                return res
        return solve(amount)