class Solution:
    def change(self, amount: int, coins) -> int:
        if amount == 0:
            return 0

        def solve(amt):
            if amt in coins:
                return 1
            res = 0
            for coin in coins:
                if amt - coin > 0:
                    res += solve(amt - coin)
            return res

        return solve(amount)
