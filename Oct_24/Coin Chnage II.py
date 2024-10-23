class Solution:
    def change(self, amount: int, coins) -> int:
        if amount == 0:
            return 0
        n = len(coins)

        def solve(ind, amt):
            if ind >= n:
                return 0
            if amt == 0:
                return 1
            if amt < coins[ind]:
                return solve(ind + 1, amt)
            take = solve(ind, amt - coins[ind])
            skip = solve(ind + 1, amt)
            return take + skip

        return solve(0, amount)

print(Solution().change(amount = 5, coins = [1,2,5]))
