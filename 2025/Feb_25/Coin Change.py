class Solution:
    def coinChange(self, coins, amount: int) -> int:
        memo = [-2] * (amount + 1)

        def solve(amt):
            if memo[amt] == -2:
                if amt == 0:
                    memo[amt] = 0
                else:
                    res = float('inf')
                    for c in coins:
                        if amt >= c:
                            res = min(res, solve(amt - c) + 1)
                    memo[amt] = res
            return memo[amt]

        result = solve(amount)
        if result == float('inf'):
                return -1
        return result


print(Solution().coinChange(coins = [1,5,2], amount = 11))