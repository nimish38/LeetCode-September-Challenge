class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0
        def solve(change):
            if change in coins:
                return 1
            res = float('inf')
            for coin in coins:
                if change - coin > 0:
                    temp = 1 + solve(change - coin)
                    res = min(temp, res)
            return res
        ans = solve(amount)
        if ans == float('inf'):
            return -1
        return ans

print(Solution().coinChange(coins = [2,5], amount = 11))