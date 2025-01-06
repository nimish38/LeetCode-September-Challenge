class Solution:
    def change(self, amount: int, coins) -> int:
        n, memo = len(coins), []
        for _ in range(n + 1):
            memo.append([-1] * (amount + 1))

        def solve(ind, amt):
            if ind >= n:
                return 0
            if amt == 0:
                return 1
            if memo[ind][amt] == -1:
                if amt < coins[ind]:
                    return solve(ind + 1, amt)
                take = solve(ind, amt - coins[ind])
                skip = solve(ind + 1, amt)
                memo[ind][amt] = take + skip
            return memo[ind][amt]

        return solve(0, amount)

print(Solution().change(amount = 5, coins = [1,2,5]))
