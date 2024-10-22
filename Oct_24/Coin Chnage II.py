class Solution:
    def change(self, amount: int, coins) -> int:
        if amount == 0:
            return 0
        self.temp, memo = 0, [False]*(amount+1)

        def solve(amt):
            if not memo[amt]:
                for coin in coins:
                    if amt - coin == 0:
                        self.temp += 1
                    elif amt - coin > 0:
                        solve(amt - coin)
                memo[amt] = True
        solve(amount)
        return self.temp
        # return self.res

print(Solution().change(amount = 5, coins = [1,2,5]))
