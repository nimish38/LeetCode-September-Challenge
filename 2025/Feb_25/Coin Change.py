class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0

        def solve(amt):
            if amt == 0:
                return 0
            res = float('inf')
            for c in coins:
                if amt >= c:
                    res = min(res, solve(amt - c) + 1)
            if res == float('inf'):
                return -1
            return res

        return solve(amount)


print(Solution().coinChange(coins = [1,2,5], amount = 11))