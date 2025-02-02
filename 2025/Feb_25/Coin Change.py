class Solution:
    def coinChange(self, coins, amount: int) -> int:
        def solve(amt):
            if amt == 0:
                return 0
            res = float('inf')
            for c in coins:
                if amt >= c:
                    res = min(res, solve(amt - c) + 1)
            return res
        result = solve(amount)
        if result == float('inf'):
                return -1
        return result


print(Solution().coinChange(coins = [2], amount = 3))